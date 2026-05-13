from flask import Flask, render_template, request
import os
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    if 'resume' not in request.files:
        return "No file uploaded"

    file = request.files['resume']

    if file.filename == '':
        return "No selected file"

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    resume_text = extract_text_from_pdf(filepath)

    skills = extract_skills(resume_text)

    score = len(skills) * 10

    if score > 100:
        score = 100

    questions = []

    question_bank = {
        "python": [
            "What is list comprehension?",
            "Explain OOP concepts in Python"
        ],
        "machine learning": [
            "What is overfitting?",
            "Difference between supervised and unsupervised learning"
        ],
        "sql": [
            "What is normalization?",
            "Difference between DELETE and TRUNCATE"
        ]
    }

    for skill in skills:
        skill_lower = skill.lower()

        if skill_lower in question_bank:
            questions.extend(question_bank[skill_lower])

    return render_template(
        'result.html',
        skills=skills,
        score=score,
        questions=questions
    )

if __name__ == '__main__':
    app.run(debug=True)