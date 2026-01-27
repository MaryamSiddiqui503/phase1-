# ADR-003: Separation of Concerns Architecture Pattern

## Status
Accepted

## Date
2026-01-27

## Context
The application needs to follow clean architecture principles with clear separation of concerns to ensure maintainability and testability. The specification outlines distinct responsibilities for different parts of the system: Main Application, Task Manager, Input Validator, and Output Formatter.

## Decision
We will implement a layered architecture with clear separation of concerns:
- **Models Layer** (`src/models/task.py`): Contains the Task entity definition with validation rules
- **Services Layer** (`src/services/task_manager.py`): Handles business logic and in-memory operations for tasks
- **CLI Layer** (`src/cli/menu.py`): Manages user interface and input/output operations
- **Main Module** (`src/main.py`): Orchestrates the application flow

This follows the architecture outlined in the specification with responsibilities distributed across modules as:
- Data models: Task entity definition and validation
- Business logic: Task operations (CRUD) and state management
- Presentation: Console interface and user interaction handling

## Alternatives Considered
- Monolithic approach with all functionality in a single file (rejected for maintainability concerns)
- MVC (Model-View-Controller) pattern (rejected as overkill for console application)
- Event-driven architecture (rejected as unnecessary complexity for this scope)

## Consequences
Positive:
- Clear separation of business logic, data models, and presentation
- Improved testability with isolated components
- Better maintainability with focused responsibilities
- Easier to extend individual components without affecting others
- Aligns with clean code principles and PEP 8 compliance

Negative:
- More files and modules to navigate
- Potential overhead from inter-module communication
- Slightly more complex initial setup

## References
- Plan.md: Project Structure section
- spec.md: High-Level Architecture section
- Plan.md: Structure Decision section