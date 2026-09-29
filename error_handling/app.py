from flask import Flask, render_template

app = Flask(__name__)

# Catch 404 Page Not Found errors globally
@app.errorhandler(404)
def page_not_found(error):
    # 'error' contains the internal description from Flask
    return render_template('errors/404.html'), 404

# Catch 500 Internal Server errors globally
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500
