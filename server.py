from flask import Flask, render_template,request,redirect
from operator import itemgetter
import csv

app = Flask(__name__)

def write_to_file(data):
    with open('database.txt',mode='a') as db:
        email,subject,message = itemgetter('email','subject','message')(data)
        file= db.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    # with open('database.csv',mode='a') as db:
    #     email,subject,message = itemgetter('email','subject','message')(data)
    #     csv_writer = csv.writer(db,delimiter=',')
    #     csv_writer.writerow([email,subject,message])
        # pass
    with open('database.csv', 'a', newline='') as csvfile:
        fieldnames = ['email','subject','message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # writer.writeheader()
        writer.writerow(data)

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page_navigation(page_name):
    return render_template(page_name)


@app.route('/submit_form',methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)
            # write_to_file(data)
            write_to_csv(data)
        except:
            return "something went wrong!"
    return redirect('/thankyou.html')