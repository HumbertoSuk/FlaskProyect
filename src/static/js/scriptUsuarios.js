function mostrarFormularioEdicion(id, username, fullname, usertype) {
    // Llenar el formulario con los datos actuales
    document.getElementById('editarId').value = id;
    document.getElementById('editarUsername').value = username;
    document.getElementById('editarFullname').value = fullname;
    document.getElementById('editarUsertype').value = usertype;

    // Mostrar el formulario de edición
    document.getElementById('formularioEdicion').style.display = 'block';
}

// Función para cerrar el formulario de edición
document.querySelector('.close-button').addEventListener('click', function () {
    document.getElementById('formularioEdicion').style.display = 'none';
});