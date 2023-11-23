from .entities.users import User
from .entities.productos import Producto

class ModelUsers:
    @classmethod
    def get_by_id(cls, db, user_id):
        try:
            with db.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, username, usertype, fullname FROM users WHERE id = %s", (
                        user_id,)
                )
                row = cursor.fetchone()
                if row:
                    return User(row[0], row[1], None, row[2], row[3])
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def login(cls, db, user):
        try:
            with db.connection.cursor() as cursor:
                cursor.execute("call sp_verifyIdentity(%s, %s)",
                               (user.username, user.password))
                row = cursor.fetchone()
                if row and row[0] is not None:
                    return User(row[0], row[1], row[2], row[4], row[3])
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)

    # Métodos relacionados con productos
    @classmethod
    def obtener_todos_los_productos(cls, db):
        try:
            with db.connection.cursor() as cursor:
                cursor.callproc('obtener_productos')
                rows = cursor.fetchall()
                productos = [Producto(row[0], row[1], row[2], row[3])
                             for row in rows]
                return productos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def agregar_producto(cls, db, nombre, imagen, precio):
        try:
            with db.connection.cursor() as cursor:
                cursor.callproc('agregar_producto', (nombre, imagen, precio))
                db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtener_producto_por_id(cls, db, producto_id):
        try:
            with db.connection.cursor() as cursor:
                cursor.callproc('obtener_producto_por_id', (producto_id,))
                row = cursor.fetchone()
                if row:
                    return Producto(row[0], row[1], row[2], row[3])
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def actualizar_producto(cls, db, producto_id, nombre, imagen, precio):
        try:
            with db.connection.cursor() as cursor:
                cursor.callproc('actualizar_producto',
                                (producto_id, nombre, imagen, precio))
                db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def eliminar_producto(cls, db, producto_id):
        try:
            with db.connection.cursor() as cursor:
                cursor.callproc('eliminar_producto', (producto_id,))
                db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    # Métodos relacionados con usuarios
    @classmethod
    def obtener_todos_los_usuarios(cls, db):
        try:
            with db.connection.cursor() as cursor:
                cursor.callproc('obtener_usuarios')
                rows = cursor.fetchall()
                usuarios = [User(row[0], row[1], None, row[2], row[3])
                             for row in rows]
                return usuarios
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def agregar_usuario(cls, db, username, password, fullname, usertype):
        try:
            with db.connection.cursor() as cursor:
                cursor.callproc('agregar_usuario', (username, password, fullname, usertype))
                db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtener_usuario_por_id(cls, db, usuario_id):
        try:
            with db.connection.cursor() as cursor:
                cursor.callproc('obtener_usuario_por_id', (usuario_id,))
                row = cursor.fetchone()
                if row:
                    return User(row[0], row[1], None, row[2], row[3])
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def actualizar_usuario(cls, db, usuario_id, username, password, fullname, usertype):
        try:
            with db.connection.cursor() as cursor:
                cursor.callproc('actualizar_usuario', (usuario_id, username, password, fullname, usertype))
                db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def eliminar_usuario(cls, db, usuario_id):
        try:
            with db.connection.cursor() as cursor:
                cursor.callproc('eliminar_usuario', (usuario_id,))
                db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
