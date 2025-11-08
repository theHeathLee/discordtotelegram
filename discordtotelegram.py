import discord
import requests
import os
import random

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']


intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)

# load phrases from phrases.txt (one phrase per line). Falls back to defaults.
def load_phrases(path=None):
    if path is None:
        base = os.path.dirname(__file__)
        path = os.path.join(base, "phrases.txt")
    try:
        with open(path, "r", encoding="utf-8") as f:
            phrases = [line.strip() for line in f if line.strip()]
        if not phrases:
            raise ValueError("no phrases found")
        return phrases
    except Exception:
        return [
            "has joined",
        ]

PHRASES = load_phrases()

def random_message(display_name):
    phrase = random.choice(PHRASES)
    return f"{display_name} {phrase}"

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.name != "Secret Coup":
            if member.display_name == "GEEK Music":
                #do not send message for GEEK Music
                return
            else:
                message = random_message(member.display_name)
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            requests.post(url, data={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message
            })

client.run(DISCORD_TOKEN)
