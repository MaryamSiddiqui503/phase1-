"""
CLI Menu for the Todo App Phase I.

This module implements the console interface for interacting with tasks,
including functions for adding, viewing, updating, deleting, and marking tasks.
"""

from typing import Optional
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from services.task_manager import TaskManager


def display_menu() -> None:
    """
    Display the main menu options to the user.
    """
    print("\n--- Todo App Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete/Incomplete")
    print("6. Exit")
    print("---------------------")


def get_user_choice() -> str:
    """
    Get the user's menu choice.

    Returns:
        The user's choice as a string
    """
    return input("Please select an option (1-6): ").strip()


def get_task_details() -> tuple[str, Optional[str]]:
    """
    Get task details from user input.

    Returns:
        A tuple containing the title and optional description
    """
    title = input("Enter task title: ").strip()

    description_input = input("Enter task description (optional, press Enter to skip): ").strip()
    description = description_input if description_input else None

    return title, description


def get_task_id() -> Optional[int]:
    """
    Get a task ID from user input.

    Returns:
        The task ID if valid, None otherwise
    """
    try:
        task_id_input = input("Enter task ID: ").strip()
        if not task_id_input:
            print("Task ID cannot be empty.")
            return None

        task_id = int(task_id_input)
        if task_id <= 0:
            print("Task ID must be a positive integer.")
            return None

        return task_id
    except ValueError:
        print("Invalid task ID. Please enter a valid integer.")
        return None


def add_task_ui(task_manager: TaskManager) -> None:
    """
    UI function for adding a new task.

    Args:
        task_manager: The TaskManager instance to use
    """
    print("\n--- Add New Task ---")
    try:
        title, description = get_task_details()

        # Validate title
        if not title.strip():
            print("Error: Task title cannot be empty.")
            return

        task = task_manager.add_task(title=title, description=description)
        print(f"Task '{task.title}' added successfully with ID: {task.id}")
    except ValueError as e:
        print(f"Error: {e}")


def view_tasks_ui(task_manager: TaskManager) -> None:
    """
    UI function for viewing all tasks.

    Args:
        task_manager: The TaskManager instance to use
    """
    print("\n--- All Tasks ---")
    tasks = task_manager.get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "✓" if task.completed else "○"
        desc = task.description if task.description else "(No description)"
        print(f"{status} [{task.id}] {task.title}")
        print(f"    Description: {desc}")
        print()


def update_task_ui(task_manager: TaskManager) -> None:
    """
    UI function for updating a task.

    Args:
        task_manager: The TaskManager instance to use
    """
    print("\n--- Update Task ---")
    task_id = get_task_id()
    if task_id is None:
        return

    # Check if task exists
    existing_task = task_manager.get_task_by_id(task_id)
    if existing_task is None:
        print(f"No task found with ID {task_id}.")
        return

    print(f"Updating task: {existing_task.title}")

    # Get new details, keeping existing values if user doesn't provide new ones
    title_input = input(f"Enter new title (current: '{existing_task.title}', press Enter to keep current): ").strip()
    title = title_input if title_input else existing_task.title

    description_input = input(f"Enter new description (current: '{existing_task.description or '(No description)'}', press Enter to keep current): ").strip()
    description = description_input if description_input != "" else existing_task.description

    try:
        updated_task = task_manager.update_task(task_id, title=title, description=description)
        if updated_task:
            print(f"Task updated successfully: '{updated_task.title}'")
        else:
            print("Failed to update task.")
    except ValueError as e:
        print(f"Error: {e}")


def delete_task_ui(task_manager: TaskManager) -> None:
    """
    UI function for deleting a task.

    Args:
        task_manager: The TaskManager instance to use
    """
    print("\n--- Delete Task ---")
    task_id = get_task_id()
    if task_id is None:
        return

    # Check if task exists
    existing_task = task_manager.get_task_by_id(task_id)
    if existing_task is None:
        print(f"No task found with ID {task_id}.")
        return

    print(f"Deleting task: {existing_task.title}")
    confirm = input("Are you sure? (y/N): ").strip().lower()

    if confirm in ['y', 'yes']:
        if task_manager.delete_task(task_id):
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            print(f"Failed to delete task with ID {task_id}.")
    else:
        print("Deletion cancelled.")


def toggle_task_status_ui(task_manager: TaskManager) -> None:
    """
    UI function for toggling a task's completion status.

    Args:
        task_manager: The TaskManager instance to use
    """
    print("\n--- Toggle Task Status ---")
    task_id = get_task_id()
    if task_id is None:
        return

    # Check if task exists
    existing_task = task_manager.get_task_by_id(task_id)
    if existing_task is None:
        print(f"No task found with ID {task_id}.")
        return

    current_status = "completed" if existing_task.completed else "incomplete"
    new_status = "incomplete" if existing_task.completed else "completed"

    print(f"Task '{existing_task.title}' is currently {current_status}.")
    confirm = input(f"Do you want to mark it as {new_status}? (y/N): ").strip().lower()

    if confirm in ['y', 'yes']:
        if existing_task.completed:
            updated_task = task_manager.mark_task_incomplete(task_id)
            status_text = "incomplete"
        else:
            updated_task = task_manager.mark_task_completed(task_id)
            status_text = "completed"

        if updated_task:
            print(f"Task marked as {status_text} successfully.")
        else:
            print("Failed to update task status.")
    else:
        print("Status change cancelled.")


def handle_menu_option(choice: str, task_manager: TaskManager) -> bool:
    """
    Handle the user's menu choice.

    Args:
        choice: The user's menu choice
        task_manager: The TaskManager instance to use

    Returns:
        True if the application should continue, False if it should exit
    """
    try:
        if choice == "1":
            add_task_ui(task_manager)
        elif choice == "2":
            view_tasks_ui(task_manager)
        elif choice == "3":
            update_task_ui(task_manager)
        elif choice == "4":
            delete_task_ui(task_manager)
        elif choice == "5":
            toggle_task_status_ui(task_manager)
        elif choice == "6":
            print("Thank you for using the Todo App. Goodbye!")
            return False
        else:
            print("Invalid option. Please select a number between 1 and 6.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return True


def run_menu_loop(task_manager: TaskManager) -> None:
    """
    Run the main menu loop.

    Args:
        task_manager: The TaskManager instance to use
    """
    print("Welcome to the Todo App!")

    while True:
        display_menu()
        choice = get_user_choice()

        if not handle_menu_option(choice, task_manager):
            break