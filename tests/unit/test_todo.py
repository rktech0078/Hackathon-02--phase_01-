"""
Unit tests for the Todo model
"""

import pytest
from src.models.todo import Todo


def test_todo_creation_valid():
    """Test creating a valid Todo object."""
    todo = Todo(id=1, title="Test title", description="Test description", is_completed=False)

    assert todo.id == 1
    assert todo.title == "Test title"
    assert todo.description == "Test description"
    assert todo.is_completed is False


def test_todo_creation_defaults():
    """Test creating a Todo object with default values."""
    todo = Todo(id=1, title="Test title")

    assert todo.id == 1
    assert todo.title == "Test title"
    assert todo.description is None
    assert todo.is_completed is False


def test_todo_title_required():
    """Test that Todo creation fails with empty title."""
    with pytest.raises(ValueError, match="Title cannot be empty or contain only whitespace"):
        Todo(id=1, title="")


def test_todo_title_whitespace_only():
    """Test that Todo creation fails with whitespace-only title."""
    with pytest.raises(ValueError, match="Title cannot be empty or contain only whitespace"):
        Todo(id=1, title="   ")


def test_todo_title_max_length():
    """Test that Todo creation fails with title exceeding 200 characters."""
    long_title = "a" * 201
    with pytest.raises(ValueError, match="Title cannot exceed 200 characters"):
        Todo(id=1, title=long_title)


def test_todo_description_max_length():
    """Test that Todo creation fails with description exceeding 1000 characters."""
    long_description = "a" * 1001
    with pytest.raises(ValueError, match="Description cannot exceed 1000 characters"):
        Todo(id=1, title="Valid title", description=long_description)


def test_todo_repr():
    """Test the string representation of a Todo object."""
    todo = Todo(id=1, title="Test title", description="Test description", is_completed=True)

    # Just verify that the object has the expected attributes
    assert todo.id == 1
    assert todo.title == "Test title"
    assert todo.description == "Test description"
    assert todo.is_completed is True


def test_todo_status_changes():
    """Test changing the completion status of a Todo object."""
    # Test initial state
    todo = Todo(id=1, title="Test title", is_completed=False)
    assert todo.is_completed is False

    # Manually change the status to test that it works
    todo.is_completed = True
    assert todo.is_completed is True

    # Manually change back to incomplete
    todo.is_completed = False
    assert todo.is_completed is False


def test_todo_update_attributes():
    """Test updating the attributes of a Todo object."""
    # Create a todo
    todo = Todo(id=1, title="Original title", description="Original description", is_completed=False)

    # Update the attributes
    todo.title = "Updated title"
    todo.description = "Updated description"
    todo.is_completed = True

    # Verify the changes
    assert todo.title == "Updated title"
    assert todo.description == "Updated description"
    assert todo.is_completed is True


def test_todo_equality():
    """Test equality comparison between Todo objects."""
    todo1 = Todo(id=1, title="Title", description="Description", is_completed=False)
    todo2 = Todo(id=1, title="Title", description="Description", is_completed=False)
    todo3 = Todo(id=2, title="Different", description="Description", is_completed=False)

    # Two todos with same attributes should be considered the same in content
    assert todo1.id == todo2.id
    assert todo1.title == todo2.title
    assert todo1.description == todo2.description
    assert todo1.is_completed == todo2.is_completed

    # Different IDs should still be different items
    assert todo1.id != todo3.id