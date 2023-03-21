CREATE TABLE Categorie(
   classe VARCHAR(50),
   tarif_normal DOUBLE,
   tarif_special DOUBLE,
   PRIMARY KEY(classe)
);

CREATE TABLE InformationHotel(
   nomHotel VARCHAR(30),
   nbre_niv INT,
   nbre_chambre INT,
   date_debut DATE,
   adresse TEXT,
   tel VARCHAR(20),
   PRIMARY KEY(nomHotel)
);

CREATE TABLE Client(
   tel VARCHAR(30),
   date_sortie DATE,
   nom VARCHAR(10),
   prenom VARCHAR(20),
   date_entree DATE,
   PRIMARY KEY(tel)
);

CREATE TABLE ser_annexes(
   nomService VARCHAR(30),
   tarif DOUBLE,
   nomHotel VARCHAR(30) NOT NULL,
   PRIMARY KEY(nomService),
   FOREIGN KEY(nomHotel) REFERENCES InformationHotel(nomHotel)
);

CREATE TABLE facture(
   idFacture INT,
   tarif_spe CURRENCY,
   tarif_chambre CURRENCY,
   tarif_pti_dej CURRENCY,
   tarif_phone CURRENCY,
   tarif_bar CURRENCY,
   total CURRENCY,
   tel VARCHAR(30) NOT NULL,
   PRIMARY KEY(idFacture),
   FOREIGN KEY(tel) REFERENCES Client(tel)
);

CREATE TABLE Gerant(
   identifiant TEXT,
   motDePasse TEXT,
   nomHotel VARCHAR(30) NOT NULL,
   PRIMARY KEY(identifiant),
   FOREIGN KEY(nomHotel) REFERENCES InformationHotel(nomHotel)
);

CREATE TABLE StockApprovisionnement(
   idArticle VARCHAR(50),
   categorieArticle VARCHAR(50),
   nomArticle VARCHAR(50),
   imageArticle ,
   caractéristiques TEXT,
   prixUnitaire CURRENCY,
   quantiteStock INT,
   dateApprovisionnement DATE,
   montantTotal CURRENCY,
   PRIMARY KEY(idArticle)
);

CREATE TABLE Chambre(
   nomHotel VARCHAR(30),
   numero VARCHAR(5),
   etat VARCHAR(1),
   classe VARCHAR(50) NOT NULL,
   PRIMARY KEY(nomHotel, numero),
   FOREIGN KEY(nomHotel) REFERENCES InformationHotel(nomHotel),
   FOREIGN KEY(classe) REFERENCES Categorie(classe)
);

CREATE TABLE reserve(
   nomHotel VARCHAR(30),
   numero VARCHAR(5),
   tel VARCHAR(30),
   classe VARCHAR(1),
   date_reser DATE,
   tarif_chambre DOUBLE,
   nuite INT,
   pti_dej LOGICAL,
   phone LOGICAL,
   bar LOGICAL,
   PRIMARY KEY(nomHotel, numero, tel),
   FOREIGN KEY(nomHotel, numero) REFERENCES Chambre(nomHotel, numero),
   FOREIGN KEY(tel) REFERENCES Client(tel)
);

CREATE TABLE prendreService(
   tel VARCHAR(30),
   nomService VARCHAR(30),
   PRIMARY KEY(tel, nomService),
   FOREIGN KEY(tel) REFERENCES Client(tel),
   FOREIGN KEY(nomService) REFERENCES ser_annexes(nomService)
);

CREATE TABLE gererStock(
   identifiant TEXT,
   idArticle VARCHAR(50),
   PRIMARY KEY(identifiant, idArticle),
   FOREIGN KEY(identifiant) REFERENCES Gerant(identifiant),
   FOREIGN KEY(idArticle) REFERENCES StockApprovisionnement(idArticle)
);

CREATE TABLE generer(
   idFacture INT,
   identifiant TEXT,
   PRIMARY KEY(idFacture, identifiant),
   FOREIGN KEY(idFacture) REFERENCES facture(idFacture),
   FOREIGN KEY(identifiant) REFERENCES Gerant(identifiant)
);
