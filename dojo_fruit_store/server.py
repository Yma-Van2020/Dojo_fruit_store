from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    return render_template("checkout.html", fname = request.form['first_name'], 
                           lname = request.form['last_name'], sid = request.form['student_id'],
                           rasp = request.form['raspberry'], straw = request.form['strawberry'], apple = request.form['apple'],
                           count = int(request.form['raspberry']) + int(request.form['strawberry']) + int(request.form['apple']),
                           fullname = request.form['first_name'] + ' ' + request.form['last_name'])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    