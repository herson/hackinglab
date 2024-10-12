from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Vulnerable API'

@app.route('/vulnerable', methods=['GET'])
def vulnerable():
    user_input = request.args.get('input')
    # Vulnerable to code injection
    eval(user_input)
    return 'Executed'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
