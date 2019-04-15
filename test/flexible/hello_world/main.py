import logging
import os
import cloudstorage as gcs
import webapp2

from google.appengine.api import app_identity

from flask import Flask, render_template, url_for, request


app = Flask(__name__)

def get(self):
  bucket_name = os.environ.get('BUCKET_NAME',
                               app_identity.get_default_gcs_bucket_name())

  self.response.headers['Content-Type'] = 'text/plain'
  self.response.write('Demo GCS Application running from Version: '
                      + os.environ['CURRENT_VERSION_ID'] + '\n')
  self.response.write('Using bucket name: ' + bucket_name + '\n\n')

    
def create_file(self, filename):
  """Create a file.

  The retry_params specified in the open call will override the default
  retry params for this particular file handle.

  Args:
    filename: filename.
  """
  self.response.write('Creating file %s\n' % filename)

  write_retry_params = gcs.RetryParams(backoff_factor=1.1)
  gcs_file = gcs.open(filename,
                      'w',
                      content_type='text/plain',
                      options={'x-goog-meta-foo': 'foo',
                               'x-goog-meta-bar': 'bar'},
                      retry_params=write_retry_params)
  gcs_file.write('abcde\n')
  gcs_file.write('f'*1024*4 + '\n')
  gcs_file.close()
  self.tmp_filenames_to_clean_up.append(filename)
    
    
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

 
@app.route('/upload2')
def fileupload(num = None):
    return render_template('upload2.html', num = num)

@app.route('/showupload',methods=['POST'])
def showtext(num=None):
    if request.method == 'POST':
        temp = request.form['num']
    return redirect(url_for('fileupload', num = temp))
  
  
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
