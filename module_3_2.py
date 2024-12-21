
#Домашнее задание по теме "Return" №1/№2

def send_emai(message, recipient, sender = 'university.help@gmail.com'):
    if '@' not in recipient or '@' not in sender or not recipient.endswih(('.com','.ru', '.net')) or not sender.endswih(
            ('.com','.ru', '.net')):
       print(f"Невозможно отправить письмо с адреса - {sender} на адрес - {recipient}")
    if recipient == recipient or sender==sender:
        print("Нельзя отправить письмо самому себе!")
    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса - {sender}  на адрес - {recipient}")
    if sender != 'university.help@gmail.com':
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!  Письмо отправлено с адреса - {sender} на адрес - {recipient}")


send_emai ('Привет!', 'recipient', 'sender')