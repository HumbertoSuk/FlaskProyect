
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);


-- PROCEDIMIENTOS PARA PRODUCTOS:
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


-- PROCEDIMIENTOS PARA USUARIOS:

USE store;
DELIMITER //

CREATE PROCEDURE obtener_usuarios()
BEGIN
    SELECT * FROM users;
END //

CREATE PROCEDURE obtener_usuario_por_id(in usuario_id INT)
BEGIN
    SELECT * FROM users WHERE id = usuario_id;
END //

CREATE PROCEDURE agregar_usuario(in username VARCHAR(20), in password CHAR(102), in fullname VARCHAR(50), in usertype TINYINT)
BEGIN
    INSERT INTO users (username, password, fullname, usertype) VALUES (username, password, fullname, usertype);
END //

CREATE PROCEDURE actualizar_usuario(in usuario_id INT, in username VARCHAR(20), in password CHAR(102), in fullname VARCHAR(50), in usertype TINYINT)
BEGIN
    UPDATE users SET username = username, password = password, fullname = fullname, usertype = usertype WHERE id = usuario_id;
END //

CREATE PROCEDURE eliminar_usuario(in usuario_id INT)
BEGIN
    DELETE FROM users WHERE id = usuario_id;
END //

DELIMITER ;

