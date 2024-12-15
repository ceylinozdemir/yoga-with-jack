from flask import Flask, render_template

# Create Flask app instance
app = Flask(__name__)

# Define route
@app.route('/')
def home():
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)