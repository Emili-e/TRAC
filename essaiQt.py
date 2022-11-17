from PyQt5.QtWidgets import QApplication, QLabel
"""
app = QApplication([])
label = QLabel('Hello World!')

#w.setWindowTitle("Guru99")
label.show()
app.exec()"""

from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QVBoxLayout,QPushButton
import sys

class TextEditDemo(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)

                self.setWindowTitle("QTextEdit")
                self.resize(300,270)

                self.textEdit = QTextEdit()

                layout = QVBoxLayout()
                layout.addWidget(self.textEdit)
                self.setLayout(layout)


        def btnPress1_Clicked(self):
                self.textEdit.setPlainText("Hello PyQt5!\nfrom pythonpyqt.com")

        def btnPress2_Clicked(self):
                self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\nHello</font>")

if __name__ == '__main__':
        app = QApplication(sys.argv)
        win = TextEditDemo()
        win.show()
        sys.exit(app.exec_())
