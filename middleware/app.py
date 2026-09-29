from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Naina'


@app.before_request
def security_gatekeeper():
    print(f"Gatekeeper running for path: {request.path}")
    public_endpoints = ['home', 'login', 'static']
    if request.endpoint in public_endpoints:
        return None 

    if 'logged_in' not in session:
        print("Access Denied! Redirecting to login page...")
        return redirect(url_for('login'))

@app.after_request
def add_response_headers(response):
    print(f"Appending headers to the server response.")
    response.headers['X-Custom-Middleware-Header'] = 'Injected-By-Flask'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

@app.route('/')
def home():
    return '''
        <h1>Public Home Page</h1>
        <p>Status: Anyone can view this page without logging in.</p>
        <p><a href="/dashboard">Go to Private Dashboard</a></p>
    '''

@app.route('/login')
def login():
    session['logged_in'] = True
    return '''
        <h1>Login Processed</h1>
        <p>A mock session cookie has been saved to your browser automatically!</p>
        <p><a href="/dashboard">Now try visiting the Private Dashboard</a></p>
    '''

@app.route('/dashboard')
def dashboard():
    return '''
        <h1>Private User Dashboard</h1>
        <p>Welcome! You are seeing this page because your session is verified.</p>
        <p><a href="/logout">Logout</a></p>
    '''

@app.route('/logout')
def logout():
    session.clear()
    return '''
        <h1>Logged Out</h1>
        <p>Your session has been cleared.</p>
        <p><a href="/dashboard">Try going back to Dashboard (Will be blocked)</a></p>
    '''


if __name__ == '__main__':
    app.run(debug=True)
