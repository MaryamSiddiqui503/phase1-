"""
Unit tests for the Task model.

This module contains unit tests for the Task class and its validation rules.
"""

import pytest
from src.models.task import Task


def test_task_creation_valid():
    """Test creating a valid Task instance."""
    task = Task(id=1, title="Test Task", description="Test Description", completed=False)

    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False


def test_task_creation_minimal():
    """Test creating a Task with minimal required parameters."""
    task = Task(id=1, title="Minimal Task")

    assert task.id == 1
    assert task.title == "Minimal Task"
    assert task.description is None
    assert task.completed is False


def test_task_creation_default_completed():
    """Test creating a Task with default completed status."""
    task = Task(id=1, title="Default Completed Task", description="Task with default status")

    assert task.id == 1
    assert task.title == "Default Completed Task"
    assert task.description == "Task with default status"
    assert task.completed is False


def test_task_creation_completed_true():
    """Test creating a Task with completed status set to True."""
    task = Task(id=1, title="Completed Task", completed=True)

    assert task.id == 1
    assert task.title == "Completed Task"
    assert task.completed is True


def test_task_id_validation_positive():
    """Test that Task ID must be a positive integer."""
    with pytest.raises(ValueError):
        Task(id=0, title="Invalid ID Task")

    with pytest.raises(ValueError):
        Task(id=-1, title="Negative ID Task")

    with pytest.raises(ValueError):
        Task(id="invalid", title="String ID Task")


def test_task_title_required():
    """Test that Task title cannot be empty."""
    with pytest.raises(ValueError):
        Task(id=1, title="")

    with pytest.raises(ValueError):
        Task(id=1, title="   ")  # Only whitespace

    with pytest.raises(ValueError):
        Task(id=1, title="\t\n")  # Whitespace characters


def test_task_title_type_validation():
    """Test that Task title must be a string."""
    with pytest.raises(ValueError):
        Task(id=1, title=123)

    with pytest.raises(ValueError):
        Task(id=1, title=None)


def test_task_description_optional():
    """Test that Task description can be None or empty."""
    task = Task(id=1, title="Valid Task", description=None)
    assert task.description is None

    task = Task(id=1, title="Valid Task", description="")
    assert task.description == ""


def test_task_description_type_validation():
    """Test that Task description must be a string or None."""
    with pytest.raises(ValueError):
        Task(id=1, title="Valid Task", description=123)

    with pytest.raises(ValueError):
        Task(id=1, title="Valid Task", description=[])


def test_task_completed_validation():
    """Test that Task completed status must be a boolean."""
    with pytest.raises(ValueError):
        Task(id=1, title="Invalid Completed Task", completed="true")

    with pytest.raises(ValueError):
        Task(id=1, title="Invalid Completed Task", completed=1)

    with pytest.raises(ValueError):
        Task(id=1, title="Invalid Completed Task", completed=0)


def test_task_title_trimmed():
    """Test that Task title is trimmed of leading/trailing whitespace."""
    task = Task(id=1, title="  Trimmed Title  ")
    assert task.title == "Trimmed Title"


def test_task_to_dict():
    """Test converting Task to dictionary representation."""
    task = Task(id=1, title="Test Task", description="Test Description", completed=True)
    expected_dict = {
        "id": 1,
        "title": "Test Task",
        "description": "Test Description",
        "completed": True
    }

    assert task.to_dict() == expected_dict


def test_task_repr():
    """Test string representation of Task."""
    task = Task(id=1, title="Test Task", description="Test Description", completed=True)
    repr_str = repr(task)

    assert "Task" in repr_str
    assert "id=1" in repr_str
    assert "title='Test Task'" in repr_str
    assert "description='Test Description'" in repr_str
    assert "completed=True" in repr_str


def test_task_equality():
    """Test equality comparison between Task instances."""
    task1 = Task(id=1, title="Test Task", description="Test Description", completed=True)
    task2 = Task(id=1, title="Test Task", description="Test Description", completed=True)

    assert task1 == task2

    # Different ID
    task3 = Task(id=2, title="Test Task", description="Test Description", completed=True)
    assert task1 != task3

    # Different title
    task4 = Task(id=1, title="Different Task", description="Test Description", completed=True)
    assert task1 != task4

    # Compare with non-Task object
    assert task1 != "not a task"


def test_task_properties_setters():
    """Test that property setters enforce validation."""
    task = Task(id=1, title="Initial Title")

    # Valid updates
    task.title = "New Title"
    assert task.title == "New Title"

    task.description = "New Description"
    assert task.description == "New Description"

    task.completed = True
    assert task.completed is True

    # Invalid updates should raise exceptions
    with pytest.raises(ValueError):
        task.id = -1

    with pytest.raises(ValueError):
        task.title = ""

    with pytest.raises(ValueError):
        task.completed = "not a boolean"