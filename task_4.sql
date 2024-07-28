-- Use the ALX book store database
USE alx_book_store;

-- Print the full description of the 'books' table
SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    DATA_TYPE,
    CHARACTER_MAXIMUM_LENGTH,
    IS_NULLABLE,
    COLUMN_KEY,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_NAME = 'Books'
ORDER BY
    ORDINAL_POSITION;
