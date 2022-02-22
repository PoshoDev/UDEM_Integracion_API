from flask import Flask, jsonify, request
import jwt
from functools import wraps
import datetime as dt
import loaf
import json
from flask_cors import CORS
import requests

#lmao

app = Flask(__name__)
CORS(app)

loaf.bake(
	host = "dcrhg4kh56j13bnu.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
	user = "tk9mk9jdjgn403cs",
	pasw = "mk3iroztogmxr7gc",
	port = 3306,
	db =   "a46z1ky47vgl43sn"
)


# Tools

def error(msg):
    return jsonify({"error":msg})

def tokenize(user, pasw):
    token = jwt.encode({"usenamer":user, "password":pasw, "exp":dt.datetime.utcnow()+dt.timedelta(days=14)}, app.config["SECRET_KEY"])
    return jsonify({"token":token.decode("UTF-8")})

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get("token")
        if not token: return jsonify({"message":"No hay token."})
        try: data = jwt.decode(token, app.config["SECRET_KEY"])
        except: return jsonify({"message":"El token es invalido."})
        return f(*args, **kwargs)
    return decorated


# Routes

@app.route("/", methods=["GET"])
def home():
    data = {
        "message":"¡Estás en la página principal! Lee nuestra documentación para saber como generar un request. :)",
		"docs":"https://github.com/PoshoDev/UDEM_Integracion_API/blob/main/README.md"
        }
    return json.dumps(data)

# /user/?user=USERNAME
@app.route("/user/", methods=["GET"])
def request_user():
    query = str(request.args.get("user"))
    data = {
        "Page":"Request:User",
        "Message":f"Attempting to fetch from user: {query}"
        }
    return json.dumps(data)

# /inventario/?marca=USERNAME
@app.route("/inventario/", methods=["GET"])
def request_inventario():
    marca = str(request.args.get("marca"))
    desde = str(request.args.get("desde"))
    hasta = str(request.args.get("hasta"))
    if (desde!="None" and hasta!="None"):
        q = loaf.call("AutomovilGetFecha", desde, hasta)
        print(desde, hasta)
        print(q)
    else:
        if marca == "None": q = loaf.call("AutomovilGetAll")
        else: q = loaf.call("AutomovilGetMarca", marca)
    inventario = []
    for elem in q:
        inventario.append({
            "id":       elem[0],
            "marca":    elem[1],
            "modelo":   elem[2],
            "color":    elem[3],
            "precio":   elem[4],
            "foto":     elem[5]
        })
    return jsonify(inventario)

@app.route("/reserva/", methods=["GET"])
def request_reserva():
    # Variable retrieval
    id1 =    str(request.args.get("id1"))
    id2 =    str(request.args.get("id2"))
    id3 =    str(request.args.get("id3"))
    desde =  str(request.args.get("desde"))
    hasta =  str(request.args.get("hasta"))
    cuenta = str(request.args.get("cuenta"))
    pin =    str(request.args.get("pin"))
    # ID(rip) Check™
    autos = []
    if id1 == "None": return error("Se requiere mínimo el id de un automóvil.")
    autos.append(int(id1))
    if id2 != "None": autos.append(int(id2))
    if id3 != "None": autos.append(int(id3))
    print("AUTOS", autos)
    # Availability
    if desde=="None" or hasta=="None": return error("Se requiere un rango de fechas.")
    q = loaf.call("AutomovilGetFecha", desde, hasta)
    print("AVAILABLES")
    for elem in q:
        print(elem)
    available = []
    for elem in q: available.append(elem)
    count, suma = 0, 0
    for i in autos:
        for j in available:
            if i == j[0]:
                count += 1
                suma += j[4]
    print("LAMOAO")
    if count != len(autos): return error("Uno o más ids de autos no están disponibles para estas fechas.")
    # Date ranges
    check1 = dt.datetime.strptime(desde,'%Y-%m-%d')
    print("CHECK1", check1)
    check2 = dt.datetime.strptime(hasta,'%Y-%m-%d')
    delta = (check2 - check1).days
    print("DELTA", delta)
    if delta < 0: return error("Las fechas están en desorden.")
    suma *= delta
    # Bank request
    r = requests.put(f'http://bancoapi2.azurewebsites.net/api/Cuentas?cuenta1={cuenta}&pin={pin}&cuenta2=4255555557&dinero={suma}')
    try:
        jobject = r.json()
        banco_msg = jobject["Message"]
        print("RESPONSE:", banco_msg)
    except ValueError:
        print("ENTRE")
        usr = loaf.query(f"SELECT id FROM cliente WHERE usuario={cuenta}")
        if not usr:
            loaf.query(f"INSERT INTO cliente(usuario, nombre_completo) VALUES({cuenta}, 'Dr. Frixxxol')")
            usr = loaf.query(f"SELECT id FROM cliente WHERE usuario={cuenta}")
        print(usr, desde, hasta)
        loaf.query(f"INSERT INTO reserva(cliente, fecha_desde, fecha_hasta) VALUES({usr[0][0]}, '{desde}', '{hasta}')")
        reserva = loaf.query(f"SELECT id FROM reserva ORDER BY id DESC LIMIT 1")[0][0]
        for elem in autos: loaf.query(f"INSERT INTO reserva_unidad VALUES({reserva}, {elem})")
        ret = {
            "message": "¡Reserva exitosa!",
            "precio": suma,
            "reserva": reserva
		}
        return jsonify(ret)
    return error("Algo salió mal con el API de Bancos.")



# Main
if __name__ == "__main__":
    app.run(debug=True)
