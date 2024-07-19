from quart import Quart

# Import blueprints
from utilities import import_packages
from webhook_manager.webhook_listener import webhook_listener

# Importing some packages before getting started.
packages_to_import_early = ["webhook_manager", "automations"]
import_packages(packages_to_import_early)

app = Quart(__name__)

# Register blueprints
app.register_blueprint(webhook_listener)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
