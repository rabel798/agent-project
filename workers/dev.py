from gemini import call_gemini

def build_code(plan):
    prompt = f"Write full working code for:\n{plan}"
    return call_gemini(prompt)