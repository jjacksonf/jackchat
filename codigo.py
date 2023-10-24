# JACKCHAT
# Passos:
# Criar botão para iniciar o chat;
# Exibir popup para entrar no chat;
# Ao ingressar no chat, deverá ocorrer o seguinte: (deverá aparecer para todos que estiverem no chat.)
# Mensagem de que a pessoa ingressou no chat;
# Campo para eecrever as mensagens e o botão para envia-las;
# Ao enviar a mensagem, o layout deverá ser o seguinte: (deverá aparecer para todos que estiverem no chat.)
# Nome: mensagem enviada;


import flet as ft


def main(pag_inicial):
    texto = ft.Text("JackChat")

    chat = ft.Column()

    # O comando "TextField" insere um campo de texto
    nome_usuario = ft.TextField(label="Digite seu nome aqui.")

    def enviar_msg_tunel(msg):
        tipo = msg["tipo"]
        if tipo == "msg":
            texto_msg = msg["texto"]
            usuario_msg = msg["usuario"]
            chat.controls.append(ft.Text(f"{usuario_msg}: {texto_msg}"))

        else:
            usuario_msg = msg["usuario"]
            chat.controls.append(ft.Text(f"{usuario_msg} entrou no chat",
                                         size=12, italic=True, color=ft.colors.BLUE_900))
        pag_inicial.update()

    # Criando um "Túnel de comunicação" (PUBLISH SUBSCRIBE)
    pag_inicial.pubsub.subscribe(enviar_msg_tunel)

    def enviar_msg(evento):
        pag_inicial.pubsub.send_all({"texto": campo_msg.value, "usuario": nome_usuario.value,
                                     "tipo": "msg"})

        campo_msg.value = ""  # Limpar campo de mensagem
        pag_inicial.update()

    # O comando on_submit, tem como objetivo enviar a mensagem após clicar a tecla "enter".
    campo_msg = ft.TextField(
        label="Digite uma mensagem.", on_submit=enviar_msg)
    botao_enviar_msg = ft.ElevatedButton("Enviar", on_click=enviar_msg)

    def entrar_popup(evento):
        pag_inicial.pubsub_all(
            {"usuario": nome_usuario.value, "tipo": "entrada"})
        pag_inicial.add(chat)  # Adiciona o chat
        popup.open = False  # Fecha o popup
        pag_inicial.remove(botao_inicio)  # Remove o botão de iniciaar o chat.
        pag_inicial.remove(texto)
        pag_inicial.add(ft.Row([campo_msg, botao_enviar_msg]))
        # pag_inicial.add(botao_enviar_msg)
        pag_inicial.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Seja bem vindo ao JackChat"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
    )

    def acessar_chat(evento):
        pag_inicial.dialog = popup
        popup.open = True
        pag_inicial.update()

    botao_inicio = ft.ElevatedButton("Iniciar chat", on_click=acessar_chat)
    # Para visualizar algo na página precisa-se usar o comando "nome_pagina.add()"
    pag_inicial.add(texto)
    pag_inicial.add(botao_inicio)


# o comando "target", serve para mostrar qual a página que o app irá ter como principal, além de permitir que possamos escolher como o programa será aberto, se em formato "browser" ou "app".
ft.app(target=main, view=ft.WEB_BROWSER)
