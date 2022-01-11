from peoples import peoples
from santa import get_santas
from santa_mail import send_mail

# Список тайных сант
santas = get_santas()

# Отправляем на сервисный email, чтобы если кому нибудь не придет письмо потом его реплейнуть вручную
for santa in santas:
    santa_from = peoples[santa['name']]
    santa_to = peoples[santa['gift']]
    send_mail('secretsanta@gmail.com', santa_from['name'], santa_to['text'])

# Отправляем ребзям на мыло
for santa in santas:
    santa_from = peoples[santa['name']]
    santa_to = peoples[santa['gift']]
    send_mail(santa_from['email'], santa_from['name'], santa_to['text'])
