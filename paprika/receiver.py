# receiver
import requests
from datetime import datetime
import time

after = 0

while True:
	# вегда смотри на наличие скобок. в скобках - строка должна быть отделена от функций.
	response = requests.get('http://127.0.0.1:5000/get_messages', params={'after' : after})
	if response.status_code == 200:
		messages = response.json()['messages']
		for message in messages:
			after = message['time']
			ftime = datetime.fromtimestamp(message['time']).strftime('%d/%m/%Y %H:%M:%S')
			print(message['author'], ftime)
			print(message['text'])
			print()

	# чтобы не за DDOSить сервер - нужно поставить ограничение выполнения цикла. Хотя бы на 1 секунду
	time.sleep(1)


