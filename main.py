from flask import Flask, jsonify, request

# Inicializamos la aplicación que será el host de nuestra API
app = Flask(__name__)

# ----------------------------------------------------
# Endpoint 1: Root (Raíz)
# Método por defecto: GET
# ----------------------------------------------------
@app.route('/')
def root():
    return "holaaaa"

# ----------------------------------------------------
# Endpoint 2: Obtener un usuario por ID
# Método por defecto: GET
# ----------------------------------------------------
@app.route('/users/<user_id>')
def get_user(user_id):
    # Simulamos los datos que normalmente vendrían de una base de datos
    user = {
        "id": user_id, 
        "name": "test", 
        "telefono": "999 666 333"
    }
    
    # Verificamos si nos pasan un parámetro extra a través de la URL (Query Params)
    query = request.args.get("query")
    if query:
        user["query"] = query
        
    # Retornamos la información en formato JSON junto con un código de éxito 200
    return jsonify(user), 200

# ----------------------------------------------------
# Endpoint 3: Crear un nuevo usuario
# Método explícito: POST
# ----------------------------------------------------
@app.route('/users', methods=['POST'])
def create_user():
    # Obtenemos la información (el Body en formato JSON) que envía el cliente
    data = request.get_json()
    
    # Agregamos un campo de estado para confirmar la acción
    data["status"] = "user created"
    
    # Retornamos la misma data y un código 201 que significa "Creado"
    return jsonify(data), 201

# ----------------------------------------------------
# Ejecución del servidor en modo de desarrollo
# ----------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)