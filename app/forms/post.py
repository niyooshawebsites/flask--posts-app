from  wtforms import Form, StringField, validators, TextAreaField

class PostForm(Form):
    title = StringField("Title", [validators.Length(min=10, max=200), validators.DataRequired()])
    content = TextAreaField("Content", render_kw={"id": "editor"})