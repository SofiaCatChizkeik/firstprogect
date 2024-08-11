from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication
card_width, card_height = 600, 500

app = QApplication([])

from main_window import *
from menu_window import *

def click_ok():
    if btn_next.text() == "Відповісти":
        gb_question.hide()
        gb_answer.show()

        btn_next.setText("Наступне запитання")
    else:
        gb_question.show()
        gb_answer.hide()

        btn_next.setText('Відповісти')

def check_result():
    correct = answer.isChecked()
    if correct:
        lb_Result.setText('Правильно')
        answer.got_right()
    else:
        lb_Result.setText('Неправильно')
        answer.got_wrong()

def switch_screen():
    if btn_answer.text() == 'Відповісти':
        check_result()
        gb_question.hide()
        gb_answer.show()

        btn_answer.setText('Наступне запитання')
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()

        btn_answer.setText('Відповісти')

def rest(sp_rest):
    sleep(10)
    sp_rest.value()

btn_next.clicked.connect(click_ok)

window.show()
app.exec_()

class Question():
    def __init__(self, quest, ans1, ans2, ans3, ans4, trieds, right_answer, next):
        self.question = quest
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.trieds = 0
        self.right_answer = 0
        self.next = True
    def got_right(self):
        self.trieds += 1
        self.right_answer += 1
    def got_wrong(self):
        self.trieds += 1

quest1 = Question("Кіт", "cat", "elephant", "rabbit", "snake")
quest2 = Question("Королева", "king", "queen", "prince", "princess")
quest3 = Question("Екран", "phone", "laptop", "screen", "computer")
quest4 = Question("Село", "town", "city", "river", "village")

questions = [q1, q2, q3, q4]
random_question = choice(questions)

radio_list = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]

shuffle(radio_list)

answer = radio_list[0]
wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]

answer.setText(cur_question.answer)
wrong_answer1.setText(cur_question.wrong_answer1)
wrong_answer2.setText(cur_question.wrong_answer2)
wrong_answer3.setText(cur_question.wrong_answer3)