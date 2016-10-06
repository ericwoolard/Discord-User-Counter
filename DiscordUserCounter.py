import discord
import logging
from time import time
# Project Imports
import log

logging.basicConfig(level=logging.INFO)
client = discord.Client()


@client.event
async def on_ready():
    print('Logging in as ' + client.user.name)
    print('Client ID: ' + client.user.id)

    # log.log('\tGetting number of Discord users...')
    # startTime = time()

    online = 0
    idle = 0
    offline = 0

    for server in client.servers:
        for member in server.members:
            if str(member.status) == 'online':
                online += 1
            elif str(member.status) == 'idle':
                idle += 1
            elif str(member.status) == 'offline':
                offline += 1

        # elapsedTime = '\BLUE(%s s)' % str(round(time() - startTime, 3))
        # log.log('\t\t... done! %s' % elapsedTime)
        print('Online: ' + str(online))
        print('Idle: ' + str(idle))
        print('Offline: ' + str(offline))

    return '1. []('link_to_discord_server_here') %d users ' % \
           (online + idle), await client.close()

client.run('token')
