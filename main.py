import flet as ft 


def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    greeting_text = ft.Text(value='Hello world')

    def on_button_click(_):
        name = name_input.value.strip()
        hour = hour_input.value.strip()
        minut = minut_input.value.strip()

        if name:
            greeting_text.color = None
            name_input.value = None
            if 11 >= int(hour) >= 6 and 59 >= int(minut) >= 0:
                greeting_text.value = f'Good morning {name}'
            elif 17 >= int(hour) >= 12 and 59 >= int(minut) >= 0:
                greeting_text.value = f'Good day {name}'
            elif 23 >= int(hour) >= 18 and 59 >= int(minut) >= 0:
                greeting_text.value = f'Good evening {name}'
            elif 6 >= int(hour) >= 0 and 59 >= int(minut) >= 0:
                greeting_text.value = f'Good night {name}'
            else:
                greeting_text.value = f'Problems with time'
                greeting_text.color = ft.Colors.RED
        
        else:
            greeting_text.value = f'Eror with name try one more time'
            greeting_text.color = ft.Colors.RED

        page.update()
    hour_input = ft.TextField(label='Введите time', on_submit=on_button_click)
    minut_input = ft.TextField(label='Введите minute', on_submit=on_button_click)
    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    input_button_text = ft.TextButton(text='send', icon=ft.Icons.SEND_ROUNDED, on_click=on_button_click)


    page.add(greeting_text, name_input, hour_input, minut_input, input_button_text)


ft.app(target=main_page)