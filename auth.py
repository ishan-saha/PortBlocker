import base64, webview, threading
from socket import *
from flask import Flask as flask

app = flask(__name__)

Server=('xxx.xxx.xxx.xxx',9090)

@app.route("/")
def index():
    body= """<html><head></head><body><form action='auth' method='POST'><input type='text' name='username' placeholder='username' minlength=5 maxlength=5 required><br><input type='password' required minlength=20 maxlength=20 placeholder='Password'><br><button type=submit>UnBlock</button></form></body></html>"""
    return body
@app.route("/auth",methods=['POST'])
def auth():
    if request.method == 'POST':
        data=request.form['username']+'-'+base64.b64encode(request.form['password'])
        sender_sock=socket(AF_INET,SOCK_DGRAM)
        sender_sock.sendto(data,Server)
        Auth=sender_sock.recvfrom('5')
        if Auth.decode()== 'True':
            return "<html><body><script>alert('Authenticated');</script></body></html>"
        else:
            return "<html><body><script>alert('Failed');</script></body></html>"
def server():
    app.run(debug=False)

flaskapp = threading.Thread(target = server)
flaskapp.daemon = True
flaskapp.start()
window = webview.create_window('Authenticate','http://127.0.0.1:5000')
webview.start()
