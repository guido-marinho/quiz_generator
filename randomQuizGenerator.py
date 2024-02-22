import os
import random
import json


def generate_quizzes():
    capitals = json.load(open("data.json"))

    if not os.path.exists("randomQuiz"):
        os.makedirs("randomQuiz")

    for quiz_num in range(35):
        """Cria os arquivos com os questionários e as respostas."""
        quiz_file = open(
            os.path.join(
                "randomQuiz",
                "capitalsquiz%s.txt" % (quiz_num + 1),
            ),
            "w",
        )
        answer_key_file = open(
            os.path.join(
                "randomQuiz",
                "capitalsquiz_answers%s.txt" % (quiz_num + 1),
            ),
            "w",
        )

        """Escreve o cabeçalho do questionário."""
        quiz_file.write("Nome:\n\nData:\n\nPeríodo:\n\n")
        quiz_file.write(
            (" " * 20) + "Quiz de Capital dos Estados (Form %s)" %
            (quiz_num + 1),
        )
        quiz_file.write("\n\n")

        """Embaralha a ordem dos estados."""
        states = list(capitals.keys())
        random.shuffle(states)

        """Percorre todos os 26 estados, criando uma pergunta para cada um."""
        for question_num in range(26):
            corret_answer = capitals[states[question_num]]
            wrong_answers = list(capitals.values())
            del wrong_answers[wrong_answers.index(corret_answer)]
            wrong_answers = random.sample(wrong_answers, 3)
            answer_options = wrong_answers + [corret_answer]
            random.shuffle(answer_options)

            """
                Escreve a pergunta e as opções de
                resposta no arquivo do questionário
            """
            quiz_file.write(
                "%s. Qual é a capital de %s?\n"
                % (
                    question_num + 1,
                    states[question_num],
                )
            )
            for i in range(4):
                quiz_file.write(" %s. %s\n" % ("ABCD"[i], answer_options[i]))
            quiz_file.write("\n")

            """Escreve a resposta no arquivo de respostas."""
            answer_key_file.write(
                "%s. %s\n"
                % (
                    question_num + 1,
                    "ABCD"[answer_options.index(corret_answer)],
                )
            )

        quiz_file.close()
        answer_key_file.close()


generate_quizzes()
