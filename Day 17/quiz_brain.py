import main as mn

pontuacao = 0
question_bank = mn.questions_bank_method()
for question in question_bank:
    print(question.text)
    resp = input("True or False?")
    if question.answer != resp:
        print(f"Resposta errada. Sua pontuacao: {pontuacao}")
        break
    else:
        pontuacao += 1
