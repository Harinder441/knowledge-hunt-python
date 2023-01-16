from tkinter import *
from quiz_brain import QASolver

THEME_COLOR = "#375362"
RED = "#EE665D"
GREEN = "#29B677"
FONT_NAME = "Courier"


class Ui:
    def __init__(self, quiz:QASolver):

        self.quiz = quiz
        self.win = Tk()
        self.win.title("Widget Examples")
        self.win.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score = Label(text=f"Score:{0}", font=(FONT_NAME, 12, "bold"), fg="white", bg=THEME_COLOR,
                           width=30)
        self.score.grid(row=0, column=0, columnspan=2, pady=(0, 4))
        self.canvas = Canvas(height=400, width=400)
        self.question_label = self.canvas.create_text(200, 200, text="Website", font=(FONT_NAME, 16, "bold"),
                                                      fill=THEME_COLOR,
                                                      width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        self.get_ques()
        true_image = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_image, highlightthickness=0, command=lambda: self.user_input("True"))
        self.true_btn.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_image, highlightthickness=0, command=lambda: self.user_input("False"))
        self.false_btn.grid(row=2, column=1)
        self.win.mainloop()

    def user_input(self, inp:str):
        if self.quiz.is_end():
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_label, text="End of the quiz", fill=THEME_COLOR)
            return
        if self.quiz.is_correct(inp):
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.score.config(text=f"Score:{self.quiz.score}")
        self.canvas.itemconfig(self.question_label, fill="white")
        self.win.after(500, self.get_ques)

    def get_ques(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_label, text=self.quiz.select_qs(), fill=THEME_COLOR)
