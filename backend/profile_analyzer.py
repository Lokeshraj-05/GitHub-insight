from collections import Counter

def analyze_profile(profile, repos):

    languages = []

    for repo in repos:
        lang = repo.get("language")
        if lang:
            languages.append(lang)

    return {
        "name": profile.get("name"),
        "bio": profile.get("bio"),
        "followers": profile.get("followers"),
        "repositories": len(repos),
        "languages": Counter(languages)
    }