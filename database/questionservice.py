from database.models import Question, db
import random


def get_questions_db(level):
    if level == 'all':
        questions = []
        all_questions = Question.query.all()

        for i in range(20):
            questions.append(random.choice(all_questions))

        return questions

    questions_form_level = Question.query.filter_by(level=level).all()

    questions = [random.choice(questions_form_level) for i in range(20)]

    return questions


def check_user_answer_db(question_id, user_answer):
    current_question = Question.query.get(question_id)

    if current_question.correct_answer == user_answer:
        return True

    return False


# добавление вопросов в базу
def add_question_db(main_question, answer_1, answer_2, answer_3, answer_4, correct_answer):
    add_question = Question.query.all()
    return add_question
