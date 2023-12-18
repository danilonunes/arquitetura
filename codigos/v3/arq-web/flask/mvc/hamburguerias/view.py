from flask import render_template
from hamburguerias import model

def init_app(app):
    app.add_url_rule("/", view_func=index)
#    app.add_url_rule("/login", methods=['GET', 'POST'])

def index():
    h = model.Hamburgueria.query.all()
    l = []
    for i in h:
       l.append(i.nome)

    return render_template("index.html", hamburguerias=l)

#def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
#    form = LoginForm()
#    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
#        login_user(user)

#        flask.flash('Logged in successfully.')

 #       next = flask.request.args.get('next')
        # url_has_allowed_host_and_scheme should check if the url is safe
        # for redirects, meaning it matches the request host.
        # See Django's url_has_allowed_host_and_scheme for an example.
#        if not url_has_allowed_host_and_scheme(next, request.host):
#            return flask.abort(400)

#        return flask.redirect(next or flask.url_for('index'))
#    return flask.render_template('login.html', form=form)
