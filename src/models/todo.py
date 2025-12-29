"""
Todo data model for the Todo CLI Application
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Todo:
    """
    Represents a single todo item with id, title, description, and completion status.
    """
    id: int
    title: str
    description: Optional[str] = None
    is_completed: bool = False

    def __post_init__(self):
        """
        Validate the todo after initialization.
        """
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty or contain only whitespace")
        
        if len(self.title) > 200:
            raise ValueError("Title cannot exceed 200 characters")
        
        if self.description and len(self.description) > 1000:
            raise ValueError("Description cannot exceed 1000 characters")