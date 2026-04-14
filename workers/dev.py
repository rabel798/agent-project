from gemini import call_gemini

def run_dev(task: str):
    prompt = f"""
    You are a senior developer.

    Build full working code for:
    {task}

    Return only code.
    """

    return call_gemini(prompt)
#this writes code based on the plan provided by the planner
