from flask import Flask ,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy    # ORM manejador de DB
from flask_marshmallow import Marshmallow  # Manejo JSON

app=Flask(__name__)
CORS(app)

# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:1234@localhost/aleman'
                                                    #  user:clave@localhost/nombreBaseDatos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
ma=Marshmallow(app)

# defino las tablas (en este ejemplo tenemos sólo una, la tabla producto)
class Alumno(db.Model):                        # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   # define los campos de la tabla
    nombre=db.Column(db.String(50))
    dni=db.Column(db.Integer)
    mail=db.Column(db.String(30))
    telefono=db.Column(db.Integer)
    nivel=db.Column(db.String(4))
    curso=db.Column(db.String(50))

    def __init__(self,nombre,dni,mail,telefono,nivel,curso):   # crea el  constructor de la clase
        self.nombre=nombre                    # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.dni=dni
        self.mail=mail
        self.telefono=telefono
        self.nivel=nivel
        self.curso=curso

db.create_all()  # crea las tablas
#  ************************************************************ 

class AlumnoSchema(ma.Schema):
    class Meta:                             # Matchea los campos con los valores para generar el JSON
        fields=('id','nombre','dni','mail','telefono','nivel','curso')
alumno_schema=AlumnoSchema()            # para crear un producto
alumnos_schema=AlumnoSchema(many=True)  # multiples registros


# Programo los mapeos o las rutas / endpoint / la URL (json)
@app.route('/alumnos',methods=['GET'])
def get_Alumnos():
    all_alumnos=Alumno.query.all()           # query.all() lo hereda de db.Model
    result=alumnos_schema.dump(all_alumnos)  # .dump() lo hereda de ma.schema
    return jsonify(result)                       # Retorna un JSON con todos los productos


@app.route('/alumnos/<id>',methods=['GET'])    # Retorna un determinado producto del JSON, el que le pida 
def get_alumno(id):
    alumno=Alumno.query.get(id)
    return alumno_schema.jsonify(alumno)

@app.route('/alumno/<id>',methods=['DELETE']) # Ruta o Endpoint para ELIMINAR registros
def delete_alumno(id):
    alumno=Alumno.query.get(id)
    db.session.delete(alumno)
    db.session.commit()
    return alumno_schema.jsonify(alumno)

@app.route('/alumnos', methods=['POST'])   # Ruta o Endpoint para INSERTAR un producto nuevo
def create_alumno():
    print(request.json)                      # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    dni=request.json['dni']
    mail=request.json['mail']
    telefono=request.json['telefono']
    nivel=request.json['nivel']
    curso=request.json['curso']
    new_alumno=Alumno(nombre,dni,mail,telefono,nivel,curso)
    db.session.add(new_alumno)
    db.session.commit()
    return alumno_schema.jsonify(new_alumno)

@app.route('/alumnos/<id>' ,methods=['PUT'])  # Ruta o Endpoint para MODIFICAR un alumno
def update_alumno(id):
    alumno=Alumno.query.get(id)
    nombre=request.json['nombre']
    dni=request.json['dni']
    mail=request.json['mail']
    telefono=request.json['telefono']
    nivel=request.json['nivel']
    curso=request.json['curso']
    alumno.nombre=nombre
    alumno.dni=dni
    alumno.mail=mail
    alumno.telefono=telefono
    alumno.nivel=nivel
    alumno.curso=curso
    db.session.commit()
    return alumno_schema.jsonify(alumno)

#Las app tienen que ir arriba del programa principal y después de las clases

# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)  

