from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clerk_id = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False, default='user')

    jobs = db.relationship('Job', backref='user', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'clerk_id': self.clerk_id,
            'email': self.email,
            'role': self.role
        }