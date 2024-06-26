from models.ProductModel import ProductModel

def productMiddleWare(product):
    try:
        return ProductModel(product["proName"], product["proStock"], product["proHeight"], product["proLength"], product["proWidth"], product["proWeight"], product["proBuyPrice"], product["proSellPrice"], product["proMinStock"], product["proMaxStock"], product["proDescription"], product["proTypeID"])
    except KeyError as e:
        return None


