import gi


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


class HotelMainPage(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Page main")
        # Création de la barre de navigation
        headerbar = Gtk.HeaderBar()
        headerbar.set_show_close_button(True)
        headerbar.props.title = "SEN HOTEL"
        headerbar.props.subtitle = "bienvenue dans votre hotel "

        # Ajout du bouton pour l'administrateur
        button = Gtk.Button(label="Administrateur")
        button.connect("clicked", self.admin_button)
        headerbar.pack_end(button)
        self.set_titlebar(headerbar)

        # Autres éléments de l'interface
        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("/Users/macbookair/Downloads/img_hotel.jpg", 1000, 1500, True)
        image.set_from_pixbuf(pixbuf)

        self.add(image)

    def admin_button(self, widget):
        self.hide()
        login_window = interface_admin()
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

            # Création de l'image à ajouter
            # image = Gtk.Image.new_from_file("/Users/macbookair/Downloads/img_hotel.jpg")
            # image.set_size_request(100, 100)
            # Ajout de l'image au milieu de la grille
            # grid.attach(image, 0, 0, 1, 1)

            label2 = Gtk.Label()
            grid.attach(label2, 0, 2, 1, 1)

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
                        # Ajouter bouton nom_categorie
                        self.add_category = Gtk.Entry()
                        grid.attach(self.add_category, 1, 2, 1, 1)

                        label2 = Gtk.Label(label="Tarifs(cfa)")
                        grid.attach(label2, 0, 4, 1, 1)
                        # Ajouter bouton tarifs
                        self.add_tarif = Gtk.Entry()
                        grid.attach(self.add_tarif, 1, 4, 1, 1)

                        # Ajouter un bouton pour valider
                        button = Gtk.Button(label="Ajouter")
                        # button.connect("clicked", self.add_category)
                        grid.attach(button, 0, 5, 2, 1)

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
                    # Ajouter bouton nom
                    self.add_nom = Gtk.Entry()
                    grid.attach(self.add_nom, 1, 2, 1, 1)

                    label4 = Gtk.Label(label="Prenom")
                    grid.attach(label4, 0, 4, 1, 1)
                    # Ajouter bouton prenom
                    self.add_prenom = Gtk.Entry()
                    grid.attach(self.add_prenom, 1, 4, 1, 1)

                    # Ajouter un bouton pour valider
                    button = Gtk.Button(label="Ajouter")
                    # button.connect("clicked", self.add_category)
                    grid.attach(button, 0, 5, 2, 1)

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

                label5 = Gtk.Label(label="Nom")
                grid.attach(label5, 0, 2, 1, 1)
                # Ajouter bouton nom
                self.add_nom = Gtk.Entry()
                grid.attach(self.add_nom, 1, 2, 1, 1)

                label6 = Gtk.Label(label="Prenom")
                grid.attach(label6, 0, 4, 1, 1)
                # Ajouter bouton prenom
                self.add_prenom = Gtk.Entry()
                grid.attach(self.add_prenom, 1, 4, 1, 1)

                # Ajouter un bouton pour valider
                button = Gtk.Button(label="Ajouter")
                # button.connect("clicked", self.add_category)
                grid.attach(button, 0, 5, 2, 1)
        pass

if __name__ == "__main__":
        win = HotelMainPage()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()
