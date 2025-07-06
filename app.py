from flask import Flask, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Route: Homepage
@app.route('/')
def home():
    return jsonify({"message": "Cloud Compliance Advisor is live!"})

# Main execution
if __name__ == '__main__':
    app.run(debug=True)