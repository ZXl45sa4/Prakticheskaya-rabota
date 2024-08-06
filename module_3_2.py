def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    com_1 = recipient
    ru_1 = recipient
    net_1 = recipient
    com_2 = sender
    ru_2 = sender
    net_2 = sender
    for i in recipient:
        if i != '@':
            continue
            print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        # elif '.com' != com_1[len(recipient) - 4:] and '.ru' != ru_1[len(recipient) - 3:] and '.net' != net_1[len(recipient) - 4:]:
        #     print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        elif '.com' != com_2[len(sender) - 4:] and '.ru' != ru_2[len(sender) - 3:] and '.net' != net_2[len(sender) - 4:]:
            print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        elif recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
        else:
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')