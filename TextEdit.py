from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit, QVBoxLayout
import sys
import socket

class TextEditDemo(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)
                # Creation de la fenêtre de texte
                self.setWindowTitle("QTextEdit")
                self.setStyleSheet("color : white ; background: rgba(0,0,0,0%)")
                self.resize(260,260)
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.textEdit = QTextEdit()

                layout = QVBoxLayout()
                layout.addWidget(self.textEdit)
                self.setLayout(layout)
                
                self.textEdit.textChanged.connect(self.recupText)
                #print(self.recupText)
        
        """Pas utile du tout, je le garde au cas où"""
        def btnPress1_Clicked(self):
                myText = self.textEdit.toPlainText()
                print(myText) # on peut le faire passer dans un parseur, c'est nice
                self.textEdit.setPlainText(myText)
        
        def recupText(self):
                myText = self.textEdit.toPlainText()
                #print(myText) # on peut le faire passer dans un parseur, c'est nice
                self.sock.sendto(myText.encode(), ("127.0.0.1", 1234))
                
                
       
if __name__ == '__main__':
        
        app = QApplication(sys.argv)
        win = TextEditDemo()
        win.show()
        # Récupération du contenu de l'éditeur
        sys.exit(app.exec_())
        """
        app = QGuiApplication(argc, argv)
        window = RasterWindow()
        window.show()
        sys.exit(app.exec())
        """
