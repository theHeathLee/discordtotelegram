import discord
import requests
import os

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']


intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.name != "Secret Coup":
            if member.display_name != "Hunterly":
                #do not send message for GEEK Music
                return
            else:
                message = f"{member.display_name} the bitch just joined {after.channel.name}"
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            requests.post(url, data={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message
            })

client.run(DISCORD_TOKEN)
