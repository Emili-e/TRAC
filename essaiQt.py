from PyQt5.QtWidgets import QApplication, QLabel
"""
app = QApplication([])
label = QLabel('Hello World!')

#w.setWindowTitle("Guru99")
label.show()
app.exec()"""

from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit, QVBoxLayout
from PyQt5.QtGui import QGuiApplication
import sys
from threading import Timer  
#import lexer

class TextEditDemo(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)

                self.setWindowTitle("QTextEdit")
                self.resize(260,260)

                self.textEdit = QTextEdit()

                layout = QVBoxLayout()
                layout.addWidget(self.textEdit)
                self.setLayout(layout)
                
                self.textEdit.textChanged.connect(self.recupText)
        
        """Pas utile du tout, je le garde au cas où"""
        def btnPress1_Clicked(self):
                myText = self.textEdit.toPlainText()
                print(myText) # on peut le faire passer dans un parseur, c'est nice
                self.textEdit.setPlainText(myText)
        
        def recupText(self):
                myText = self.textEdit.toPlainText()
                print(myText) # on peut le faire passer dans un parseur, c'est nice
                #lexer.lexing(myText)
                
                
       
if __name__ == '__main__':
        
        app = QApplication(sys.argv)
        win = TextEditDemo()
        win.show()
        
        sys.exit(app.exec_())
        """
        app = QGuiApplication(argc, argv)
        window = RasterWindow()
        window.show()
        sys.exit(app.exec())
        """
