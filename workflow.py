def run_agent_task(task: str) -> dict:
    """Placeholder for the future agent workflow.

    Later milestones will add planning, repository context, code changes,
    test execution and human approval. This function deliberately does not
    execute code or modify files yet.
    """
    if not task.strip():
        raise ValueError("Task cannot be empty")

    return {
        "status": "not_implemented",
        "task": task,
        "message": "Agent workflow will be implemented in a later milestone.",
    }
