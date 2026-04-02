from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show')
def show():
    name = request.args.get('name', 'Little Artist')
    return render_template('show.html', name=name)

@app.route('/result')
def result():
    name = request.args.get('name', 'Friend')
    return render_template('result.html', name=name)

if __name__ == '__main__':
    # host='0.0.0.0' allows your phone to connect via QR
    app.run(host='0.0.0.0', port=5000, debug=True)