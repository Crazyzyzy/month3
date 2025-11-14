import flet as ft 
from datetime import datetime

def main_page(page: ft.Page):
    page.title = 'My first test'
    greeting_text = ft.Text(value='Welcome to my first test')

    def on_button_click(_):
        name = name_input.value.strip()
        if name:
            time = datetime.now().strftime('%H')
            greeting_text.color = None
            name_input.value = None
            if 23 >= int(time) >= 12:
                night_list.append(f'good evening {name}')
                night_text.value = 'night list:\n' + ' \n'.join(night_list) 
                if len(night_list) > 4:
                    night_list.pop(-5)  
            elif 11 >= int(time) >= 0:
                day_list.append(f'good morning {name}')  
                day_text.value = 'day list:\n' + ' \n'.join(day_list)   
                if len(day_list) > 4:
                    day_list.pop(-5)  
        else:
            greeting_text.value = f'eror'
            greeting_text.color = ft.Colors.RED

        page.update()


    def clean_day_history(_):
        if len(day_list):
            day_list.pop()
            day_text.value = f'day list:\n' + '\n'.join(day_list) 
        else:
            greeting_text.value = f'nothing to clean'
            greeting_text.color = ft.Colors.RED
        page.update()
    clean_day_button = ft.TextButton(text='delete', icon=ft.Icons.DELETE, on_click=clean_day_history)

    def clean_night_history(_):
        if len(night_list):
            night_list.pop()
            night_text.value = f'night list:\n' + '\n'.join(night_list) 
        else:
            greeting_text.value = f'nothing to clean'
            greeting_text.color = ft.Colors.RED
        page.update()
    clean_night_button = ft.TextButton(text='delete', icon=ft.Icons.DELETE, on_click=clean_night_history)





    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    input_button_text = ft.TextButton(text='send', icon=ft.Icons.SEND_ROUNDED, on_click=on_button_click)

    day_list = []
    day_text = ft.Text('day list')
    night_list = []
    night_text = ft.Text('night list')




    page.add(greeting_text, name_input, input_button_text, day_text, clean_day_button, night_text, clean_night_button)


ft.app(target=main_page)