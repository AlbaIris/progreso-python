from flask import Flask, render_template
from flask_wtf import Flaskfrom
from wtfforms import stringField, submitField

app = Flask (__name__)

app.config['SECRET_KEY'] = 'clavesecreta'

class Formulario(Flaskfrom):
    nombre = stringField("Nombre")
    enviar = submitField("enviar")

    @app.route('/', methods=['GET,''POST'])
    def principal():
        nombre =''
        enviado = False
        Formulario = Formulario()

        if Formulario.validate_on_submit():
            enviado = True
            nombre  = Formulario.nombre.data
            Formulario.nombre.data =''

            return render_template('app_10_formulario.html, enviado=enviado,nombre=nombre,formulario=formulario')
        
        if __name__ == 'main_':
           app.run(debug=True)