from flask import Flask, render_template, request

app = Flask('MyApp')

@app.route('/')
def hello():
    return render_template(
    'index.html'
    )

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        comments = request.form.get('comments')

        print(name)
        print(email)
        print(comments)

    return render_template(
    'contact.html'
    )

app.run(debug=True)
