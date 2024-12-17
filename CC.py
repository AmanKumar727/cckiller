import flask

app = flask.Flask(__name__)

def luhn_algorithm(card_number):
    """
    Checks the validity of a credit card number using the Luhn algorithm.

    Args:
        card_number (str): The credit card number to validate.

    Returns:
        bool: True if the card number is valid, False otherwise.
    """

    def digits_of(number):
        return [int(digit) for digit in str(number)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits) + sum(map(lambda x: sum(divmod(x * 2, 10)), even_digits))
    return checksum % 10 == 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        cc_number = flask.request.form['cc_number']
        if luhn_algorithm(cc_number):
            result = "The card number appears to be valid."
        else:
            result = "The card number is invalid."
        return flask.render_template('index.html', result=result)
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
  
