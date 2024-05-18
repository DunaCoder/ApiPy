from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify ({"messsage": 'pong!'})

@app.route('/products')
def get_products():  # Assuming you have a function to retrieve products
    # Add your product retrieval logic here
    return jsonify({"products": products})  # Replace with actual product data


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    # recorre y compara si encuntra el que coincida con el nombre lo devuelve
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product":  productsFound[0]})
    else:
        return jsonify({"message":"no encontrado :("})
    
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": 10
    }
    products.append(new_product)
    return ({"message":"articulo agregado", "products": products})


@app.route('/products/<string:product_name>', methods =["PUT"])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name ]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "producto actualizado",
            "product" : productsFound[0]
        })
    return jsonify({"message": "porducto no encontrado"})

@app.route('/products/<string:product_name>', methods=['DELETE'])

def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            "message": "producto eliminado",
            "products": products
        })
    return jsonify({
        "message": "prducto no econtrado "
    })


if __name__ == '__main__' :
    app.run(debug = True, port=40000)