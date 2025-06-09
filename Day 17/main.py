import question_model as qm
import data as dt

def questions_bank_method():
    question_bank = []
    for data in dt.question_data:
        question_bank.append(qm.Question(data["text"], data["answer"]))
    return  question_bank
