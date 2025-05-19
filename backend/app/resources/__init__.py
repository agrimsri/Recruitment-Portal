from .test import Test
from .webhooks import ClerkWebhook, UpdateMetadata
from .jobs import Jobs, SingleJob

def init_resources(api):
    """Initialize all API resources"""
    api.add_resource(Test, '/api/test')
    api.add_resource(ClerkWebhook, '/api/webhooks/clerk/user')
    api.add_resource(UpdateMetadata, '/api/updateMetadata')
    api.add_resource(Jobs, '/api/jobs')
    api.add_resource(SingleJob, '/api/jobs/<int:job_id>')

__all__ = [
    'Test',
    'ClerkWebhook',
    'UpdateMetadata',
    'Jobs',
    'SingleJob',
    'init_resources'
]
