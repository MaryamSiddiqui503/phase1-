"""
Unit tests for the TaskManager class.

This module contains unit tests for the TaskManager class and its functionality.
"""

import pytest
from src.models.task import Task
from src.services.task_manager import TaskManager


def test_task_manager_initialization():
    """Test initializing a TaskManager instance."""
    tm = TaskManager()

    assert tm.get_task_count() == 0
    assert len(tm.get_all_tasks()) == 0
    assert tm.get_next_id() == 1


def test_add_task_basic():
    """Test adding a basic task to the TaskManager."""
    tm = TaskManager()

    task = tm.add_task(title="Test Task", description="Test Description")

    assert tm.get_task_count() == 1
    assert len(tm.get_all_tasks()) == 1
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False


def test_add_multiple_tasks():
    """Test adding multiple tasks to the TaskManager."""
    tm = TaskManager()

    task1 = tm.add_task(title="First Task")
    task2 = tm.add_task(title="Second Task", description="Second Description", completed=True)

    assert tm.get_task_count() == 2
    assert len(tm.get_all_tasks()) == 2

    # Check that IDs are auto-incremented
    assert task1.id == 1
    assert task2.id == 2

    # Check that both tasks are retrievable
    retrieved_task1 = tm.get_task_by_id(1)
    retrieved_task2 = tm.get_task_by_id(2)

    assert retrieved_task1 is not None
    assert retrieved_task2 is not None
    assert retrieved_task1.title == "First Task"
    assert retrieved_task2.title == "Second Task"
    assert retrieved_task2.completed is True


def test_get_all_tasks_sorted():
    """Test that get_all_tasks returns tasks sorted by ID."""
    tm = TaskManager()

    # Add tasks in reverse order to test sorting
    tm.add_task(title="Third Task")  # ID: 3
    tm.add_task(title="First Task")  # ID: 1
    tm.add_task(title="Second Task")  # ID: 2

    tasks = tm.get_all_tasks()

    assert len(tasks) == 3
    assert tasks[0].id == 1
    assert tasks[1].id == 2
    assert tasks[2].id == 3


def test_get_task_by_id():
    """Test retrieving a task by its ID."""
    tm = TaskManager()

    task = tm.add_task(title="Test Task", description="Test Description")

    retrieved_task = tm.get_task_by_id(task.id)
    assert retrieved_task is not None
    assert retrieved_task.id == task.id
    assert retrieved_task.title == task.title
    assert retrieved_task.description == task.description
    assert retrieved_task.completed == task.completed

    # Test retrieving non-existent task
    non_existent_task = tm.get_task_by_id(999)
    assert non_existent_task is None


def test_update_task():
    """Test updating an existing task."""
    tm = TaskManager()

    original_task = tm.add_task(title="Original Title", description="Original Description", completed=False)

    # Update all fields
    updated_task = tm.update_task(
        task_id=original_task.id,
        title="Updated Title",
        description="Updated Description",
        completed=True
    )

    assert updated_task is not None
    assert updated_task.id == original_task.id
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Updated Description"
    assert updated_task.completed is True

    # Verify the task was actually updated in storage
    retrieved_task = tm.get_task_by_id(original_task.id)
    assert retrieved_task is not None
    assert retrieved_task.title == "Updated Title"
    assert retrieved_task.description == "Updated Description"
    assert retrieved_task.completed is True


def test_update_task_partial():
    """Test updating only some fields of a task."""
    tm = TaskManager()

    original_task = tm.add_task(title="Original Title", description="Original Description", completed=False)

    # Update only the title
    updated_task = tm.update_task(task_id=original_task.id, title="Updated Title")

    assert updated_task is not None
    assert updated_task.id == original_task.id
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Original Description"  # Should remain unchanged
    assert updated_task.completed is False  # Should remain unchanged

    # Update only the completion status
    updated_task2 = tm.update_task(task_id=original_task.id, completed=True)

    assert updated_task2 is not None
    assert updated_task2.id == original_task.id
    assert updated_task2.title == "Updated Title"  # Should remain unchanged
    assert updated_task2.description == "Original Description"  # Should remain unchanged
    assert updated_task2.completed is True


def test_update_nonexistent_task():
    """Test updating a task that doesn't exist."""
    tm = TaskManager()

    result = tm.update_task(task_id=999, title="Should Not Exist")
    assert result is None


def test_delete_task():
    """Test deleting an existing task."""
    tm = TaskManager()

    task = tm.add_task(title="Task to Delete")

    # Verify task exists
    assert tm.get_task_count() == 1
    assert tm.get_task_by_id(task.id) is not None

    # Delete the task
    result = tm.delete_task(task.id)
    assert result is True

    # Verify task is gone
    assert tm.get_task_count() == 0
    assert tm.get_task_by_id(task.id) is None

    # Try to delete the same task again
    result = tm.delete_task(task.id)
    assert result is False


def test_delete_nonexistent_task():
    """Test deleting a task that doesn't exist."""
    tm = TaskManager()

    result = tm.delete_task(999)
    assert result is False


def test_mark_task_completed():
    """Test marking a task as completed."""
    tm = TaskManager()

    task = tm.add_task(title="Incomplete Task", completed=False)

    # Verify initial state
    assert task.completed is False

    # Mark as completed
    updated_task = tm.mark_task_completed(task.id)
    assert updated_task is not None
    assert updated_task.completed is True

    # Verify the change was persisted
    retrieved_task = tm.get_task_by_id(task.id)
    assert retrieved_task is not None
    assert retrieved_task.completed is True


def test_mark_task_incomplete():
    """Test marking a task as incomplete."""
    tm = TaskManager()

    task = tm.add_task(title="Complete Task", completed=True)

    # Verify initial state
    assert task.completed is True

    # Mark as incomplete
    updated_task = tm.mark_task_incomplete(task.id)
    assert updated_task is not None
    assert updated_task.completed is False

    # Verify the change was persisted
    retrieved_task = tm.get_task_by_id(task.id)
    assert retrieved_task is not None
    assert retrieved_task.completed is False


def test_mark_nonexistent_task():
    """Test marking completion status of a task that doesn't exist."""
    tm = TaskManager()

    result = tm.mark_task_completed(999)
    assert result is None

    result = tm.mark_task_incomplete(999)
    assert result is None


def test_next_id_generation():
    """Test that the next ID is correctly generated."""
    tm = TaskManager()

    assert tm.get_next_id() == 1

    tm.add_task(title="First Task")
    assert tm.get_next_id() == 2

    tm.add_task(title="Second Task")
    assert tm.get_next_id() == 3

    # Delete a task - next ID should continue from where it left off
    tm.delete_task(1)
    assert tm.get_next_id() == 3


def test_task_validation_in_add_task():
    """Test that validation is enforced when adding tasks."""
    tm = TaskManager()

    # Attempt to add a task with invalid title
    with pytest.raises(ValueError):
        tm.add_task(title="", description="This should fail")

    # Verify no task was added
    assert tm.get_task_count() == 0


def test_task_validation_in_update_task():
    """Test that validation is enforced when updating tasks."""
    tm = TaskManager()

    task = tm.add_task(title="Valid Task")

    # Attempt to update with invalid title
    with pytest.raises(ValueError):
        tm.update_task(task_id=task.id, title="")


def test_get_task_count():
    """Test getting the task count."""
    tm = TaskManager()

    assert tm.get_task_count() == 0

    tm.add_task(title="First Task")
    assert tm.get_task_count() == 1

    tm.add_task(title="Second Task")
    assert tm.get_task_count() == 2

    tm.delete_task(1)
    assert tm.get_task_count() == 1

    tm.delete_task(2)
    assert tm.get_task_count() == 0