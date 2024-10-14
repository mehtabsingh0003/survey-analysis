from flask import Flask, request, jsonify

app = Flask(__name__)

# Store products (in memory, no database yet)
products = []

# Route to list all products
@app.route('/products', methods=['GET'])
def list_products():
    return jsonify(products)

# Route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    product = request.json
    products.append(product)
    return jsonify({"message": "Product added successfully!"})

# Start the service on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
