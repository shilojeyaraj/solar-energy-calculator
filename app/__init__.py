from flask import Flask, redirect, url_for

def create_app():
    app = Flask(__name__)
    
    # Import routes after app creation
    from .app import app as solar_blueprint
    
    # Register blueprint
    app.register_blueprint(solar_blueprint)
    
    @app.route('/')
    def index():
        return redirect('/solar/')
    
    # Debug print
    print("\nAll registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule} - {rule.endpoint}")
    
    return app