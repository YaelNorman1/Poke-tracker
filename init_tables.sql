-- CREATE DATABASE Poke_tracker;
USE Poke_tracker;

-- CREATE TABLE pokemon(
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     p_name VARCHAR(50),
--     type VARCHAR(50),
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
--     PRIMARY KEY (p_id,R),
--     FOREIGN KEY (p_id) REFERENCES pokemon(id),
--     FOREIGN KEY (t_name) REFERENCES trainer(name)
-- );

INSERT IGNORE INTO trainer VALUES("ELIK","BSheva");

-- SELECT * FROM trainer;

-- IF EXISTS (SELECT name FROM trainer WHERE name = 'ash')
-- BEGIN
-- END
-- ELSE
-- BEGIN
-- SELECT * FROM trainer
-- END