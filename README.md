# Todo CLI Application

A Python-based in-memory command-line Todo application built using spec-driven development. The application allows users to manage their tasks through a professional and intuitive GUI-style CLI interface using the Rich library.

## Features

- Add, view, update, delete, and mark todos as complete/incomplete
- Professional menu-driven interface with arrow-key navigation
- Formatted output using the Rich library for enhanced UX
- In-memory storage (data is lost when the application exits)
- Visual distinction between completed and incomplete tasks
- Confirmation prompts for critical operations
- User-friendly form-based input

## Prerequisites

- Python 3.13 or higher
- UV package manager

## Setup

1. Clone or create the project directory
2. Ensure Python 3.13+ is installed
3. Install dependencies using UV:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e .
   ```

## Running the Application

```bash
python main.py
```

Or if installed with the project script:

```bash
todo
```

## User Interface

The application features a professional menu-driven interface:

1. ➕ Add Todo - Add a new task with title and description
2. 📋 View Todos - Display all tasks in a formatted table
3. ✏️ Update Todo - Modify existing task details
4. 🗑️ Delete Todo - Remove a task (with confirmation)
5. ✅ Mark Complete - Mark an incomplete task as complete
6. 🔄 Mark Incomplete - Mark a completed task as incomplete
7. ❌ Exit - Close the application

## Example Workflow

1. Launch the application with `python main.py`
2. Use the number keys to select options from the menu:
   - Press 1 to add a new task
   - Press 2 to view all tasks
   - Press 5 to mark a task as complete
   - Press 7 to exit the application

## Architecture

The application follows a three-tier architecture:
- **Models** (`src/models/`): Handle data definitions and validation
- **Services** (`src/services/`): Implement business logic
- **CLI** (`src/cli/`): Handle user interaction and presentation

## Files Structure

```
src/
├── models/
│   └── todo.py          # Todo data model
├── services/
│   └── todo_service.py  # Todo business logic
├── cli/
│   └── cli.py           # Command-line interface
└── lib/
    └── utils.py         # Helper functions

tests/
├── unit/
│   └── test_todo.py     # Unit tests for todo model
├── integration/
│   └── test_todo_service.py # Integration tests
└── contract/
    └── test_cli.py      # CLI contract tests

main.py                  # Application entry point
```

## Testing

The project includes unit and integration tests. To run tests:

```bash
pytest
```

Tests are organized in the `tests/` directory with separate folders for unit and integration tests.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request