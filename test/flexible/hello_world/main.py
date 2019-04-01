
import logging

from flask import Flask, render_template, url_for, request


app = Flask(__name__)


@app.route('/')
def hello(name=None):
    """Return a friendly HTTP greeting."""
    return render_template("test.html", name=name)

@app.route('/')
@app.route('/calc/<num1>&<num2>&<ope>')
def calc(num1,num2,ope):
    a = int(num1)
    b = int(num2)
    if ope =='add':
        c = a + b
        ope = '+'
        c = str(c)
    if ope =='sub':
        c = a - b
        ope = '-'
        c = str(c)
    if ope =='multi':
        c = a * b
        ope = '×'
        c = str(c)
    if ope =='div':
        c = a / b
        ope = '÷'
        c = str(c)
    return render_template('test_2.html', num1=num1, num2=num2, ope=ope, out = c)




@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
