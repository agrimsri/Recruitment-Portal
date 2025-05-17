from ..extensions import db
from datetime import datetime

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100))
    posted_by = db.Column(db.String(128), db.ForeignKey('user.clerk_id'), nullable=False)
    posted_at = db.Column(db.DateTime, default=datetime.now())

    # Define relationship with User model
    poster = db.relationship('User', backref=db.backref('jobs', lazy=True))

    def __repr__(self):
        return f'<Job {self.title}>'