import json
import os
import datetime

NOTES_FILE = 'notes.json'


def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            return json.load(file)
    else:
        return []


def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=4)


def add_note(title, message):
    notes = load_notes()
    note = {
        'id': len(notes) + 1,
        'title': title,
        'message': message,
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    notes.append(note)
    save_notes(notes)
    print('Заметка успешно добавлена.')


def list_notes(filter_date=None):
    notes = load_notes()
    if filter_date:
        filtered_notes = [
            note for note in notes if note['timestamp'] >= filter_date]
    else:
        filtered_notes = notes

    for note in filtered_notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Содержание: {note['message']}")
        print(f"Дата/время: {note['timestamp']}")
        print('-' * 30)


def delete_note(note_id):
    notes = load_notes()
    updated_notes = [note for note in notes if note['id'] != note_id]
    save_notes(updated_notes)
    print('Заметка успешно удалена.')


if __name__ == "__main__":
    while True:
        print("Выберите действие:")
        print("1. Добавить заметку")
        print("2. Список заметок")
        print("3. Удалить заметку")
        print("4. Выход")

        choice = input()

        if choice == '1':
            title = input("Введите заголовок заметки: ")
            message = input("Введите текст заметки: ")
            add_note(title, message)
        elif choice == '2':
            filter_date = input("Введите дату для фильтрации (гггг-мм-дд): ")
            list_notes(filter_date)
        elif choice == '3':
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif choice == '4':
            break
