Flask API Devlopment

-> A new flask application is created using flask.libraries in pycharm.
->Then using flask the following routes are created.
   /hello : return String "hello world!".
   /users : return display all the users in database,In the form of table using html (mySql is connected using host name ,root,name,password,databasename).
   /new_user: render html page to accept input from the user and store the information in database.
   /users/<id>: to retirve specific users detials.
 Database Interation
->The database is created with the name of "users".
->The database have the following rows id,name,e-mail,role.
->The required queries are writtern to insterted and retrived the values from the database.
 Documentation 
 These application is used to get users information and store the information in the database and also able to retrive the entire table (or) specfic user using there id.
