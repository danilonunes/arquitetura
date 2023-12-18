
def init_app(app):
    app.config["TITLE"]="App Hamburguerias"
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mvc.db"
    app.config['SECRET_KEY'] = 'something-secret'
    app.config['SIMPLELOGIN_LOGIN_URL'] = '/signin/'
    app.config['SIMPLELOGIN_LOGOUT_URL'] = '/exit/'
    app.config['SIMPLELOGIN_HOME_URL'] = '/'
