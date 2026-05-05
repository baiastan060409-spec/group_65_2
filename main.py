import flet as ft


def main_page(page: ft. Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft. ThemeMode. LIGHT

    hello_text = ft. Text(value='Hello world')

    name_input = ft.TextField(label='Введите имя')

    
    def on_button_click(_):
        #print(name_input.value)
        #pass
        name = name_input.value.strip()

        if name:
            #print(name)
            hello_text.color = None
            hello_text.value = f'Hello {name}'
            name_input.value = None
        else:
            #print('Error')
            hello_text.value = ''
            hello_text.color = ft.Colors.RED

    name_input = ft.TextField(label='f', on_submit=on_button_click)
    elevated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    #text_button = ft.TextButton(text='SEND', icon=ft.Icons.SEND)
    #icon_button = ft.IconButton(icon=ft.Icons.SEND)

    
    page.add(hello_text, name_input, elevated_button,)


ft.app(main_page)
#ft.app(main_page, view=ft.AppView.WEB_BROWSER)

