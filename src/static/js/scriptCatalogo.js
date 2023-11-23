
    // Función para mostrar un mensaje de confirmación antes de eliminar un producto
    function mostrarConfirmacion(productoId) {
        const confirmar = confirm("¿Estás seguro de que deseas eliminar este producto?");

        if (confirmar) {
            eliminarProducto(productoId);
        }
    }
    
    function mostrarFormularioEdicion(id, nombre, imagen, precio) {
        // Llenar el formulario con los datos actuales
        document.getElementById('editarId').value = id;
        document.getElementById('editarNombre').value = nombre;
        document.getElementById('editarImagen').value = imagen;
        document.getElementById('editarPrecio').value = precio;
    
        // Mostrar el formulario de edición
        document.getElementById('formularioEdicion').style.display = 'block';
        
    }
    
    // Función para cerrar el formulario de edición
    document.querySelector('.close-button').addEventListener('click', function() {
        document.getElementById('formularioEdicion').style.display = 'none';
    });