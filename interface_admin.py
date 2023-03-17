# import gi
#
# gi.require_version("Gtk", "3.0")
# from gi.repository import Gtk
#
#
# class Handler:
#
#     def __init__(self):
#         # Créer une variable pour le widget principal (la fenêtre)
#         self.window = builder.get_object("window")
#
#     def onButtonPressed(button1):
#         # Charger le formulaire depuis un fichier glade séparé
#         builder2 = Gtk.Builder()
#         builder2.add_from_file("formulaire_add_category.glade")
#         formulaire = builder2.get_object("formulaire")
#
#         # Afficher le formulaire dans une nouvelle fenêtre modale
#         # dialog = Gtk.Dialog(parent=self.adminWindow, title="Formulaire", modal=True)
#         # dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
#         #                    Gtk.STOCK_OK, Gtk.ResponseType.OK)
#         # box = dialog.get_content_area()
#
#         dialog.vbox.pack_start(formulaire, True, True, 0)
#         dialog.show_all()
#         dialog.run()
#         dialog.destroy()
#     '''def onDestroy(self, *args):
#         Gtk.main_quit()
#
#     def onButtonPressed(self, button):
#         print("Hello World!")'''
#
# if __name__ == "__main__":
#     # Initialiser la boucle principale Gtk
#     Gtk.init([])
#
# builder = Gtk.Builder()
# builder.add_from_file("interface_admin.glade")
# builder.connect_signals(Handler())
#
# window = builder.get_object("adminWindow")
# window.show_all()
#
# Gtk.main()

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class AdminWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="SENHOTEL")

        # Chargement du fichier glade
        builder = Gtk.Builder()
        builder.add_from_file("interface_admin.glade")

        # Création d'un conteneur fixe
        self.fixed = Gtk.Fixed()

        # Ajout du conteneur fixe à la fenêtre
        self.add(self.fixed)

        # Création d'un bouton
        self.button1 = Gtk.Button(label="Ajouter une categorie")
        self.button1.connect("clicked", self.on_button1_clicked)

        # Ajout du bouton au conteneur fixe
        self.fixed.put(self.button1, 50, 50)

        # Récupération des widgets
        self.button1 = builder.get_object("button1")
        self.add_room = builder.get_object("add_room")
        self.add_client = builder.get_object("add_client")
        self.image = builder.get_object("image")
        self.headerbar = builder.get_object("headerbar")

        # Connexion des signaux
        self.button1.connect("add", self.on_button1_add)
        self.button1.connect("clicked", self.on_button1_clicked)
        self.button1.connect("destroy", self.on_button1_destroy)
        self.add_room.connect("clicked", self.on_add_room_clicked)
        self.add_client.connect("clicked", self.on_add_client_clicked)

        # Ajout des widgets à la fenêtre
        fixed = builder.get_object("fixed")
        fixed.add(self.button1)
        fixed.add(self.add_room)
        fixed.add(self.add_client)
        fixed.add(self.image)
        fixed.add(self.headerbar)

    # Callbacks des signaux
    def on_button1_add(self, button):
        # Ajouter une catégorie
        pass

    def on_button1_clicked(self, button):
        # Callback pour le clic du bouton1
        pass

    def on_button1_destroy(self, button):
        # Callback pour la destruction du bouton1
        pass

    def on_add_room_clicked(self, button):
        # Ajouter une chambre
        pass

    def on_add_client_clicked(self, button):
        # Ajouter un client
        pass

win = AdminWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
