from flask import Flask, request
from waitress import serve
from query import query_card_detail
app = Flask(__name__, static_folder='.')
# app.config['DEBUG'] = True

@app.route('/')
def hello_world():
   return app.send_static_file("QueryPage.html")

@app.route('/Index')
def index():
   return 'hello'

@app.route('/Query', methods=['GET', 'POST'])
def query():
   if request.method == 'POST':
      userName = request.form['userName']
      password = request.form['password']
      return query_card_detail(userName, password)
      # return '''
      #    <h1>UserName is {}</h1>
      #    <h1>Password is {}</h1>
      # '''.format(userName, password)

   return '''
      test
   '''

# if __name__ == '__main__':
#    app.run()

serve(app, host='0.0.0.0', port=5000, threads=1) #WAITRESS