import sys
import gi

# Adicionando a versão que eu quero.

gi.require_version('Gtk', '3.0')

# Importando o Gtk

from gi.repository import Gtk

# Definindo minha classe principal.

class MeuSegundoApp(Gtk.Application):
    def __init__(self): # Construtor.

        # Mesma coisa com java. Só lembrar do conceito de Override ou algo do tipo.

        super().__init__(application_id='br.com.exemplo.meusegundoapp') # 'application_id' = parâmetro.

        self.connect('activate', self.when_activate) # when_activate(quando_ativar) = Metodo.


    # Função Hello World, ela vai substituir os textos das labels já criadas na função when_activate
    def func_hello_world(self, botao):

        name = 'Olá Mundo!'
        when_pressed = 'Pressionando!'
        self.label2.set_text(name)
        self.button.set_label(label=when_pressed)

    # Fazendo a função de quando o aplicativo for inicializado
    def when_activate(self, app):

        window = Gtk.ApplicationWindow(application=app)
        window.set_title('Meu segundo app')
        window.set_default_size(400,250)

        # Criando os widget de texto.

        self.label = Gtk.Label(label='Aperte no botão abaixo!')
        self.label2 = Gtk.Label(label='')

        # Criando o botão.

        self.button = Gtk.Button(label="Aqui")

        # Conectando o sinal a função de substituição.
        self.button.connect('clicked', self.func_hello_world)

        # Criando uma caixa para organizar widgets (Vertical nesse caso).


        vertical_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 50) # spacing = espaçamento. '6' = 6 pixels

        # Centralizando a box

        vertical_box.set_halign(Gtk.Align.CENTER)   # Horizontalmente
        vertical_box.set_valign(Gtk.Align.CENTER)   # Verticalmente

        # Adicionando todos os widgets a box.
        vertical_box.add(self.label)
        vertical_box.add(self.button)
        vertical_box.add(self.label2)

        # Adicionando box à janela.
        window.add(vertical_box)

        # Mostrando a porra toda
        window.show_all()


if __name__ == '__main__': # Criando a main

    app = MeuSegundoApp()

    exit_status = app.run(sys.argv)

    sys.exit(exit_status)


