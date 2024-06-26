from flask import Blueprint
from controllers.ProductController import getProducts, getProduct, postProduct, putProduct, dropProduct,download_file, getProductsBrief, getProductsStatus


def setupRoutesProduct(app):
    bp = Blueprint('products', __name__)

    # Rutas para CRUD de items productos
    bp.route('/dwimg/<string:imgName>', methods=['GET'])(download_file)
    bp.route('/products', methods=['GET'])(getProducts)
    bp.route('/products/<string:productId>', methods=['GET'])(getProduct)
    bp.route('/products', methods=['POST'])(postProduct)
    bp.route('/products/<string:productId>', methods=['PUT'])(putProduct)
    bp.route('/products/<string:productId>', methods=['DELETE'])(dropProduct)
    bp.route('/products/brief', methods=['GET'])(getProductsBrief)
    bp.route('/products/status', methods=['GET'])(getProductsStatus)
    
    app.register_blueprint(bp)
    


