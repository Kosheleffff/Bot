import requests

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot_token = '6518090421:AAGLc8WYyvy8ZFY9k1MNGLqCOkWMYqrakMY'
chat_id = '1'  # Здесь вам нужно указать ID чата с пользователем

# Текст сообщения, которое вы хотите отправить
message = 'Привет, это ответ от бота!'

# Отправляем сообщение через бота
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
params = {'chat_id': chat_id, 'text': message}
response = requests.post(url, data=params)

# Проверяем, что сообщение успешно отправлено
if response.status_code == 200:
    print('Сообщение успешно отправлено')
else:
    print('Ошибка при отправке сообщения')
