from fastapi import FastAPI

from github_api import (
    get_profile,
    get_repositories,
    get_readme
)

from profile_analyzer import analyze_profile
from repo_classifier import classify_repo
from ai_analyzer import analyze_project

app = FastAPI()


@app.get("/analyze/{username}")
def analyze(username):

    profile = get_profile(username)

    repos = get_repositories(username)

    result = []

    for repo in repos:

        readme = get_readme(
            username,
            repo["name"]
        )

        result.append({

            "repo":
            repo["name"],

            "type":
            classify_repo(repo),

            "analysis":
            analyze_project(
                repo,
                readme
            )
        })

    return {
        "profile":
        analyze_profile(
            profile,
            repos
        ),

        "repositories":
        result
    }