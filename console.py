from quiz_brain import QASolver
def play_quiz(qs_list):
    full_form = {"t": "True", "f": "False"}
    quiz = QASolver(qs_list)
    while not quiz.is_end():
        quiz.select_qs()
        user_ans = full_form[input(quiz.format_qs()).lower()]
        win = quiz.is_correct(user_ans)
        if win:
            print(f"you got it right (+100) \n score = {quiz.score}")
        else:
            print(f"wrong answer (-50) \n score =  {quiz.score}")
