import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 

def enviar_email(destinatario, titulo, corpo, caminhos_imagens=None):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()

    smtp.login('seuEmail@email.com', 'seuCodigoDeSegurança')

    msg = MIMEMultipart()
    msg['From'] = 'seuEmail@email.com'
    msg['Subject'] = titulo
    msg['To'] = destinatario
    msg.attach(MIMEText(corpo, 'plain'))

    if caminhos_imagens:
        for caminhoImagem in caminhos_imagens:
            try:
                with open(caminhoImagem, 'rb') as image:
                    imagem = MIMEImage(image.read())
                    imagem.add_header('Content-Disposition', 'attachment', filename=caminhoImagem.split('/')[-1])
                    msg.attach(imagem)
            except Exception as e:
                print(f'Erro ao abrir imagem: {e}')
    
    smtp.sendmail('seuEmail@email.com', destinatario, msg.as_string())
    smtp.quit()