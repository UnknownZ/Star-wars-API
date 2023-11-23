from models import db

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    favorites = db.relationship("Favorite", backref="user")
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username
        }
    
    def serialize_with_favorites(self):
        return {
            "id": self.id,
            "username": self.username,
            "favorites": self.list_favorites
        }
    
    def list_favorites(self):
        return list(map(lambda favorite: favorite.serialize(), self.favorites))