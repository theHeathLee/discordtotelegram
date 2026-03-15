# Discord to Telegram

A bot that notifies a Telegram group when someone joins a Discord voice channel. Built for a friend group — when someone hops into Discord, everyone gets pinged in Telegram so they know it's time to join.

## What it does

- Watches for voice channel joins in a Discord server
- Sends a notification to a Telegram group chat
- Supports custom messages per person (e.g. "All Rise for King Heath")
- Ignores specific channels (e.g. Secret Coup) and bots (e.g. GEEK Music)

## Setup

### Prerequisites

- Python 3.x
- A Discord bot token with **Server Members Intent** enabled
- A Telegram bot token (from [@BotFather](https://t.me/BotFather))
- The Telegram chat ID of your group

### Environment Variables

| Variable | Description |
|---|---|
| `DISCORD_TOKEN` | Your Discord bot token |
| `TELEGRAM_TOKEN` | Your Telegram bot token |
| `TELEGRAM_CHAT_ID` | The chat ID of your Telegram group |

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run

```bash
python discordtotelegram.py
```

## Deployment

This project is deployed on [Railway](https://railway.app). Pushing to `master` triggers a new production deployment.

For testing, a separate Railway service runs on the `develop` branch with a different Discord bot (pointing at a private test server) and `TELEGRAM_CHAT_ID` set to a personal chat — so test notifications don't reach the group.

## Adding a new person

Add an entry to `name_map` for their display name → friendly name, and optionally a custom message in `name_messages`:

```python
name_map = {
    "DiscordDisplayName": "Friendly Name",
}

name_messages = {
    "DiscordDisplayName": "{name} has entered the chat",
}
```
