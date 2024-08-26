def send_email(message, recipient, *, sender="university.help@gmail.com"):

    recipient_email_ident = 0  # Счетчик ошибок в адресе получателя
    sender_email_ident = 0  # Счетчик ошибок в адресе отправителя

    #  Проверка адреса получателя на ошибки
    if ".com" not in recipient or "@" not in recipient:
        recipient_email_ident += 1
    if ".ru" not in recipient or "@" not in recipient:
        recipient_email_ident += 1
    if ".net" not in recipient or "@" not in recipient:
        recipient_email_ident += 1
    if recipient_email_ident > 2:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверка адреса отправителя на ошибки
    if ".com" not in sender or "@" not in sender:
        sender_email_ident += 1
    if ".ru" not in sender or "@" not in sender:
        sender_email_ident += 1
    if ".net" not in sender or "@" not in sender:
        sender_email_ident += 1
    if sender_email_ident > 2:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверка на совпадение адреса отправителя и получателя
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    # Проверка на совпадение адреса отправления адресу по умолчанию
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        return
    elif sender != recipient:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
