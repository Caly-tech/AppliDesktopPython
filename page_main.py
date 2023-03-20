import gi
import requests

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk


class HotelMainPage(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Page main")
        # Création de la barre de navigation
        headerbar = Gtk.HeaderBar()
        headerbar.set_show_close_button(True)
        headerbar.props.title = "SEN HOTEL"
        headerbar.props.subtitle = "Bienvenue dans votre hotel"

        # Ajout du bouton pour l'administrateur
        button = Gtk.Button(label="Administrateur")
        button.connect("clicked", self.admin_button)
        headerbar.pack_end(button)
        self.set_titlebar(headerbar)

        # Ajout du bouton pour l'utilisateur
        button = Gtk.Button(label="Utilisateur")
        button.connect("clicked", self.user_button)
        headerbar.pack_end(button)
        self.set_titlebar(headerbar)

        # Ajout de l'image de fond
        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("/Users/macbookair/Downloads/img_hotel.jpg", 1000, 1500, True)
        image.set_from_pixbuf(pixbuf)

        self.add(image)

    def admin_button(self, widget):
        self.hide()
        login_window = interface_admin()
        login_window.show_all()

    def user_button(self, widget):
        self.hide()
        login_window = interface_user()
        login_window.show_all()

class interface_admin(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title="Interface admin")
            self.set_border_width(10)
            headerbar = Gtk.HeaderBar()
            headerbar.set_show_close_button(True)
            headerbar.props.title = "SEN HOTEL"
            headerbar.props.subtitle = "Interface administrateur"
            self.set_titlebar(headerbar)

            grid = Gtk.Grid()
            grid.set_column_spacing(100)
            grid.set_row_spacing(100)
            self.add(grid)

            label2 = Gtk.Label()
            grid.attach(label2, 0, 2, 1, 1)

            menubar = Gtk.MenuBar()
            menubar.set_hexpand(True)
            grid.attach(menubar, 0, 0, 1, 1)

            menuitem_file = Gtk.MenuItem(label="Accueil")
            menubar.append(menuitem_file)
            menuitem_file = Gtk.MenuItem(label="Les chambres")
            menubar.append(menuitem_file)
            menuitem_file = Gtk.MenuItem(label="les clients")
            menubar.append(menuitem_file)


            # Bouton pour ajouter uner categorie
            self.button = Gtk.Button(label="Ajouter une categorie")
            self.button.connect("clicked", self.add_category)
            grid.attach(self.button, 2, 3, 2, 2)
            # rgba = Gtk.RGBA.from_color(Gdk.color_parse("#D4F5E6"))
            # self.category.override_background_color(Gtk.StateFlags.NORMAL, rgba)

            # Bouton pour ajouter un client
            self.button = Gtk.Button(label="Ajouter un client")
            self.button.connect("clicked", self.add_client)
            grid.attach(self.button, 2, 5, 2, 2)

            # Bouton pour ajouter une chambre
            self.button = Gtk.Button(label="Ajouter une chambre")
            self.button.connect("clicked", self.add_room)
            grid.attach(self.button, 2, 7, 2, 2)

        def add_category(self, widget):
            self.hide()
            login_window = Category()
            login_window.show_all()

        def add_client(self, widget):
            self.hide()
            login_window = Client()
            login_window.show_all()

        def add_room(self, widget):
            self.hide()
            login_window = Room()
            login_window.show_all()


class interface_user(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Interface user")
        self.set_border_width(10)
        headerbar = Gtk.HeaderBar()
        headerbar.set_show_close_button(True)
        headerbar.props.title = "SEN HOTEL"
        headerbar.props.subtitle = "Interface utilisateur"
        self.set_titlebar(headerbar)

        grid = Gtk.Grid()
        grid.set_column_spacing(100)
        grid.set_row_spacing(100)
        self.add(grid)

        label2 = Gtk.Label()
        grid.attach(label2, 0, 2, 1, 1)



class Category(Gtk.Window):
        def __init__(self):
                        Gtk.Window.__init__(self, title="Ajouter une categorie")
                        self.set_border_width(10)

                        grid = Gtk.Grid()
                        grid.set_column_spacing(10)
                        grid.set_row_spacing(10)
                        self.add(grid)

                        etiquette = Gtk.Label()
                        etiquette.set_markup("<span foreground='#ffff78780000' font_desc='Times New Roman 20'>Ajouter une categorie</span>")
                        grid.attach(etiquette, 1, 1, 1, 1)

                        label1 = Gtk.Label(label="Nom categorie")
                        grid.attach(label1, 0, 2, 1, 1)
                        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                        label1.override_background_color(Gtk.StateFlags.NORMAL, rgba)
                        # Ajouter bouton nom_categorie
                        self.add_category = Gtk.Entry()
                        grid.attach(self.add_category, 1, 2, 1, 1)
                        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                        self.add_category.override_background_color(Gtk.StateFlags.NORMAL, rgba)

                        label2 = Gtk.Label(label="Tarifs(cfa)")
                        grid.attach(label2, 0, 4, 1, 1)
                        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                        label2.override_background_color(Gtk.StateFlags.NORMAL, rgba)
                        # Ajouter bouton tarifs
                        self.add_tarif = Gtk.Entry()
                        grid.attach(self.add_tarif, 1, 4, 1, 1)
                        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                        self.add_tarif.override_background_color(Gtk.StateFlags.NORMAL, rgba)

                        # Ajouter un bouton pour valider
                        button = Gtk.Button(label="Ajouter")
                        button.connect("clicked", self.on_button_clicked_category)
                        grid.attach(button, 0, 5, 2, 1)

        def on_button_clicked_category(self, widget):
            # Récupérer les valeurs saisies par l'utilisateur
            NomCategorie = self.add_category.get_text()
            Tarifs = int(self.add_tarif.get_text())

            # Appeler l'API Go avec les données saisies
            url = 'http://localhost:3000/createCategories'
            data = {'NomCategorie': NomCategorie, 'Tarifs': Tarifs}
            response = requests.post(url, data=data)

            # Vérifier si l'appel a réussi et afficher un message de confirmation
            if response.status_code == 200:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,"Les données ont été enregistrées avec succès.")
                dialog.run()
                dialog.destroy()
            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK,"Une erreur s'est produite lors de l'enregistrement des données.")
                dialog.run()
                dialog.destroy()


class Client(Gtk.Window):
        def __init__(self):
                    Gtk.Window.__init__(self, title="Ajouter un client")
                    self.set_border_width(10)

                    grid = Gtk.Grid()
                    grid.set_column_spacing(10)
                    grid.set_row_spacing(10)
                    self.add(grid)

                    etiquette = Gtk.Label()
                    etiquette.set_markup("<span foreground='#ffff78780000' font_desc='Times New Roman 20'>Ajouter un client</span>")
                    grid.attach(etiquette, 1, 1, 1, 1)

                    label3 = Gtk.Label(label="Nom")
                    grid.attach(label3, 0, 2, 1, 1)
                    rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                    label3.override_background_color(Gtk.StateFlags.NORMAL, rgba)
                    # Ajouter bouton nom
                    self.add_nom = Gtk.Entry()
                    grid.attach(self.add_nom, 1, 2, 1, 1)
                    rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                    self.add_nom.override_background_color(Gtk.StateFlags.NORMAL, rgba)

                    label4 = Gtk.Label(label="Prenom")
                    grid.attach(label4, 0, 4, 1, 1)
                    rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                    label4.override_background_color(Gtk.StateFlags.NORMAL, rgba)
                    # Ajouter bouton prenom
                    self.add_prenom = Gtk.Entry()
                    grid.attach(self.add_prenom, 1, 4, 1, 1)
                    rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                    self.add_prenom.override_background_color(Gtk.StateFlags.NORMAL, rgba)

                    label5 = Gtk.Label(label="Telephone")
                    grid.attach(label5, 0, 6, 1, 1)
                    rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                    label5.override_background_color(Gtk.StateFlags.NORMAL, rgba)
                    # Ajouter bouton prenom
                    self.add_telephone = Gtk.Entry()
                    grid.attach(self.add_telephone, 1, 6, 1, 1)
                    rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                    self.add_telephone.override_background_color(Gtk.StateFlags.NORMAL, rgba)

                    # label5 = Gtk.Label(label="Date de naissance")
                    # grid.attach(label5, 0, 6, 1, 1)
                    # rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                    # label5.override_background_color(Gtk.StateFlags.NORMAL, rgba)
                    # # Ajouter bouton
                    # self.add_ddn = Gtk.Entry()
                    # grid.attach(self.add_ddn, 1, 6, 1, 1)
                    # rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                    # self.add_ddn.override_background_color(Gtk.StateFlags.NORMAL, rgba)

                    # Ajouter un bouton pour valider
                    button = Gtk.Button(label="Ajouter")
                    button.connect("clicked", self.on_button_clicked)
                    grid.attach(button, 0, 8, 2, 1)

        def on_button_clicked(self, widget):
            # Récupérer les valeurs saisies par l'utilisateur
            Name = self.add_nom.get_text()
            Prenom = self.add_prenom.get_text()
            Telephone = int(self.add_telephone.get_text())

            # Appeler l'API Go avec les données saisies
            url = 'http://localhost:3000/createClients'
            data = {'Name': Name, 'Prenom': Prenom, 'Telephone': Telephone}
            response = requests.post(url, data=data)

            # Vérifier si l'appel a réussi et afficher un message de confirmation
            if response.status_code == 200:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,"Les données ont été enregistrées avec succès.")
                dialog.run()
                dialog.destroy()
            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK,"Une erreur s'est produite lors de l'enregistrement des données.")
                dialog.run()
                dialog.destroy()

class Room(Gtk.Window):
        def __init__(self):
                Gtk.Window.__init__(self, title="Ajouter une chambre")
                self.set_border_width(10)

                grid = Gtk.Grid()
                grid.set_column_spacing(10)
                grid.set_row_spacing(10)
                self.add(grid)

                etiquette = Gtk.Label()
                etiquette.set_markup("<span foreground='#ffff78780000' font_desc='Times New Roman 20'>Ajouter une chambre</span>")
                grid.attach(etiquette, 1, 1, 1, 1)

                label10 = Gtk.Label(label="Etat de la chambre")
                grid.attach(label10, 0, 2, 1, 1)
                rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                label10.override_background_color(Gtk.StateFlags.NORMAL, rgba)
                # Ajouter bouton numero
                self.add_etat_chambre = Gtk.Entry()
                grid.attach(self.add_etat_chambre, 1, 2, 1, 1)
                rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                self.add_etat_chambre.override_background_color(Gtk.StateFlags.NORMAL, rgba)

                label9 = Gtk.Label(label="Nombre de lits")
                grid.attach(label9, 0, 4, 1, 1)
                rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                label9.override_background_color(Gtk.StateFlags.NORMAL, rgba)
                # Ajouter bouton numero
                self.add_nb_lits = Gtk.Entry()
                grid.attach(self.add_nb_lits, 1, 4, 1, 1)
                rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                self.add_nb_lits.override_background_color(Gtk.StateFlags.NORMAL, rgba)

                label5 = Gtk.Label(label="Description")
                grid.attach(label5, 0, 6, 1, 1)
                rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                label5.override_background_color(Gtk.StateFlags.NORMAL, rgba)
                # Ajouter bouton nom
                self.add_description = Gtk.Entry()
                grid.attach(self.add_description, 1, 6, 1, 1)
                rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                self.add_description.override_background_color(Gtk.StateFlags.NORMAL, rgba)

                label6 = Gtk.Label(label="Capacite")
                grid.attach(label6, 0, 8, 1, 1)
                rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                label6.override_background_color(Gtk.StateFlags.NORMAL, rgba)
                # Ajouter bouton numero
                self.add_capacite = Gtk.Entry()
                grid.attach(self.add_capacite, 1, 8, 1, 1)
                rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                self.add_capacite.override_background_color(Gtk.StateFlags.NORMAL, rgba)

                label7 = Gtk.Label(label="Service")
                grid.attach(label7, 0, 10, 1, 1)
                rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                label7.override_background_color(Gtk.StateFlags.NORMAL, rgba)
                # Ajouter bouton numero
                self.add_service = Gtk.Entry()
                grid.attach(self.add_service, 1, 10, 1, 1)
                rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                self.add_service.override_background_color(Gtk.StateFlags.NORMAL, rgba)

                label8 = Gtk.Label(label="Surface")
                grid.attach(label8, 0, 12, 1, 1)
                rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                label8.override_background_color(Gtk.StateFlags.NORMAL, rgba)
                # Ajouter bouton numero
                self.add_surface = Gtk.Entry()
                grid.attach(self.add_surface, 1, 12, 1, 1)
                rgba = Gdk.RGBA.from_color(Gdk.color_parse("#ffffa3a34848"))
                self.add_surface.override_background_color(Gtk.StateFlags.NORMAL, rgba)





                # Ajouter un bouton pour valider
                button = Gtk.Button(label="Ajouter")
                button.connect("clicked", self.on_button_clicked_room)
                grid.attach(button, 0, 16, 2, 1)

        def on_button_clicked_room(self, widget):
            # Récupérer les valeurs saisies par l'utilisateur
            EtatChambre = self.add_etat_chambre.get_text()
            NbreLits = int(self.add_nb_lits.get_text())
            Description = self.add_description.get_text()
            Capacites = int(self.add_capacite.get_text())
            Services = self.add_service.get_text()
            Surfaces = int(self.add_surface.get_text())

            # Appeler l'API Go avec les données saisies
            url = 'http://localhost:3000/createChambres'
            data = {'EtatChambre': EtatChambre,'NbreLits': NbreLits, 'Description': Description, 'Capacites': Capacites, 'Services': Services, 'Surfaces': Surfaces}
            response = requests.post(url, data=data)

            # Vérifier si l'appel a réussi et afficher un message de confirmation
            if response.status_code == 200:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,"Les données ont été enregistrées avec succès.")
                dialog.run()
                dialog.destroy()
            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK,"Une erreur s'est produite lors de l'enregistrement des données.")
                dialog.run()
                dialog.destroy()
        pass

if __name__ == "__main__":
        win = HotelMainPage()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()
