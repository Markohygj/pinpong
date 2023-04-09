from PyQt5.QtWidgets import *
import code
app = QApplication([])
window = QWidget()
shooterBtn = QPushButton("Шутер")

line = QHBoxLayout()
line.addWidget(shooterBtn)


window.setLayout(line)
shooterBtn.clicked.connect(code.game)
window.show()
app.exec_()