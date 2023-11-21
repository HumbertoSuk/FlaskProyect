-- Crear la base de datos "store"
CREATE SCHEMA store;

-- Conectar a la base de datos "store"
USE store;

-- Crear la tabla "users"
CREATE TABLE users (
    id smallint unsigned NOT NULL AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    password char(102) NOT NULL,
    fullname varchar(50),
    usertype tinyint NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);


-- Stored Procedure sp_AddUser
DELIMITER //
CREATE PROCEDURE sp_AddUser(IN pUserName VARCHAR(20), IN pPassword VARCHAR(102), IN pFullName VARCHAR(50), IN pUserType tinyint)
BEGIN
    DECLARE hashedPassword VARCHAR(255);
    SET hashedPassword = SHA2(pPassword, 256);
    
    INSERT INTO users (username, password, fullname, usertype)
    VALUES (pUserName, hashedPassword, pFullName, pUserType);
END //
DELIMITER ;

-- Stored Procedure sp_verifyIdentity
DELIMITER //
CREATE PROCEDURE sp_verifyIdentity(IN pUsername VARCHAR(20), IN pPlainTextPassword VARCHAR(20))
BEGIN
    DECLARE storedPassword VARCHAR(255);

    SELECT password INTO storedPassword FROM users
    WHERE username = pUsername COLLATE utf8mb4_unicode_ci;

    IF storedPassword IS NOT NULL AND storedPassword = SHA2(pPlainTextPassword, 256) THEN
        SELECT id, username, storedPassword, fullname, usertype FROM users
        WHERE username = pUsername COLLATE utf8mb4_unicode_ci;
    ELSE
        SELECT NULL;usersusers
    END IF;
END //
DELIMITER ;


DELIMITER //

CREATE PROCEDURE obtener_productos()
BEGIN
    SELECT * FROM productos;
END //

CREATE PROCEDURE obtener_producto_por_id(in producto_id INT)
BEGIN
    SELECT * FROM productos WHERE id = producto_id;
END //

CREATE PROCEDURE agregar_producto(in nombre VARCHAR(255), in imagen VARCHAR(255), in precio DECIMAL(10, 2))
BEGIN
    INSERT INTO productos (nombre, imagen, precio) VALUES (nombre, imagen, precio);
END //

CREATE PROCEDURE actualizar_producto(in producto_id INT, in nombre VARCHAR(255), in imagen VARCHAR(255), in precio DECIMAL(10, 2))
BEGIN
    UPDATE productos SET nombre = nombre, imagen = imagen, precio = precio WHERE id = producto_id;
END //

CREATE PROCEDURE eliminar_producto(in producto_id INT)
BEGIN
    DELETE FROM productos WHERE id = producto_id;
END //

DELIMITER ;


call sp_AddUser("juan","123","juan perez",1);
call sp_AddUser("julio","1234","julio lopez",1);
call sp_AddUser("Anna","123","Anna Talamantes",2);
call sp_verifyIdentity("juan","123");

DELETE FROM users where username="juan";