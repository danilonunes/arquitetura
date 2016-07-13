# third party imports
from flask import g, session

# local application imports
from app.usuarios.constants import SESSION_NAME_USER_ID
from app.usuarios.models import Usuario


def app_before_request():
    # pull user's profile from the db before every request are treated
    g.user = None
    if SESSION_NAME_USER_ID in session and session[SESSION_NAME_USER_ID] is not None:
        g.user = Usuario.query.get(session[SESSION_NAME_USER_ID])