from planner import plan_task
from dev import build_code
from web import browse
from router import route
from caveman import clean_output

def run_agent():
    task = input("Enter your task: ")

    decision = route(task)

    if decision == "dev":
        plan = plan_task(task)
        print("\n🧠 Plan:\n", plan)

        code = build_code(plan)
        code = clean_output(code)

        print("\n💻 Code:\n", code)

    elif decision == "web":
        url = input("Enter URL: ")
        browse(url)

    else:
        plan = plan_task(task)
        print("\n🧠 Plan:\n", plan)


if __name__ == "__main__":
    run_agent()