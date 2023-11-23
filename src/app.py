from flask import Flask, redirect, render_template, request, url_for, flash, abort
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from functools import wraps
from config import config
from models.ModelUsers import ModelUsers
from models.entities.users import User

app = Flask(__name__)
app.config.from_object(config['development'])
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUsers.get_by_id(db, id)


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        # Verificar si el usuario está autenticado y es un administrador
        if not current_user.is_authenticated or current_user.usertype != 1:
            abort(403)  # Acceso prohibido
        return func(*args, **kwargs)

    return decorated_view


@app.route("/")
def index():
    return redirect("login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        print(
            f"Intento de inicio de sesión: Usuario - {usuario}, Contraseña - {contrasena}")

        user = User(0, usuario, contrasena, 0)
        logged_user = ModelUsers.login(db, user)

        if logged_user is not None:
            print(f"Usuario autenticado: {logged_user}")

            login_user(logged_user)
            return redirect(url_for("principal"))
        else:
            flash("Acceso rechazado. Verifica usuario y contraseña.")
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")


@app.route("/principal")
@login_required
def principal():
    return render_template("main.html")


@app.route("/acerca")
@login_required
def acerca():
    return render_template("Acerca_de.html")


@app.route("/catalogo")
@login_required
@admin_required
def catalogo():
    return render_template("catalogo.html")


@app.route("/tienda")
@login_required
def tienda():
    return render_template("tienda.html")


@app.route("/ticket")
@login_required
def ticket():
    return render_template("ticket.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/agregar_producto", methods=["POST"])
@login_required
@admin_required
def agregar_producto():
    if request.method == "POST":
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        imagen = request.form['imagen']
        precio = request.form['precio']

        # Llamar al método para agregar el producto
        ModelUsers.agregar_producto(db, nombre, imagen, precio)

    mostrar_productos()
    return redirect(url_for("catalogo"))


@app.route("/editar_producto/<int:id>", methods=["POST"])
@login_required
@admin_required
def editar_producto(id):
    if request.method == "POST":
<<<<<<< HEAD
        # Obtener datos del formulario de edición
        nuevo_nombre = request.form.get("nombre")
        nueva_imagen = request.form.get("imagen")
        nuevo_precio = request.form.get("precio")

        ModelUsers.actualizar_producto(
            db, id, nuevo_nombre, nueva_imagen, nuevo_precio)

    # Redireccionar a la página de catálogo o a donde sea apropiado
=======
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        imagen = request.form['imagen']
        precio = request.form['precio']

        # Llamar al método para actualizar el producto
        ModelUsers.actualizar_producto(db, id, nombre, imagen, precio)

>>>>>>> 03cb2531b5e47d75c30c35cf6a1d346054a87a85
    return redirect(url_for("catalogo"))


@app.route("/eliminar_producto/<int:id>", methods=["POST"])
@login_required
@admin_required
def eliminar_producto(id):
    # Llamar al método para eliminar el producto
    ModelUsers.eliminar_producto(db, id)

    return redirect(url_for("catalogo"))


@app.route('/mostrar_productos')
def mostrar_productos():
    try:
        # Obtén todos los productos desde la base de datos
        productos = ModelUsers.obtener_todos_los_productos(db)

        # Imprime productos para depuración
        print(productos)

        # Renderiza la plantilla y pasa la lista de productos
        return render_template('catalogo.html', productos=productos)
    except Exception as ex:
        # Maneja la excepción según tus necesidades
        return f"Error: {ex}"


<<<<<<< HEAD
# Rutas y lógica para la gestión de usuarios
@app.route("/mostrar_usuarios")
@login_required
@admin_required
def mostrar_usuarios():
    try:
        # Obtén todos los usuarios desde la base de datos
        usuarios = ModelUsers.obtener_todos_los_usuarios(db)

        # Imprime usuarios para depuración
        print(usuarios)

        # Renderiza la plantilla y pasa la lista de usuarios
        return render_template('usuarios.html', usuarios=usuarios)
    except Exception as ex:
        # Maneja la excepción según tus necesidades
        return f"Error: {ex}"


@app.route("/agregar_usuario", methods=["POST"])
@login_required
@admin_required
def agregar_usuario():
    if request.method == "POST":
        # Obtener los datos del formulario
        username = request.form['username']
        password = request.form['password']
        fullname = request.form['fullname']
        usertype = request.form['usertype']

        # Llamar al método para agregar el usuario
        ModelUsers.agregar_usuario(db, username, password, fullname, usertype)

    mostrar_usuarios()
    return redirect(url_for("mostrar_usuarios"))


@app.route("/editar_usuario/<int:id>", methods=["POST"])
@login_required
@admin_required
def editar_usuario(id):
    if request.method == "POST":
        # Obtener los datos del formulario
        username = request.form['username']
        password = request.form['password']
        fullname = request.form['fullname']
        usertype = request.form['usertype']

        # Llamar al método para actualizar el usuario
        ModelUsers.actualizar_usuario(
            db, id, username, password, fullname, usertype)

    return redirect(url_for("mostrar_usuarios"))


@app.route("/eliminar_usuario/<int:id>", methods=["POST"])
@login_required
@admin_required
def eliminar_usuario(id):
    # Llamar al método para eliminar el usuario
    ModelUsers.eliminar_usuario(db, id)

    return redirect(url_for("mostrar_usuarios"))


=======
>>>>>>> 03cb2531b5e47d75c30c35cf6a1d346054a87a85
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
