from ..extensions import db
from datetime import datetime

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100))
    posted_by = db.Column(db.String(128), db.ForeignKey('user.clerk_id'), nullable=False)
    posted_at = db.Column(db.DateTime, default=datetime.now())

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'location': self.location,
            'posted_by': self.posted_by,
            'posted_at': self.posted_at.isoformat()
        }