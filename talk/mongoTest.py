from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def main(num=None):
    return render_template('myPage.html', num=num)


@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):
    if request.method == 'POST':
        temp = request.form['num']
        temp = int(temp)
        temp1 = request.form['char1']
        return render_template('main.html', num=temp, char1=temp1)


if __name__=='__main__':
    app.run(debug=True, threaded=True)