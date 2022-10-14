from flask import render_template, make_response, request, Flask, redirect, url_for, session
import os
app = Flask(__name__)
app.secret_key = os.urandom(24) # This is an important step. 
# Flask will not allow you to use cookies without a secret key, as doing so is inherently insecure


@app.route('/', methods=['GET', 'POST'])
def index():
    if not (session.get('user')):
        if not request.cookies.get('choice'):
            if request.method == 'POST':
                colour = str(request.form['colour'])
                response = make_response("Setting your Cookie and Session! Please refresh the page to see the results - ")
                # make_response binds a certain event, in this case a string , to the formation of a cookie. You may find
                # this function to include redirects or even render templates in other examples. 
                response.set_cookie('choice', colour)
                session['user'] = str(request.form['name'])
                return response
        else:
            response = make_response(render_template('output.html', cookie = str(request.cookies.get('choice')), user = (str(session.get('user')))))
            return response
            
    else:
        return render_template('output.html', cookie = str(request.cookies.get('choice')), user = (str(session.get('user'))))

    return render_template('index.html')

if __name__ == '__main__':  
    app.run(debug = True)  