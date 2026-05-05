import fleat as ft

def main_page(page: ft.Page):
    
    hello_text = ft.Text(value='Hello world')

    page.add(hello_text)


ft.app(main_page)