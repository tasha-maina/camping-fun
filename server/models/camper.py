from server.config import db

class Camper(db.Model):
    __tablename__ = "campers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    signups = db.relationship("Signup", backref="camper")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }
