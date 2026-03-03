#!usr/bin/env python3
"""TaskFlow - A CLI Task Management Application

This is the main entry point for TaskFlow. It handles command-line arguments and routes them to hte appropriate functions.
"""
import sys
from storage import load_tasks, save_tasks

__version__ = "0.1.0"
__author__ = "Oussama BOUSSAHLA"

def add_task(title, priority="medium"):
    """Add a new task to the task list.
    
    Args:
        title: The task description
        priority: Priority level (low, medium, high)
    """
    data = load_tasks()
    task = {
        "id": data["next_id"],
        "title": title,
        "priority": priority,
        "completed": False
    }
    data["tasks"].append(task)
    data["next_id"] += 1
    save_tasks(data)
    print(f"Task #{task['id']} added : {title}")
    
def list_tasks():
    """Display all tasks with their status."""
    data = load_tasks()
    if not data["tasks"]:
        print("No tasks yet. Add one with: taskflow add <title>")
        return
    print("\nYour Tasks:")
    print("-" * 40)
    for task in data["tasks"]:
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{status} #{task['id']}  {task['title']} ({task['priority']})")
        
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

def complete_task(task_id):
    """Mark a task as completed.
    
    Args:
        task_id: The ID of the task to complete
    """
    data = load_tasks()
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(data)
            print(f"Task #{task_id} marked as complete!")
            return
    print(f"Task #{task_id} not found")
    
def main():
    """Main entry point for TaskFlow.
    
    This function displays the welcome message and usage instructions.
    We'll expand this to handle actual commdans in later steps.
    """
    
    if len(sys.argv) < 2:
        print (f" TaskFlow v{ __version__ }")
        print (" Your command - line task manager ")
        print ("\nUsage : python taskflow.py <command> [options]")
        print ("\nCommands :")
        print (" add    Add a new task ")
        print (" list   List all tasks ")
        print (" help   Show this help message ")
        return
    
    command = sys.argv[1]
    
    if command == "add" and len(sys.argv) >=3:
        title = " ".join(sys.argv[2:])
        add_task(title)
    elif command == "list":
        list_tasks()
    elif command == "done" and len(sys.argv) >= 3:
        task_id = int(sys.argv[2])
        complete_task(task_id)
    else:
        print(f"Unknown command: {command}")
    
if __name__ == "__main__":
    main()