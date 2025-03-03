from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

# Crear la aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  # Clave secreta para formularios


# Definir el formulario
class MiFormulario(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    correo = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    submit = SubmitField('Enviar')


# Ruta para el formulario
@app.route('/', methods=['GET', 'POST'])
def formulario():
    form = MiFormulario()
    if request.method == 'POST' and form.validate():
        # Obtener datos del formulario
        nombre = form.nombre.data
        telefono = form.telefono.data
        correo = form.correo.data

        # Redirigir a la página de resultado con los datos en la URL
        return redirect(url_for('resultado', nombre=nombre, telefono=telefono, correo=correo))

    return render_template('formulario.html', form=form)


# Ruta para mostrar los datos ingresados
@app.route('/resultado')
def resultado():
    nombre = request.args.get('nombre', 'No proporcionado')
    telefono = request.args.get('telefono', 'No proporcionado')
    correo = request.args.get('correo', 'No proporcionado')

    return render_template('resultado.html', nombre=nombre, telefono=telefono, correo=correo)


# Ruta para la página "About"
@app.route('/about')
def about():
    return render_template('about.html')


# Ruta para la página de inicio
@app.route('/index')
def index():
    return render_template('index.html')


# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
