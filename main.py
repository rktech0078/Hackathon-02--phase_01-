"""
Main entry point for the Todo CLI Application
"""

from src.cli.cli import TodoCLI


def main():
    """
    Main function to start the Todo CLI Application.
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()