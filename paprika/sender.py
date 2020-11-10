# файл для отправки запросов писем.
# Чтобы оправлять - нужно воспользоваться библиотекой requests
import requests

# Позволяет обращаться одной из app.route(), указать post method
response = requests.post('http://127.0.0.1:5000/send_message',
	json = {'text'    :  'Русский работает',
			'author'  :  'Папочка'
			}

	)
print(response.status_code)
print(response.text)