from  wtforms import Form, StringField, validators, TextAreaField

class PostForm(Form):
    title = StringField("Title", [validators.Length(min=10, max=200), validators.DataRequired()])
    content = TextAreaField("Content", [validators.Length(min=100), validators.DataRequired()])