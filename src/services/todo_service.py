"""
TodoService for the Todo CLI Application
Implements the business logic for managing todos in memory.
"""

from typing import Dict, List, Optional
from src.models.todo import Todo


class TodoService:
    """
    Service class to handle all todo-related business logic.
    All todos are stored in memory using a dictionary with id as the key.
    """
    
    def __init__(self):
        """
        Initialize the TodoService with an empty storage and counter for next ID.
        """
        self._todos: Dict[int, Todo] = {}
        self._next_id: int = 1
    
    def add_todo(self, title: str, description: Optional[str] = None) -> Todo:
        """
        Add a new todo to the storage.
        
        Args:
            title: Title of the todo (required)
            description: Description of the todo (optional)
        
        Returns:
            Todo: The newly created Todo object with assigned ID
        
        Raises:
            ValueError: If title is empty or invalid
        """
        # Create a new todo with the next available ID
        new_todo = Todo(
            id=self._next_id,
            title=title,
            description=description,
            is_completed=False
        )
        
        # Add to storage
        self._todos[self._next_id] = new_todo
        
        # Increment the ID counter
        self._next_id += 1
        
        return new_todo
    
    def get_todo(self, todo_id: int) -> Optional[Todo]:
        """
        Get a single todo by its ID.
        
        Args:
            todo_id: The ID of the todo to retrieve
        
        Returns:
            Todo: The todo object if found, None otherwise
        """
        return self._todos.get(todo_id)
    
    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos from storage.
        
        Returns:
            List[Todo]: A list of all todo objects
        """
        return list(self._todos.values())
    
    def update_todo(self, todo_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Todo]:
        """
        Update an existing todo with new values.
        
        Args:
            todo_id: The ID of the todo to update
            title: New title (optional)
            description: New description (optional)
        
        Returns:
            Todo: The updated todo object if successful, None if todo doesn't exist
        
        Raises:
            ValueError: If title is provided but is empty or invalid
        """
        if todo_id not in self._todos:
            return None
        
        todo = self._todos[todo_id]
        
        # If title is provided, validate it
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Title cannot be empty or contain only whitespace")
            
            if len(title) > 200:
                raise ValueError("Title cannot exceed 200 characters")
        
        # Update the todo with provided values
        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description
        
        return todo
    
    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.
        
        Args:
            todo_id: The ID of the todo to delete
        
        Returns:
            bool: True if the todo was deleted, False if it didn't exist
        """
        if todo_id in self._todos:
            del self._todos[todo_id]
            return True
        return False
    
    def mark_complete(self, todo_id: int) -> Optional[Todo]:
        """
        Mark a todo as complete.
        
        Args:
            todo_id: The ID of the todo to mark as complete
        
        Returns:
            Todo: The updated todo object if successful, None if todo doesn't exist
        """
        if todo_id not in self._todos:
            return None
        
        self._todos[todo_id].is_completed = True
        return self._todos[todo_id]
    
    def mark_incomplete(self, todo_id: int) -> Optional[Todo]:
        """
        Mark a todo as incomplete.
        
        Args:
            todo_id: The ID of the todo to mark as incomplete
        
        Returns:
            Todo: The updated todo object if successful, None if todo doesn't exist
        """
        if todo_id not in self._todos:
            return None
        
        self._todos[todo_id].is_completed = False
        return self._todos[todo_id]