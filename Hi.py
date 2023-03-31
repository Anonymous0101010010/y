import discord
import asyncio

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

async def create_thread(channel):
    await channel.create_thread(name='name', type=discord.ChannelType.public_thread)
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    while True:
        for guild in client.guilds:
            for channel in guild.text_channels:
                await create_thread(channel)
                await asyncio.sleep(1)

client.run('MTA5MTAwOTE5NTA4MTQ3ODIwNA.G1Nn03.K_UEjlhR1l7Mq2eBCsu6I912FavGADHkP1WrYE')
