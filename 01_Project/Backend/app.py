from flask import Flask, request, jsonify
from flask_cors import CORS
import chatmodel

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def chat():
    data = request.get_json()
    user_query = data.get("query", "")
    response=chatmodel.ask(user_query,temperature=0.8 )  
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(port=3000, debug=True)
