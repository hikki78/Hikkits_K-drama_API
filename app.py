from flask import Flask, jsonify, request
app = Flask(__name__)

#GET
@app.route('/api/kdramas', methods=['GET'])
def get_kdramas():
    kdramas = [
        {'id': 1, 'title': 'Crash Landing on You', 'year': 2019},
        {'id': 2, 'title': 'Descendants of the Sun', 'year': 2016},
        {'id': 3, 'title': 'Goblin', 'year': 2016},
        # Add more K-dramas as needed
    ]
    return jsonify(kdramas)

#POST
@app.route('/api/kdramas', methods=['POST'])
def add_kdrama():
    kdrama = {
        'id': request.json['id'],
        'title': request.json['title'],
        'year': request.json['year']
    }
    # Perform additional validation or data processing if needed
    # Add the new K-drama to the data source (e.g., database)
    return jsonify(kdrama), 201

#Upadte operation 
@app.route('/api/kdramas/<int:kdrama_id>', methods=['PUT'])
def update_kdrama(kdrama_id):
    for kdrama in kdramas:
        if kdrama['id'] == kdrama_id:
            kdrama['title'] = request.json['title']
            kdrama['year'] = request.json['year']
            return jsonify(kdrama)
    return jsonify({'message': 'K-drama not found'}), 404

#Delete operation 
@app.route('/api/kdramas/<int:kdrama_id>', methods=['DELETE'])
def delete_kdrama(kdrama_id):
    for kdrama in kdramas:
        if kdrama['id'] == kdrama_id:
            kdramas.remove(kdrama)
            return jsonify({'message': 'K-drama deleted'})
    return jsonify({'message': 'K-drama not found'}), 404

if __name__ == '__main__':
    app.run(debug=False, port=8000)
