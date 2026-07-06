def generate_resume_bullets(repo):

    name = repo.get("name", "")
    desc = repo.get("description", "")

    bullets = [
        f"Developed {name} project.",
        f"Implemented features related to {desc}.",
        "Applied software engineering and problem-solving skills.",
        "Utilized Git and GitHub for version control."
    ]

    return bullets


def generate_linkedin_description(repo):

    return f"""
• Project: {repo.get('name')}

• Description:
{repo.get('description')}

• Technologies:
{repo.get('language')}

• Developed using industry-standard software engineering practices.
"""