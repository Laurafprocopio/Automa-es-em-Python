from twilio.rest import Client

def send_whatsapp_message(body, to):
    # Substitua estas credenciais pelas suas credenciais Twilio
    account_sid = '' #Sid que o Twlio Oferece
    auth_token = '' #Token que o Twilio fornece
    
    # Número do WhatsApp fornecido pela Twilio
    from_whatsapp_number = 'whatsapp:+99999999999'
    
    # Formata o número do destinatário
    to_whatsapp_number = f'whatsapp:{to}'

    # Cria uma instância do cliente Twilio
    client = Client(account_sid, auth_token)

    try:
        # Envia a mensagem via WhatsApp
        message = client.messages.create(
            body=body,                # Corpo da mensagem
            from_=from_whatsapp_number,  # Número do remetente
            to=to_whatsapp_number     # Número do destinatário
        )
        # Imprime o SID da mensagem enviada
        print(f'Mensagem enviada com sucesso. SID: {message.sid}')
        return message.sid
    except Exception as e:
        print(f'Erro ao enviar mensagem: {e}')
        return None

def check_message_status(message_sid):
    # Substitua estas credenciais pelas suas credenciais Twilio
    account_sid = ''
    auth_token = ''
    
    # Cria uma instância do cliente Twilio
    client = Client(account_sid, auth_token)
    
    try:
        # Consulta a mensagem usando o SID
        message = client.messages(message_sid).fetch()
        # Imprime o status da mensagem
        print(f'Status da mensagem: {message.status}')
    except Exception as e:
        print(f'Erro ao verificar status da mensagem: {e}')

# Exemplo de uso: Envia uma mensagem e verifica o status
message_sid = send_whatsapp_message('mensagem de teste', '+5567999999999')

if message_sid:
    check_message_status(message_sid)
