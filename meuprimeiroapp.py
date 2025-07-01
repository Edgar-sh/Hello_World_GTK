import sys
import gi

# Definindo versão do gtk

gi.require_version('Gtk', '3.0')

# Importando o módulo GTK

from gi.repository import Gtk


# Definindo a Classe Principal da aplicação
# Herdamos nosssa classe de Gtk.Application
class MeuPrimeiroApp(Gtk.Application):
    """"
    minha classe principal, lembra disso filha da puta
    """
    def __init__(self): #__init__ é o "construtor" da minha classe "MeuPrimeiroApp
                        #self é utilizado para acessar variáveis
                        #e métodos dentro de um método.
        # Chamamos o construtor da classe pai para que ela se configure
        # O 'application_id' é um identificador para o app
        super().__init__(application_id='br.com.exemplo.meuprimeiroapp')

        # self.connect serve para conectar um sinal à uma função
        # O sinal "activate" é emitido pela classe pai, quando ele é iniciado
        # Ai quando isso acontecer, self.quando_ativar será chamado.
        # "Ei, GTK, quando o sinal 'activate' acontecer, POR FAVOR, chame a minha função quando_ativar por mim."
        self.connect('activate', self.quando_ativar)

    # Nosso "callback", interface do app vai ser construida aqui.
    def quando_ativar(self, app): # app nada mais é que um nome génerico.
        # Criando a janela principal, aparentemente é melhor usar Gtk.ApplicationWindow
        # ao invés de Gtk.Window
        janela = Gtk.ApplicationWindow(application=app)
        janela.set_title("Meu primeiro app")
        janela.set_default_size(400, 250)

        # Criando um widget simples de texto no aplicativo. (um rótulo)
        simple_text = Gtk.Label(label="Hello World")

        # Adicionando nosso texto(label) à nossa janela.
        # Em GTK4, uma janela só pode ter um filho direto
        janela.add(simple_text)

        # Tornando a janela e tudo que tem nela presente visivel

        janela.show_all()

# Fora da classe, botando o programa para funcionar.

# Instanciando da classe pai.

if __name__ == "__main__":

    app = MeuPrimeiroApp()

    # Inicia o aplicativo, passando quaisquer argumentos da linha de comando.
    # O programa ficará em loop aqui, esperando por eventos (cliques, etc.)
    exit_status = app.run(sys.argv)

    # Quando a janela for fechada, o programa terminará.
    sys.exit(exit_status)




