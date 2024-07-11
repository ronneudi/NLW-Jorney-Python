from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(to_addrs, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = "587"
    from_addr = "me@contoso.com"
    mail_login = "me@contoso.com"
    mail_pwd = "secreat"

    msg = MIMEMultipart()
    msg["from"] = from_addr
    msg["to"] = ', '.join(to_addrs)
    msg["subject"] = "NLW Jorney - Confirmação de Viagem!"
    msg.attach(MIMEText(body, 'plain'))

    server = SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(mail_login, mail_pwd)

    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit()
