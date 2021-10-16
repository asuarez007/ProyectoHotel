from flask import Flask, render_template, request, flash
import os
from flask_wtf import FlaskForm
from flask_wtf import RecaptchaField

app = Flask(__name__)
app.secret_key = os.urandom(24)
#app.config['SECRET_KEY'] = 'claveoculta'
#app.config['RECAPTCHA_PUBLIC_KEY'] = '6LctrKwcAAAAANZJ2rLJ0upbuuL6pJKuz_v84uyC'
#app.config['RECAPTCHA_PRIVATE_KEY'] = '6LctrKwcAAAAAGz3kPYAZYax2fjQxmZqtedagPaU'

#-------------------------------------------> INTERFACE USUARIO <------------------------------------
@app.route("/",methods=['GET'])
def inicio():
    return render_template("index.html")

@app.route("/habitaciones", methods = ["GET", "POST"])
# Si ya inicio sesion -> le permitira realizar reservas
# Si ya escogio habitacion para reservar -> le permitira realizar pago
# Si ya inicio sesion -> le permitira valorar las habitaciones
def habitaciones():
    return render_template("users/habitaciones.html")

@app.route("/contacto", methods = ["GET", "POST"])
def contacto():
    return render_template("users/contacto.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("users/login.html")

@app.route("/registro", methods = ["GET", "POST"])
def registro():
    return render_template("users/registro.html")

@app.route("/perfil", methods = ["GET", "POST"])
def perfil():
    return render_template("users/perfil.html")

@app.route("/reservas", methods = ["GET", "POST"])
# Si ya inicio sesion -> le permitira ir a reservas desde el perfil
# le permitira cambiar o cancelar la reserva
def reservas():
    return render_template("users/reservas.html")

@app.route("/pago", methods = ["GET", "POST"])
def pago():
    return render_template("users/pago.html")


#-------------------------------------------> INTERFACE ADMINISTRADORES <------------------------------------

@app.route("/login_admin", methods = ["GET", "POST"])
def login_admin():
    return render_template("administradores/login_admin.html")

@app.route("/gestion_habitaciones", methods = ["GET", "POST"])
def gestion_habitaciones():
    return render_template("administradores/gestion_habitaciones.html")

@app.route("/tarifas", methods = ["GET", "POST"])
def tarifas():
    return render_template("administradores/tarifas.html")

@app.route("/gestion_users", methods = ["GET", "POST"])
def gestion_users():
    return render_template("administradores/gestion_users.html")

#-------------------------------------------> INTERFACE SUPER ADMINISTRADORES <------------------------------------

@app.route("/login_s", methods = ["GET", "POST"])
def login_s():
    try:
        #form = login_form()
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            error = None

            if not username:
                error = 'El usuario es obligatorio'
                flash(error)
                return render_template("super_admin/login_sadmin.html")

            if not password:
                error = 'La contraseña es obligatoria'
                flash(error)
                return render_template("super_admin/login_sadmin.html")

            if username == 'superAdmin' and password == 'super123':
                flash(error)
                return render_template("super_admin/dashboard.html")
            else:
                error = 'Usuario y/o contraseña invalidos, intente nuevamente'
                flash(error)   
                return render_template("super_admin/login_sadmin.html")
            
        return render_template("super_admin/login_sadmin.html")
    except:
        return render_template("super_admin/login_sadmin.html")

@app.route("/s_gestion_habitaciones", methods = ["GET", "POST"])
def s_gestion_habitaciones():
    return render_template("super_admin/s_gestion_habitaciones.html")

@app.route("/s_tarifas", methods = ["GET", "POST"])
def s_tarifas():
    return render_template("super_admin/s_tarifas.html")

@app.route("/s_gestion_users", methods = ["GET", "POST"])
def s_gestion_users():
    return render_template("super_admin/s_gestion_users.html")

@app.route("/s_gestion_admins", methods = ["GET", "POST"])
def gestion_admins():
    return render_template("super_admin/s_gestion_admins.html")

#CAPTCHA
class login_form(FlaskForm):
    recaptcha = RecaptchaField()

if __name__ == '__main__':
    app.run(debug=True)



