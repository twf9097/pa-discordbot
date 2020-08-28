import os
from client import client

client.run(os.environ.get('PA_DISCORD_TOKEN'))