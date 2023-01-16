# IMP
## connect to the API
## Catagary selection option
## no. of question selection
## 

from quiz_brain import QASolver
from data import question_data
from question_model import QModel
from ui import Ui

qs_list = []
for qd in question_data:
    qs_list.append(QModel(qd["question"], qd["correct_answer"]))
quiz = QASolver(qs_list)
quiz_play = Ui(quiz)







# ________________________________UI______________________________________


