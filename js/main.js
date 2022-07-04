if (document.getElementById("app")) {
    const app = new Vue({
        el: "#app",
        data: {
            alumnos: [],
            errored: false,
            loading: true
        },
        created() {
            var url = 'http://localhost:5000/alumnos'
            this.fetchData(url)
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.alumnos = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })
            },
            eliminar(alumno) {
                const url = 'http://localhost:5000/alumno/' + alumno;
                var options = {
                    method: 'DELETE',
                }
                fetch(url, options)
                    .then(res => res.text()) // or res.json()
                    .then(res => {
                        location.reload();
                    })
            }
        }
    })
}
