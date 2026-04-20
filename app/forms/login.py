from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    username = StringField("Username", [validators.Length(min=6, max=50)])
    password = PasswordField("Password", [validators.DataRequired()])