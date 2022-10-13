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
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(20),
--     city VARCHAR(20)
-- );


-- CREATE TABLE pokemon_trainer(
--     p_id INT NOT NULL,
--     t_id INT NOT NULL,
--     PRIMARY KEY (p_id,t_id),
--     FOREIGN KEY (p_id) REFERENCES pokemon(id),
--     FOREIGN KEY (t_id) REFERENCES trainer(id)
-- );