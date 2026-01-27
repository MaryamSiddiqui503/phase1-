"""
Task model for the Todo App Phase I.

This module defines the Task entity with id, title, description, and completed fields,
along with validation rules as specified in the data model.
"""

from typing import Optional


class Task:
    """
    Represents a task in the todo application.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Required title of the task
        description (Optional[str]): Optional description of the task
        completed (bool): Completion status of the task (default: False)
    """

    def __init__(self, id: int, title: str, description: Optional[str] = None, completed: bool = False):
        """
        Initialize a Task instance.

        Args:
            id: Unique identifier for the task (positive integer)
            title: Required title of the task (non-empty string after trimming)
            description: Optional description of the task
            completed: Completion status of the task (default: False)

        Raises:
            ValueError: If validation rules are violated
        """
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

        # Validate the task upon initialization
        self._validate()

    @property
    def id(self) -> int:
        """Get the task ID."""
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        """Set the task ID with validation."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"Task ID must be a positive integer, got {value}")
        self._id = value

    @property
    def title(self) -> str:
        """Get the task title."""
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        """Set the task title with validation."""
        if not isinstance(value, str):
            raise ValueError(f"Task title must be a string, got {type(value).__name__}")

        trimmed_title = value.strip()
        if not trimmed_title:
            raise ValueError("Task title cannot be empty or contain only whitespace")

        self._title = trimmed_title

    @property
    def description(self) -> Optional[str]:
        """Get the task description."""
        return self._description

    @description.setter
    def description(self, value: Optional[str]) -> None:
        """Set the task description with validation."""
        if value is not None and not isinstance(value, str):
            raise ValueError(f"Task description must be a string or None, got {type(value).__name__}")
        self._description = value

    @property
    def completed(self) -> bool:
        """Get the task completion status."""
        return self._completed

    @completed.setter
    def completed(self, value: bool) -> None:
        """Set the task completion status."""
        if not isinstance(value, bool):
            raise ValueError(f"Task completion status must be a boolean, got {type(value).__name__}")
        self._completed = value

    def _validate(self) -> None:
        """
        Validate the task according to the data model rules.

        Raises:
            ValueError: If any validation rule is violated
        """
        # Validate ID: Must be a positive integer
        if not isinstance(self._id, int) or self._id <= 0:
            raise ValueError(f"Task ID must be a positive integer, got {self._id}")

        # Validate title: Required field, must be non-empty after trimming
        if not isinstance(self._title, str):
            raise ValueError(f"Task title must be a string, got {type(self._title).__name__}")

        trimmed_title = self._title.strip()
        if not trimmed_title:
            raise ValueError("Task title cannot be empty or contain only whitespace")

    def to_dict(self) -> dict:
        """
        Convert the task to a dictionary representation.

        Returns:
            A dictionary containing the task's attributes
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    def __repr__(self) -> str:
        """String representation of the Task."""
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"

    def __eq__(self, other) -> bool:
        """Check equality with another Task."""
        if not isinstance(other, Task):
            return False
        return (
            self.id == other.id and
            self.title == other.title and
            self.description == other.description and
            self.completed == other.completed
        )