from app import db

class Person(db.Model):
    __tablename__ = 'people'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.Text(255))

    def __repr__(self):
        return f"Person with name {self.name}, age {self.age}"
    
