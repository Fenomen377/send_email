# Тестовое задание. Сервис email-рассылок
<h3>Возможности:</h3> 
<p>— подписка на рассылку после ввода имени и почты</p>
<p>— рассылка с использованием html-шаблона и переменными (имя подписчика)</p>
<p>— отложенная рассылка, реализованная с помощью celery</p>
<h2>Подписка на рассылку после ввода имени и почты</h2>
<img src="screenshots/screen_follow.png">
<h2>Рассылка с использованием html-шаблона и переменными (имя подписчика)</h2>
<img src="screenshots/screen_follow_message.png">
<h2>Отложенная рассылка, реализованная с помощью celery и redis(5 минут)</h2>
<p>Для старта отложенной рассылки необходимо применить команды:</p>
<p>python manage.py runserver  </p>
<p>celery -A send_email beat -l info</p>
<p>celery -A send_email worker -l info</p>
<img src="screenshots/screen_message_with_delay.png">
