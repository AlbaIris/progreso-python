from flask import Flask
app = Flask(__name__)

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route("/calculadora/num1/num2/operaciones")
def hello_open(num1, num2, operaciones):
   if operaciones == 'suma':
        return num1+num2 
   if operaciones == 'resta':
       return num1-num2 
   if operaciones == 'multiplicacion':
        return num1*num2
   if operaciones == 'division':
        return num1/num2
   
if __name__ == '__main__':
    app.run(debug=True)