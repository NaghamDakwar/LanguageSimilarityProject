import docx
import pandas as pd
import re


def extract_answers(docx_file: str):
    def is_bold_and_underlined(run):
        return run.bold and run.underline

    def is_underlined_only(run):
        return run.underline and not run.bold

    def clean_text(text):
        return text.replace('\n', ' ').replace('\r', '').strip()

    # Open the document
    doc = docx.Document(docx_file)
    subject_data = []
    current_subject = None
    process_question = False
    question_to_process = None
    question_ends = [str(i) for i in range(1,7)]

    for para in doc.paragraphs:
        text = clean_text(para.text)
        if not text:
            continue

        if any(is_bold_and_underlined(run) for run in para.runs):
            if current_subject:
                subject_data.append(current_subject)

            current_subject = {'subject': text, 'dyad': text.split('_')[1], 'gender': text.split('_')[2]}
            process_question = False
            for i in range(1,7):
                current_subject['Q'+str(i)] = []

        elif any(is_underlined_only(run) for run in para.runs):
            questionNum = text.split('_')[2]
            if questionNum in question_ends:
                process_question = True
                question_to_process = questionNum
            else:
                process_question = False

        elif process_question and current_subject:
            words = re.findall(r'\b[\u0590-\u05FF]+|\b[A-Za-z]+\b', text)
            current_subject["Q"+str(question_to_process)].extend(words)

    if current_subject:
        subject_data.append(current_subject)

    return subject_data

file_path = "" #trasncripts file pathway
subject_data = extract_answers(file_path)
df = pd.DataFrame(subject_data)
df.to_csv('', index=False) #where to save
