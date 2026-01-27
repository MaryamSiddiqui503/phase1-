"""
Task Manager for the Todo App Phase I.

This module implements the TaskManager class that manages in-memory storage
and operations on tasks according to the data model and specifications.
"""

from typing import Dict, List, Optional
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from models.task import Task


class TaskManager:
    """
    Manages in-memory storage and operations on tasks.

    The TaskManager stores tasks in a dictionary with `id` as key and Task object as value,
    and maintains an auto-increment counter for generating unique IDs.
    """

    def __init__(self):
        """
        Initialize the TaskManager with empty storage and ID counter.
        """
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None, completed: bool = False) -> Task:
        """
        Add a new task to the manager.

        Args:
            title: Required title of the task
            description: Optional description of the task
            completed: Completion status of the task (default: False)

        Returns:
            The newly created Task object

        Raises:
            ValueError: If validation rules are violated
        """
        # Create a new task with the next available ID
        task = Task(
            id=self._get_next_id(),
            title=title,
            description=description,
            completed=completed
        )

        # Store the task in memory
        self._tasks[task.id] = task
        return task

    def _get_next_id(self) -> int:
        """
        Get the next available ID for a task.

        Returns:
            The next available ID
        """
        next_id = self._next_id
        self._next_id += 1
        return next_id

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks managed by this TaskManager.

        Returns:
            A list of all Task objects, sorted by ID
        """
        return sorted(list(self._tasks.values()), key=lambda task: task.id)

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, title: Optional[str] = None,
                    description: Optional[str] = None, completed: Optional[bool] = None) -> Optional[Task]:
        """
        Update an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title for the task (optional)
            description: New description for the task (optional)
            completed: New completion status for the task (optional)

        Returns:
            The updated Task object if successful, None if task not found

        Raises:
            ValueError: If validation rules are violated
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return None

        # Update the task properties if provided
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if completed is not None:
            task.completed = completed

        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if the task was not found
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def mark_task_completed(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as completed.

        Args:
            task_id: The ID of the task to mark as completed

        Returns:
            The updated Task object if successful, None if task not found
        """
        return self.update_task(task_id, completed=True)

    def mark_task_incomplete(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark as incomplete

        Returns:
            The updated Task object if successful, None if task not found
        """
        return self.update_task(task_id, completed=False)

    def get_next_id(self) -> int:
        """
        Get the next ID that will be assigned to a new task.

        Returns:
            The next available ID
        """
        return self._next_id

    def get_task_count(self) -> int:
        """
        Get the total number of tasks.

        Returns:
            The number of tasks in the manager
        """
        return len(self._tasks)