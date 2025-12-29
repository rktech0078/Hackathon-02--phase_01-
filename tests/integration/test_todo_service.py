"""
Integration tests for the TodoService add and view functionality
"""

import pytest
from src.services.todo_service import TodoService


def test_add_todo_success():
    """Test adding a todo successfully."""
    service = TodoService()

    # Add a new todo
    result = service.add_todo("Test title", "Test description")

    # Verify the result
    assert result.id == 1
    assert result.title == "Test title"
    assert result.description == "Test description"
    assert result.is_completed is False

    # Verify the todo was stored
    stored_todo = service.get_todo(1)
    assert stored_todo is not None
    assert stored_todo.id == 1
    assert stored_todo.title == "Test title"
    assert stored_todo.description == "Test description"
    assert stored_todo.is_completed is False


def test_add_todo_without_description():
    """Test adding a todo without a description."""
    service = TodoService()

    # Add a new todo without description
    result = service.add_todo("Test title")

    # Verify the result
    assert result.id == 1
    assert result.title == "Test title"
    assert result.description is None
    assert result.is_completed is False


def test_add_multiple_todos():
    """Test adding multiple todos with auto-incrementing IDs."""
    service = TodoService()

    # Add first todo
    result1 = service.add_todo("First todo", "Description 1")

    # Add second todo
    result2 = service.add_todo("Second todo", "Description 2")

    # Verify the results have different IDs
    assert result1.id == 1
    assert result2.id == 2

    # Verify both todos are stored
    todos = service.get_all_todos()
    assert len(todos) == 2


def test_add_todo_empty_title_error():
    """Test that adding a todo with empty title raises an error."""
    service = TodoService()

    with pytest.raises(ValueError, match="Title cannot be empty or contain only whitespace"):
        service.add_todo("")


def test_add_todo_whitespace_title_error():
    """Test that adding a todo with whitespace-only title raises an error."""
    service = TodoService()

    with pytest.raises(ValueError, match="Title cannot be empty or contain only whitespace"):
        service.add_todo("   ")


def test_add_todo_long_title_error():
    """Test that adding a todo with too-long title raises an error."""
    service = TodoService()
    long_title = "a" * 201  # 201 characters

    with pytest.raises(ValueError, match="Title cannot exceed 200 characters"):
        service.add_todo(long_title)


def test_get_all_todos_empty():
    """Test getting all todos when none exist."""
    service = TodoService()

    todos = service.get_all_todos()

    assert len(todos) == 0


def test_get_all_todos_with_items():
    """Test getting all todos when some exist."""
    service = TodoService()

    # Add some todos
    service.add_todo("First todo", "Description 1")
    service.add_todo("Second todo", "Description 2")

    # Get all todos
    todos = service.get_all_todos()

    # Verify the results
    assert len(todos) == 2
    assert any(todo.title == "First todo" for todo in todos)
    assert any(todo.title == "Second todo" for todo in todos)


def test_get_todo_by_id():
    """Test getting a specific todo by ID."""
    service = TodoService()

    # Add a todo
    added_todo = service.add_todo("Test todo", "Description")

    # Get the todo by its ID
    retrieved_todo = service.get_todo(added_todo.id)

    # Verify it matches
    assert retrieved_todo is not None
    assert retrieved_todo.id == added_todo.id
    assert retrieved_todo.title == "Test todo"
    assert retrieved_todo.description == "Description"
    assert retrieved_todo.is_completed is False


def test_get_todo_by_id_not_found():
    """Test getting a todo by ID that doesn't exist."""
    service = TodoService()

    # Try to get a todo with an ID that doesn't exist
    retrieved_todo = service.get_todo(999)

    # Verify it returns None
    assert retrieved_todo is None


def test_mark_complete_success():
    """Test marking a todo as complete successfully."""
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Test todo", "Description")
    assert todo.is_completed is False  # Initially incomplete

    # Mark as complete
    result = service.mark_complete(todo.id)

    # Verify the result
    assert result is not None
    assert result.id == todo.id
    assert result.is_completed is True


def test_mark_complete_not_found():
    """Test marking a non-existent todo as complete."""
    service = TodoService()

    # Try to mark a todo that doesn't exist
    result = service.mark_complete(999)

    # Verify it returns None
    assert result is None


def test_mark_incomplete_success():
    """Test marking a todo as incomplete successfully."""
    service = TodoService()

    # Add a todo and mark it as complete
    todo = service.add_todo("Test todo", "Description")
    service.mark_complete(todo.id)
    assert todo.is_completed is True  # Initially complete

    # Mark as incomplete
    result = service.mark_incomplete(todo.id)

    # Verify the result
    assert result is not None
    assert result.id == todo.id
    assert result.is_completed is False


def test_mark_incomplete_not_found():
    """Test marking a non-existent todo as incomplete."""
    service = TodoService()

    # Try to mark a todo that doesn't exist
    result = service.mark_incomplete(999)

    # Verify it returns None
    assert result is None


def test_mark_complete_then_incomplete():
    """Test marking a todo as complete then incomplete."""
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Test todo", "Description")
    assert todo.is_completed is False  # Initially incomplete

    # Mark as complete
    result = service.mark_complete(todo.id)
    assert result.is_completed is True

    # Mark as incomplete
    result = service.mark_incomplete(todo.id)
    assert result.is_completed is False


def test_update_todo_success():
    """Test updating a todo successfully."""
    service = TodoService()

    # Add a todo
    original_todo = service.add_todo("Original title", "Original description")
    assert original_todo.title == "Original title"
    assert original_todo.description == "Original description"

    # Update the todo
    updated_todo = service.update_todo(original_todo.id, "Updated title", "Updated description")

    # Verify the update
    assert updated_todo is not None
    assert updated_todo.id == original_todo.id
    assert updated_todo.title == "Updated title"
    assert updated_todo.description == "Updated description"
    assert updated_todo.is_completed is False  # Status should remain unchanged


def test_update_todo_partial():
    """Test updating only specific fields of a todo."""
    service = TodoService()

    # Add a todo
    original_todo = service.add_todo("Original title", "Original description")

    # Update only the title
    updated_todo = service.update_todo(original_todo.id, title="New title")

    # Verify only the title changed
    assert updated_todo is not None
    assert updated_todo.title == "New title"
    assert updated_todo.description == "Original description"
    assert updated_todo.is_completed is False


def test_update_todo_title_only():
    """Test updating only the title of a todo."""
    service = TodoService()

    # Add a todo
    original_todo = service.add_todo("Original title", "Original description")

    # Update only the title
    updated_todo = service.update_todo(original_todo.id, title="New title")

    # Verify only the title changed
    assert updated_todo is not None
    assert updated_todo.title == "New title"
    assert updated_todo.description == "Original description"


def test_update_todo_description_only():
    """Test updating only the description of a todo."""
    service = TodoService()

    # Add a todo
    original_todo = service.add_todo("Original title", "Original description")

    # Update only the description
    updated_todo = service.update_todo(original_todo.id, description="New description")

    # Verify only the description changed
    assert updated_todo is not None
    assert updated_todo.title == "Original title"
    assert updated_todo.description == "New description"


def test_update_todo_not_found():
    """Test updating a non-existent todo."""
    service = TodoService()

    # Try to update a todo that doesn't exist
    result = service.update_todo(999, "New title", "New description")

    # Verify it returns None
    assert result is None


def test_update_todo_empty_title_error():
    """Test updating a todo with an empty title raises an error."""
    service = TodoService()

    # Add a todo
    original_todo = service.add_todo("Original title", "Original description")

    # Try to update with an empty title
    with pytest.raises(ValueError, match="Title cannot be empty or contain only whitespace"):
        service.update_todo(original_todo.id, "")


def test_update_todo_long_title_error():
    """Test updating a todo with a too-long title raises an error."""
    service = TodoService()

    # Add a todo
    original_todo = service.add_todo("Original title", "Original description")

    # Try to update with a very long title
    long_title = "a" * 201
    with pytest.raises(ValueError, match="Title cannot exceed 200 characters"):
        service.update_todo(original_todo.id, long_title)


def test_delete_todo_success():
    """Test deleting a todo successfully."""
    service = TodoService()

    # Add a todo
    original_todo = service.add_todo("Original title", "Original description")
    assert len(service.get_all_todos()) == 1  # Verify it was added

    # Delete the todo
    result = service.delete_todo(original_todo.id)

    # Verify the deletion
    assert result is True  # Deletion successful
    assert len(service.get_all_todos()) == 0  # No todos left
    assert service.get_todo(original_todo.id) is None  # Cannot retrieve deleted todo


def test_delete_todo_not_found():
    """Test deleting a non-existent todo."""
    service = TodoService()

    # Try to delete a todo that doesn't exist
    result = service.delete_todo(999)

    # Verify it returns False
    assert result is False


def test_delete_todo_among_multiple():
    """Test deleting one todo among multiple todos."""
    service = TodoService()

    # Add multiple todos
    todo1 = service.add_todo("Todo 1", "Description 1")
    todo2 = service.add_todo("Todo 2", "Description 2")
    todo3 = service.add_todo("Todo 3", "Description 3")
    assert len(service.get_all_todos()) == 3  # Verify all were added

    # Delete the middle one
    result = service.delete_todo(todo2.id)

    # Verify the deletion
    assert result is True  # Deletion successful
    all_todos = service.get_all_todos()
    assert len(all_todos) == 2  # Two todos left
    assert not any(todo.id == todo2.id for todo in all_todos)  # Deleted todo is gone
    assert any(todo.id == todo1.id for todo in all_todos)  # Other todos remain
    assert any(todo.id == todo3.id for todo in all_todos)  # Other todos remain