from app import app, db
from models import User, Book, Rating  # Import your models

def init_db():
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")

if __name__ == '__main__':
    init_db()
