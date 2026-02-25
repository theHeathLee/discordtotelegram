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
            if member.display_name == "GEEK Music":
                #do not send message for GEEK Music
                return
            elif member.display_name == "Hunterly":
                message = f"Hunters here, time to get this bread"
            elif member.display_name == "SPKross":
                message = f"Jacob the absolute legend has arrived"
            elif member.display_name == "Heath":
                message = f"All Rise for King Heath"
            elif member.display_name == "Currahee901":
                message = f"God help us, Tommy has entered the building"
            elif member.display_name == "Futsch":
                message = f"Selim is in the house"
            elif member.display_name == "Jamirous":
                message = f"Jan is here to loot in the blue zone"
            elif member.display_name == "RedLeg_198":
                message = f"Tommy is patiently waiting in discord"
            elif member.display_name == "snuslas":
                message = f"Gruess Gott, Niklas is here"
            else:
                message = f"{member.display_name} the just joined {after.channel.name}"
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            requests.post(url, data={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message
            })
        elif after.channel.name == "Arc Commies🤖":
            message = f"{member.display_name} the just joined {after.channel.name}, prepare for the revolution"
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            requests.post(url, data={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message
            })

client.run(DISCORD_TOKEN)
