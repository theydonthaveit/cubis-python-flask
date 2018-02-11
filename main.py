from flask import Flask, send_from_directory, render_template, request

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def base():
    return render_template('cubis_home.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)