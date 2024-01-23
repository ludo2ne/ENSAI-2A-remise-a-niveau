------------------------------------------------------
-- Suppression puis recreation complete du schema
------------------------------------------------------

--DROP SCHEMA IF EXISTS echecs CASCADE;
CREATE SCHEMA echecs;


------------------------------------------------------
-- Creation de la arbitre_grade
------------------------------------------------------

CREATE TABLE echecs.arbitre_grade (
  id_arbitre_grade INT PRIMARY KEY,
  nom VARCHAR(50) NOT NULL
);

-- Insertion des donnees dans la table
INSERT INTO echecs.arbitre_grade (id_arbitre_grade, nom)
VALUES
  (1, 'Arbitre Jeune'),
  (2, 'Arbitre Club'),
  (3, 'Arbitre Open'),
  (4, 'Arbitre Elite');


------------------------------------------------------
-- Creation de la table joueur
------------------------------------------------------

CREATE TABLE echecs.joueur (
    id_joueur serial4 NOT NULL,
    pseudo text NULL,
    nom text NOT NULL,
    prenom text NOT NULL,
    elo int4 NULL,
    mail text NULL,
    id_arbitre_grade int4 NULL,
    CONSTRAINT joueur_pkey PRIMARY KEY (id_joueur),
    CONSTRAINT joueur_pseudo_key UNIQUE (pseudo)
);

-- Creation d une cle etrangere referencant la table arbitre_grade
ALTER TABLE echecs.joueur ADD CONSTRAINT fk_arbitre_grade FOREIGN KEY(id_arbitre_grade) REFERENCES echecs.arbitre_grade(id_arbitre_grade);

-- Insertion des donnees dans la table
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(1, 'johndoe', 'Doe', 'John', 2000, 'john.doe@example.com', null);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(2, 'janedoe', 'Doe', 'Jane', 1800, 'jane.doe@example.com', 2);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(3, 'alice88', 'Lefevre', 'Alice', 2200, 'alice.lefevre@example.com', null);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(4, 'bobsmith', 'Smith', 'Bob', 1900, 'bob.smith@example.com', null);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(5, 'lucyf', 'Fournier', 'Lucy', 2100, 'lucy.fournier@example.com', 3);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(6, 'max78', 'Girard', 'Maxime', 2400, 'maxime.girard@example.com', null);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(7, 'sarah03', 'Simon', 'Sarah', 1700, 'sarah.simon@example.com', 3);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(8, 'thomas21', 'Dupont', 'Thomas', 2300, 'thomas.dupont@example.com', null);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(9, 'emily', 'Moreau', 'Emily', 2000, 'emily.moreau@example.com', null);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(10, 'alexander', 'Leroy', 'Alexander', 2100, 'alexander.leroy@example.com', 4);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(11, 'mike94', 'Martin', 'Mike', 1900, 'mike.martin@example.com', null);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(12, 'sophie', 'Gagnon', 'Sophie', 1800, 'sophie.gagnon@example.com', 2);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(13, 'kevin', 'Tremblay', 'Kevin', 2200, 'kevin.tremblay@example.com', null);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(14, 'laurab', 'Boucher', 'Laura', 2100, 'laura.boucher@example.com', null);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(15, 'paul23', 'Rousseau', 'Paul', 2000, 'paul.rousseau@example.com', 2);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(16, 'sylvie', 'Giroux', 'Sylvie', 2300, 'sylvie.giroux@example.com', null);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(17, 'nicolas', 'Côté', 'Nicolas', 1900, 'nicolas.cote@example.com', null);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(18, 'julie', 'Morin', 'Julie', 2100, 'julie.morin@example.com', 3);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(19, 'marc78', 'Lavoie', 'Marc', 2000, 'marc.lavoie@example.com', null);
INSERT INTO echecs.joueur(id_joueur, pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES(20, 'sandra', 'Bélanger', 'Sandra', 2200, 'sandra.belanger@example.com', 4);


------------------------------------------------------
-- Creation de la table cadence
------------------------------------------------------

CREATE TABLE echecs.cadence (
  id_cadence  INT           PRIMARY KEY,
  nom         VARCHAR(50)   NOT NULL
);

-- Insertion des données dans la table
INSERT INTO echecs.cadence (id_cadence, nom)
VALUES
  (1, 'lente'),
  (2, 'rapide'),
  (3, 'blitz');


------------------------------------------------------
-- Creation de la table tournoi
------------------------------------------------------

CREATE TABLE echecs.tournoi (
    id_tournoi serial4 NOT NULL,
    id_arbitre int4 NULL,
    nom text NULL,
    debut date NULL,
    fin date NULL,
    nb_rondes int4 NULL,
    id_cadence int4 NOT NULL,
    CONSTRAINT tournoi_pkey PRIMARY KEY (id_tournoi),
    CONSTRAINT fk_tournoi_arbitre FOREIGN KEY (id_arbitre) REFERENCES echecs.joueur(id_joueur),
    CONSTRAINT fk_tournoi_cadence FOREIGN KEY (id_cadence) REFERENCES echecs.cadence(id_cadence)
);

INSERT INTO echecs.tournoi (id_tournoi, id_arbitre, nom, debut, fin, nb_rondes, id_cadence) 
VALUES(1, 20, 'Tournoi d''été', '2023-07-01', '2023-07-08', 9, 1);
INSERT INTO echecs.tournoi (id_tournoi, id_arbitre, nom, debut, fin, nb_rondes, id_cadence) 
VALUES(2, 20, 'Rapide de printemps', '2023-04-15', '2023-04-15', 7, 2);
INSERT INTO echecs.tournoi (id_tournoi, id_arbitre, nom, debut, fin, nb_rondes, id_cadence) 
VALUES(3, 18, 'Tournoi d''hiver', '2022-12-01', '2022-12-05', 7, 1);
INSERT INTO echecs.tournoi (id_tournoi, id_arbitre, nom, debut, fin, nb_rondes, id_cadence) 
VALUES(4, 20, 'Rapide d''automne', '2023-09-30', '2023-09-30', 9, 2);
INSERT INTO echecs.tournoi (id_tournoi, id_arbitre, nom, debut, fin, nb_rondes, id_cadence) 
VALUES(5, 18, 'Blitz de Noël', '2023-12-20', '2023-12-25', 9, 3);
INSERT INTO echecs.tournoi (id_tournoi, id_arbitre, nom, debut, fin, nb_rondes, id_cadence) 
VALUES(6, 18, 'Blitz de la Galette', '2024-01-06', '2024-01-06', 9, 3);


------------------------------------------------------
-- Creation de la table participant
------------------------------------------------------

CREATE TABLE echecs.participant (
  id_tournoi INT,
  id_joueur INT,
  PRIMARY KEY (id_tournoi, id_joueur),
  FOREIGN KEY (id_tournoi) REFERENCES echecs.tournoi(id_tournoi),
  FOREIGN KEY (id_joueur) REFERENCES echecs.joueur(id_joueur)
);

-- Insertion des données dans la table
--INSERT INTO echecs.participant (id_tournoi, id_joueur)
--SELECT DISTINCT
--  (FLOOR(RANDOM() * 6) + 1) AS id_tournoi,
--  (FLOOR(RANDOM() * 17) + 1) AS id_joueur
--FROM generate_series(1, 100)
--ORDER BY 1, 2

INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(1, 2);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(1, 3);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(1, 4);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(1, 5);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(1, 7);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(1, 10);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(1, 11);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(1, 13);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(1, 15);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(1, 16);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(2, 1);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(2, 2);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(2, 3);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(2, 5);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(2, 7);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(2, 9);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(2, 11);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(2, 13);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(2, 14);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(2, 15);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(2, 16);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(2, 17);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(3, 1);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(3, 8);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(3, 9);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(3, 10);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(3, 11);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(3, 12);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(3, 13);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(3, 14);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(3, 15);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(3, 16);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(4, 1);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(4, 2);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(4, 5);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(4, 6);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(4, 7);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(4, 10);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(4, 11);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(4, 14);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(4, 15);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(4, 16);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(4, 17);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(5, 1);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(5, 2);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(5, 3);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(5, 4);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(5, 5);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(5, 6);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(5, 7);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(5, 8);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(5, 9);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(5, 10);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(5, 14);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(5, 15);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(5, 16);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(6, 1);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(6, 4);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(6, 5);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(6, 6);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(6, 8);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(6, 9);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(6, 10);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(6, 11);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(6, 12);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(6, 15);
INSERT INTO echecs.participant (id_tournoi, id_joueur) VALUES(6, 16);
