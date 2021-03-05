from flask import make_response, jsonify


def to_dictionary_array(data):
    x = []
    for dt in data:
        a = {}
        keys = dt.keys()
        for d in keys:
            a[d] = str(dt[d])
        x.append(a)
    return x


def send_response(result):
    resp = make_response(jsonify(result))
    resp.mimetype = "application/json"
    return resp
