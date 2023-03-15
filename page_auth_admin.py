import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

#Classe de l'application

class Appli(object):

    #Initialisation, creation de la fenetre principale

    def __init__(self, builder, **kwargs):
        super(Appli,self).__init__(**kwargs)

        self.builder=builder
        #les composants
        self.builder.add_from_file('page_auth_admin.glade')
        self.windowAppli=self.builder.get_object("windowAuth")

        #activation
        self.builder.connect_signals(self)
        self.windowAppli.show_all()

        #fin de l'application

        def on_windowAppli_destroy(self, widget):
            Gtk.main_quit()

        builder = Gtk.builder()
        builder.add_from_file('/Users/macbookair/Desktop/projetBdPython/page_auth_admin.glade')

        window = builder.get_object('fixedAuth')
        window = builder.get_object('windowAuth')

        window.connect('delete-event', Gtk.main_quit)


        if __name__ == "main":
            Appli(builder)
            Gtk.main()