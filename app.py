from flask import Flask, render_template , request

import pickle

app = Flask(__name__)
cv = pickle.load(open("models/cv.pkl"))
clf = pickle.load(open("models/clf.pkl"))


@app.route('/', methods=['GET', 'POST'])
def home():
    text = ""
    if request.method == 'POST':
        text = request.form.get('email-content')
    return render_template('spam_classifier.html', text=text)






if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)