from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///codes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class CodeText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # tittle = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(100), nullable=False)
    code = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<CodeText %r>' % self.id


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route('/', methods = ["POST", "GET"])
def home():
    if request.method == 'POST':
        code = make_string_without_tags(request.form['code'])
        language = request.form['coding_language']
        print(language)
        print(type(language))
        print(code)
        print(type(code))
        codetext = CodeText(code = code, language = language)
        try:
            db.session.add(codetext)
            db.session.commit()
            return redirect(f'/text_view/{codetext.id}')
        except:
            return "Чота ошибка"
    else:
        return render_template('main.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/write/<what_to_write>')
def write(what_to_write):
    return f'I can write you: {what_to_write}'


@app.route('/integer/<int:_number>')
def integer(_number):
    return f"Пишу намбер: {_number}; проверка рандома: &copy &#169"


@app.route('/template')
def template():
    return render_template('base.html')


@app.route('/test')
def test():
    return render_template('test_space.html')


def make_string_without_tags(txt):
    txt.replace('<', '&lt')
    txt.replace('>', '&gt')
    txt.replace('&', '&amp')
    txt.replace('“', '&quot')
    txt.replace('‘', '&apos')
    return txt

@app.route('/text_view/<int:id>')
def text_view(id):
    ct = CodeText.query.get_or_404(id)
    code_text = ct.code
    prefered_language = ct.language
    return render_template('text_view.html', text_id = id, code_text = code_text, prefered_language = prefered_language)


if __name__ == "__main__":
    app.run(debug=True)