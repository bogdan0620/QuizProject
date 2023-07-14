from database.models import Result, db, Rating


def get_rating_db(level):
    user_position = Rating.query.order_by(Rating.user_correct_answer.desc()).filter_by(level=level)
    user_ids = [{i.user_id: i.user_correct_answers} for i in user_position]

    return user_ids[:5]


# добавление ответа пользователя
def add_user_answer_db(user_id, user_answers, correctness):
    add_user_answer = Result.query.all()
    return add_user_answer


def add_user_rating_db(user_id, correct_answer, level):
    # есть ли пользователь в таблице rating
    user_rating = Rating.query.filter_by(user_id=user_id, level=level).first()

    if user_rating:
        user_rating.user_correct_answers += correct_answer

    else:
        user_rating = Rating(user_id=user_id,
                             user_correct_answers=correct_answer,
                             level=level)
        db.session.add(user_rating)

    db.session.commit()


def get_user_position(user_id, correct_answers, level):
    add_user_rating_db(user_id, correct_answers, level)
    user_position = Rating.query.order_by(Rating.user_correct_answers.desc()).filter_by(level=level)
    user_ids = [i.user_id for i in user_position]
    return user_ids.index(user_id) + 1
