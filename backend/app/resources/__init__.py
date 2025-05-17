from .test import Test
from .webhooks import ClerkWebhook, UpdateMetadata

def init_resources(api):
    """Initialize all API resources"""
    api.add_resource(Test, '/api/test')
    api.add_resource(ClerkWebhook, '/api/webhooks/clerk/user')
    api.add_resource(UpdateMetadata, '/api/updateMetadata')

__all__ = [
    'Test',
    'ClerkWebhook',
    'UpdateMetadata',
    'init_resources'
]
