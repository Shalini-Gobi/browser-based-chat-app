from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for storing messages
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    # Get data from request
    message = request.form['message']
    username = request.form['username']

    # Append message to the messages list
    messages.append({'username': username, 'message': message})

    return jsonify({'status': 'OK'})

@app.route('/get_messages')
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)
