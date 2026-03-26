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

name_map = {
    "Hunterly": "Hunter",
    "SPKross": "Jacob",
    "Heath": "Heath",
    "Currahee901": "Tommy",
    "Futsch": "Selim",
    "Jamirous": "Jan",
    "RedLeg_198": "Tommy",
    "snuslas": "Niklas",
}

name_messages = {
    "Hunterly": "{name}s here, time to get this bread",
    "SPKross": "{name} the absolute legend has arrived",
    "Heath": "come commit war crimes with {name}",
    "Currahee901": "God help us, {name} has entered the building",
    "Futsch": "{name} is in the house",
    "Jamirous": "{name} is here to loot in the blue zone",
    "RedLeg_198": "{name} is patiently waiting in discord",
    "snuslas": "Gruess Gott, {name} is here",
}

communist_sayings = [
    "goopatiy goopatiy",
    "lets get gooping",
    "a war chrime a day keeps the bourgeoisie away",
    "Religion is the opium of the people.",
    "Goop is greater than loot.",
    "goop is the only way to win",
    "arc raiders are the true proletariat",
    "wanna team up?",
    "Hey!, Dont shoot!",
]

pubg_sayings = [
    "lets play some classic PUBG",
    "god bless PUBG",
    "pew pew",
    "arm the tactical frying pan",
]

hunt_sayings = [
    "No bounty left for the ruling class",
    "Hunt together, die together",
    "The bayou belongs to the people",
    "The revolution will not be extracted",
    "One bounty. One people",
]

def get_name(display_name):
    return name_map.get(display_name, display_name)

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.name == "Secret Coup":
            return
        if member.display_name == "GEEK Music":
            return
        name = get_name(member.display_name)
        if after.channel.name == "Arc Commies":
            saying = random.choice(communist_sayings)
            message = f"{name} just joined {after.channel.name}. {saying}"
        elif after.channel.name == "Peoples Battleground":
            saying = random.choice(pubg_sayings)
            message = f"{name} just joined {after.channel.name}. {saying}"
        elif after.channel.name == "Peoples Hunt Showdown":
            saying = random.choice(hunt_sayings)
            message = f"{name} just joined {after.channel.name}. {saying}"
        elif member.display_name in name_messages:
            message = name_messages[member.display_name].format(name=name)
        else:
            saying = random.choice(communist_sayings)
            message = f"{name} just joined {after.channel.name}. {saying}"
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        })

if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
