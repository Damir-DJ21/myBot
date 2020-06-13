from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time



session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: '+ str(datetime.strftime(datetime.now(), "%H:%M:%S"))) #Время доставки сообщение
            print('Текст сообщения: ' + str(event.text)) #Текс того, кто написал сообщение
            print(event.user_id) #ID-шник пользователя, который написал мне
            response = event.text.lower() #Переработка всех регистров к нижнему регистру
            if event.from_user and not (event.from_me): #Проверка, если сообщение от пользователся и не от меня
                if response == "привет" or "салам" or "дамир": #Специальное слово для ответа бота
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет, друг', 'random_id': 0})#Метод отправки сообщения


