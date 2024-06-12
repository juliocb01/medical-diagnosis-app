def register_routes(app):
    from api.routes.diagnose import diagnose_bp
    from api.routes.doctors import doctors_bp

    app.register_blueprint(diagnose_bp, url_prefix='/api')
    app.register_blueprint(doctors_bp, url_prefix='/api')
