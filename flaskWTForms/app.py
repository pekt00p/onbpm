__author__ = 'onbpm'


from flask import Flask, render_template, flash, session, redirect, url_for
from wtforms import TextAreaField, TextField, validators
from wtforms.validators import DataRequired
from flask.ext.wtf import Form
from flask.ext.wtf.recaptcha import RecaptchaField
from sendMail import SendEmailToMe


DEBUG = True
SECRET_KEY = 'secret'

# keys for localhost. Change as appropriate.

RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'

app = Flask(__name__)
app.config.from_object(__name__)

class CommentForm(Form):

    comment = TextAreaField("Question:", validators=[DataRequired(message='Question cannot be empty.'),
                                                     validators.Length(max=1000, message='Message is too long: 1000 symbols maximum')])
    username = TextField("Your name:", validators=[DataRequired(), validators.Length(min=2, max=50)])
    emailAddress = TextField("E-Mail:", [validators.email()])
    recaptcha = RecaptchaField()


@app.route("/")
def index(form=None):
    if form is None:
        form = CommentForm()
    comments = session.get("comments", [])
    return render_template("index.html",
                           comments=comments,
                           form=form)


@app.route("/add/", methods=("POST",))
def add_comment():

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data.encode('utf-8')
        username = form.username.data.encode('utf-8')
        sendersEmail = form.emailAddress.data.encode('utf-8')
        sm = SendEmailToMe
        generatedid = sm(sendersEmail, username, comment).currentDatetime
        comments = session.pop('comments', [])
        comments.append(generatedid)
        session['comments'] = comments
        flash("Your question is received.")
        return redirect(url_for("index"))
    return index(form)


if __name__ == "__main__":
    app.run()


