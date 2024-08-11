# Add channels
INSTALLED_APPS = [
    'channels',
    'chat',
]

ASGI_APPLICATION = 'chat_project.asgi.application'

# Redis settings
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}