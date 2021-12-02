""" deprecated
"""

#app.config['SQLALCHEMY_DATABASE_URI'] = 'Danjoe4-2442.postgres.pythonanywhere-services.com'

# for the session, i.e passing values
app.secret_key = config_file["flask_session_key"]
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["PERMANENT_SESSION_LIFETIME"] = 60 # the session lasts 60 seconds
app.config.from_object(__name__)
Session(app)

