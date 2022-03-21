from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
 
import json
 
app = QApplication([])

notes = {
    "О планетах":
    {
        "текст": "Что если водаа Марсе это признак жизни?",
        "теги": ["Марс", "гипотезы"]
    },
    "О черных дырах":
    {
        "текст":"Сингулярность на горизонте событий отсуутствует",
        "теги": ["Сингулярность","факты"]
    }
}
with open("notes.json", "w") as f:
    json.dump(notes,f)
 
'''Интерфейс приложения'''
#параметры окна приложения
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900, 600)
 
#виджеты окна приложения
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')
 
button_note_create = QPushButton('Создать заметку') #появляется окно с полем "Введите имя заметки"
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')
 
field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')
 
#расположение виджетов по лэйаутам
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
 
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
 
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)
 
col_2.addLayout(row_3)
col_2.addLayout(row_4)
 
layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)
 
'''Функционал приложения'''
def show_notes():  
    key = list_notes.selectedItems()[0].text()
    print(key)
    list_tags.clear()
    list_tags.addItems(notes[key]['tags'])
    field_text.setText(notes[key]['text'])
    
def add_notes():
    name_note, ok = QInputDialog.getText(notes_win, 'Название заметки', 'Введите заметку:')
    if ok and name_note != "":
        notes[name_note] = {'text' : '', 'tags' : []}
        list_notes.addItem(name_note)
        with open('notes.json', 'w', encoding='utf-8') as f:
            json.dump(notes, f)
 

 
'''Запуск приложения'''
#подключение обработки событий
list_notes.itemClicked.connect(show_notes)
button_note_create.clicked.connect(add_notes)
 
#запуск приложения 
notes_win.show()
with open('notes.json', 'r', encoding='utf-8') as f:
    notes = json.load(f)
    list_notes.addItems(notes)
    
    
 
app.exec_()