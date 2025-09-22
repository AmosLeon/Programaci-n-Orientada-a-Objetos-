document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("btn-saludar").addEventListener("click", mostrarMensajePersonalizado);

});

function mostrarMensajePersonalizado() {
    let nombre = prompt("Escribe tu nombre: ");

    if (nombre) {
        alert("Bienvenido al Sistema " + nombre);
    } else {
        alert("No se ingreso ningún nombre");
    }
}
