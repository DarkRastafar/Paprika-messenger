import time


class Messenger:
  def __init__(self):
    self.db = [
      {'text': 'Привет', 'author': 'Jack', 'time': time.time()},
      {'text': 'Привет', 'author': 'Mary', 'time': time.time()},
	  ]

  def send_message(self, text, author):
    if isinstance(text, str) and isinstance(author, str):
    # todo: сохранить в бд
    #self.db  дает доступ к переменным класса
      self.db.append({
        'text': text, 
        'author': author, 
        'time': time.time() # todo: считать время
      })
      print(text, author)
      return 'Ok'
    else:
      return'Not OK'

	# Переменная self - для входа в базу данных
  def get_messages(self):
    return self.db 

#функция print - обязательна! Не будь дибилом и запомни это!
print(Messenger)
