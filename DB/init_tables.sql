-- CREATE DATABASE Poke_tracker;
USE Poke_tracker;

-- CREATE TABLE pokemon(
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     p_name VARCHAR(50),
--     -- type VARCHAR(50),
--     height INT,
--     weight INT
-- );

-- CREATE TABLE trainer(
--     name VARCHAR(20) NOT NULL PRIMARY KEY,
--     city VARCHAR(20)
-- );

-- CREATE TABLE pokemon_trainer(
--     p_id INT NOT NULL,
--     t_name VARCHAR(20) NOT NULL,
--     PRIMARY KEY (p_id,t_name),
--     FOREIGN KEY (p_id) REFERENCES pokemon(id),
--     FOREIGN KEY (t_name) REFERENCES trainer(name)
-- );

-- CREATE TABLE types(
--     id INT NOT NULL PRIMARY KEY,
--     t_name VARCHAR(20) NOT NULL
-- );

-- CREATE TABLE pokemon_type(
--     p_id INT NOT NULL,
--     p_type VARCHAR(20) NOT NULL,
--     FOREIGN KEY (p_id) REFERENCES pokemon(id),
--     PRIMARY KEY (p_id,p_type)
-- );

-- INSERT INTO pokemon_type VALUES (133,"normal")
-- SELECT * FROM pokemon_type


-- INSERT INTO pokemon VALUES (222,"yamna",10,10)
-- INSERT INTO pokemon_type VALUES (222,"bug")
-- INSERT INTO pokemon_type VALUES (222,"flying")




-- SELECT * FROM pokemon 
-- SELECT * FROM pokemon_type
-- SELECT p_type FROM pokemon_type WHERE p_id = 193
-- SELECT * FROM pokemon_trainer WHERE t_name='Archie'


-- DELETE FROM pokemon_trainer WHERE (pokemon_trainer.p_id = 21 AND pokemon_trainer.t_name = "Archie")

-- SELECT * FROM pokemon_trainer WHERE (pokemon_trainer.p_id = 21 AND pokemon_trainer.t_name = "Archie");