# ADR-005: Task Data Model Design

## Status
Accepted

## Date
2026-01-27

## Context
The application requires a standardized Task entity to represent todo items. The specification defines basic attributes for tasks, but implementation details need to be standardized. The model must support the required CRUD operations and state transitions while maintaining data integrity within the in-memory storage constraints.

## Decision
We will implement a Task entity with the following attributes and characteristics:
- **id**: int (unique identifier, auto-incremented starting from 1)
- **title**: str (required, non-empty string after trimming whitespace)
- **description**: str (optional, can be None or empty string)
- **completed**: bool (default: False)

With validation rules:
- `id`: Must be a positive integer, auto-generated, unique within the session
- `title`: Required field, must be a non-empty string after trimming whitespace
- `description`: Optional field, can be None or any string value
- `completed`: Boolean value only, default to False when creating new tasks

State transitions:
- `incomplete` → `completed`: When user marks task as complete
- `completed` → `incomplete`: When user marks task as incomplete

## Alternatives Considered
- Using a dictionary instead of a class (rejected for type safety and validation benefits)
- Adding more complex fields (due dates, categories, etc.) (rejected as out of scope per constitution)
- Using named tuples (rejected for mutability requirements)
- Using dataclasses (considered but class approach chosen for more control over validation)

## Consequences
Positive:
- Clear, standardized structure for task data
- Built-in validation rules ensuring data integrity
- Support for required state transitions
- Type safety and IDE support
- Compliance with specification requirements

Negative:
- Additional complexity compared to simple dictionary approach
- Need for validation logic maintenance
- Potential overhead for simple data storage

## References
- spec.md: Data Models section
- data-model.md: Task Entity section
- Plan.md: Project Structure showing models/task.py