from app import app, db, socketio
from app.forms import ContactForm
from app.models import Appoitments
from flask import  render_template, redirect, request, url_for
    

@app.route('/', methods=['POST', 'GET'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        user = Appoitments(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index2.html', form=form)

@app.route('/admin', methods=['GET'])   
def admin():
    appoint = Appoitments.query.all()

    return render_template('admin.html', appoint=appoint)