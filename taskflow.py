#!usr/bin/env python3
"""TaskFlow - A CLI Task Management Application

This is the main entry point for TaskFlow. It handles command-line arguments and routes them to hte appropriate functions.
"""

__version__ = "0.1.0"
__author__ = "Oussama BOUSSAHLA"
def show_help():
    """Display detailed help information.
    
    Shows all available commands with examples.
    """
    print (" TaskFlow - CLI Task Manager ")
    print ("\nAvailable commands :")
    print (" add <title >       Add a new task ")
    print (" list               List all tasks ")
    print (" done <id>          Mark task as complete ")
    print (" delete <id>        Delete a task ")

def main():
    """Main entry point for TaskFlow.
    
    This function displays the welcome message and usage instructions.
    We'll expand this to handle actual commdans in later steps.
    """
    print (f" TaskFlow v{ __version__ }")
    print (" Your command - line task manager ")
    print ("\nUsage : python taskflow.py <command> [options]")
    print ("\nCommands :")
    print (" add    Add a new task ")
    print (" list   List all tasks ")
    print (" help   Show this help message ")
    
if __name__ == "__main__":
    main()