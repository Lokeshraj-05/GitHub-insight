def analyze_project(repo, readme):

    return {
        "project": repo["name"],
        "description": repo["description"],
        "summary":
        f"""
        This repository named
        {repo['name']} demonstrates
        skills in software development,
        problem solving and
        project implementation.
        """,
    }