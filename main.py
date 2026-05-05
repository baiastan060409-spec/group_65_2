# import flet as ft 


# def main_page(page: ft.Page):
#     page.title = 'Моё первое приложение'
#     page.theme_mode = ft.ThemeMode.LIGHT

#     hello_text = ft.Text(value='Helo world')

#     greeting_history = []
#     history_text = ft.Text('История приветствий: ')


#     def on_button_click(_):
#         # print(name_input.value)
#         # pass
#         name = name_input.value.strip()
        

#         if name:
#             # print(name)
#             # hello_text = 'sdfsdfsdf'
#             hello_text.color = None
#             hello_text.value = f'Hello {name}'
#             name_input.value = None

#             greeting_history.append(name)
#             print(greeting_history)
#             history_text.value = 'История приветствий: \n-' + '\n-'.join(greeting_history)
#         else:
#             # print('Error')
#             hello_text.value = 'ОШИБКА Введите имя'
#     # text_button = ft.TextButton(text='SEND', icon=ft.Icons.SEND)
#     # icon_button = ft.IconButton(icon=ft.Icons.SEND)

#     def clear_history(_):
#         greeting_history.clear()
#         history_text.value = 'История приветствий:'
#         page.update()

#     clear_button = ft.IconButton(icon=ft.Icons.CLEAR, on_click=clear_history)

#     page.add(hello_text, name_input, elevated_button, clear_button, history_text)

# ft.app(main_page) 
# ft.app(main_page, view=ft.AppView.WEB_BROWSER)
# ft.app(main_page, view=ft.AppView.WEB_BROWSER)

# from datetime import datetime

# while True:
#     name = input("Введите имя (или 'выход'): ")

#     if name.lower() == "выход":
#         break

#     now = datetime.now()
#     time_str = now.strftime("%Y:%m:%d - %H:%M:%S")

#     print(f"{time_str} - Привет, {name}!")

import random

names = ["Алексей", "Мария", "Иван", "Ольга", "Анна"]

while True:
    print("\n1 - Случайное имя")
    print("2 - Ввести своё имя")
    print("0 - Выход")

    choice = input("Выбери: ")

    if choice == "1":
        print("Случайное имя:", random.choice(names))

    elif choice == "2":
        name = input("Введите имя: ")
        print(f"Привет, {name}!")

    elif choice == "0":
        print("Выход...")
        break

    else:
        print("Неверный выбор")