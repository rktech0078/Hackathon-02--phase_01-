# Quickstart Guide: Todo CLI Application

## Overview
This guide provides a quick overview of how to set up and use the Todo CLI Application.

## Prerequisites
- Python 3.13 or higher
- UV package manager (as specified in the constitution)

## Setup Instructions

1. Clone or create the project directory
2. Ensure Python 3.13+ is installed
3. Install dependencies using UV:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install rich
   ```

## Running the Application
```bash
python main.py
```

## Available Commands
Once the application is running, you can use the following commands:

- `add` - Add a new todo
  - Usage: `add "Title" "Description"`
  - Example: `add "Buy groceries" "Milk, bread, eggs"`

- `view` - View all todos
  - Usage: `view`
  - Displays todos in a formatted table with visual indicators for completed/incompleted tasks

- `update` - Update an existing todo
  - Usage: `update <id> "New Title" "New Description"`
  - Example: `update 1 "Updated title" "Updated description"`

- `delete` - Delete a todo
  - Usage: `delete <id>`
  - Example: `delete 1`

- `complete` - Mark a todo as complete
  - Usage: `complete <id>`
  - Example: `complete 1`

- `incomplete` - Mark a todo as incomplete
  - Usage: `incomplete <id>`
  - Example: `incomplete 1`

- `help` - Show available commands
  - Usage: `help`

- `exit` - Exit the application
  - Usage: `exit`

## Example Workflow
```bash
# Add a new todo
add "Complete project" "Finish the todo application project"

# View all todos
view

# Mark the todo as complete (assuming it has id 1)
complete 1

# Update the todo
update 1 "Completed project" "Successfully finished the todo application project"

# View the updated todo list
view

# Delete the todo
delete 1

# Exit the application
exit
```

## Features
- In-memory storage (data is lost when the application exits)
- Formatted output using the Rich library
- Visual distinction between completed and incomplete tasks
- User-friendly error messages
- Input validation