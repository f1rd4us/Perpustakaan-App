from app import app
from app.controllers import borrows_controller
from flask import Blueprint, request

borrows_blueprint = Blueprint("borrows_router", __name__)

@app.route("/borrows", methods=["GET"])
def showBorrow():
    return borrows_controller.shows()

@app.route("/borrows/insert", methods=["POST"])
def insertBorrow():
    params = request.json
    return borrows_controller.insert(**params)

@app.route("/borrows/status", methods=["POST"])
def updateStatus():
    params = request.json
    return borrows_controller.changeStatus(**params)