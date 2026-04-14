from core.router import route_task

def run_agent():
    task = input("Enter your task: ")
    result = route_task(task)
    print("\n⚡ OUTPUT:\n", result)

if __name__ == "__main__":
    run_agent()

# what doest this file do in short?

# This file serves as the main entry point for the agent application. 
# It prompts the user to enter a task, routes the task to the appropriate worker 
# using the 'route_task' function from 'core.router', and then prints the output result.
