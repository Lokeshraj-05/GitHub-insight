from collections import Counter


def calculate_github_score(profile, repos):

    score = 0

    # Followers
    followers = profile.get("followers", 0)
    score += min(followers, 20)

    # Number of repositories
    repo_count = len(repos)
    score += min(repo_count, 20)

    # Documentation
    documented = sum(
        1 for r in repos
        if r.get("description")
    )

    if repo_count:
        score += int((documented / repo_count) * 20)

    # Stars
    stars = sum(
        r.get("stargazers_count", 0)
        for r in repos
    )

    score += min(stars, 20)

    # Languages diversity
    languages = set(
        r.get("language")
        for r in repos
        if r.get("language")
    )

    score += min(len(languages) * 2, 20)

    return min(score, 100)


def skill_distribution(repos):

    categories = []

    for repo in repos:

        text = (
            f"{repo.get('name','')} "
            f"{repo.get('description','')}"
        ).lower()

        if any(
            x in text
            for x in [
                "ai",
                "ml",
                "yolo",
                "cnn",
                "llm"
            ]
        ):
            categories.append("AI/ML")

        elif any(
            x in text
            for x in [
                "react",
                "frontend",
                "html",
                "css"
            ]
        ):
            categories.append("Frontend")

        elif any(
            x in text
            for x in [
                "flask",
                "fastapi",
                "api",
                "backend"
            ]
        ):
            categories.append("Backend")

        elif any(
            x in text
            for x in [
                "sql",
                "powerbi",
                "analytics"
            ]
        ):
            categories.append("Data")

        else:
            categories.append("Other")

    return dict(Counter(categories))


def portfolio_rating(score):

    if score >= 85:
        return "Excellent"

    elif score >= 70:
        return "Strong"

    elif score >= 50:
        return "Average"

    return "Needs Improvement"