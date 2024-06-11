from flask import Flask, request, jsonify, render_template


app = Flask(__name__)
(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_seconds', methods=['POST'])
def receive_seconds():
    data = request.get_json()
    bank_account = data.get('bank_account')
    converted_seconds = data.get('converted_seconds')
    print(f"Received converted seconds: {converted_seconds} for bank account: {bank_account}")
    response = {"status": "success", "received_converted_seconds": converted_seconds, "bank_account": bank_account}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
