import discord

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("Hello, I am a test bot")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
client.run('NzU2NDYzNzc5MDg4MzAyMTUx.X2SNyw.5vd9UrUJYlqE4TJ8--t_3YIm5HM')