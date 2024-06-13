from flask import Flask
from flask_cors import CORS

from config.config import config
from database.database import configure_database
from database.database import db
import os

# Routes
from routes.DealersRoutes import setupRoutesDealer
from routes.ShoppingsRoutes import setupRoutesShopping
from routes.SalesRoutes import setupRoutesSales
from routes.ProductsRoutes import setupRoutesProduct
from routes.ArticlesRoutes import setupRoutesArticle
from routes.TypesRoutes import setupRoutesType
from routes.AdminUserRoutes import setupRoutesAdminUser
from routes.ClientsRoutes import setupRoutesClients
from routes.AuthRoutes import setupRoutesAuth
from routes.EmailRoutes import setupRoutesEmail
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:4200"}})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS, GET, PUT, DELETE')
    response.headers.add('X-DNS-Prefetch-Control', 'off')
    return response


UPLOAD_FOLDER = os.path.join(os.getcwd(),'images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def init_app(config):
    # Configuration
    app.config.from_object(config)

    configure_database(app)
    setupRoutesDealer(app)
    setupRoutesShopping(app)
    setupRoutesSales(app)
    setupRoutesProduct(app)
    setupRoutesArticle(app)
    setupRoutesType(app)
    setupRoutesAdminUser(app)
    setupRoutesClients(app)
    setupRoutesAuth(app)
    setupRoutesEmail(app)

    CORS(app)

    return app

configuration = config['development']
app = init_app(configuration)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()