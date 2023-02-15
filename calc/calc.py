import sys

from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QPushButton


class Button(QPushButton):
    def __init__(self, name):
        super().__init__(name)
        self.name = name


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("калькулятор")
        self.setFixedSize(QSize(1280, 720))
        self.result = '0'
        self.label = QLabel(self.result)
        self.label.setFixedSize(1080, 100)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label)

        self.number_1 = Button('1')
        self.number_2 = Button('2')
        self.number_3 = Button('3')
        self.number_4 = Button('4')
        self.number_5 = Button('5')
        self.number_6 = Button('6')
        self.number_7 = Button('7')
        self.number_8 = Button('8')
        self.number_9 = Button('9')
        self.number_0 = Button('0')
        self.ac = Button('AC')
        self.multiply = Button('*')
        self.divide = Button('/')
        self.plus = Button('+')
        self.minus = Button('-')
        self.ravno = Button('=')

        self.number_1.clicked.connect(lambda: self.clicked_(self.number_1.name))
        self.number_2.clicked.connect(lambda: self.clicked_(self.number_2.name))
        self.number_3.clicked.connect(lambda: self.clicked_(self.number_3.name))
        self.number_4.clicked.connect(lambda: self.clicked_(self.number_4.name))
        self.number_5.clicked.connect(lambda: self.clicked_(self.number_5.name))
        self.number_6.clicked.connect(lambda: self.clicked_(self.number_6.name))
        self.number_7.clicked.connect(lambda: self.clicked_(self.number_7.name))
        self.number_8.clicked.connect(lambda: self.clicked_(self.number_8.name))
        self.number_9.clicked.connect(lambda: self.clicked_(self.number_9.name))
        self.number_0.clicked.connect(lambda: self.clicked_(self.number_0.name))
        self.ac.clicked.connect(lambda: self.clicked_(self.ac.name))
        self.multiply.clicked.connect(lambda: self.clicked_(self.multiply.name))
        self.divide.clicked.connect(lambda: self.clicked_(self.divide.name))
        self.plus.clicked.connect(lambda: self.clicked_(self.plus.name))
        self.minus.clicked.connect(lambda: self.clicked_(self.minus.name))
        self.ravno.clicked.connect(self.equals)

        self.layout.addWidget(self.number_7, 1, 0)
        self.layout.addWidget(self.number_8, 1, 1)
        self.layout.addWidget(self.number_9, 1, 2)
        self.layout.addWidget(self.divide, 1, 3)
        self.layout.addWidget(self.number_4, 2, 0)
        self.layout.addWidget(self.number_5, 2, 1)
        self.layout.addWidget(self.number_6, 2, 2)
        self.layout.addWidget(self.multiply, 2, 3)
        self.layout.addWidget(self.number_1, 3, 0)
        self.layout.addWidget(self.number_2, 3, 1)
        self.layout.addWidget(self.number_3, 3, 2)
        self.layout.addWidget(self.minus, 3, 3)
        self.layout.addWidget(self.ac, 4, 0)
        self.layout.addWidget(self.number_0, 4, 1)
        self.layout.addWidget(self.plus, 4, 2)
        self.layout.addWidget(self.ravno, 4, 3)

        self.layout.setContentsMargins(100, 52, 100, 40)
        self.layout.setHorizontalSpacing(0)
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

    def clicked_(self, button):
        if button == 'AC':
            self.label.setText('0')
        else:
            if self.label.text() == "0":
                self.label.setText("")

            self.label.setText(f'{self.label.text()}{button}')

    def equals(self):
        screen = self.label.text()
        try:
            answer = eval(screen)
            self.label.setText(str(answer))
        except:
            self.label.setText("что-то не так")


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QLabel {
            background-color: white;
            font-size: 60px;
        }

        QPushButton {
            Width: 270px;
            min-height: 100px;
            max-height: 150px;
            font-size: 35px;
        }
    """)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()