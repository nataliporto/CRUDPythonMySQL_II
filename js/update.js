var args = location.search.substr(1).split('&');
// lee los argumentos pasados a este formulario
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
console.log(args)
document.getElementById("txtId").value = parts[0][1]
document.getElementById("txtNombre").value = parts[1][1]
document.getElementById("txtDni").value = parts[2][1]
document.getElementById("txtMail").value = parts[3][1]
document.getElementById("txtTelefono").value = parts[4][1]
document.getElementById("txtNivel").value = parts[5][1]
document.getElementById("txtCurso").value = parts[6][1]

function modificar() {
    let id = document.getElementById("txtId").value
    let n = document.getElementById("txtNombre").value
    let d = document.getElementById("txtDni").value
    let m = document.getElementById("txtMail").value
    let t = document.getElementById('txtTelefono').value
    let niv = document.getElementById('txtNivel').value
    let c = document.getElementById('txtCurso').value

    let alumno = {
        nombre: n,
        dni: d,
        mail: m,
        telefono: t,
        nivel: niv,
        curso: c
    }
    let url = "http://localhost:5000/alumnos/"+id
    var options = {
        body: JSON.stringify(alumno),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al Modificar")
        })      
}
