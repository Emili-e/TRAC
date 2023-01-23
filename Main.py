import socket
import subprocess
import time
import lexer



# Lancement d'un programme externe avec Popen()
processText = subprocess.Popen(["python","TextEdit.py"])
processDraw = subprocess.Popen(["python","DrawWindow.py"])

# parser = Parser
# Création d'un socket UDP
sockText = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Liaison du socket à une adresse IP et un port
sockText.bind(("127.0.0.1", 1234))

# Réception d'un message
time.sleep(2)
test_int = 10
while True:
    # Attend de recevoir tout ce qui a été écrit dans la fenêtre
    Text = sockText.recvfrom(100000)
    #sockText.sendto(str("clear").encode(), ("127.0.0.1", 1111))
    # Appelle le lexer
    lexer.lexing(Text.__getitem__(0).decode(), sockText)
    """
    test_int = test_int + 1
    test_char = str(test_int)
    """
    
