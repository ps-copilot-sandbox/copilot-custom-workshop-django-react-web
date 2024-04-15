CREATE TABLE cats (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    breed VARCHAR(50),
    age INT
);

INSERT INTO cats (name, breed, age) VALUES 
('Whiskers', 'Tabby', 2),
('Shadow', 'Maine Coon', 5),
('Molly', 'Siamese', 3),
('Oliver', 'British Shorthair', 1),
('Kitty', 'Persian', 4),
('Simba', 'Bengal', 2),
('Chloe', 'Ragdoll', 5),
('Bella', 'Sphynx', 3),
('Lucy', 'Russian Blue', 1),
('Lily', 'Scottish Fold', 4),
('Max', 'Abyssinian', 2);