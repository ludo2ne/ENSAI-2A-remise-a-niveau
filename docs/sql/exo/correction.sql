-- Quelques elemnts de correction


SELECT * 
  FROM echecs.joueur j;
 
SELECT * 
  FROM echecs.joueur j
 ORDER BY elo DESC;
 
 SELECT * 
  FROM echecs.joueur j
 WHERE elo <= 2000
   AND UPPER(prenom) LIKE '%E%';

DELETE FROM echecs.joueur 
 WHERE pseudo = 'marc78';
 
DELETE FROM echecs.joueur
 WHERE id_joueur = 20;
-- impossible de supprimer car ce joueur est référencé en tant qu'arbitre de tounoi
-- dans la table tournoi, la colonne id_arbitre référence des joueurs
-- pour supprimer ce joueur, il ne faut plus que l'id_joueur 20 apparaisse à cet endroit
 
SELECT * FROM echecs.tournoi t
 
SELECT * 
  FROM echecs.joueur j 
 WHERE id_arbitre_grade IS NOT NULL;
 

ALTER TABLE echecs.joueur
ADD COLUMN est_arbitre boolean DEFAULT false;

UPDATE echecs.joueur
SET est_arbitre = true
WHERE id_arbitre_grade IS NOT NULL;


SELECT j.nom,
       j.prenom,
       ag.nom
  FROM echecs.joueur j
  JOIN echecs.arbitre_grade ag USING(id_arbitre_grade);
  --JOIN echecs.arbitre_grade ag ON j.id_arbitre_grade = ag.id_arbitre_grade
  
SELECT j.nom,
       j.prenom,
       ag.nom
  FROM echecs.joueur j
  LEFT JOIN echecs.arbitre_grade ag USING(id_arbitre_grade);
  
SELECT COUNT(1)
  FROM echecs.joueur j
  JOIN echecs.arbitre_grade ag USING(id_arbitre_grade);
  
    
SELECT ag.nom AS grade,
       AVG(j.elo),
       COUNT(1)
  FROM echecs.joueur j
  JOIN echecs.arbitre_grade ag USING(id_arbitre_grade)
 GROUP BY ag.nom
 HAVING AVG(j.elo) > 2000;
 
 
 SELECT t.nom,
        a.nom || ' ' || a.prenom AS arbitre,
        c.nom AS cadence,
        COUNT(1) AS nb_joueurs,
        MAX(j.elo) AS max_elo
   FROM echecs.tournoi t
   JOIN echecs.participant p USING(id_tournoi)
   JOIN echecs.joueur j USING(id_joueur)
   JOIN echecs.joueur a ON t.id_arbitre = a.id_joueur
   JOIN echecs.cadence c USING(id_cadence)
  WHERE c.nom = 'lente'
 GROUP BY 1, 2, 3
 ORDER BY 3
  
 INSERT INTO echecs.joueur(pseudo, nom, prenom, elo, mail, id_arbitre_grade)
VALUES('mich', 'Dupont', 'Micheline', 1999, 'mich@example.com', null);
