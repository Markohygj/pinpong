import json

from PyQt5.QtWidgets import *
'''Замітки в json'''
notes = {}

with open("notes_data.json", "r", encoding="utf-8") as file:
    notes = json.load(file)
print(notes)
app = QApplication([])
app.setStyleSheet("""
        
QWidget{
 background: #e5fffe;


}

""")
window = QWidget()
window.setWindowTitle("Розумні замітки")
window.resize(900, 600)

textEdit = QTextEdit()
text1 = QLabel("Список заміток")
listNotes = QListWidget()
createBtn = QPushButton("Створити замітку")
deleteBtn = QPushButton("Видалити замітку")
changeBtn = QPushButton("Змінити замітку")
addBtn = QPushButton("Додати до замітки")
vidkripBtn = QPushButton("Відкріпити від замітки")
poshukBtn = QPushButton("Пошук за тегом")

text2 = QLabel("Список тегів")
listTag = QListWidget()
lineEdit = QLineEdit()


mainLine = QHBoxLayout()
column1 = QVBoxLayout()
column1.addWidget(textEdit)
mainLine.addLayout(column1)
column2 = QVBoxLayout()
column2.addWidget(text1)

column2.addWidget(listNotes)
column2.addWidget(createBtn)

column2.addWidget(deleteBtn)
column2.addWidget(changeBtn)
column2.addWidget(text2)
column2.addWidget(listTag)
column2.addWidget(lineEdit)
column2.addWidget(addBtn)
column2.addWidget(vidkripBtn)
column2.addWidget(poshukBtn)


mainLine.addLayout(column2)

window.setLayout(mainLine)


listNotes.addItems(notes)

def showText():
    key = listNotes.selectedItems()[0].text()
    text = notes[key]["текст"]
    textEdit.setText(text)
    listTag.clear()
    listTag.addItems(notes[key]["теги"])

def create():
    key, ok = QInputDialog.getText(window, "Створення змітки", "Назва замітки: ")
    if ok == True:
        notes[key] = {
            "текст":"",
            "теги":[]
        }
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
        listNotes.clear()
        listNotes.addItems(notes)


def deleted():
    key = listNotes.selectedItems()[0].text()
    notes.pop(key)

    with open("notes_data.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)
    listNotes.clear()
    listNotes.addItems(notes)

def addtag ():
    key = listNotes.selectedItems()[0].text()
    tag = lineEdit.text()
    notes[key]["теги"].append(tag)
    listTag.clear()
    listTag.addItems(notes[key]["теги"])

addBtn.clicked.connect(addtag)
listNotes.itemClicked.connect(showText)
createBtn.clicked.connect(create)
deleteBtn.clicked.connect(deleted)
window.show()
app.exec_()