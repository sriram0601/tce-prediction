from flask import Flask, request, render_template, redirect, url_for
import models as m

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == "POST":
        d= request.form['d']
        h=request.form['h']
        m=request.form['m']

        return redirect(url_for('result',day=d,hour=h,min=m))
    else:
        return render_template('index.html')

@app.route('/result/<day><hour><min>')
def result(day,hour,min):

    res = m.powerPrediction(day,hour,min)

    context = {
        'day':day,
        'hour':hour,
        'minute':min,
        'result':res,
    }
    return render_template('result.html',rday=context)
if __name__ == '__main__':
    app.run()
