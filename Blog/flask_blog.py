from flask import Flask
from flask import render_template


app = Flask(__name__)

mock_post = [
    {
        'author': 'Edwin C',
        'date': '02/10/2018',
        'title': 'first blog',
        'content': 'bla bla',
    },

    {
        'author': 'Vingo C',
        'date': '02/14/2018',
        'title': 'se blog',
        'content': 'blsd s da bla',
    },
]


@app.route("/")
def hello():
    return render_template('home.html', data=mock_post)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
