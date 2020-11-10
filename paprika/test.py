from main import Messenger


m1 = Messenger()
m2 = Messenger()
m1.send_message('Hello new massage', 'Pavel')

print(m1.get_messages())
