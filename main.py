from flask import Flask, render_template, request
from confi import CLIENT
import json
from pymongo import MongoClient
app = Flask(__name__)
print(CLIENT)
db_reg= CLIENT.registration
new_user= db_reg.user
@app.route('/', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        if request.form['submit'] == 'sub':
            if request.form['submit'] == 'sub':
                user_json= {'username': request.form['username'], 'emailid': request.form['email'], 'password':request.form['password']}
                print(user_json)
                ##ADDED
                new_user.insert_one(user_json)
                return 'Added'
    else:
        return render_template('register_user.html')

if __name__ == '__main__':
    app.run()