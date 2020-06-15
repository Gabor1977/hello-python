from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    print(request.__dict__)
    print(request.environ.get('HTTP_CF_CONNECTING_IP', request.remote_addr))
    return "HTTP_CF_CONNECTING_IP + request _dic_ line active v3.8!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
