from backend import app, database
from backend.models import Usuario, Post

if __name__ == '__main__':
    with app.app_context():
        database.create_all()
    app.run(debug=True)

