"""Демо модуль для курса"""

# Notification - ...
# EmailNotification - отправка через email


class Notification:
    def __init__(self, sender):
        self.sender = sender

    def send(self, message):
        self.sender.send(message)

    def get_ack(self):
        pass


class EmailSender:
    def send(self, message):
        print(f"Отправлно сообщение {message}")


notification = Notification(EmailSender())
notification.send("Сообщение")
