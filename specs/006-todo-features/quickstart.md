# Quickstart Guide: Todo App Phase I

## Running the Application

1. Ensure Python 3.8+ is installed on your system
2. Navigate to the project root directory
3. Run the application with: `python src/main.py`
4. The menu-driven interface will start, allowing you to manage tasks

## Available Operations

1. **Add Task**: Create a new task with title and optional description
2. **View Tasks**: Display all tasks with their ID, title, description, and completion status
3. **Update Task**: Modify an existing task's title or description
4. **Delete Task**: Remove a task from the in-memory storage
5. **Mark Task Complete/Incomplete**: Toggle the completion status of a task
6. **Exit**: Quit the application (all data will be lost)

## Example Usage

```
Welcome to the Todo App!
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

Choose an option: 1
Enter task title: Buy groceries
Enter task description (optional): Need to buy milk, bread, eggs
Task added successfully with ID: 1
```

## Development Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install pytest` for testing
5. Run tests: `pytest tests/`