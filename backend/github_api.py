import requests

BASE = "https://api.github.com"

def get_profile(username):

    url = f"{BASE}/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()


def get_repositories(username):

    url = f"{BASE}/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    return response.json()


def get_readme(username, repo):

    url = f"{BASE}/repos/{username}/{repo}/readme"

    headers = {
        "Accept":
        "application/vnd.github.raw+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return ""

    return response.text