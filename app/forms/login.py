from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    email = StringField("Email", [validators.Length(min=6, max=50)])
    password = PasswordField("Password", [validators.DataRequired()])