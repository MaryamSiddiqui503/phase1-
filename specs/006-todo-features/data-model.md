# Data Model: Todo App Phase I

## Task Entity

### Fields
- **id**: int (unique identifier, auto-incremented starting from 1)
- **title**: str (required, non-empty string)
- **description**: str (optional, can be None or empty string)
- **completed**: bool (default: False)

### Validation Rules
- `id`: Must be a positive integer, auto-generated, unique within the session
- `title`: Required field, must be a non-empty string after trimming whitespace
- `description`: Optional field, can be None or any string value
- `completed`: Boolean value only, default to False when creating new tasks

### State Transitions
- `incomplete` → `completed`: When user marks task as complete
- `completed` → `incomplete`: When user marks task as incomplete

### Relationships
- No relationships with other entities (standalone entity for this phase)

## In-Memory Storage Structure
- Store tasks in a Python dictionary with `id` as key and Task object as value
- Maintain an auto-increment counter for generating unique IDs
- All data exists only in application memory, lost upon program termination