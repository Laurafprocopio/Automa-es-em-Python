# Ler arquivo csv
import csv
import smtplib
import email.message
from time import sleep

email_enviados = []
email_enviados_antes = []
email_assunto = 'AUTOMATIZAÇÃO EFICIENTE DE TAREFAS COM PYTHON: AUTOMATIZADO DE MENSAGENS VIA WHAS-TSAPP E E-MAIL'
email_corpo   = '''
A automatização de tarefas é crucial para melhorar a produtividade e reduzir o tem-po gasto com atividades repetitivas. Python, com sua flexibilidade e simplicidade, oferece uma plataforma robusta para criar scripts de automação e integrar com di-versas APIs, como WhatsApp e Gmail.

Python disponibiliza uma vasta gama de bibliotecas e pacotes, como smtplib para envio de e-mails e requests para interações com APIs. Essas ferramentas permitem criar soluções personalizadas, aumentar a eficiência e minimizar erros.

A comunicação eficaz é vital em qualquer organização. O envio manual de mensa-gens é demorado e sujeito a erros, o que pode comprometer a qualidade da comu-nicação e a eficiência dos processos. Automatizar o envio de mensagens pode ga-rantir uma comunicação mais precisa e oportuna.

Este artigo explora como Python pode ser utilizado para automatizar o envio de mensagens via WhatsApp e e-mail. A estrutura do artigo é a seguinte:

1.	Ferramentas e Bibliotecas Disponíveis: Revisão das principais ferramentas e bibliotecas para integração com APIs de WhatsApp e serviços de e-mail.
2.	Desenvolvimento do Script de Automação: Guia passo a passo para de-senvolver um script Python que envia mensagens automaticamente.
3.	Exemplo Prático: Demonstração de uma implementação real para envio em massa de mensagens, destacando a eficiência e a escalabilidade do sistema de automação.

                '''

def enviar_email( to ) -> None:  
    # caso o email ja tenha sido enviado, retorna
    if to in email_enviados+email_enviados_antes:
        print(f'Email enviado anteriormente - {to}')
        return
    
    msg = email.message.Message()
    msg['Subject'] = email_assunto
    msg['From'] = 'laura.f@exemplo.com.br' # seu email
    msg['To'] = to

    password = ''  # Senha gerada pelo google
    # msg.add_header('Content-Type', 'text/html')
    msg.set_payload( email_corpo )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    
    email_enviados.append(to)
    print(f'Email enviado - {to}')
    # salva o email no arquivo de emailenviado
    with open('emailenviado.txt','a') as arquivo:    
        arquivo.writelines( f'{to}\n')  
 
# abre arquivo de emails enviados      
try:
    with open('emailenviado.txt','r') as arquivo:
        linha = arquivo.readlines()
        email_enviados_antes = [ email.replace('\n','') for email in linha ]  
except Exception as error:
    # cria o arquivo de email enviado, caso nao tenha 
    with open('emailenviado.txt','w') as arquivo:
        ...

# Le arquivo de dados que contem o email da pessoa
with open('enviaremail.csv','r',encoding='utf8',newline='\r\n') as arquivo:
    linha = csv.reader(arquivo)
    lPessoas = [ x for x in linha] 
    
# percorre a lista de emails     
for pessoa in lPessoas:
    # chama a rotina de envio de email passando o email 
    enviar_email( pessoa[1])
    sleep(2)