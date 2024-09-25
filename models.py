from app import db

class User(db.Model):
    uid = db.Column(db.String, primary_key=True) 
    name = db.Column(db.String(100), nullable=True)  # User name can be nullable
    ratings = db.relationship('Rating', backref='user', lazy=True)

class Book(db.Model):
    bookid = db.Column(db.String, primary_key=True)  # Book ID 
    title = db.Column(db.String(200), nullable=False)  # Title cannot be null
    price = db.Column(db.Float, nullable=True)  # Price can be nullable
    description = db.Column(db.Text, nullable=True)  # Description can be nullable
    image = db.Column(db.String(500), nullable=True)  # Image URL can be nullable
    publisher = db.Column(db.String(200), nullable=True)  # Publisher can be nullable
    published_date = db.Column(db.Integer, nullable=True)  # Published date can be nullable
    info_link = db.Column(db.String(500), nullable=True)  # Info link can be nullable
    categories = db.Column(db.String(500), nullable=True)  # Categories can be nullable
    categories_split = db.Column(db.String(500), nullable=True)  # Split categories can be nullable
    ratings = db.relationship('Rating', backref='book', lazy=True)

class Rating(db.Model):
    rid = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.uid'), nullable=False)  # FK to User
    book_id = db.Column(db.String, db.ForeignKey('book.bookid'), nullable=False)  # FK to Book
    rating = db.Column(db.Integer, nullable=False)  # Rating cannot be null
