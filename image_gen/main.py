import base64
import json
import os
import re
import time
from pathlib import Path
from typing import List, Tuple

import requests
from dotenv import load_dotenv
from PIL import Image

IMAGE_GEN_DIR = Path(__file__).resolve().parent
ROOT_DIR = IMAGE_GEN_DIR.parent
CONFIG_PATH = IMAGE_GEN_DIR / "config.json"

# Load .env from image_gen folder so API key is available
load_dotenv(IMAGE_GEN_DIR / ".env")

# Google AI Studio / Gemini Images (Nano Banana) - official model from ai.google.dev/gemini-api/docs/image-generation
GEMINI_IMAGE_MODEL = "gemini-2.5-flash-image"
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta"

# Primary env var name for the Google AI Studio key.
API_KEY_ENV = "GOOGLE_AI_STUDIO_API_KEY"
# Fallback to the old name if present, so existing .env still works.
LEGACY_API_KEY_ENV = "NANOBANANA_API_KEY"


def load_config() -> dict:
    """Load configuration from config.json."""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    # Basic validation / defaults
    required_keys = ["input_file", "output_folder", "output_folder_name", "pdf"]
    for key in required_keys:
        if key not in cfg:
            raise ValueError(f"Missing required config key: {key}")

    return cfg

def get_api_key() -> str:
    api_key = os.getenv(API_KEY_ENV) or os.getenv(LEGACY_API_KEY_ENV)
    if not api_key:
        raise RuntimeError(
            f"Environment variable {API_KEY_ENV} (or legacy {LEGACY_API_KEY_ENV}) is not set. "
            "Set your Google AI Studio API key in the environment before running."
        )
    return api_key


def parse_prompts(markdown_path: Path) -> List[Tuple[int, str]]:
    """
    Parse prompts from the markdown file.

    Looks for section headers "### Slide N: ..." then the next line
    **Prompt:** "..." and returns a list of (slide_number, prompt_text)
    so image filenames can be slide_18.png, slide_19.png, etc.
    """
    header_pattern = re.compile(r'^###\s+Slide\s+(\d+)\s*:')
    prompt_pattern = re.compile(r'^\*\*Prompt:\*\*\s*"(.*)"\s*$')

    prompts: List[Tuple[int, str]] = []
    current_slide: int | None = None

    with open(markdown_path, "r", encoding="utf-8") as f:
        for line in f:
            header_m = header_pattern.match(line.strip())
            if header_m:
                current_slide = int(header_m.group(1))
                continue
            prompt_m = prompt_pattern.match(line.strip())
            if prompt_m and current_slide is not None:
                text = prompt_m.group(1).strip()
                prompts.append((current_slide, text))
                current_slide = None

    if not prompts:
        raise RuntimeError(f"No prompts found in {markdown_path}")

    return prompts


def _slide_number_from_path(p: Path) -> int:
    """Extract slide number from filename like slide_18.png for sorting."""
    match = re.search(r"slide_(\d+)", p.name)
    return int(match.group(1)) if match else 0


def generate_image_with_gemini(prompt: str, api_key: str, dest_path: Path) -> None:
    """
    Call Google Gemini Images (Nano Banana) for a single prompt
    and save the resulting image as a PNG at dest_path.
    """
    url = (
        f"{GEMINI_BASE_URL}/models/{GEMINI_IMAGE_MODEL}:generateContent"
        f"?key={api_key}"
    )

    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ],
            }
        ],
        "generationConfig": {
            "responseModalities": ["Image"],
            "imageConfig": {
                "aspectRatio": "4:3"
            },
        },
    }

    resp = requests.post(url, headers=headers, json=payload, timeout=60)
    if not resp.ok:
        try:
            err_body = resp.json()
        except Exception:
            err_body = resp.text
        raise RuntimeError(
            f"Gemini API error {resp.status_code}: {err_body}"
        )
    data = resp.json()

    try:
        part = data["candidates"][0]["content"]["parts"][0]
        inline = part.get("inlineData") or part.get("inline_data")
        if not inline:
            raise KeyError("inlineData not found in response")
        b64_data = inline["data"]
    except Exception as e:
        raise RuntimeError(f"Unexpected response format from Gemini: {data}") from e

    image_bytes = base64.b64decode(b64_data)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "wb") as f:
        f.write(image_bytes)


def generate_all_images(
    prompts: List[Tuple[int, str]],
    api_key: str,
    images_dir: Path,
) -> List[Path]:
    """
    For each prompt, call the API and save the image as slide_<N>.png
    where N is the slide number from the markdown. Returns paths in slide order.
    """
    images_dir.mkdir(parents=True, exist_ok=True)
    result_paths: List[Path] = []

    total = len(prompts)
    for slide_num, prompt in prompts:
        print(f"Generating image for slide {slide_num} ({len(result_paths) + 1}/{total})...")

        dest = images_dir / f"slide_{slide_num}.png"
        generate_image_with_gemini(prompt, api_key, dest)
        result_paths.append(dest)

        # Small delay between calls to be gentle with rate limits
        time.sleep(0.5)

    return result_paths


def build_pages_8_up(
    image_paths: List[Path],
    output_pdf_path: Path,
    dpi: int = 150,
) -> None:
    """
    Arrange images 8-per-page (4x2 grid) on landscape pages and save as a PDF.
    """
    if not image_paths:
        raise RuntimeError("No images to layout")

    # US Letter landscape: 11 x 8.5 inches
    page_width_in = 11.0
    page_height_in = 8.5
    page_width_px = int(page_width_in * dpi)
    page_height_px = int(page_height_in * dpi)

    # Grid: 4 columns x 2 rows
    cols = 4
    rows = 2

    margin_px = int(0.25 * dpi)  # 0.25 inch margins

    available_width = page_width_px - 2 * margin_px
    available_height = page_height_px - 2 * margin_px

    cell_width = available_width // cols
    cell_height = available_height // rows

    pages: List[Image.Image] = []

    # Process in chunks of 8
    for page_start in range(0, len(image_paths), cols * rows):
        chunk = image_paths[page_start : page_start + cols * rows]
        page = Image.new("RGB", (page_width_px, page_height_px), color="white")

        for i, img_path in enumerate(chunk):
            try:
                img = Image.open(img_path).convert("RGB")
            except Exception as e:
                print(f"Warning: failed to open {img_path}: {e}")
                continue

            # Resize image to fit within cell while preserving aspect ratio
            img.thumbnail((cell_width, cell_height), Image.LANCZOS)

            row = i // cols
            col = i % cols

            x_offset = margin_px + col * cell_width + (cell_width - img.width) // 2
            y_offset = margin_px + row * cell_height + (cell_height - img.height) // 2

            page.paste(img, (x_offset, y_offset))

        pages.append(page)

    # Save as multi-page PDF
    output_pdf_path.parent.mkdir(parents=True, exist_ok=True)

    first_page, *rest_pages = pages
    first_page.save(
        output_pdf_path,
        "PDF",
        resolution=dpi,
        save_all=True,
        append_images=rest_pages,
    )


def main() -> None:
    cfg = load_config()
    api_key = get_api_key()

    input_file = (ROOT_DIR / cfg["input_file"]).resolve()
    if not input_file.is_file():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    output_folder = (ROOT_DIR / cfg["output_folder"]).resolve()
    # Use output_folder_name as a prefix for a run-specific subfolder
    run_root = output_folder / cfg["output_folder_name"]
    images_dir = run_root / "images"
    pdf_path = run_root / cfg["pdf"]

    print(f"Input markdown: {input_file}")
    print(f"Images directory: {images_dir}")
    print(f"Output PDF: {pdf_path}")

    prompts = parse_prompts(input_file)
    print(f"Found {len(prompts)} prompts.")

    # Generate images (comment out this line if you already have images and just want to rebuild the PDF)
    image_paths = generate_all_images(prompts, api_key, images_dir)

    # If you already have images, you could instead glob and sort by slide number:
    # image_paths = sorted(images_dir.glob("slide_*.png"), key=_slide_number_from_path)

    # Ensure PDF page order is by slide number (e.g. slide_2 before slide_18)
    image_paths = sorted(image_paths, key=_slide_number_from_path)
    build_pages_8_up(image_paths, pdf_path)
    print(f"Done. PDF written to: {pdf_path}")


if __name__ == "__main__":
    main()

