import requests
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from .env import API_KEY



def gemini_call(prompt):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    
    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(url, json=data)
    result = response.json()
    
    return result["candidates"][0]["content"]["parts"][0]["text"]


# Planner Agent
def planner_agent(task):
    prompt = f"Break this into steps: {task}"
    return gemini_call(prompt)


# Dev Agent
def dev_agent(plan):
    prompt = f"Execute this plan and write code:\n{plan}"
    return gemini_call(prompt)


# Run system
task = "Build a simple calculator in Python"

plan = planner_agent(task)
print("\n🧠 Plan:\n", plan)

output = dev_agent(plan)
print("\n💻 Code:\n", output)