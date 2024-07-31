import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse

# Carregar contatos de um arquivo Excel
contatos_df = pd.read_excel("Enviar.xlsx")
print(contatos_df)

try:
    # Inicializar o navegador com as configurações padrão
    navegador = webdriver.Chrome()
    navegador.get("https://web.whatsapp.com/")

    # Esperar até que o WhatsApp Web esteja carregado
    WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.ID, "side")))

    # Envio das mensagens
    for i, row in contatos_df.iterrows():
        pessoa = row["Pessoa"]
        numero = row["Número"]
        mensagem = row["Mensagem"]

        # Preparar o texto da mensagem
        texto = urllib.parse.quote(mensagem)
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"

        # Navegar para o link do WhatsApp com o número e mensagem
        navegador.get(link)

        try:
            # Esperar até que o botão de enviar esteja visível
            # A localização do botão pode variar dependendo da versão do WhatsApp Web
            enviar_button = WebDriverWait(navegador, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]'))
            )

            # Verificar se o botão de enviar está visível e habilitado
            if enviar_button.is_displayed() and enviar_button.is_enabled():
                print(f"Enviando mensagem para {pessoa} ({numero})")
                enviar_button.click()

                # Esperar um pouco antes de enviar a próxima mensagem
                time.sleep(10)
            else:
                print(f"Botão de enviar não está interagível para {pessoa} ({numero})")

        except Exception as e:
            print(f"Erro ao enviar mensagem para {pessoa} ({numero}): {e}")

    navegador.quit()

except Exception as e:
    print(f"Erro ao inicializar o navegador: {e}")
