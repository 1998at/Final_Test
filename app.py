from flask import Flask, render_template, Response, jsonify, request


app = Flask(__name__)

@app.route('/data/<name>')
def say_hi(name):
    return render_template('index.html',filename=name)
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
