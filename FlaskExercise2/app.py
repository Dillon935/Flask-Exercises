from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <form method="get" action="/check">
        <label>Enter an integer:</label>
        <input type="text" name="number">
        <input type="submit" value="Check">
    </form>
    '''
    return html

@app.route('/check')
def check_number():
    number = request.args.get('number')
    if number is not None and number.isdigit():
        number = int(number)
        if number % 2 == 0:
            result = f"{number} is an even number."
        else:
            result = f"{number} is an odd number."
    else:
        result = f"{number} is not an integer."
    result += ' <a href="/">Go back home</a>'
    return result

if __name__ == '__main__':
    app.run(debug=True)
