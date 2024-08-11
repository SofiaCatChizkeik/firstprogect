from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit

window = QWidget()

btn_menu = QPushButton('Меню')
btn_newquestion = QPushButton('Дотати запитання')
btn_clean = QPushButton('Очистити')
btn_back = QPushButton('Назад')

lb_newquestion = QLabel('Введіть запитання:')
lb_rightanswer = QLabel('Введіть вірну відповідь:')
lb_wronganswer1 = QLabel('Введіть першу хибну відповідь:')
lb_wronganswer2 = QLabel('Введіть другу хибну відповідь:')
lb_wronganswer3 = QLabel('Введіть третю хибну відповідь:')
lb_statistic = QLabel('Статистика')
