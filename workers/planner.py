from gemini import call_gemini

def run_planner(task: str):
    prompt = f"""
    Break this into clear steps:

    Task: {task}
    """

    return call_gemini(prompt)
#this takes a task as input and breaks it down into clear steps using the Gemini API.