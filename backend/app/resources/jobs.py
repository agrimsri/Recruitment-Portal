from flask import request, jsonify
from flask_restful import Resource
from app.utils import token_required, roles_accepted
from app.models.job import Job
from app.extensions import db
from datetime import datetime

class Jobs(Resource):
    @token_required
    def get(self):
        jobs = Job.query.all()
        return jsonify([job.to_dict() for job in jobs])
    
    @token_required
    @roles_accepted('recruiter' )
    def post(self):
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['title', 'description']
        for field in required_fields:
            if field not in data:
                return jsonify({'message': f'Missing required field: {field}'}), 400
        
        new_job = Job(
            title=data['title'],
            description=data['description'],
            location=data.get('location'),
            posted_by=request.clerk_id,
            posted_at=datetime.now()
        )
        
        db.session.add(new_job)
        db.session.commit()
        
        return jsonify({
            'message': 'Job created successfully',
            'job': new_job.to_dict()
        }), 201


class SingleJob(Resource):
    @token_required
    def get(self, job_id):
        job = Job.query.get_or_404(job_id)
        return jsonify(job.to_dict())

    @token_required
    def put(self, job_id):
        job = Job.query.get_or_404(job_id)
        
        # Check if user is the owner or an admin
        if request.clerk_id != job.posted_by and \
           request.public_metadata.get('role') != 'admin':
            return jsonify({'message': 'Unauthorized to modify this job'}), 403
        
        data = request.get_json()
        
        if 'title' in data:
            job.title = data['title']
        if 'description' in data:
            job.description = data['description']
        if 'location' in data:
            job.location = data['location']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Job updated successfully',
            'job': job.to_dict()
        })

    @token_required
    def delete(self, job_id):
        job = Job.query.get_or_404(job_id)
        
        # Check if user is the owner or an admin
        if request.clerk_id != job.posted_by and \
           request.public_metadata.get('role') != 'admin':
            return jsonify({'message': 'Unauthorized to delete this job'}), 403
        
        db.session.delete(job)
        db.session.commit()
        
        return jsonify({'message': 'Job deleted successfully'})