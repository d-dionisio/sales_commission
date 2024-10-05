from flask import Blueprint, request, jsonify
from src.models.sales import Sales
from database import db
from datetime import datetime

sales_route_bp = Blueprint("sales_route_bp", __name__)

@sales_route_bp.route("/sales", methods=["POST"])
def create_new_sale():
    data = request.json
    new_sale = Sales(customer=data['customer'], telephone=data['telephone'], value=data['value'], flat=data['flat'], insurance=data['insurance'])

    db.session.add(new_sale)
    db.session.commit()

    return jsonify({"message": "Venda criada com sucesso!"})

@sales_route_bp.route("/sales", methods=["GET"])
def get_sales():
    sales = Sales.query.all()

    sales_list = []

    for sale in sales:
        sales_list.append({
            "id": sale.id,
            "customer": sale.customer,
            "flat": sale.flat,
            "insurance": sale.insurance,
            "date": sale.create_at.strftime("%d/%m/%Y")
        })

    return sales_list