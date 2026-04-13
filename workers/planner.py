from gemini import call_gemini

def plan_task(task):
    prompt = f"Break this into clear steps:\n{task}"
    return call_gemini(prompt)