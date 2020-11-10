from flask import Flask, Response, request
from datetime import datetime
import time



app = Flask(__name__)


db = [
	{'text': 'Привет', 'author': 'Jack', 'time': time.time()},
    {'text': 'Привет', 'author': 'Mary', 'time': time.time()},
]


@app.route("/")
def hello():
    return '''Приветствую Вас в Paprika!
    <br><a href='/status'>Статус</br>
    <br><a href='/status_server'>Статус сервера</br>
    <br><a href='/send_message'>Отправить сообщение</br>
    <br><a href='/get_messages'>Получить сообщения</br>
    '''


@app.route("/status")
def status():
	# Проще создать переменную для подсчета времени перед функцией return,
	# и в последствии - использовать в качестве переменной.
	dt = time.time()
	#json объект - возволяет легко парсить. Лучше, чем XML.
	return {
		"status"	:  	True, 
		"name"  	: 	"Paprika", 
		"time"  	:  	dt
	}


@app.route("/status_server")
def status_server():
	return "Server is ON<br><a href='/..'>Назад</br>"

# необходимо указать метод ['POST]
@app.route("/send_message", methods =['POST'])
def send_message():
	# берет входящий json и преобразует к питоновскому объекту
	data = request.json
	# Нужно проверить, что объект data не является пустым, а является словарем:
	# (Проще сразу ставить если нет, чтобы не сдвигать все последующее в ветвление функции)	
	if not isinstance(data, dict):
		return Response('not json', 400)
	
	# можно обратиться по ключу и получить питоновский словарик , например text = data.get['text']
	# Указываем data.get[], чтобы если пусто - выводилось none
	text = data.get('text')
	author = data.get('author')
	
	if isinstance(text, str) and isinstance(author, str):
    # todo: сохранить в бд
    #self.db  дает доступ к переменным класса
		db.append({
			'text': text, 
			'author': author, 
			'time': time.time() # todo: считать время
		})
      #  теле сервера надо передавать не строки, а json; Меняем return 'OK' на return {'Ok' : True}.
      # Response - принимает на вход статус.
		return Response('Ok')
	else:
		# Ошибка 400 - значит, что сообщение было прислано не правильно.
		return Response('wrong format', 400)


@app.route("/get_messages")
def get_messages():
	#нужно ограничить выкачивание сообщений только последними.
	after = request.args.get('after', '0')
	try:
		after = float(after)
	except:
		return Response('wrong format', 400)
	


	new_messages = [message for message in db if message['time'] > after]
	return {'messages' : new_messages}


app.debug = True
app.run()


