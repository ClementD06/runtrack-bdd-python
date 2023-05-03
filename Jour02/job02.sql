-- Création de la table "etage"
CREATE TABLE etage (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255),
  numero INT,
  superficie INT
);

-- Création de la table "salles"
CREATE TABLE salles (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255),
  id_etage INT,
  capacite INT,
  FOREIGN KEY (id_etage) REFERENCES etage(id)
);

-- Affichage dans le terminal
-- +------------------------+
-- | Tables_in_laplateforme |
-- +------------------------+
-- | etage                  |
-- | etudiants              |
-- | salles                 |
-- +------------------------+