from flask import Flask

# Import blueprints
from automations.attio_to_python import attio_deal_modified_wh

app = Flask(__name__)

# Register blueprints
app.register_blueprint(attio_deal_modified_wh)

if __name__ == "__main__":
    app.run(port = 5000, debug=True)