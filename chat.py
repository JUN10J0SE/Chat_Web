import flet as ft
from dataclasses import dataclass#importacao para nao precisar digitar o metodo construtor

@dataclass#recurso de importacao para nao precisar digitar o metodo construtor
class Mensagens:       #criacao da classe que permitira a troca de mensagens entre 2 pessoas
    usuario: str
    texto: str  #criacao de atributos
    tipo_msg: str

    def __del__(self):
        return f'{self.usuario} destruido com sucesso'

def main(page: ft.Page):

    page.title = 'Oh Chat'
    page.scroll = 'adaptive'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = '#EEE8AA'

    def on_mensage(msg: Mensagens):# permitir  identificar a mensagem de um usuario(quem envia)
        if msg.tipo_msg == 'chat_message': #saber qual tipo de mensagem esta enviando
            chat.controls.append(ft.Text(f'{msg.usuario}: {msg.texto}'))
        elif msg.tipo_msg == 'login_message':
            chat.controls.append(ft.Text(msg.texto, italic=True, color=ft.colors.BLACK,size=12))
        else:
            ...
        page.update() 

    page.pubsub.subscribe(on_mensage)#daz a atualizacao entre as mensagens em tempo real  

    def enviar(e):#acrescentar mensagem de conversacao
        page.pubsub.send_all(Mensagens(usuario=page.session.get('nome_usuario'), texto=nova_msg.value,tipo_msg='chat_message'))#.recebe e identifica a mensagem pelo outro receptor(quem recebe)
        nova_msg.value = ''
        page.update()

    def entrar(e):#criacao do nome de usuario(identificacao)
        if not nome_usuario.value:
            nome_usuario.error_text = 'Nome de usuario não pode ficar em branco!'
            nome_usuario.update()
        else:
            page.session.set('nome_usuario', nome_usuario.value)
            page.dialog.open = False
            page.pubsub.send_all(Mensagens(usuario=nome_usuario.value,texto=f'{nome_usuario.value} entrou no chat.', tipo_msg='Login_message'))
            page.update()
    
    #Variaveis
    chat = ft.Column()
    nova_msg = ft.TextField(label='Digite sua mensagem:', bgcolor='white', on_submit=enviar)
    nome_usuario = ft.TextField(label = 'Entre com seu nome de usuario:')

    page.dialog = ft.AlertDialog(#criacao da caicxa de login
        open=True,
        modal=True,
        title=ft.Column([nome_usuario], tight=True),
        actions=[ft.ElevatedButton(text='Entrar no chat', on_click=entrar)],
        actions_alignment='end'
    )

    page.add(
        ft.Row(
            [ft.Text('Oh Chat', size=60, weight='bold',color='black')],#adiconando o titulo da linha
            alignment=ft.MainAxisAlignment.CENTER
        ),
        chat,
        ft.Row(
            controls=[nova_msg, ft.ElevatedButton('Enviar', on_click=enviar)],#adiconando o botao chamado 'enviar' na mesma linha da caixa de texto
            alignment=ft.MainAxisAlignment.CENTER                             #caso quisesse abaixo, criar uma Row so para o botao
        )
    )

    page.update()

#executor da pagina
ft.app(main)