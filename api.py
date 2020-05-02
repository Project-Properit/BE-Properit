from app import create_app
from app.models import db

app = create_app()
db.create_all(app=app)

if __name__ == '__main__':  # For Debugging
    app.run(host='0.0.0.0', port=8080, threaded=True)
