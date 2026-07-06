import re


def extract_username(github_input):
    """
    Extract GitHub username from either:
    username
    or
    github profile URL
    """

    github_input = github_input.strip()

    if "github.com" in github_input:

        pattern = r'github\.com/([^/]+)'
        match = re.search(pattern, github_input)

        if match:
            return match.group(1)

    return github_input


def clean_text(text):

    if not text:
        return ""

    text = text.replace("\n", " ")
    text = text.replace("\r", " ")

    return text.strip()


def percentage(part, total):

    if total == 0:
        return 0

    return round((part / total) * 100, 2)