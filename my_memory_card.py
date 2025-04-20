#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import randint


def show_result():
    Gbutton.setText('Следующий вопрос')
    RadioGroupBox1.hide()
    RadioGroupBox2.show()
    RadioGroupBox2.setLayout(result_line)
    h_line.addWidget(RadioGroupBox2)
    
def show_question():
    RadioGroupBox2.hide()
    RadioGroupBox1.show()
    Gbutton.setText('Ответить')
    RadioGroup.setExclusive(False)    
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    RadioGroup.setExclusive(True) 

#def start_test():
    #text = Gbutton.text()
    #if text == 'Ответить':
        #show_result()
    #else:
        #show_question()


#def ask(question, right_ans, wrong1, wrong2, wrong3):
    #global answers
    #answers = [ans1, ans2, ans3, ans4]
    #shuffle(answers)
    #result.setText(right_ans)
    #answers[0].setText(right_ans)
    #answers[1].setText(wrong1)
    #answers[2].setText(wrong2)
    #answers[3].setText(wrong3)
    #question = QLabel(question)
    #layout_line4.addWidget(question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
    #show_question()
    





#def show_correct(res):
    #h_line3.addWidget(result, alignment = Qt.AlignCenter)
    #text.setText(res)
    #show_result()

app = QApplication([])
my_win = QWidget()
my_win.resize(333,300)
my_win.show()

class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
def ask(q: Question):
    global answers
    answers = [ans1, ans2, ans3, ans4]
    shuffle(answers)
    result.setText(q.right_ans)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    layout_line4.addWidget(question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
    show_question()
my_win.answers = 0
my_win.total_questions = 0
def check_answer():
    global count_TRUE
    global count_answers
    global res
    if answers[0].isChecked() == True:
        my_win.answers += 1
        res = 'Правильно!' 
    else:
        res = 'Неверно'
    print('Статистика\n-Всего вопросов:', my_win.total_questions, '\n-Правильных ответов:', my_win.answers,'\n-Рейтинг:', my_win.answers/my_win.total_questions * 100, '%')
    show_correct(res)


def show_correct(res):
    h_line3.addWidget(result, alignment = Qt.AlignCenter)
    text.setText(res)
    show_result()



my_win.cur_question = 0
def next_question():
    my_win.total_questions += 1
    my_win.total += 1
    if my_win.total >= len(questions_list)-1:
        my_win.total = -1
        my_win.cur_question = 0
        shuffle(questions_list)
    ask(questions_list[my_win.cur_question]) 
    my_win.cur_question += 1
def click_OK():
    text = Gbutton.text()
    if text == 'Ответить':
        check_answer()
    else:
        next_question()



my_win.setWindowTitle('Memory Card')
RadioGroupBox1 = QGroupBox('Варианты ответов')
RadioGroupBox2 = QGroupBox('Результат теста')
question = QLabel('Информатика (более полно, точно) – наука, изучающая:')
Gbutton = QPushButton('Ответить')
ans1 = QRadioButton()
ans2 = QRadioButton()
ans3 = QRadioButton()
ans4 = QRadioButton()
text = QLabel('Правильно/Неправильно')
result = QLabel()
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_line4 = QHBoxLayout()
layout_line5 = QHBoxLayout()
h_line = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
result_line = QVBoxLayout()
h_line2.addWidget(text, alignment = Qt.AlignLeft)


result_line.addLayout(h_line2)
result_line.addLayout(h_line3)

layout_ans2.addWidget(ans1)
layout_ans2.addWidget(ans2)
layout_ans3.addWidget(ans3)
layout_ans3.addWidget(ans4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox1.setLayout(layout_ans1)

h_line.addWidget(RadioGroupBox1)
layout_line5.addStretch(2)
layout_line5.addWidget(Gbutton, stretch=3)
layout_line5.addStretch(2)
layout_line5.setAlignment(Qt.AlignCenter)

main_line = QVBoxLayout()
main_line.setSpacing(5)
main_line.addLayout(layout_line4)
main_line.addLayout(h_line)
main_line.addLayout(layout_line5)


RadioGroup = QButtonGroup() 
RadioGroup.addButton(ans1)
RadioGroup.addButton(ans2)
RadioGroup.addButton(ans3)
RadioGroup.addButton(ans4)

questions_list = []
questions_list.append(
Question('Государственный язык Португалии', 'Португальский', 'Английский', 'Испанский', 'Французский'))
questions_list.append(
Question('Что изучает информатика?', 'Компьютерные технологии и среды',
'Компьютеры', 'Программирование',
'Операционные системы и среды'))
questions_list.append(
Question('2*(7+4)^2', '242', '272', '44', '42'))

shuffle(questions_list)
my_win.total = -1
my_win.cur_question = 0
Gbutton.clicked.connect(click_OK)
next_question()




my_win.setLayout(main_line)
app.exec_()