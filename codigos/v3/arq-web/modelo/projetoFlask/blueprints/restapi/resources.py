from flask import jsonify, abort
from flask_restful import Resource
from projetoFlask.ext.database import Product

class ProductResource(Resource):
    def get(self):
        products = Product.query.all() or abort(204)
        return jsonify(
            {'products':[ 
                {
                    'id':product.id,
                    'name':product.name,
                    'description':product.description,
                    'price':product.price,
                    'type': product.type.description
                }
                for product in products
            ]}
        )

class ProductItemResource(Resource):
    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first() or abort(
            404
        )
        
        return jsonify(product.to_dict())