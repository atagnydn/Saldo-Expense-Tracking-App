from flask import Flask
from flask_cors import CORS
from backend.routes.users import users
from backend.routes.groups import groups
from backend.routes.expenses import expenses
from backend.routes.notifications import notifications
from backend.routes.debts import debts
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Allow CORS for specific methods and headers
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}},
     supports_credentials=True)

app.register_blueprint(users)
app.register_blueprint(groups)
app.register_blueprint(expenses)
app.register_blueprint(notifications)
app.register_blueprint(debts)

if __name__ == '__main__':
    app.run(debug=True, port=5005)
