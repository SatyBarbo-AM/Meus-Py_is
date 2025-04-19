import smtplib
import ssl
from email.message import EmailMessage

def enviar_email(remetente, senha, destinatario, assunto, corpo):
    msg = EmailMessage()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.set_content(corpo)
    
    contexto = ssl.create_default_context()
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as servidor:
            servidor.login(remetente, senha)
            servidor.send_message(msg)
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    remetente = input("Digite seu e-mail: ")
    senha = input("Digite sua senha (use App Password se necessário): ")
    destinatario = input("Digite o e-mail do destinatário: ")
    assunto = input("Digite o assunto do e-mail: ")
    corpo = input("Digite o corpo do e-mail: ")
    
    enviar_email(remetente, senha, destinatario, assunto, corpo)
