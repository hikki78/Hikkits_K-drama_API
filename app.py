from flask import Flask, request, jsonify

app = Flask(__name__)

#Kdrama data
kdramas = [
    {"id": 1, "title": "Crash Landing on You", "genre": "Romance"},
    {"id": 2, "title": "Goblin", "genre": "Fantasy"},
    {"id": 3, "title": "Reply 1988", "genre": "Drama"}
]

# Route to retrieve all Kdramas
@app.route('/kdramas', methods=['GET'])
def get_kdramas():
    return jsonify(kdramas)

# Route to retrieve a specific Kdrama by ID
@app.route('/kdramas/<int:kdrama_id>', methods=['GET'])
def get_kdrama(kdrama_id):
    kdrama = next((kdrama for kdrama in kdramas if kdrama['id'] == kdrama_id), None)
    if kdrama:
        return jsonify(kdrama)
    else:
        return jsonify({"message": "Kdrama not found"}), 404

# Route to create a new Kdrama
@app.route('/kdramas', methods=['POST'])
def create_kdrama():
    new_kdrama = {
        'id': len(kdramas) + 1,
        'title': request.json['title'],
        'genre': request.json['genre']
    }
    kdramas.append(new_kdrama)
    return jsonify(new_kdrama), 201

# Route to update an existing Kdrama
@app.route('/kdramas/<int:kdrama_id>', methods=['PUT'])
def update_kdrama(kdrama_id):
    kdrama = next((kdrama for kdrama in kdramas if kdrama['id'] == kdrama_id), None)
    if kdrama:
        kdrama['title'] = request.json['title']
        kdrama['genre'] = request.json['genre']
        return jsonify(kdrama)
    else:
        return jsonify({"message": "Kdrama not found"}), 404

# Route to delete an existing Kdrama
@app.route('/kdramas/<int:kdrama_id>', methods=['DELETE'])
def delete_kdrama(kdrama_id):
    kdrama = next((kdrama for kdrama in kdramas if kdrama['id'] == kdrama_id), None)
    if kdrama:
        kdramas.remove(kdrama)
        return jsonify({"message": "Kdrama deleted"})
    else:
        return jsonify({"message": "Kdrama not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #http://localhost:5000/kdramas
