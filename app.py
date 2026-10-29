from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    year = request.form.get('year')
    return render_template('success.html', name=name, year=year)

if __name__ == '__main__':
    app.run(port=5002, debug=False)