from flask import Blueprint, jsonify
import random

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/rng/', methods= ["GET"])
def random_number_generator():
    output = {
        "rng" : random.randrange(1, 10)
    }
    return jsonify(output)