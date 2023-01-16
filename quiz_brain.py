import random as rd
import html

class QASolver:
    def __init__(self, qs_data):
        self.score = 0
        self.qs_data = qs_data
        self.select_list = [i for i in range(len(self.qs_data))]
        self.rd_index = -1
        self.q_no = 0
        self.total_qs=10

    def select_qs(self):
        self.q_no += 1
        self.rd_index = rd.choice(self.select_list)
        self.select_list.remove(self.rd_index)
        return html.unescape(self.qs_data[self.rd_index].question)

    def format_qs(self):
        return f"Q.{self.q_no}: {html.unescape(self.qs_data[self.rd_index].question)} (T/F)? "

    def is_correct(self, u_ans):
        if self.qs_data[self.rd_index].answer == u_ans:
            self.score += 100
            return 1
        else:
            self.score -= 50
            return 0

    def is_end(self):
        if len(self.select_list) == 0 or self.q_no == self.total_qs:
            return 1
        else:
            return 0
