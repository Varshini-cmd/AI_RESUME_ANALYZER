import spacy

nlp = spacy.load("en_core_web_sm")

skills_list = [
    "python",
    "java",
    "machine learning",
    "deep learning",
    "sql",
    "flask",
    "html",
    "css",
    "javascript",
    "nlp",
    "tensorflow",
    "pandas",
    "numpy"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill in text:
            found_skills.append(skill)

    return found_skills