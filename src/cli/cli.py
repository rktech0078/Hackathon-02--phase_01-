"""
Command-line interface for the Todo CLI Application
"""

import sys
from typing import List, Optional
from src.services.todo_service import TodoService
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm, IntPrompt
from rich import print
from rich.layout import Layout
from rich.align import Align
from rich.box import ROUNDED, DOUBLE, SIMPLE

# Custom Theme for a "Cyber/Modern" look
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green",
    "header": "bold magenta",
    "title": "bold cyan",
    "option": "bold yellow",
    "text": "white",
    "dim": "dim white",
})

class TodoCLI:
    """
    Command-line interface class to handle user interaction with the todo application.
    """

    def __init__(self):
        """
        Initialize the CLI with a TodoService and console.
        """
        self.service = TodoService()
        self.console = Console(theme=custom_theme)

    def run(self):
        """
        Run the main CLI with a menu-based interface.
        """
        while True:
            self.console.clear()
            self._display_header()
            self._display_menu()

            try:
                # Using a visually distinct prompt
                self.console.print("\n[title]Choose a command[/title] [dim](1-7)[/dim]: ", end="")
                choice = IntPrompt.ask(
                    "",
                    choices=["1", "2", "3", "4", "5", "6", "7"],
                    show_choices=False,
                    show_default=False
                )

                if choice == 1:
                    self._add_todo()
                elif choice == 2:
                    self._view_todos()
                elif choice == 3:
                    self._update_todo()
                elif choice == 4:
                    self._delete_todo()
                elif choice == 5:
                    self._mark_complete()
                elif choice == 6:
                    self._mark_incomplete()
                elif choice == 7:
                    self._exit_app()
            except KeyboardInterrupt:
                self._exit_app()
            except Exception as e:
                self._print_error(f"An error occurred: {e}")
                
    def _display_header(self):
        """
        Display the application header with stats.
        """
        # Calculate stats
        todos = self.service.get_all_todos()
        total = len(todos)
        completed = sum(1 for t in todos if t.is_completed)
        pending = total - completed

        title = Text("🚀 Todo CLI Master", style="header", justify="center")
        stats = Text(f"Total: {total} | Pending: {pending} | Completed: {completed}", style="dim cyan", justify="center")
        
        grid = Table.grid(expand=True)
        grid.add_column(justify="center")
        grid.add_row(title)
        grid.add_row(stats)
        
        panel = Panel(
            grid,
            style="cyan",
            border_style="magenta",
            box=DOUBLE,
            padding=(0, 2)
        )
        self.console.print(panel)

    def _display_menu(self):
        """
        Display the main menu options using a grid layout.
        """
        table = Table(show_header=False, box=ROUNDED, expand=True, border_style="dim blue")
        table.add_column("Command", justify="left")
        table.add_column("Description", justify="left")

        # Adding icons for better visual cue
        options = [
            ("[bold cyan]1[/bold cyan]", "➕  Add New Task", "Create a new todo item"),
            ("[bold cyan]2[/bold cyan]", "📋  View Tasks", "Display all your todos"),
            ("[bold cyan]3[/bold cyan]", "✏️   Update Task", "Modify an existing todo"),
            ("[bold cyan]4[/bold cyan]", "🗑️   Delete Task", "Remove a todo permanently"),
            ("[bold cyan]5[/bold cyan]", "✅  Mark Complete", "Set status to done"),
            ("[bold cyan]6[/bold cyan]", "🔄  Mark Incomplete", "Reset status to pending"),
            ("[bold red]7[/bold red]", "❌  Exit", "Close the application"),
        ]

        for idx, (num, label, desc) in enumerate(options):
            # Styling the row content
            cmd_text = Text.from_markup(f"{num}  {label}")
            desc_text = Text.from_markup(f"[dim]{desc}[/dim]")
            table.add_row(cmd_text, desc_text)

        self.console.print(Panel(table, title="[bold white]Main Menu[/bold white]", border_style="blue", box=ROUNDED))

    def _print_success(self, message: str):
        """Helper to print success messages consistently."""
        self.console.print(Panel(f"✅ {message}", style="success", border_style="green", box=ROUNDED))
        self.console.input("\n[dim]Press Enter to continue...[/dim]")

    def _print_error(self, message: str):
        """Helper to print error messages consistently."""
        self.console.print(Panel(f"⚠️ {message}", style="error", border_style="red", box=ROUNDED))
        self.console.input("\n[dim]Press Enter to continue...[/dim]")

    def _wait(self):
        """Brief pause."""
        self.console.input("\n[dim]Press Enter to continue...[/dim]")

    def _create_todo_table(self, todos: List, title: str = "📝 Your Tasks") -> Table:
        """
        Create a rich Table object for a list of todos.
        """
        table = Table(title=title, show_header=True, header_style="bold magenta", box=ROUNDED, expand=True, border_style="dim white")
        table.add_column("ID", style="cyan", justify="center", width=4)
        table.add_column("Status", justify="center", width=4)
        table.add_column("Title", style="white", ratio=1)
        table.add_column("Description", style="dim white", ratio=2)

        for todo in todos:
            if todo.is_completed:
                status = "✅"
                title_text = f"[strike dim green]{todo.title}[/]"
            else:
                status = "⭕"
                title_text = f"[bold white]{todo.title}[/bold white]"
            
            description = todo.description if todo.description else ""
            if todo.is_completed:
                 description = f"[dim]{description}[/dim]"

            table.add_row(
                str(todo.id), 
                status, 
                title_text, 
                description
            )
        return table

    def _add_todo(self):
        """
        Add a new todo with a user-friendly form.
        """
        self.console.clear()
        self._display_header()
        self.console.print(Panel("[bold]➕ Add New Todo[/bold]", style="title", border_style="cyan", box=ROUNDED))

        try:
            self.console.print("\n[text]Enter the title for your task:[/text]")
            title = Prompt.ask("[bold cyan]>[/bold cyan]")

            if not title.strip():
                self._print_error("Title cannot be empty!")
                return

            self.console.print("\n[text]Enter description (optional):[/text]")
            description = Prompt.ask("[bold cyan]>[/bold cyan]", default="")

            todo = self.service.add_todo(title, description if description else None)
            self._print_success(f"Todo added successfully! (ID: [bold]{todo.id}[/bold])")

        except ValueError as e:
            self._print_error(str(e))
        except KeyboardInterrupt:
            return

    def _view_todos(self):
        """
        Display all todos in a formatted table.
        """
        self.console.clear()
        self._display_header()

        todos = self.service.get_all_todos()

        if not todos:
            self.console.print(Panel("📭 Your todo list is empty. Add something new!", style="warning", border_style="yellow", box=ROUNDED))
            self._wait()
            return

        table = self._create_todo_table(todos)
        self.console.print(table)
        self._wait()

    def _update_todo(self):
        """
        Update an existing todo.
        """
        self.console.clear()
        self._display_header()

        todos = self.service.get_all_todos()
        if not todos:
            self._print_error("No todos available to update.")
            return

        # Show list contextually
        self.console.print(self._create_todo_table(todos, title="Select Todo to Update"))

        try:
            todo_id = IntPrompt.ask("\n[bold]Enter the ID of the todo to update[/bold]")

            existing_todo = self.service.get_todo(todo_id)
            if not existing_todo:
                self._print_error(f"Todo with ID {todo_id} not found.")
                return

            self.console.print(Panel(
                f"[bold]Current Title:[/bold] {existing_todo.title}\n"
                f"[bold]Current Desc:[/bold]  {existing_todo.description or '[dim]None[/dim]'}",
                title="Current Details",
                border_style="dim"
            ))

            self.console.print("\n[text]New title (leave blank to keep current):[/text]")
            new_title = Prompt.ask("[bold cyan]>[/bold cyan]", default=existing_todo.title)
            
            self.console.print("\n[text]New description (leave blank to keep current):[/text]")
            new_description = Prompt.ask("[bold cyan]>[/bold cyan]", default=existing_todo.description or "")

            new_description = new_description if new_description else None

            result = self.service.update_todo(todo_id, new_title, new_description)

            if result:
                self._print_success(f"Todo {todo_id} updated successfully!")
            else:
                self._print_error(f"Todo {todo_id} could not be updated.")

        except ValueError as e:
            self._print_error(str(e))
        except KeyboardInterrupt:
            return

    def _delete_todo(self):
        """
        Delete a todo.
        """
        self.console.clear()
        self._display_header()

        todos = self.service.get_all_todos()
        if not todos:
            self._print_error("No todos available to delete.")
            return

        # Show list contextually
        self.console.print(self._create_todo_table(todos, title="Select Todo to Delete"))

        try:
            todo_id = IntPrompt.ask("\n[bold]Enter the ID of the todo to delete[/bold]")

            confirm = Confirm.ask(f"[bold red]⚠️ Are you sure you want to delete todo {todo_id}?[/bold red]")

            if confirm:
                result = self.service.delete_todo(todo_id)
                if result:
                    self._print_success(f"Todo {todo_id} deleted forever.")
                else:
                    self._print_error(f"Todo {todo_id} not found.")
            else:
                self.console.print("[yellow]Deletion cancelled.[/yellow]")
                self._wait()

        except ValueError as e:
            self._print_error(str(e))
        except KeyboardInterrupt:
            return

    def _mark_complete(self):
        """
        Mark a todo as complete.
        """
        self.console.clear()
        self._display_header()

        # Show only incomplete todos contextually
        all_todos = self.service.get_all_todos()
        incomplete_todos = [todo for todo in all_todos if not todo.is_completed]

        if not incomplete_todos:
            self._print_error("No incomplete todos to mark as complete.")
            return

        self.console.print(self._create_todo_table(incomplete_todos, title="Select Todo to Complete"))

        try:
            todo_id = IntPrompt.ask("\n[bold]Enter ID to mark complete[/bold]")
            result = self.service.mark_complete(todo_id)

            if result:
                self._print_success(f"High five! Todo {todo_id} completed.")
            else:
                 t = self.service.get_todo(todo_id)
                 if t and t.is_completed:
                     self._print_error(f"Todo {todo_id} is already complete.")
                 else:
                     self._print_error(f"Todo {todo_id} not found.")

        except ValueError as e:
            self._print_error(str(e))
        except KeyboardInterrupt:
            return

    def _mark_incomplete(self):
        """
        Mark a todo as incomplete.
        """
        self.console.clear()
        self._display_header()

        todos = self.service.get_all_todos()
        complete_todos = [todo for todo in todos if todo.is_completed]
        
        if not complete_todos:
             self._print_error("No completed todos found!")
             return

        self.console.print(self._create_todo_table(complete_todos, title="Select Todo to Mark Incomplete"))

        try:
            todo_id = IntPrompt.ask("\n[bold]Enter ID to mark incomplete[/bold]")
            result = self.service.mark_incomplete(todo_id)

            if result:
                self._print_success(f"Todo {todo_id} marked as incomplete.")
            else:
                 self._print_error(f"Todo {todo_id} not found or already incomplete.")

        except ValueError as e:
            self._print_error(str(e))
        except KeyboardInterrupt:
            return

    def _exit_app(self):
        """
        Exit the application.
        """
        self.console.clear()
        self.console.print(Panel("👋 Thanks for being productive! See you soon.", style="bold cyan", box=ROUNDED, expand=False))
        sys.exit(0)