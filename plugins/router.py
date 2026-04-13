def route(task):
    if "build" in task or "app" in task:
        return "dev"
    elif "open" in task or "website" in task:
        return "web"
    else:
        return "plan"