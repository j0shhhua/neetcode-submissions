CREATE TABLE products(
    name TEXT NOT NULL DEFAULT 'Unknown',
    price INT NOT NULL,
    quantity INT DEFAULT 0
);






-- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'products';
