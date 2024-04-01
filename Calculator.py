from PyQt5.QtCore import Qt
import PyQt5.QtWidgets as P

class Calculator(P.QWidget):
    def __init__(self):
        super().__init__()

        self.lst = list()

        self.setWindowTitle("Calculator")
        self.li1 = P.QLabel(self)
        self.li1.setFixedSize(500, 50)
        self.li1.setStyleSheet("font-size:40px")

        self.b1 = P.QPushButton("7", self)
        self.b1.setGeometry(0, 50, 100, 100)
        self.b1.clicked.connect(self.seven)

        self.b2 = P.QPushButton("8", self)
        self.b2.setGeometry(100, 50, 100, 100)
        self.b2.clicked.connect(self.eight)

        self.b3 = P.QPushButton("9", self)
        self.b3.setGeometry(200, 50, 100, 100)
        self.b3.clicked.connect(self.nine)

        self.b4 = P.QPushButton("*", self)
        self.b4.setGeometry(300, 50, 100, 100)
        self.b4.clicked.connect(self.times)

        self.b5 = P.QPushButton("4", self)
        self.b5.setGeometry(0, 150, 100, 100)
        self.b5.clicked.connect(self.four)

        self.b6 = P.QPushButton("5", self)
        self.b6.setGeometry(100, 150, 100, 100)
        self.b6.clicked.connect(self.five)

        self.b7 = P.QPushButton("6", self)
        self.b7.setGeometry(200, 150, 100, 100)
        self.b7.clicked.connect(self.six)

        self.b8 = P.QPushButton("/", self)
        self.b8.setGeometry(300, 150, 100, 100)
        self.b8.clicked.connect(self.divide)

        self.b9 = P.QPushButton("3", self)
        self.b9.setGeometry(0, 250, 100, 100)
        self.b9.clicked.connect(self.thread)

        self.b10 = P.QPushButton('2', self)
        self.b10.setGeometry(100, 250, 100, 100)
        self.b10.clicked.connect(self.two)

        self.b11 = P.QPushButton('1', self)
        self.b11.setGeometry(200, 250, 100, 100)
        self.b11.clicked.connect(self.one)

        self.b12 = P.QPushButton('+', self)
        self.b12.setGeometry(300, 250, 100, 100)
        self.b12.clicked.connect(self.plus)

        self.b13 = P.QPushButton('0', self)
        self.b13.setGeometry(0, 350, 100, 100)
        self.b13.clicked.connect(self.null)

        self.b14 = P.QPushButton('=', self)
        self.b14.setGeometry(100, 350, 200, 100)
        self.b14.clicked.connect(self.result)

        self.b15 = P.QPushButton('-', self)
        self.b15.setGeometry(300, 350, 100, 100)
        self.b15.clicked.connect(self.subtraction)
        
        self.b16 = P.QPushButton('clear', self)
        self.b16.setGeometry(0, 450, 400, 50)
        self.b16.clicked.connect(self.clear)

        self.setFixedSize(400, 500)
        self.move(700, 100)

    def one(self):
        one = self.b11.text()
        self.lst.append(one)
        self.li1.setText(one)

    def null(self):
        null = self.b13.text()
        self.lst.append(null)
        self.li1.setText(null)

    def two(self):
        two = self.b10.text()
        self.lst.append(two)
        self.li1.setText(two) 

    def three(self):
        three = self.b9.text()
        self.lst.append(three)
        self.li1.setText(three)

    def four(self):
        four = self.b5.text()
        self.lst.append(four)
        self.li1.setText(four)

    def five(self):
        five = self.b6.text()
        self.lst.append(five)
        self.li1.setText(five)

    def six(self):
        six = self.b7.text()
        self.lst.append(six)
        self.li1.setText(six)

    def seven(self):
        seven = self.b1.text()
        self.lst.append(seven)
        self.li1.setText(seven)

    def eight(self):
        eight = self.b2.text()
        self.lst.append(eight)
        self.li1.setText(eight)

    def nine(self):
        nine = self.b3.text()
        self.lst.append(nine)
        self.li1.setText(nine)

    def times(self):
        times = self.b4.text()
        self.lst.append(times)
        self.li1.setText(times)

    def divide(self):
        divide = self.b8.text()
        self.lst.append(divide)
        self.li1.setText(divide)

    def plus(self):
        plus = self.b12.text()
        self.lst.append(plus)
        self.li1.setText(plus)

    def subtraction(self):
        subtraction = self.b15.text()
        self.lst.append(subtraction)
        self.li1.setText(subtraction)

    def clear(self):
        self.li1.setText("")
        self.lst = list()

    def result(self):
        self.li1.setText((str(eval("".join(self.lst)))))

app = P.QApplication([])
win = Calculator()
win.show()
app.exec_()
