"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template
from .forms import LogUserForm, secti,masoform,lide,pokuta,getLide
from ..data.database import db
from ..data.models import LogUser,Lide,Pokuty
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(Lide).all()
    print (type(pole))
    print (pole)
    print (pole[0].jmeno)
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/secti', methods=['GET','POST'])
def scitani():
    form = secti()
    if form.validate_on_submit():
        return render_template('public/vystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/secti.tmpl', form=form)

@blueprint.route('/maso', methods=['GET','POST'])
def masof():
    form = masoform()
    if form.validate_on_submit():
        return render_template('public/masovystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/maso.tmpl', form=form)

@blueprint.route('/pokuta', methods=['GET','POST'])
def pokutaAdd():
    form = pokuta()
    lide = getLide.getLide()
    print ("Lel")
    if form.validate_on_submit():
        print("Success")
        Pokuty.create(**form.data)
        return render_template('public/success.tmpl')
    return render_template('public/pokutaAdd.tmpl', form=form,lide=lide)

@blueprint.route('/lide', methods=['GET','POST'])
def lideAdd():
    form = lide()
    if form.validate_on_submit():
        Lide.create(**form.data)
        return render_template('public/success.tmpl')
    return render_template('public/lideAdd.tmpl', form=form)

@blueprint.route('/pokuty',methods=['GET'])
def listPokuty():
    pole = db.session.query(Pokuty).all()
    lide = db.session.query(Lide).all()
    return render_template("public/listPokuty.tmpl",data = pole,lide = lide)