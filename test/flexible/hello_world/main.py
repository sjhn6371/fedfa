
import logging

from flask import Flask, render_template, url_for, request


app = Flask(__name__)


class calculator:

    def __init__(self):
        self.ac=''

    def processing(self, num1, num2, ope):
        k = ope
        equ = '='
        if k == 'add':
            result = float(num1) + float(num2)
            if result - int(result)==0:
                result = int(result)
            k = '+'

        elif k == 'sub':
            result = float(num1) - float(num2)
            if result - int(result)==0:
                result = int(result)
            k = '-'

        elif k == 'multi':
            result = float(num1) * float(num2)
            if result - int(result)==0:
                result = int(result)
            k = '×'

        elif k == 'div':
            result = float(num1) / float(num2)
            if result - int(result)==0:
                result = int(result)
            k = '÷'
        else:
            return 'Error. Check your operation'

        self.ac = str(num1) + k + str(num2) + ' ' + equ + ' ' + str(result)

        return self.ac


@app.route('/')
def hello(name=None):
    """Return a friendly HTTP greeting."""
    return render_template("test.html", name=name)


@app.route('/')
@app.route('/calc/<num1>&<num2>&<ope>')
def calc(num1,num2,ope):
    ca1 = calculator()
    return render_template('test_2.html', out = ca1.processing(num1, num2, ope))


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
