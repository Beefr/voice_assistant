
from flask import Flask, render_template, request, redirect, session
import os
import presentation.sessionManager as sm


from mainModule.voiceAssistant import *

app = Flask(__name__)
SESSION_TYPE='redis'
app.config.from_object(__name__)

secretkey_path = os.path.join(os.getcwd(), "presentation\\secretkey")
with open(secretkey_path, 'r') as file:
    app.secret_key = file.read()
    print(app.secret_key)

camera=True
soundInput=True
soundOutput=False # False for raspberry /!\
va= VoiceAssistant(camera, soundInput, soundOutput)
va.run()
#va.currentFrame() # pour choper les frames actuelles

@app.route("/", methods=['GET', 'POST'])
def menu():
    if request.method == 'GET':
        return redirect('/login/')
    if request.method == 'POST':
        try: 
            user_input = request.form["user_input"]
            if session['validation']:
                pass # ok show
            else:
                pass # wrong
        
        except:
            pass

        


@app.route("login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        return redirect("/")
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug= True, use_reloader=False)



