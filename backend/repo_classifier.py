def classify_repo(repo):

    name = repo.get("name","").lower()
    desc = repo.get("description","")

    text = f"{name} {desc}".lower()

    if any(x in text for x in
           ["ml","ai","yolo","cnn","nlp"]):
        return "AI/ML"

    elif any(x in text for x in
             ["react","html","css","js"]):
        return "Web"

    elif any(x in text for x in
             ["leetcode","dsa","algorithm"]):
        return "DSA"

    elif any(x in text for x in
             ["data","analytics","powerbi"]):
        return "Data Analytics"

    return "Other"