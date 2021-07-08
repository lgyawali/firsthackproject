from flask import Flask, request

app = Flask(__name__)

@app.route('/dump', methods=['POST'])
def dump():
    fname = request.form['fname']
    lname = request.form['lname']
    print(fname)
    print(lname)

    return fname + ' ' + lname

@app.route('/test', methods=['GET'])
def test():
    return "hello world!"

if __name__ == '__main__':
    app.run()