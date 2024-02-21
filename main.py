from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# implementation of additional pages in flask
    # @app.route('/add-and-multiply', methods=['POST']) 
    # def add_and_multiply(): 
    #     data = request.get_json()  # retrieve the data sent from JavaScript 
    #     x = float(data.get('x', 0))  # convert to float, default to 0 if not present
    #     y = float(data.get('y', 0))
    #     result = (x + y) * 2
    #     return jsonify(result=result) 

if __name__ == '__main__':
    app.run(debug=True)