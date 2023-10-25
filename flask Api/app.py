from flask import Flask,render_template,request
app = Flask(_name_)
import mysql.connector

dk= mysql.connector.connect(
    host="localhost",
    user="root",
    password="dilip@123",
    database = "users"
)

@app.route('/')
@app.route('/hello')
def hello():
    return "hello world!"

@app.route('/users')
 def users():
    cursor = dk.cursor()
    cursor.execute("select id , name , email , role FROM users ")
    users_data = cursor.fetchcall()
    return render_template('retrive.html,')

@app.route('/new_user' , methods = ['GET' , 'POST'])
def new_user():
    if request.method == 'GET':
        return render_template('Registration.html')
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role= request.form['role']

        cursor  = dk.cursor()
query = "insert into users(name,email,role) VALUES (%s , %s ,%s)"
cursor.execute(query,(name,email,role))
db.commit()
return "user added succesfully"

@app.route('/user/<int : id>')
def get_user(id):
    cursor = dk.cursor()
    query = " select id, name ,email ,role FROM users WHERE id = %s"
    cursor.execute(query,(id))
    user_data = cursor.fetchone()
    if user_data : return f "user id :
    {user_data [0] }, Name :
    {user_data[1]}, E-Mail:
    {user_data[2]}, Role:
    {user_data[3]}"
    else :
    abort(404)
    @app.errorhandler(404)
    def page_not_found(error):
        return "forbidden - 404", 404


if _name=="main_":
    app.run(debug=True)
