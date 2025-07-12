from flask import Flask, render_template, request
import math
app = Flask(__name__)

def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(not c.isalnum() for c in password): pool += 32
    if pool == 0: return 0
    return round(len(password) * math.log2(pool), 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    feedback = None
    entropy = None
    if request.method == 'POST':
        pwd = request.form['password']
        entropy = calculate_entropy(pwd)
        feedback = "Weak" if entropy < 28 else "Moderate" if entropy < 50 else "Strong"
    return render_template('index.html', feedback=feedback, entropy=entropy)

if __name__ == '__main__':
    app.run(debug=True)
