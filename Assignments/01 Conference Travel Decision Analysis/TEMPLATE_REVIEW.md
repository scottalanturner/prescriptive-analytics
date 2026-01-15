# Assignment Template Review
## Issues Identified by Comparing Template with Working Example Solution

### CRITICAL ISSUES (Will cause errors if not addressed)

#### 1. **Missing Guidance on Combination Variables Approach**
**Location:** Cell 15 (Variable Definition), Cell 17 (Constraints)

**Problem:**
- Template suggests creating separate variables: `lodging_vars[i]`, `flight_vars[i]`, and `num_people`
- This leads to non-linear expressions like `num_people * lodging_vars[i]` which PuLP cannot handle
- Template comment says: `Total cost = (lodging_cost * nights * num_people) + (flight_cost * num_people)`
- This would require multiplying variables, causing `TypeError: Non-constant expressions cannot be multiplied`

**What Example Solution Does:**
- Uses combination variables: `solution_vars[(i, j, k)]` representing (lodging_i AND flight_j AND team_size_k)
- This makes all cost coefficients constants, keeping the model linear
- Includes explanatory comment: "This approach avoids multiplying variables, which PuLP requires for linear models"

**Recommendation:**
- Add guidance about the combination variable approach
- Explain why it's necessary (PuLP requires linear expressions)
- Provide example structure for creating combination variables
- Warn against trying to multiply separate variables

---

#### 2. **Misleading Cost Calculation Comments**
**Location:** Cell 17 (Constraints), Cell 18 (Solution Display)

**Problem:**
- Template comment: `# Total cost = (lodging_cost * nights * num_people) + (flight_cost * num_people)`
- This suggests multiplying `num_people` (a variable) by costs, which won't work
- Template comment: `# - Lodging cost: $X (cost_per_night * nights * num_people)`
- This is misleading about how costs are actually calculated in the model

**What Example Solution Does:**
- Pre-calculates costs for each combination: `lodging_cost = cost_per_night * conference_dates * k` (where k is a constant team size in that combination)
- Then multiplies by the binary combination variable: `lodging_cost * solution_vars[(i, j, k)]`
- This keeps everything linear

**Recommendation:**
- Update comments to explain combination-based cost calculation
- Clarify that costs are calculated as constants for each (lodging, flight, team_size) combination
- Remove misleading examples that suggest variable multiplication

---

#### 3. **Missing Solution Extraction Guidance**
**Location:** Cell 18 (Solution Display)

**Problem:**
- Template suggests: `# for var in model.variables(): print(f"{var.name}: {value(var)}")`
- This doesn't explain how to extract which combination was selected
- Doesn't show how to get lodging_idx, flight_idx, and team_size from combination variables

**What Example Solution Does:**
- Iterates through `solution_vars.items()` to find the activated combination
- Extracts `selected_lodging_idx = i`, `selected_flight_idx = j`, `selected_team_size = k`
- Uses these extracted values for all subsequent display logic

**Recommendation:**
- Add guidance on extracting solutions from combination variables
- Show the iteration pattern: `for (i, j, k), var in solution_vars.items(): if value(var) == 1: ...`
- Explain that team_size comes from the combination variable, not from `value(num_people)` directly

---

#### 4. **Missing Import for LpStatus**
**Location:** Cell 18 (Solution Display)

**Problem:**
- Template uses: `print(f"Solution Status: {model.status}")`
- This prints a numeric code (e.g., 1) instead of readable status (e.g., "Optimal")
- Missing `from pulp import LpStatus` in imports

**What Example Solution Does:**
- Imports `LpStatus` in the solve cell
- Uses `status = LpStatus[model.status]` to get readable status
- Displays "Optimal" instead of "1"

**Recommendation:**
- Add `LpStatus` to the imports in Cell 3
- Update Cell 18 to use `LpStatus[model.status]` for readable output

---

#### 5. **Missing Guidance on Hotel vs Airbnb Cost Structure**
**Location:** Cell 17 (Constraints)

**Problem:**
- Template doesn't explain that hotels charge per room (2 people) vs Airbnbs charge per person
- No guidance on how to handle this in the linear model
- Students might try to use integer division `(num_people + 1) // 2` which is non-linear

**What Example Solution Does:**
- Uses linear approximation: `(cost_per_night / 2) * conference_dates * k` for hotels
- Explains this is an approximation (room cost divided by 2, then multiplied by team size)
- Notes this is reasonable for the model

**Recommendation:**
- Add explanation of hotel vs Airbnb cost structure
- Explain the linear approximation approach
- Note that exact room calculation (integer division) would be non-linear

---

### MODERATE ISSUES (May cause confusion or errors)

#### 6. **Part 2: Missing Warning About Non-Linear Expressions**
**Location:** Cells 21, 23 (Stakeholder Considerations Implementation)

**Problem:**
- Template doesn't warn students about avoiding non-linear expressions in demonstration cells
- Students might try to create PuLP expressions like `(event_cost * attend_event) * num_people`
- This would cause the same multiplication error

**What Example Solution Does:**
- Uses regular Python numbers for demonstration calculations
- Includes comment: "NOTE: This cell demonstrates the concept with example calculations"
- Notes that actual PuLP implementation is in the next cell

**Recommendation:**
- Add warning in Part 2 cells about using regular Python numbers for demonstrations
- Clarify that PuLP model updates should be in separate cells
- Warn against multiplying PuLP variables in demonstration cells

---

#### 7. **Part 2: Missing Guidance on Updating Model**
**Location:** Cells 21, 23 (Stakeholder Considerations Implementation)

**Problem:**
- Template just says: "# TODO: Update your PuLP model to incorporate Consideration 1"
- Doesn't explain that students should create a NEW model (`model_updated`) or recreate the existing one
- Doesn't mention that they'll need to use the same combination variable approach
- Doesn't explain how to handle new costs (like per diem or networking events) that depend on team size

**What Example Solution Does:**
- Creates `model_updated = LpProblem(...)` as a new model
- Uses `solution_vars2` with the same combination approach
- For per diem: adds cost to each combination as a constant
- For networking events: uses `event_team_vars` to link events to team sizes

**Recommendation:**
- Add guidance on whether to create new model or update existing
- Explain that combination variable approach must be maintained
- Provide guidance on handling new costs that depend on team size
- Show pattern for adding costs to combination variables

---

#### 8. **Missing Guidance on Constraint Structure**
**Location:** Cell 17 (Constraints)

**Problem:**
- Template lists constraints but doesn't explain the structure needed
- Doesn't mention the "One_Combination" constraint (exactly one solution_vars[(i,j,k)] == 1)
- Doesn't explain the "Link_Num_People" constraint that connects num_people to the combination
- Doesn't show how to structure rating/distance constraints with combination variables

**What Example Solution Does:**
- Includes "One_Combination" constraint ensuring exactly one combination is selected
- Includes "Link_Num_People" constraint: `num_people == lpSum([k * solution_vars[(i,j,k)] ...])`
- Shows how to structure rating constraint using nested `lpSum` with combination variables
- Shows pattern for distance constraint

**Recommendation:**
- Add explanation of required constraint structure
- Show the "One_Combination" and "Link_Num_People" constraints as required
- Provide examples of how to structure rating/distance constraints with combination variables

---

### MINOR ISSUES (Clarity and consistency)

#### 9. **Inconsistent Variable Naming in Comments**
**Location:** Throughout template

**Problem:**
- Template uses generic names in comments (e.g., `variable_name`, `cost_i`)
- Doesn't match the actual variable names students should use
- Could be clearer about naming conventions

**Recommendation:**
- Use more descriptive example names that match the domain
- Consider showing actual variable name patterns (e.g., `solution_vars`, `num_people`)

---

#### 10. **Missing Hotel Cost Calculation in Solution Display**
**Location:** Cell 18 (Solution Display)

**Problem:**
- Template comment: `# - Lodging cost: $X (cost_per_night * nights * num_people)`
- Doesn't account for hotel vs Airbnb difference
- Doesn't show the `num_rooms = (team_size + 1) // 2` calculation for hotels

**What Example Solution Does:**
- Checks lodging type and calculates differently for hotels vs Airbnbs
- Uses integer division for hotels: `num_rooms = (team_size + 1) // 2`
- Uses direct multiplication for Airbnbs: `cost_per_night * conference_dates * team_size`

**Recommendation:**
- Update solution display guidance to show hotel vs Airbnb cost calculation
- Explain that this is for display only (not in the model)

---

#### 11. **Part 2: Missing Guidance on Model Recreation**
**Location:** Cell 24 (Solve Updated Model)

**Problem:**
- Template says: `# Solve the updated model` but doesn't clarify if `model` was updated or if it's `model_updated`
- Doesn't explain that if they created a new model, they need to use that model name

**What Example Solution Does:**
- Uses `model_updated.solve()` since a new model was created
- Clearly separates original model from updated model

**Recommendation:**
- Clarify which model variable to use for solving
- If suggesting new model creation, be explicit about variable names

---

#### 12. **Missing Guidance on Comparison Variables**
**Location:** Cell 26 (Comparison Visualization)

**Problem:**
- Template doesn't explain that students need to save values from the original solution
- Doesn't mention that `selected_team_size` needs to be stored for comparison
- Doesn't explain how to access values from the original model after creating a new model

**What Example Solution Does:**
- Stores `selected_team_size` from first model solution
- Uses `selected_team_size` and `selected_team_size2` for comparison
- Shows how to access both original and updated solution values

**Recommendation:**
- Add guidance on storing original solution values before creating updated model
- Explain how to access values from both models for comparison

---

### SUMMARY OF PRIORITIES

**MUST FIX (Will cause errors):**
1. Add combination variables approach guidance (Cell 15)
2. Fix cost calculation comments (Cell 17)
3. Add solution extraction guidance (Cell 18)
4. Add LpStatus import (Cell 3, Cell 18)
5. Add hotel vs Airbnb cost structure explanation (Cell 17)

**SHOULD FIX (Will cause confusion/errors in Part 2):**
6. Add warning about non-linear expressions in Part 2 (Cells 21, 23)
7. Add guidance on updating model structure (Cells 21, 23)
8. Add constraint structure explanation (Cell 17)

**NICE TO FIX (Clarity):**
9. Improve variable naming in comments
10. Add hotel cost calculation to solution display guidance
11. Clarify model variable naming in Part 2
12. Add comparison variable storage guidance

---

### KEY INSIGHT

The fundamental issue is that the template doesn't address PuLP's linearity requirement. Students will naturally try to create separate variables and multiply them (e.g., `num_people * lodging_vars[i]`), which is intuitive but mathematically non-linear. The combination variable approach is a standard linearization technique, but it's not obvious to beginners. The template needs explicit guidance on this approach.
