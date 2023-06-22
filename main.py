import requests
import customtkinter as tk

from CTkMessagebox import CTkMessagebox


class ConverterApplication(tk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.geometry('200x200')
        self.resizable(False, False)
        self.title('Converter App')

        self.valutes = ['🇦🇺 AUD', '🇦🇿 AZN', '🇬🇧 GBP', '🇧🇾 BYN', '🇧🇬 BGN',
                        '🇧🇷 BRL', '🇭🇰 HKD', '🇬🇪 GEL', '🇩🇰DKK', '🇦🇪 AED',
                        '🇺🇸 USD', '🇪🇺 EUR', '🇨🇦 CAD', '🇶🇦 QAR', '🇨🇳 CNY',
                        '🇳🇿 NZD', '🇵🇱 PLN', '🇷🇴 RON', '🇸🇬 SGD', '🇨🇭CHF']
        self.label_input_valute = tk.CTkLabel(self, text='Выберите валюту:').pack()

        self.list_of_valutes = tk.CTkComboBox(self, values=self.valutes, state='readonly', hover=True)
        self.list_of_valutes.pack()

        self.input_value = tk.CTkEntry(self, placeholder_text='Введите сумму:')
        self.input_value.pack()

        self.submit_button = tk.CTkButton(self, text='Конвертировать', command=self.convert_valute).pack(pady=15)

        self.output_value = tk.CTkEntry(self, placeholder_text='0')
        self.output_value.pack()

        self.github_link = tk.CTkLabel(self, text='https://github.com/shp3x')
        self.github_link.pack()

    def convert_valute(self):
        try:
            url = 'https://www.cbr-xml-daily.ru/daily_json.js'
            req = requests.get(url).json()['Valute'][self.list_of_valutes.get().split()[1]]
            value = int(self.input_value.get()) * int(req['Value'])
            self.output_value.delete(0, tk.END)
            self.output_value.insert(0, str(value) + ' ₽')
        except (ValueError, IndexError):
            CTkMessagebox(title='Ошибка', message='Произошла ошибка!')


if __name__ == '__main__':
    ConverterApplication().mainloop()
