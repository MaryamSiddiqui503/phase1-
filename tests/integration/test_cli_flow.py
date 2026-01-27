"""
Integration tests for the CLI flow.

This module contains integration tests for the full application flow,
testing the interaction between the CLI interface and the TaskManager.
"""

import io
import sys
from unittest.mock import patch, MagicMock
from src.services.task_manager import TaskManager
from src.cli.menu import (
    display_menu, get_user_choice, get_task_details, get_task_id,
    add_task_ui, view_tasks_ui, update_task_ui, delete_task_ui,
    toggle_task_status_ui, handle_menu_option, run_menu_loop
)


def test_display_menu(capsys):
    """Test that the menu is displayed correctly."""
    display_menu()
    captured = capsys.readouterr()

    output = captured.out
    assert "--- Todo App Menu ---" in output
    assert "1. Add Task" in output
    assert "2. View Tasks" in output
    assert "3. Update Task" in output
    assert "4. Delete Task" in output
    assert "5. Mark Task as Complete/Incomplete" in output
    assert "6. Exit" in output


def test_get_user_choice():
    """Test getting user choice from input."""
    with patch('builtins.input', return_value='1'):
        choice = get_user_choice()
        assert choice == '1'


def test_get_task_details():
    """Test getting task details from user input."""
    with patch('builtins.input', side_effect=['Test Title', 'Test Description']):
        title, description = get_task_details()
        assert title == 'Test Title'
        assert description == 'Test Description'


def test_get_task_details_no_description():
    """Test getting task details with empty description."""
    with patch('builtins.input', side_effect=['Test Title', '']):
        title, description = get_task_details()
        assert title == 'Test Title'
        assert description is None


def test_get_task_id_valid():
    """Test getting a valid task ID."""
    with patch('builtins.input', return_value='5'):
        task_id = get_task_id()
        assert task_id == 5


def test_get_task_id_invalid():
    """Test getting an invalid task ID."""
    with patch('builtins.input', return_value='abc'):
        task_id = get_task_id()
        assert task_id is None


def test_get_task_id_negative():
    """Test getting a negative task ID."""
    with patch('builtins.input', return_value='-1'):
        task_id = get_task_id()
        assert task_id is None


def test_add_task_ui_success():
    """Test adding a task via UI."""
    task_manager = TaskManager()

    with patch('builtins.input', side_effect=['New Task Title', 'New Task Description']):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            add_task_ui(task_manager)

            # Check that the task was added
            assert task_manager.get_task_count() == 1
            task = task_manager.get_all_tasks()[0]
            assert task.title == 'New Task Title'
            assert task.description == 'New Task Description'

            # Check output message
            output = mock_stdout.getvalue()
            assert 'added successfully' in output


def test_view_tasks_ui_empty():
    """Test viewing tasks when there are no tasks."""
    task_manager = TaskManager()

    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        view_tasks_ui(task_manager)

        output = mock_stdout.getvalue()
        assert 'No tasks found.' in output


def test_view_tasks_ui_with_tasks():
    """Test viewing tasks when there are tasks."""
    task_manager = TaskManager()
    task_manager.add_task(title='Task 1', description='Description 1')
    task_manager.add_task(title='Task 2', completed=True)

    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        view_tasks_ui(task_manager)

        output = mock_stdout.getvalue()
        assert 'Task 1' in output
        assert 'Description 1' in output
        assert 'Task 2' in output


def test_update_task_ui():
    """Test updating a task via UI."""
    task_manager = TaskManager()
    task = task_manager.add_task(title='Old Title', description='Old Description')

    # Mock user input: task ID, new title, new description
    with patch('builtins.input', side_effect=[str(task.id), 'New Title', 'New Description']):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            update_task_ui(task_manager)

            # Check that the task was updated
            updated_task = task_manager.get_task_by_id(task.id)
            assert updated_task.title == 'New Title'
            assert updated_task.description == 'New Description'

            output = mock_stdout.getvalue()
            assert 'Task updated successfully' in output


def test_delete_task_ui():
    """Test deleting a task via UI."""
    task_manager = TaskManager()
    task = task_manager.add_task(title='Task to Delete')

    # Mock user input: task ID, confirmation
    with patch('builtins.input', side_effect=[str(task.id), 'y']):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            delete_task_ui(task_manager)

            # Check that the task was deleted
            assert task_manager.get_task_by_id(task.id) is None

            output = mock_stdout.getvalue()
            assert 'deleted successfully' in output


def test_toggle_task_status_ui_complete():
    """Test marking a task as complete via UI."""
    task_manager = TaskManager()
    task = task_manager.add_task(title='Incomplete Task', completed=False)

    # Mock user input: task ID, confirmation
    with patch('builtins.input', side_effect=[str(task.id), 'y']):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            toggle_task_status_ui(task_manager)

            # Check that the task status was updated
            updated_task = task_manager.get_task_by_id(task.id)
            assert updated_task.completed is True

            output = mock_stdout.getvalue()
            assert 'marked as completed' in output


def test_toggle_task_status_ui_incomplete():
    """Test marking a task as incomplete via UI."""
    task_manager = TaskManager()
    task = task_manager.add_task(title='Complete Task', completed=True)

    # Mock user input: task ID, confirmation
    with patch('builtins.input', side_effect=[str(task.id), 'y']):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            toggle_task_status_ui(task_manager)

            # Check that the task status was updated
            updated_task = task_manager.get_task_by_id(task.id)
            assert updated_task.completed is False

            output = mock_stdout.getvalue()
            assert 'marked as incomplete' in output


def test_handle_menu_option_add_task():
    """Test handling the 'add task' menu option."""
    task_manager = TaskManager()

    with patch('builtins.input', side_effect=['New Task', 'New Description']):
        with patch('sys.stdout', new_callable=io.StringIO):
            continue_app = handle_menu_option('1', task_manager)

            # Should continue the app
            assert continue_app is True
            # Should have added a task
            assert task_manager.get_task_count() == 1


def test_handle_menu_option_exit():
    """Test handling the 'exit' menu option."""
    task_manager = TaskManager()

    continue_app = handle_menu_option('6', task_manager)

    # Should not continue the app
    assert continue_app is False


def test_handle_menu_option_invalid():
    """Test handling an invalid menu option."""
    task_manager = TaskManager()

    with patch('sys.stdout', new_callable=io.StringIO):
        continue_app = handle_menu_option('99', task_manager)

        # Should continue the app (just show error)
        assert continue_app is True


def test_full_application_flow():
    """Test the full application flow with multiple operations."""
    task_manager = TaskManager()

    # Add a task
    task_manager.add_task(title="Initial Task", description="Initial Description")
    assert task_manager.get_task_count() == 1

    # Get the task
    task = task_manager.get_all_tasks()[0]
    assert task.title == "Initial Task"
    assert task.description == "Initial Description"
    assert task.completed is False

    # Update the task
    updated_task = task_manager.update_task(
        task_id=task.id,
        title="Updated Task",
        description="Updated Description",
        completed=True
    )
    assert updated_task is not None
    assert updated_task.title == "Updated Task"
    assert updated_task.description == "Updated Description"
    assert updated_task.completed is True

    # Mark as incomplete
    incomplete_task = task_manager.mark_task_incomplete(task.id)
    assert incomplete_task is not None
    assert incomplete_task.completed is False

    # Delete the task
    deleted = task_manager.delete_task(task.id)
    assert deleted is True
    assert task_manager.get_task_count() == 0