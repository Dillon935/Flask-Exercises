from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Define a global dictionary to store registered users
registered_users = {}

# Define a list of available student organizations
organizations = [
    'Organization A',
    'Organization B',
    'Organization C',
    'Organization D',
    'Organization E'
]

# Define a layout template for the app
@app.route('/')
def home():
    return render_template('layout.html')

# Define a home page with a registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        organization = request.form['organization']
        
        # Validate form inputs
        if not name or not organization:
            error = 'Please fill out all fields.'
            return render_template('register.html', organizations=organizations, error=error)
        
        if organization not in organizations:
            error = 'Invalid organization selected.'
            return render_template('register.html', organizations=organizations, error=error)
        
        # Save the user's registration data
        registered_users[name] = organization
        
        # Redirect to the list of registered users
        return redirect(url_for('users'))
    
    return render_template('register.html', organizations=organizations)

# Define a page that shows the list of registered users
@app.route('/users')
def users():
    return render_template('users.html', registered_users=registered_users)

if __name__ == '__main__':
    app.run(debug=True)
