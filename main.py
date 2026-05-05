import flet as ft
import os

def load_history():
    if os.path.exists('history.txt'):
        with open('history.txt', 'r', encoding='utf-8') as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

def save_history(history):
    with open('history.txt', 'w', encoding='utf-8') as f:
        for name in history:
            f.write(name + '\n')

def main_page(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    hello_text = ft.Text(value='Hello world')
    greeting_history = load_history()
    history_text = ft.Text('История приветствий:')

    def update_history_text():
        if greeting_history:
            history_text.value = 'История приветствий:\n- ' + '\n- '.join(greeting_history)
        else:
            history_text.value = 'История приветствий:'
        page.update()

    update_history_text()

    def on_button_click(_):          
        name = name_input.value.strip() if name_input.value else ""

        if name:
            hello_text.color = None
            hello_text.value = f'Hello {name}'
            name_input.value = None

            greeting_history.append(name)
            if len(greeting_history) > 5:
                greeting_history[:] = greeting_history[-5:]

            save_history(greeting_history)
            update_history_text()
        else:
            hello_text.value = 'ОШИБКА Введите имя'
            page.update()

    def clear_history(_):
        greeting_history.clear()
        save_history(greeting_history)
        update_history_text()

    name_input = ft.TextField(
        label="Введите имя", 
        width=300,
        on_submit=on_button_click  
    )

    elevated_button = ft.ElevatedButton("Отправить", on_click=on_button_click)

    clear_button = ft.IconButton(icon=ft.Icons.CLEAR, on_click=clear_history)

    page.add(
        hello_text,
        name_input,
        elevated_button,
        clear_button,
        history_text
    )

ft.app(main_page)




# from datetime import datetime

# while True:
#     name = input("Введите имя (или 'выход'): ")

#     if name.lower() == "выход":
#         break

#     now = datetime.now()
#     time_str = now.strftime("%Y:%m:%d - %H:%M:%S")

#     print(f"{time_str} - Привет, {name}!")



# import random

# names = ["Алексей", "Мария", "Иван", "Ольга", "Анна"]

# while True:
#     print("\n1 - Случайное имя")
#     print("2 - Ввести своё имя")
#     print("0 - Выход")

#     choice = input("Выбери: ")

#     if choice == "1":
#         print("Случайное имя:", random.choice(names))

#     elif choice == "2":
#         name = input("Введите имя: ")
#         print(f"Привет, {name}!")

#     elif choice == "0":
#         print("Выход...")
#         break

#     else:
#         print("Неверный выбор")