from flask import Flask, request, render_template
from airtable import Airtable
import smtplib

app = Flask(__name__)
airtable = Airtable('appaVdzZcX4TfXXe8', 'user details', api_key='keyFE90QcwKJZ28UP')
airtable2 = Airtable('appaVdzZcX4TfXXe8', 'bookings', api_key='keyFE90QcwKJZ28UP')
def send_mail(name,data,email_id,car_model,date):
    print('sending email')
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("balajitheratipally1212@gmail.com", "vyvrfoazdjphkzcd")

    subject = 'New Registration'
    body = 'Dear {},Thank you for booking a car {} for testdrive  at {} on {} '.format(name,car_model,data,date)

    message = f'Subject : {subject}\n\n{body}\n'

    server.sendmail('balajitheratipally1212@gmail.com', 
                    ['balajitheratipally1212@gmail.com',email_id,'ch.koushik123@gmail.com'],
                    message)

    print('email sent')
def send_mail2(name,email_id):
    print('sending email')
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("balajitheratipally1212@gmail.com", "vyvrfoazdjphkzcd")

    subject = 'New booking'
    body = 'Thank you {} for booking Car'.format(name)

    message = f'Subject : {subject}\n\n{body}\n'

    server.sendmail('balajitheratipally1212@gmail.com', 
                    ['balajitheratipally1212@gmail.com',email_id,'ch.koushik123@gmail.com'],
                    message)

    print('email sent')
@app.route('/')
def home():
    return render_template('video.html')
@app.route('/book',methods=["POST"])
def url_2():
    print(request.form)
    name = request.form['name']
    phone_number = request.form['phone_number']
    email_id = request.form['email_id']
    
    car_model = request.form['car_model']

    details = {'name': name, 'phone_number': phone_number, 'email_id': email_id,
              'car_model': car_model}

    airtable2.insert(details)
    
    send_mail2(name,email_id)

    return '<h1>Booking done Successfully..!Thanks for booking.Check your mail for further details..!! </h1>'
@app.route('/<ext>')
def ext_url(ext):
   return render_template(ext) 
@app.route('/<ext>',methods=["POST"])
def url_1(ext):
        print(request.form)
        name = request.form['name']
        phone_number = request.form['phone_number']
        email_id = request.form['email_id']
        date = request.form['date']
        
        car_model = request.form['car_model']
    
        a=['1AM','2AM','3AM']
        data=''
        
        x=request.form['options']
         
        data=data+x+''
        details = {'name': name, 'phone_number': phone_number, 'date': date, 'email_id': email_id,
                'car_model': car_model, 'data': data}

        airtable.insert(details)
    
        send_mail(name,data,email_id,car_model,date)

        return '<h1>Successfly registered</h1>'



    
if __name__=="__main__":
    app.run(debug=True)