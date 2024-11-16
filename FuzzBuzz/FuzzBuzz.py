#Create a form with a label FuzzBuzz and a box to display the numbers 1 to 100 using PYQT5

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont

class FuzzBuzz(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #set gridlayout to show the heading label FuzzBuzz
        layout = QVBoxLayout()
        layout.addWidget(QLabel('FuzzBuzz'))
        self.setLayout(layout)

        #create a label to display the numbers 1 to 100 and place in centre screen
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 20))
        layout.addWidget(self.label)
        #add wordwrap
        self.label.setWordWrap(True)


        #Create a loop to display the numbers 1 to 100
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                self.label.setText(self.label.text() + ' FuzzBuzz ')
            elif i % 3 == 0:
                self.label.setText(self.label.text() + ' Fuzz ')
            elif i % 5 == 0:
                self.label.setText(self.label.text() + ' Buzz ')
            else:
                self.label.setText(self.label.text() + ' ' + str(i))

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FuzzBuzz()
    sys.exit(app.exec_())