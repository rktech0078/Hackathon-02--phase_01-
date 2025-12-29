# Data Model: Todo CLI Application

## Overview
This document defines the data model for the Todo CLI Application, including entity definitions, relationships, validation rules, and state transitions.

## Entity: Todo Item

### Fields
- **id** (integer, unique, required)
  - Auto-generated unique identifier
  - Auto-incrementing sequence
  - Primary identifier for each todo item

- **title** (string, required)
  - Short description of the task
  - Maximum length: 200 characters
  - Cannot be empty or whitespace only

- **description** (string, optional)
  - Detailed description of the task
  - Maximum length: 1000 characters

- **is_completed** (boolean, required)
  - Indicates completion status
  - Default value: false

### Relationships
- The Todo Item entity stands alone with no direct relationships to other entities
- All todos are stored in a collection within the application's memory

### Validation Rules
- **id**: Must be a positive integer; must be unique across all todos
- **title**: 
  - Required field
  - Minimum 1 non-whitespace character
  - Maximum 200 characters
  - Cannot be empty or contain only whitespace
- **description**: Optional field; if provided, maximum 1000 characters
- **is_completed**: Must be a boolean value (true/false)

### State Transitions
- **New Todo**: Created with is_completed = false
- **Mark Complete**: is_completed transitions from false to true
- **Mark Incomplete**: is_completed transitions from true to false
- **Update**: Any field (except id) can be modified
- **Delete**: Todo is removed from the collection

## Data Storage
- Todos are stored in-memory using a Python dictionary with the id as the key
- The application maintains a counter for the next available ID
- Storage is only valid during application runtime (lost on exit)