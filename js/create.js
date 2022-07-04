function guardar() {

    let n = document.getElementById("txtNombre").value
    let d = document.getElementById("txtDni").value
    let m = document.getElementById("txtMail").value
    let t = document.getElementById("txtTelefono").value
    let niv = document.getElementById("txtNivel").value
    let c = document.getElementById("txtCurso").value

    let alumno = {
        nombre: n,
        dni: d,
        mail: m,
        telefono: t,
        nivel: niv,
        curso: c,
    }
    let url = "http://localhost:5000/alumnos"
    var options = {
        body: JSON.stringify(alumno),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")

            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar")
            console.error(err);
        })
}
