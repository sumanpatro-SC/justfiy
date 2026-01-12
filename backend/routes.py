from flask import Blueprint, request, jsonify
import json


bp = Blueprint("api", __name__)

@bp.get("/health")
def health():
    return {"status": "ok"}