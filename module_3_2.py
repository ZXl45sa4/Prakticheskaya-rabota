def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if '@' not in recipient or '.ru' not in recipient and '.com' not in recipient and '.net' not in recipient:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    if '@' not in sender or '.ru' not in sender and '.com' not in sender and '.net' not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif "university.help@gmail.com" in sender:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.ru')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')



