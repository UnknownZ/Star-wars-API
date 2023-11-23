from models import db

class Favorite(db.Model):
    __tablename__='favorites'
    id = db.Column(db.Integer, primary_key=True)
    id_planet = db.Column(db.Integer, db.ForeignKey('planets.id'))
    id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
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
            "id_people": self.id_people,
            "id_planet:": self.id_planet,
            "id_user": self.id_user
        }