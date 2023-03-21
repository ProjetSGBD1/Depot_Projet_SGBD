#!/usr/bin/python3
import sys
import gi
import datetime
from datetime import date
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject


class Fenetre_gestion_hotel(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Informations sur les catégories
        self.classe = "economique"
        self.tarif_normal = 200.0
        self.tarif_special = 100.0

#Informations sur le gérant
        self.identifiant = "paulito"
        self.mot_de_passe = "paulito"

#Informations de l'hotel
        self.nom_hotel = "sama_hotel"
        self.nombre_chambre = 200
        self.date_debut = date(1999,2,24)
        self.adresse = "keurmassarPAU:9"
        self.tel = "780113280"

# Informations sur le client
        self.nom = "Ndour"
        self.prenom = "Paul"
        self.date_entree = date(2023,2,24)
        self.date_sortie = date(2023,3,24)
        self.tel_client = "762617136"

# Informations sur les services annexes
        self.nom_service = "Bar"
        self.tarif = 200.0

# Informations sur la facture
        self.id_facture = 1
        self.tarif_special_facture = 200.0
        self.tarif_chambre = 310.0
        self.tarif_petit_dej = 10.0
        self.tarif_phone = 10.0
        self.tarif_bar = 10.0
        self.total = self.tarif_special + self.tarif_chambre + self.tarif_petit_dej + self.tarif_phone + self.tarif_bar
        self.total = self.total

# Informations sur le stock et approvisionnement
        self.id_article = 1
        self.categorie_article = "boisson"
        self.nom_article = "Coca-cola"
        self.image_article = ""
        self.caracteristiques = "consomable"
        self.prix_unitaire = 100.0
        self.quantite_stock = 100
        self.date_appro = date(2022,2,24)
        self.montant_total = 1000.0

# Informations sur la chambre
        self.numero_chambre = 1
        self.etat = 'L'

# Informations sur la reservation
        self.date_reservation = date(2008,3,9)
        self.nuite = 'O'
        self.petit_dej = 'O'
        self.phone = 'O'
        self.bar = 'O'


# Transition entre les pages
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(1000)
        self.add(self.stack)

# Creer un boutton précedent
        button_precedent = Gtk.Button.new_with_label("Menu")
        button_precedent.connect("clicked", self.on_button_precedent_clicked)

        button_preceden = Gtk.Button.new_with_label("Menu")
        button_preceden.connect("clicked", self.on_button_preceden_clicked)

        button_precede = Gtk.Button.new_with_label("Menu")
        button_precede.connect("clicked", self.on_button_precede_clicked)

        button_prece = Gtk.Button.new_with_label("Menu")
        button_prece.connect("clicked", self.on_button_prece_clicked)

        button_prec = Gtk.Button.new_with_label("Menu")
        button_prec.connect("clicked", self.on_button_prec_clicked)

        button_pre = Gtk.Button.new_with_label("Menu")
        button_pre.connect("clicked", self.on_button_pre_clicked)

        button_pr = Gtk.Button.new_with_label("Menu")
        button_pr.connect("clicked", self.on_button_pr_clicked)


# Afficher le formulaire d'authentification
        question = Gtk.Label("Quel est l'identifiant et le mot de passe du gérant  ?")
        label1 = Gtk.Label("Identifiant")
        label2 = Gtk.Label("Mot de passe:")

        button_connexion = Gtk.Button.new_with_mnemonic("connexion")
        button_connexion.set_relief(Gtk.ReliefStyle.NORMAL)
        button_connexion.set_size_request(1, 5)

        id = Gtk.Entry()
        mot_d_passe = Gtk.Entry()
        mot_d_passe.set_visibility(False)
        mot_d_passe.set_invisible_char("*")

        button_connexion.connect("clicked", self.on_button_connexion_clicked, id, mot_d_passe)

        auth_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        auth_box.pack_start(question, False, False, 100)
        auth_box.pack_start(label1, False, False, 5)
        auth_box.pack_start(id, False, False, 5)
        auth_box.pack_start(label2, False, False, 5)
        auth_box.pack_start(mot_d_passe, False, False, 5)
        auth_box.pack_start(button_connexion, False, False, 0)

        hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        hbox.pack_start(auth_box, False, True, 0)

        self.stack.add_titled(hbox, "auth", "Authentication")

#Gerer le menu
        menu_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        button_gerer_reservation = Gtk.Button.new_with_mnemonic("Reservation")
        button_gerer_chambre = Gtk.Button.new_with_mnemonic("Chambres")
        button_gerer_clients = Gtk.Button.new_with_mnemonic("Clients")
        button_gerer_services_annexes = Gtk.Button.new_with_mnemonic("Services annexes")
        button_gerer_stock_et_approvisionnements = Gtk.Button.new_with_mnemonic("Stocks et approvisionnement")
        button_consulter = Gtk.Button.new_with_mnemonic("Consulter")
        button_reglages = Gtk.Button.new_with_mnemonic("Reglages")

        button_gerer_reservation.connect("clicked", self.on_button_gerer_reservation_clicked)
        button_gerer_chambre.connect("clicked", self.on_button_gerer_chambre_clicked)
        button_gerer_clients.connect("clicked", self.on_button_gerer_clients_clicked)
        button_gerer_services_annexes.connect("clicked", self.on_button_gerer_services_annexes_clicked)
        button_gerer_stock_et_approvisionnements.connect("clicked", self.on_button_stock_approvisionnement_clicked)
        button_consulter.connect("clicked", self.on_button_consulter_clicked)
        button_reglages.connect("clicked", self.on_button_reglages_clicked)

        menu_page.pack_start(Gtk.Label("Bienvenue dans votre application " + self.nom_hotel), True, True, 0)
        menu_page.pack_start(button_gerer_reservation, True, True, 0)
        menu_page.pack_start(button_gerer_chambre, True, True, 0)
        menu_page.pack_start(button_gerer_clients, True, True, 0)
        menu_page.pack_start(button_gerer_services_annexes, True, True, 0)
        menu_page.pack_start(button_gerer_stock_et_approvisionnements, True, True, 0)
        menu_page.pack_start(button_consulter, True, True, 0)
        menu_page.pack_start(button_reglages, True, True, 0)

        hobox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        hobox.pack_start(menu_page, False, True, 0)
        self.stack.add_titled(hobox, "menu", "Secure Content")

# gerer reservation
        reservation_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        button_ajouter_reservation = Gtk.Button.new_with_mnemonic("Ajouter une reservation")
        button_annuler_chambre = Gtk.Button.new_with_mnemonic("Annuler une reservation")
        button_liste_reservations = Gtk.Button.new_with_mnemonic("Liste des reservations")

        button_ajouter_reservation.connect("clicked", self.on_button_ajouter_reservation_clicked)
        button_liste_reservations.connect("clicked", self.on_button_liste_reservations_clicked)

        reservation_box.pack_start(button_ajouter_reservation, True, True, 0)
        reservation_box.pack_start(button_annuler_chambre, True, True, 0)
        reservation_box.pack_start(button_liste_reservations, True, True, 0)
        reservation_box.pack_start(button_precedent, True, True, 0)

        horbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        horbox.pack_start(reservation_box, False, True, 0)

        self.stack.add_titled(horbox, "reservation", "montrer reservation_box")

# gerer chambre
        chambre_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        button_ajouter_categorie = Gtk.Button.new_with_mnemonic("Ajouter une categorie")
        button_ajouter_chambre = Gtk.Button.new_with_mnemonic("Ajouter une chambre")
        button_liste_chambres = Gtk.Button.new_with_mnemonic("Liste des chambres")

        button_ajouter_categorie.connect("clicked", self.on_button_ajouter_categorie_clicked)
        button_ajouter_chambre.connect("clicked", self.on_button_ajouter_chambre_clicked)
        button_liste_chambres.connect("clicked", self.on_button_liste_chambres_clicked)

        chambre_box.pack_start(button_ajouter_categorie, True, True, 0)
        chambre_box.pack_start(button_ajouter_chambre, True, True, 0)
        chambre_box.pack_start(button_liste_chambres, True, True, 0)
        chambre_box.pack_start(button_preceden, True, True, 0)

        horibox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        horibox.pack_start(chambre_box, False, True, 0)

        self.stack.add_titled(horibox, "chambres", "montrer chambre_box")

# gerer clients
        client_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        button_ajouter_client = Gtk.Button.new_with_mnemonic("Ajouter un client")
        button_liste_clients = Gtk.Button.new_with_mnemonic("Liste des clients")
        button_generer_facture = Gtk.Button.new_with_mnemonic("Facture")

        button_ajouter_client.connect("clicked", self.on_button_ajouter_client_clicked)
        button_generer_facture.connect("clicked", self.on_button_generer_facture_clicked)
        button_liste_clients.connect("clicked", self.on_button_liste_clients_clicked)

        client_box.pack_start(button_ajouter_client, True, True, 0)
        client_box.pack_start(button_liste_clients, True, True, 0)
        client_box.pack_start(button_generer_facture, True, True, 0)
        client_box.pack_start(button_prec, True, True, 0)

        horizbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        horizbox.pack_start(client_box, False, True, 0)

        self.stack.add_titled(horizbox, "clients", "montrer client_box")

# gerer services annexes
        services_annexes_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        button_ajouter_service_annexe = Gtk.Button.new_with_mnemonic("Ajouter un service annexe")
        button_liste_services_annexes = Gtk.Button.new_with_mnemonic("Liste des services annexes")
        button_attribuer_services_annexes_client = Gtk.Button.new_with_mnemonic("Attribuer un service annexe à un client")

        button_ajouter_service_annexe.connect("clicked", self.on_button_ajouter_service_annexe_clicked)
        button_liste_services_annexes.connect("clicked", self.on_button_liste_services_annexes_clicked)
        button_attribuer_services_annexes_client.connect("clicked", self.on_button_attribuer_services_annexes_client_clicked)

        services_annexes_box.pack_start(button_ajouter_service_annexe, True, True, 0)
        services_annexes_box.pack_start(button_liste_services_annexes, True, True, 0)
        services_annexes_box.pack_start(button_attribuer_services_annexes_client, True, True, 0)
        services_annexes_box.pack_start(button_pre, True, True, 0)

        horizobox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        horizobox.pack_start(services_annexes_box, False, True, 0)

        self.stack.add_titled(horizobox, "services_annexes", "montrer services_annexes_box")

# gerer stock et approvisionnement
        stock_appro_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        button_a_article = Gtk.Button.new_with_mnemonic("Ajouter un article")
        button_liste_articles = Gtk.Button.new_with_mnemonic("Liste des articles")

        button_a_article.connect("clicked", self.on_button_a_article_clicked)
        button_liste_articles.connect("clicked", self.on_button_liste_articles_clicked)

        stock_appro_box.pack_start(button_a_article, True, True, 0)
        stock_appro_box.pack_start(button_liste_articles, True, True, 0)
        stock_appro_box.pack_start(button_precede, True, True, 0)

        horizonbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        horizonbox.pack_start(stock_appro_box, False, True, 0)

        self.stack.add_titled(horizonbox, "stocks", "montrer stock_appro_box")

# consulter
        consulter_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        button_recettes = Gtk.Button.new_with_mnemonic("Recettes")
        button_depenses = Gtk.Button.new_with_mnemonic("Depenses")
        button_statistiques = Gtk.Button.new_with_mnemonic("Statistiques")

        consulter_box.pack_start(button_recettes, True, True, 0)
        consulter_box.pack_start(button_depenses, True, True, 0)
        consulter_box.pack_start(button_statistiques, True, True, 0)
        consulter_box.pack_start(button_prece, True, True, 0)

        horizontbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        horizontbox.pack_start(consulter_box, False, True, 0)

        self.stack.add_titled(horizontbox, "consulter", "montrer consulter_box")

# Reglages
        reglages_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        button_informations_hotel = Gtk.Button.new_with_mnemonic("Informations de l'hotel")
        button_changer = Gtk.Button.new_with_mnemonic("Inforamtions Gerant")

        button_informations_hotel.connect("clicked", self.on_button_information_hotel_clicked)
        button_changer.connect("clicked", self.on_button_changer_clicked)

        reglages_box.pack_start(button_informations_hotel, True, True, 0)
        reglages_box.pack_start(button_changer, True, True, 0)
        reglages_box.pack_start(button_pr, True, True, 0)

        horizontabox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        horizontabox.pack_start(reglages_box, False, True, 0)

        self.stack.add_titled(horizontabox, "reglages", "montrer reglages_box")

    # Afficher le menu si l'authentification est correcte ou non
    def on_button_connexion_clicked(self,button_connexion,id,mot_d_passe):
        if self.identifiant == (id.get_text()) and self.mot_de_passe == str(mot_d_passe.get_text()):
            self.stack.set_visible_child_name("menu")
        else:
            dialog = Gtk.MessageDialog(parent=self, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="identifiant ou mot de passe incorrectes")
            dialog.run()
            dialog.destroy()


# Afficher la page de gestion de reservation
    def on_button_gerer_reservation_clicked(self, button_gerer_reservation):
        self.stack.set_visible_child_name("reservation")


# Afficher la page de gestion des chambres
    def on_button_gerer_chambre_clicked(self, button_gerer_chambre):
        self.stack.set_visible_child_name("chambres")


# Afficher la page de gestion des clients
    def on_button_gerer_clients_clicked(self, button_gerer_chambre):
        self.stack.set_visible_child_name("clients")

# Afficher la page de gestion des services annexes
    def on_button_gerer_services_annexes_clicked(self, button_gerer_services_annexes):
        self.stack.set_visible_child_name("services_annexes")

# Afficher la page de gestion de stocks et approvisionnement
    def on_button_stock_approvisionnement_clicked(self, button_gerer_stock_et_approvisionnements):
        self.stack.set_visible_child_name("stocks")


# Afficher la page de consultation
    def on_button_consulter_clicked(self, button_consulter ):
        self.stack.set_visible_child_name("consulter")

# Afficher les reglages
    def on_button_reglages_clicked(self, button_reglages):
        self.stack.set_visible_child_name("reglages")


# Permet d'afficher la page précédente
    def on_button_precedent_clicked(self, widget):
        self.stack.set_visible_child_name("menu")

    def on_button_preceden_clicked(self, widget):
        self.stack.set_visible_child_name("menu")

    def on_button_precede_clicked(self, widget):
        self.stack.set_visible_child_name("menu")

    def on_button_prece_clicked(self, widget):
        self.stack.set_visible_child_name("menu")

    def on_button_prec_clicked(self, widget):
        self.stack.set_visible_child_name("menu")

    def on_button_pre_clicked(self, widget):
        self.stack.set_visible_child_name("menu")

    def on_button_pr_clicked(self, widget):
        self.stack.set_visible_child_name("menu")

# Ajouter une categorie
    def on_button_ajouter_categorie_clicked(self, button_ajouter_categorie):
        dialog = Gtk.Dialog(title="Ajouter une categorie", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("APPLIQUER", Gtk.ResponseType.APPLY)
        dialog.add_button("RETOUR", Gtk.ResponseType.CANCEL)
        dialog.set_default_response(Gtk.ResponseType.APPLY)
        label1 = Gtk.Label("Classe : ")
        label2 = Gtk.Label("Tarif normal : ")
        label3 = Gtk.Label("Tarif special : ")
        classe = Gtk.Entry()
        tarif_normal = Gtk.Entry()
        tarif_special = Gtk.Entry()
        classe.set_text(self.classe)
        tarif_normal.set_text(str(self.tarif_normal))
        tarif_special.set_text(str(self.tarif_special))
        grille = Gtk.Grid()
        grille.attach(label1, 0, 0, 1, 1)
        grille.attach(label2, 0, 1, 1, 1)
        grille.attach(label3, 0, 2, 1, 1)
        grille.attach(classe, 1, 0, 1, 1)
        grille.attach(tarif_normal, 1, 1, 1, 1)
        grille.attach(tarif_special, 1, 2, 1, 1)
        dialog.vbox.pack_start(grille, False, False, 5)
        dialog.show_all()
        resultat = dialog.run()
        if resultat == Gtk.ResponseType.APPLY:
            print("Classe : " + classe.get_text())
            print("tarif_normal : " + str(tarif_normal.get_text()))
            print("tarif_special : " + str(tarif_special.get_text()))
        dialog.destroy()


# Afficher ou modifier les informations sur l'hotel
    def on_button_information_hotel_clicked(self, button_information_hotel):
        dialog = Gtk.Dialog(title="Informations sur l'hotel", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("OK", Gtk.ResponseType.OK)
        dialog.add_button("APPLIQUER", Gtk.ResponseType.APPLY)
        dialog.set_default_response(Gtk.ResponseType.OK)
        label1 = Gtk.Label("Nom de l'hotel : ")
        label2 = Gtk.Label("Nombre de chambres : ")
        label3 = Gtk.Label("Date de debut : ")
        label4 = Gtk.Label("Adresse : ")
        label5 = Gtk.Label("Telephone : ")
        nom_hotel = Gtk.Entry()
        nb_chambre = Gtk.Entry()
        date_debut = Gtk.Entry()
        adresse = Gtk.Entry()
        tel = Gtk.Entry()
        nom_hotel.set_text(self.nom_hotel)
        nb_chambre.set_text(str(self.nombre_chambre))
        date_debut.set_text(str(self.date_debut))
        adresse.set_text(self.adresse)
        tel.set_text(str(self.tel))
        grille = Gtk.Grid()
        grille.attach(label1, 0, 0, 1, 1)
        grille.attach(label2, 0, 1, 1, 1)
        grille.attach(label3, 0, 2, 1, 1)
        grille.attach(label4, 0, 3, 1, 1)
        grille.attach(label5, 0, 4, 1, 1)
        grille.attach(nom_hotel, 1, 0, 1, 1)
        grille.attach(nb_chambre, 1, 1, 1, 1)
        grille.attach(date_debut, 1, 2, 1, 1)
        grille.attach(adresse, 1, 3, 1, 1)
        grille.attach(tel, 1, 4, 1, 1)
        dialog.vbox.pack_start(grille, False, False, 5)
        dialog.show_all()
        resultat = dialog.run()
        if resultat == Gtk.ResponseType.OK:
            print("nom de l'hotel : " + nom_hotel.get_text())
            print("nombre de chambre : " + str(nb_chambre.get_text()))
            print("date de debut : " + str(date_debut.get_text()))
            print("adresse : " + (adresse.get_text()))
            print("telephone : " + (tel.get_text()))
        dialog.destroy()

# Afficher ou modifier les informations sur le gérant
    def on_button_changer_clicked(self,button_changer):
        dialog = Gtk.Dialog(title="Informations sur le gerant", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("OK", Gtk.ResponseType.OK)
        dialog.add_button("APPLIQUER", Gtk.ResponseType.APPLY)
        dialog.set_default_response(Gtk.ResponseType.OK)
        label1 = Gtk.Label("Identifiant : ")
        label2 = Gtk.Label("Mot de passe : ")
        id = Gtk.Entry()
        mdp = Gtk.Entry()
        id.set_text(self.identifiant)
        mdp.set_text(self.mot_de_passe)
        grille = Gtk.Grid()
        grille.attach(label1, 0, 0, 1, 1)
        grille.attach(label2, 0, 1, 1, 1)
        grille.attach(id, 1, 0, 1, 1)
        grille.attach(mdp, 1, 1, 1, 1)
        dialog.vbox.pack_start(grille, False, False, 5)
        dialog.show_all()
        resultat = dialog.run()
        if resultat == Gtk.ResponseType.OK:
            print("Identifiant : " + id.get_text())
            print("Mot de passe: " + mdp.get_text())
        dialog.destroy()

# Ajouter un client
    def on_button_ajouter_client_clicked(self, button_ajouter_client):
        dialog = Gtk.Dialog(title="Ajouter un client", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("APPLIQUER", Gtk.ResponseType.APPLY)
        dialog.add_button("RETOUR", Gtk.ResponseType.CANCEL)
        dialog.set_default_response(Gtk.ResponseType.APPLY)
        label1 = Gtk.Label("Nom : ")
        label2 = Gtk.Label("Prenom : ")
        label3 = Gtk.Label("Telephone : ")
        label4 = Gtk.Label("Date d'entree : ")
        label5 = Gtk.Label("Date de sortie : ")
        nom_client = Gtk.Entry()
        prenom_client = Gtk.Entry()
        tel_client = Gtk.Entry()
        date_entree = Gtk.Entry()
        date_sortie = Gtk.Entry()
        nom_client.set_text(self.nom)
        prenom_client.set_text(self.prenom)
        tel_client.set_text(self.tel_client)
        date_entree.set_text(str(self.date_entree))
        date_sortie.set_text(str(self.date_sortie))
        grille = Gtk.Grid()
        grille.attach(label1, 0, 0, 1, 1)
        grille.attach(label2, 0, 1, 1, 1)
        grille.attach(label3, 0, 2, 1, 1)
        grille.attach(label4, 0, 3, 1, 1)
        grille.attach(label5, 0, 4, 1, 1)
        grille.attach(nom_client, 1, 0, 1, 1)
        grille.attach(prenom_client, 1, 1, 1, 1)
        grille.attach(tel_client, 1, 2, 1, 1)
        grille.attach(date_entree, 1, 3, 1, 1)
        grille.attach(date_sortie, 1, 4, 1, 1)
        dialog.vbox.pack_start(grille, False, False, 5)
        dialog.show_all()
        resultat = dialog.run()
        if resultat == Gtk.ResponseType.APPLY:
            print("Nom : " + nom_client.get_text())
            print("Prenom  : " + prenom_client.get_text())
            print("telephone : " + tel_client.get_text())
            print("Date d'entree : " + str(date_entree.get_text()))
            print("Date de sortie : " + str(date_sortie.get_text()))
        dialog.destroy()

# Ajouter un service annexe
    def on_button_ajouter_service_annexe_clicked(self, button_ajouter_service_annexe):
        dialog = Gtk.Dialog(title="Ajouter un service annexe", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("APPLIQUER", Gtk.ResponseType.APPLY)
        dialog.add_button("RETOUR", Gtk.ResponseType.CANCEL)
        dialog.set_default_response(Gtk.ResponseType.APPLY)
        label1 = Gtk.Label("Nom du service : ")
        label2 = Gtk.Label("Tarif : ")
        nom_service = Gtk.Entry()
        tarif_service = Gtk.Entry()
        nom_service.set_text(self.nom_service)
        tarif_service.set_text(str(self.tarif))
        grille = Gtk.Grid()
        grille.attach(label1, 0, 0, 1, 1)
        grille.attach(label2, 0, 1, 1, 1)
        grille.attach(nom_service, 1, 0, 1, 1)
        grille.attach(tarif_service, 1, 1, 1, 1)
        dialog.vbox.pack_start(grille, False, False, 5)
        dialog.show_all()
        resultat = dialog.run()
        if resultat == Gtk.ResponseType.APPLY:
            print("Nom du service : " + nom_service.get_text())
            print("Tarif  : " + str(tarif_service.get_text()))
        dialog.destroy()

# attribuer un service annexe à un client
    def on_button_attribuer_services_annexes_client_clicked(self, button_attribuer_services_annexes_client):
        dialog = Gtk.Dialog(title="Attribuer un service à un client", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("APPLIQUER", Gtk.ResponseType.APPLY)
        dialog.add_button("RETOUR", Gtk.ResponseType.CANCEL)
        dialog.set_default_response(Gtk.ResponseType.APPLY)
        label1 = Gtk.Label("Nom du client : ")
        label2 = Gtk.Label("Prenom du client : ")
        label3 = Gtk.Label("Telephone : ")
        label4 = Gtk.Label("nom service : ")
        nom_client = Gtk.Entry()
        prenom_client = Gtk.Entry()
        tel_client = Gtk.Entry()
        nom_service = Gtk.Entry()
        nom_client.set_text(self.nom)
        prenom_client.set_text(self.prenom)
        tel_client.set_text(self.tel_client)
        nom_service.set_text(self.nom_service)
        grille = Gtk.Grid()
        grille.attach(label1, 0, 0, 1, 1)
        grille.attach(label2, 0, 1, 1, 1)
        grille.attach(label3, 0, 2, 1, 1)
        grille.attach(label4, 0, 3, 1, 1)
        grille.attach(nom_client, 1, 0, 1, 1)
        grille.attach(prenom_client, 1, 1, 1, 1)
        grille.attach(tel_client, 1, 2, 1, 1)
        grille.attach(nom_service, 1, 3, 1, 1)
        dialog.vbox.pack_start(grille, False, False, 5)
        dialog.show_all()
        resultat = dialog.run()
        if resultat == Gtk.ResponseType.APPLY:
            print("Nom : " + nom_client.get_text())
            print("Prenom  : " + prenom_client.get_text())
            print("telephone : " + tel_client.get_text())
            print("Date d'entree : " + str(nom_service.get_text()))
        dialog.destroy()



# Generation de facture
    def on_button_generer_facture_clicked(self, button_generer_facture ):
        dialog = Gtk.Dialog(title="Génerer un facture", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("GENERER", Gtk.ResponseType.APPLY)
        dialog.add_button("ANNULER", Gtk.ResponseType.CANCEL)
        dialog.set_default_response(Gtk.ResponseType.APPLY)
        label1 = Gtk.Label("Numero : ")
        label2 = Gtk.Label("Nom : ")
        label3 = Gtk.Label("Prenom : ")
        label4 = Gtk.Label("Telephone : ")
        label5 = Gtk.Label("Tarif special : ")
        label6 = Gtk.Label("Tarif chambre : ")
        label7 = Gtk.Label("Tarif petit dej : ")
        label8 = Gtk.Label("Tarif phone : ")
        label9 = Gtk.Label("Tarif bar : ")
        id_facture = Gtk.Entry()
        nom_client = Gtk.Entry()
        prenom_client = Gtk.Entry()
        tel_client = Gtk.Entry()
        tarif_special = Gtk.Entry()
        tarif_chambre = Gtk.Entry()
        tarif_petit_dej = Gtk.Entry()
        tarif_phone = Gtk.Entry()
        tarif_bar = Gtk.Entry()
        id_facture.set_text(str(self.id_facture))
        nom_client.set_text(self.nom)
        prenom_client.set_text(self.prenom)
        tel_client.set_text(self.tel_client)
        tarif_special.set_text(str(self.tarif_special_facture))
        tarif_chambre.set_text(str(self.tarif_chambre))
        tarif_petit_dej.set_text(str(self.tarif_petit_dej))
        tarif_phone.set_text(str(self.tarif_phone))
        tarif_bar.set_text(str(self.tarif_bar))
        grille = Gtk.Grid()
        grille.attach(label1, 0, 0, 1, 1)
        grille.attach(label2, 0, 1, 1, 1)
        grille.attach(label3, 0, 2, 1, 1)
        grille.attach(label4, 0, 3, 1, 1)
        grille.attach(label5, 0, 4, 1, 1)
        grille.attach(label6, 0, 5, 1, 1)
        grille.attach(label7, 0, 6, 1, 1)
        grille.attach(label8, 0, 7, 1, 1)
        grille.attach(label9, 0, 8, 1, 1)
        grille.attach(id_facture, 1, 0, 1, 1)
        grille.attach(nom_client, 1, 1, 1, 1)
        grille.attach(prenom_client, 1, 2, 1, 1)
        grille.attach(tel_client, 1, 3, 1, 1)
        grille.attach(tarif_special, 1, 4, 1, 1)
        grille.attach(tarif_chambre, 1, 5, 1, 1)
        grille.attach(tarif_petit_dej, 1, 6, 1, 1)
        grille.attach(tarif_phone, 1, 7, 1, 1)
        grille.attach(tarif_bar, 1, 8, 1, 1)
        dialog.vbox.pack_start(grille, False, False, 5)
        dialog.show_all()
        resultat = dialog.run()
        if resultat == Gtk.ResponseType.APPLY:
            print("Numéro : " + id_facture.get_text())
            print("Nom : " + nom_client.get_text())
            print("Prenom  : " + prenom_client.get_text())
            print("telephone : " + tel_client.get_text())
            print("Tarif special : " + str(tarif_special.get_text()))
            print("Tarif chambre : " + str(tarif_chambre.get_text()))
            print("Tarif petit dej : " + str(tarif_petit_dej.get_text()))
            print("Tarif phone : " + str(tarif_phone.get_text()))
            print("Tarif bar : " + str(tarif_bar.get_text()))
        dialog.destroy()

# Ajouter un article
    def on_button_a_article_clicked(self, button_a_article):
        dialog = Gtk.Dialog(title="Ajouter un article", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("APPLIQUER", Gtk.ResponseType.APPLY)
        dialog.add_button("ANNULER", Gtk.ResponseType.CANCEL)
        dialog.set_default_response(Gtk.ResponseType.APPLY)
        label1 = Gtk.Label("Numero : ")
        label2 = Gtk.Label("Categorie: ")
        label3 = Gtk.Label("nom article : ")
        label4 = Gtk.Label("caracteristiques : ")
        label5 = Gtk.Label("prix unitaire : ")
        label6 = Gtk.Label("quantité en stock : ")
        label7 = Gtk.Label("date d'approvisionnement : ")
        id_article = Gtk.Entry()
        categorie = Gtk.Entry()
        nom_article = Gtk.Entry()
        caracteristiques = Gtk.Entry()
        prix_unitaire = Gtk.Entry()
        quantite_stock= Gtk.Entry()
        date_appro = Gtk.Entry()
        id_article.set_text(str(self.id_article))
        categorie.set_text(self.categorie_article)
        nom_article.set_text(self.nom_article)
        caracteristiques.set_text(self.caracteristiques)
        prix_unitaire.set_text(str(self.prix_unitaire))
        quantite_stock.set_text(str(self.quantite_stock))
        date_appro.set_text(str(self.date_appro))
        grille = Gtk.Grid()
        grille.attach(label1, 0, 0, 1, 1)
        grille.attach(label2, 0, 1, 1, 1)
        grille.attach(label3, 0, 2, 1, 1)
        grille.attach(label4, 0, 3, 1, 1)
        grille.attach(label5, 0, 4, 1, 1)
        grille.attach(label6, 0, 5, 1, 1)
        grille.attach(label7, 0, 6, 1, 1)
        grille.attach(id_article, 1, 0, 1, 1)
        grille.attach(categorie, 1, 1, 1, 1)
        grille.attach(nom_article, 1, 2, 1, 1)
        grille.attach(caracteristiques, 1, 3, 1, 1)
        grille.attach(prix_unitaire, 1, 4, 1, 1)
        grille.attach(quantite_stock, 1, 5, 1, 1)
        grille.attach(date_appro, 1, 6, 1, 1)
        dialog.vbox.pack_start(grille, False, False, 5)
        dialog.show_all()
        resultat = dialog.run()
        if resultat == Gtk.ResponseType.APPLY:
            print("Numero : " + id_article.get_text())
            print("Categorie : " + categorie.get_text())
            print("Nom article  : " + nom_article.get_text())
            print("Caractéristique : " + caracteristiques.get_text())
            print("Prix unitaire : " + str(prix_unitaire.get_text()))
            print("Quantité stock : " + str(quantite_stock.get_text()))
            print("Date appro : " + str(date_appro.get_text()))
        dialog.destroy()

# Ajouter une chambre
    def on_button_ajouter_chambre_clicked(self, button_ajouter_chambre):
        dialog = Gtk.Dialog(title="Ajouter une chambre", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("APPLIQUER", Gtk.ResponseType.APPLY)
        dialog.add_button("ANNULER", Gtk.ResponseType.CANCEL)
        dialog.set_default_response(Gtk.ResponseType.APPLY)
        label1 = Gtk.Label("Numero : ")
        label2 = Gtk.Label("Etat: ")
        label3 = Gtk.Label("Classe: ")
        num_chambre = Gtk.Entry()
        etat = Gtk.Entry()
        classe = Gtk.Entry()
        num_chambre.set_text(str(self.numero_chambre))
        etat.set_text(self.etat)
        classe.set_text(self.classe)
        grille = Gtk.Grid()
        grille.attach(label1, 0, 0, 1, 1)
        grille.attach(label2, 0, 1, 1, 1)
        grille.attach(label3, 0, 2, 1, 1)
        grille.attach(num_chambre, 1, 0, 1, 1)
        grille.attach(etat, 1, 1, 1, 1)
        grille.attach(classe, 1, 2, 1, 1)
        dialog.vbox.pack_start(grille, False, False, 5)
        dialog.show_all()
        resultat = dialog.run()
        if resultat == Gtk.ResponseType.APPLY:
            print("Numero : " + str(num_chambre.get_text()))
            print("Etat : " + etat.get_text())
            print("Classe : " + classe.get_text())
        dialog.destroy()

# Ajouter une reservation
    def on_button_ajouter_reservation_clicked(self, button_ajouter_resrvation):
        dialog = Gtk.Dialog(title="Ajouter une reservation", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("APPLIQUER", Gtk.ResponseType.APPLY)
        dialog.add_button("ANNULER", Gtk.ResponseType.CANCEL)
        dialog.set_default_response(Gtk.ResponseType.APPLY)
        label1 = Gtk.Label("Numero chambre : ")
        label2 = Gtk.Label("Nom : ")
        label3 = Gtk.Label("Prenom : ")
        label4 = Gtk.Label("Telephone : ")
        label5 = Gtk.Label("Classe : ")
        label6 = Gtk.Label("Date reservation : ")
        label7 = Gtk.Label("Nuite : ")
        label8 = Gtk.Label("Tarif chambre : ")
        label9 = Gtk.Label("Petit dej : ")
        label10 = Gtk.Label("Phone : ")
        label11 = Gtk.Label("Bar : ")
        label12 = Gtk.Label("Date entree : ")
        label13 = Gtk.Label("Date Sortie : ")
        num = Gtk.Entry()
        nom = Gtk.Entry()
        prenom = Gtk.Entry()
        tel = Gtk.Entry()
        classe = Gtk.Entry()
        date_r = Gtk.Entry()
        tarif_chambre = Gtk.Entry()
        nuite = Gtk.Entry()
        petit_dej = Gtk.Entry()
        phone = Gtk.Entry()
        bar = Gtk.Entry()
        date_e = Gtk.Entry()
        date_s = Gtk.Entry()
        num.set_text(str(self.numero_chambre))
        nom.set_text(self.nom)
        prenom.set_text(self.prenom)
        tel.set_text(self.tel_client)
        classe.set_text(self.classe)
        date_r.set_text(str(self.date_reservation))
        nuite.set_text(self.nuite)
        tarif_chambre.set_text(str(self.tarif_chambre))
        petit_dej.set_text(self.petit_dej)
        phone.set_text(self.phone)
        bar.set_text(self.bar)
        date_e.set_text(str(self.date_entree))
        date_s.set_text(str(self.date_sortie))
        grille = Gtk.Grid()
        grille.attach(label1, 0, 0, 1, 1)
        grille.attach(label2, 0, 1, 1, 1)
        grille.attach(label3, 0, 2, 1, 1)
        grille.attach(label4, 0, 3, 1, 1)
        grille.attach(label5, 0, 4, 1, 1)
        grille.attach(label6, 0, 5, 1, 1)
        grille.attach(label7, 0, 6, 1, 1)
        grille.attach(label8, 0, 7, 1, 1)
        grille.attach(label9, 0, 8, 1, 1)
        grille.attach(label10, 0, 9, 1, 1)
        grille.attach(label11, 0, 10, 1, 1)
        grille.attach(label12, 0, 11, 1, 1)
        grille.attach(label13, 0, 12, 1, 1)
        grille.attach(num, 1, 0, 1, 1)
        grille.attach(nom, 1, 1, 1, 1)
        grille.attach(prenom, 1, 2, 1, 1)
        grille.attach(tel, 1, 3, 1, 1)
        grille.attach(classe, 1, 4, 1, 1)
        grille.attach(date_r, 1, 5, 1, 1)
        grille.attach(nuite, 1, 6, 1, 1)
        grille.attach(tarif_chambre, 1, 7, 1, 1)
        grille.attach(petit_dej, 1, 8, 1, 1)
        grille.attach(phone, 1, 9, 1, 1)
        grille.attach(bar, 1, 10, 1, 1)
        grille.attach(date_e, 1, 11, 1, 1)
        grille.attach(date_s, 1, 12, 1, 1)
        dialog.vbox.pack_start(grille, False, False, 5)
        dialog.show_all()
        resultat = dialog.run()
        if resultat == Gtk.ResponseType.APPLY:
            print("Numéro : " + num.get_text())
            print("Nom : " + nom.get_text())
            print("Prenom  : " + prenom.get_text())
            print("telephone : " + tel.get_text())
            print("Classe : " + classe.get_text())
            print("Date reservation : " + str(date_r.get_text()))
            print("Nuite : " + nuite.get_text())
            print("Tarif chambre : " + str(tarif_chambre.get_text()))
            print("petit dej : " + petit_dej.get_text())
            print("phone : " + phone.get_text())
            print("bar : " + bar.get_text())
            print("Date entree : " + str(date_e.get_text()))
            print("Date sortie : " + str(date_s.get_text()))
        dialog.destroy()

# Liste des reservations
    def on_button_liste_reservations_clicked(self, widget):
        dialog = Gtk.Dialog(title="Liste des reservations", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("OK", Gtk.ResponseType.OK)
        dialog.add_button("CANCEL", Gtk.ResponseType.CANCEL)
        dialog.set_default_response(Gtk.ResponseType.OK)

        # Créer un modèle pour notre TreeView
        liststore = Gtk.ListStore(int, str, str, str, str, str, str, float, str, str, str, str, str )
        liststore.append([self.numero_chambre, self.nom, self.prenom, self.tel_client, self.classe, str(self.date_reservation), self.nuite, self.tarif_chambre, self.petit_dej, self.phone, self.bar, str(self.date_entree), str(self.date_sortie)])

        # Créer un TreeView colonnes
        treeview = Gtk.TreeView(model=liststore)
        treeviewcolumn1 = Gtk.TreeViewColumn("Numero chambre", Gtk.CellRendererText(), text=0)
        treeview.append_column(treeviewcolumn1)
        treeviewcolumn2 = Gtk.TreeViewColumn("Nom", Gtk.CellRendererText(), text=1)
        treeview.append_column(treeviewcolumn2)
        treeviewcolumn3 = Gtk.TreeViewColumn("Prenom", Gtk.CellRendererText(), text=2)
        treeview.append_column(treeviewcolumn3)
        treeviewcolumn4 = Gtk.TreeViewColumn("Telephone", Gtk.CellRendererText(), text=3)
        treeview.append_column(treeviewcolumn4)
        treeviewcolumn5 = Gtk.TreeViewColumn("Classe", Gtk.CellRendererText(), text=4)
        treeview.append_column(treeviewcolumn5)
        treeviewcolumn6 = Gtk.TreeViewColumn("Date reservation", Gtk.CellRendererText(), text=5)
        treeview.append_column(treeviewcolumn6)
        treeviewcolumn7 = Gtk.TreeViewColumn("Nuite", Gtk.CellRendererText(), text=6)
        treeview.append_column(treeviewcolumn7)
        treeviewcolumn8 = Gtk.TreeViewColumn("Tarif chambre", Gtk.CellRendererText(), text=7)
        treeview.append_column(treeviewcolumn8)
        treeviewcolumn9 = Gtk.TreeViewColumn("Peti dej", Gtk.CellRendererText(), text=8)
        treeview.append_column(treeviewcolumn9)
        treeviewcolumn10 = Gtk.TreeViewColumn("Phone", Gtk.CellRendererText(), text=9)
        treeview.append_column(treeviewcolumn10)
        treeviewcolumn11 = Gtk.TreeViewColumn("Bar", Gtk.CellRendererText(), text=10)
        treeview.append_column(treeviewcolumn11)
        treeviewcolumn12 = Gtk.TreeViewColumn("Date entree", Gtk.CellRendererText(), text=11)
        treeview.append_column(treeviewcolumn12)
        treeviewcolumn13 = Gtk.TreeViewColumn("Date sortie", Gtk.CellRendererText(), text=12)
        treeview.append_column(treeviewcolumn13)

        dialog.vbox.pack_start(treeview, False, False, 5)
        dialog.show_all()
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("OK button clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")

        dialog.destroy()

# Liste des chambres
    def on_button_liste_chambres_clicked(self, widget):
        dialog = Gtk.Dialog(title="Liste des chambres", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("OK", Gtk.ResponseType.OK)
        dialog.add_button("CANCEL", Gtk.ResponseType.CANCEL)
        dialog.set_default_response(Gtk.ResponseType.OK)

        # Créer un modèle pour notre TreeView
        liststore = Gtk.ListStore(int, str, str)
        liststore.append([self.numero_chambre, self.etat, self.classe])

        # Créer un TreeView colonnes
        treeview = Gtk.TreeView(model=liststore)
        treeviewcolumn1 = Gtk.TreeViewColumn("Numero chambre", Gtk.CellRendererText(), text=0)
        treeview.append_column(treeviewcolumn1)
        treeviewcolumn2 = Gtk.TreeViewColumn("Etat", Gtk.CellRendererText(), text=1)
        treeview.append_column(treeviewcolumn2)
        treeviewcolumn3 = Gtk.TreeViewColumn("Classe", Gtk.CellRendererText(), text=2)
        treeview.append_column(treeviewcolumn3)

        dialog.vbox.pack_start(treeview, False, False, 5)
        dialog.show_all()
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("OK button clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")

        dialog.destroy()

    # Liste des clients
    def on_button_liste_clients_clicked(self, widget):
        dialog = Gtk.Dialog(title="Liste des clients", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("OK", Gtk.ResponseType.OK)
        dialog.add_button("CANCEL", Gtk.ResponseType.CANCEL)
        dialog.set_default_response(Gtk.ResponseType.OK)

        # Créer un modèle pour notre TreeView
        liststore = Gtk.ListStore(str, str, str, str, str)
        liststore.append([self.nom, self.prenom, self.tel_client, str(self.date_entree), str(self.date_sortie)])

        # Créer un TreeView colonnes
        treeview = Gtk.TreeView(model=liststore)
        treeviewcolumn1 = Gtk.TreeViewColumn("Nom", Gtk.CellRendererText(), text=0)
        treeview.append_column(treeviewcolumn1)
        treeviewcolumn2 = Gtk.TreeViewColumn("Prenom", Gtk.CellRendererText(), text=1)
        treeview.append_column(treeviewcolumn2)
        treeviewcolumn3 = Gtk.TreeViewColumn("Telephone", Gtk.CellRendererText(), text=2)
        treeview.append_column(treeviewcolumn3)
        treeviewcolumn4 = Gtk.TreeViewColumn("Date entree", Gtk.CellRendererText(), text=3)
        treeview.append_column(treeviewcolumn4)
        treeviewcolumn5 = Gtk.TreeViewColumn("Date Sortie", Gtk.CellRendererText(), text=4)
        treeview.append_column(treeviewcolumn5)

        dialog.vbox.pack_start(treeview, False, False, 5)
        dialog.show_all()
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("OK button clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")

        dialog.destroy()

# Liste des services annexes:
    def on_button_liste_services_annexes_clicked(self, widget):
        dialog = Gtk.Dialog(title="Liste des services annexes", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("OK", Gtk.ResponseType.OK)
        dialog.add_button("CANCEL", Gtk.ResponseType.CANCEL)
        dialog.set_default_response(Gtk.ResponseType.OK)

        # Créer un modèle pour notre TreeView
        liststore = Gtk.ListStore(str, float)
        liststore.append([self.nom_service, self.tarif])

        # Créer un TreeView avec deux colonnes
        treeview = Gtk.TreeView(model=liststore)
        treeviewcolumn1 = Gtk.TreeViewColumn("Nom Service", Gtk.CellRendererText(), text=0)
        treeview.append_column(treeviewcolumn1)
        treeviewcolumn2 = Gtk.TreeViewColumn("Tarif", Gtk.CellRendererText(), text=1)
        treeview.append_column(treeviewcolumn2)

        dialog.vbox.pack_start(treeview, False, False, 5)
        dialog.show_all()
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("OK button clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")

        dialog.destroy()

# Liste des articles
    def on_button_liste_articles_clicked(self, widget):
        dialog = Gtk.Dialog(title="Liste des articles", parent=self, flags=Gtk.DialogFlags.MODAL)
        dialog.add_button("OK", Gtk.ResponseType.OK)
        dialog.add_button("CANCEL", Gtk.ResponseType.CANCEL)
        dialog.set_default_response(Gtk.ResponseType.OK)

        # Créer un modèle pour notre TreeView
        liststore = Gtk.ListStore(str, str, str, float, int, str, float)
        liststore.append([self.categorie_article, self.nom_article, self.caracteristiques, self.prix_unitaire, self.quantite_stock, str(self.date_appro), self.montant_total])

        # Créer un TreeView colonnes
        treeview = Gtk.TreeView(model=liststore)
        treeviewcolumn1 = Gtk.TreeViewColumn("Categorie", Gtk.CellRendererText(), text=0)
        treeview.append_column(treeviewcolumn1)
        treeviewcolumn2 = Gtk.TreeViewColumn("Nom article", Gtk.CellRendererText(), text=1)
        treeview.append_column(treeviewcolumn2)
        treeviewcolumn3 = Gtk.TreeViewColumn("Caracteristiques", Gtk.CellRendererText(), text=2)
        treeview.append_column(treeviewcolumn3)
        treeviewcolumn4 = Gtk.TreeViewColumn("Prix unitaire", Gtk.CellRendererText(), text=3)
        treeview.append_column(treeviewcolumn4)
        treeviewcolumn5 = Gtk.TreeViewColumn("Quantité stock", Gtk.CellRendererText(), text=4)
        treeview.append_column(treeviewcolumn5)
        treeviewcolumn6 = Gtk.TreeViewColumn("Date appro", Gtk.CellRendererText(), text=5)
        treeview.append_column(treeviewcolumn6)
        treeviewcolumn7 = Gtk.TreeViewColumn("Montant total", Gtk.CellRendererText(), text=6)
        treeview.append_column(treeviewcolumn7)

        dialog.vbox.pack_start(treeview, False, False, 5)
        dialog.show_all()
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("OK button clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")

        dialog.destroy()

# Affichage de la fenetre
class Gestion_hotel(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = Fenetre_gestion_hotel(application=self, title="Sama_hotel")
        self.window.show_all()
        self.window.present()

if __name__ == "__main__":
    app = Gestion_hotel()
    app.run(sys.argv)