"""
Main entry point for the Todo App Phase I.

This module implements the main application class and orchestrates the entire application flow.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from services.task_manager import TaskManager
from cli.menu import run_menu_loop


class TodoApp:
    """
    Main application class for the Todo App.

    Orchestrates the entire application flow by integrating
    the TaskManager and CLI menu components.
    """

    def __init__(self):
        """
        Initialize the TodoApp with a TaskManager instance.
        """
        self.task_manager = TaskManager()

    def run(self):
        """
        Run the main application loop.
        """
        print("Starting Todo App Phase I...")
        run_menu_loop(self.task_manager)
        print("Todo App closed.")


def main():
    """
    Entry point function for the application.
    """
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()