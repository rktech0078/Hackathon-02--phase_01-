# CLI Contract: Todo CLI Application

## Overview
This document defines the contract for the Todo CLI Application's command-line interface.

## Command Structure
All commands follow the format: `command [arguments]`

## Commands

### 1. Add Todo
- **Command**: `add`
- **Arguments**: `title` (string, required), `description` (string, optional)
- **Usage**: `add "title" ["description"]`
- **Success Response**: 
  - Todo added to the list
  - Confirmation message with the created todo's details
  - New todo assigned a unique ID
- **Error Responses**:
  - "Error: Title cannot be empty" if title is not provided or is empty
  - "Success: Todo added with ID [id]"

### 2. View Todos
- **Command**: `view`
- **Arguments**: None
- **Usage**: `view`
- **Success Response**: 
  - Formatted table showing all todos
  - Columns: ID, Title, Description, Status
  - Completed todos shown with strikethrough or different color
  - If no todos exist, show "No todos found"
- **Error Responses**: None

### 3. Update Todo
- **Command**: `update`
- **Arguments**: `id` (integer, required), `title` (string, optional), `description` (string, optional)
- **Usage**: `update id "new_title" ["new_description"]`
- **Success Response**: 
  - Todo updated in the list
  - Confirmation message with the updated todo's details
- **Error Responses**:
  - "Error: Todo with ID [id] not found" if the ID doesn't exist
  - "Error: Title cannot be empty" if title is empty
  - "Success: Todo with ID [id] updated"

### 4. Delete Todo
- **Command**: `delete`
- **Arguments**: `id` (integer, required)
- **Usage**: `delete id`
- **Success Response**: 
  - Todo removed from the list
  - Confirmation message
- **Error Responses**:
  - "Error: Todo with ID [id] not found" if the ID doesn't exist
  - "Success: Todo with ID [id] deleted"

### 5. Mark Complete
- **Command**: `complete`
- **Arguments**: `id` (integer, required)
- **Usage**: `complete id`
- **Success Response**: 
  - Todo marked as complete in the list
  - Confirmation message
- **Error Responses**:
  - "Error: Todo with ID [id] not found" if the ID doesn't exist
  - "Success: Todo with ID [id] marked as complete"

### 6. Mark Incomplete
- **Command**: `incomplete`
- **Arguments**: `id` (integer, required)
- **Usage**: `incomplete id`
- **Success Response**: 
  - Todo marked as incomplete in the list
  - Confirmation message
- **Error Responses**:
  - "Error: Todo with ID [id] not found" if the ID doesn't exist
  - "Success: Todo with ID [id] marked as incomplete"

### 7. Help
- **Command**: `help`
- **Arguments**: None
- **Usage**: `help`
- **Success Response**: 
  - List of all available commands with usage
- **Error Responses**: None

### 8. Exit
- **Command**: `exit`
- **Arguments**: None
- **Usage**: `exit`
- **Success Response**: 
  - Application terminates
- **Error Responses**: None

## Error Handling
- All error messages follow the format: "Error: [descriptive message]"
- All success messages follow the format: "Success: [descriptive message]"
- Invalid commands show: "Unknown command. Type 'help' for available commands."

## Input Validation
- IDs must be positive integers
- Titles must not be empty
- Descriptions can be empty or up to 1000 characters
- All text values are trimmed of leading/trailing whitespace