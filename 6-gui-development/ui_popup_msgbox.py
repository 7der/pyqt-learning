#Import all Modules
from PyQt5.QtWidgets import QMessageBox

x = 600
y = 200
def show_info_msgbox(parent, title, message):
        msg = QMessageBox()
        # msg.setFixedMessageBox(x,y)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

def show_q_msgbox(self, title, message):
        msg = QMessageBox()
        # msg.setFixedMessageBox(x,y)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
        retval = msg.exec_()

def show_warn_msgbox(self, title, message):
        msg = QMessageBox()
        # msg.setFixedMessageBox(x,y)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

def show_crit_msgbox(self, title, message):
        msg = QMessageBox()
        # msg.setFixedMessageBox(x,y)
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

        
# Types of Message QMessageBox
# 1) Information - to inform (ok)
# 2) Question - to get an answer from user (y | n) (okay | cancel)
# 3) Warning - to INFORM (ok)
# 4) Critical - to get an answer from user about a critical action (ok)

