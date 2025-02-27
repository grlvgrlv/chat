import requests
import pandas as pd
from bs4 import BeautifulSoup
from discord import Client
import asyncio
from config import DISCORD_BOT_TOKEN
from utils import save_with_history

def fetch_bitcointalk_data():
    url = 'https://bitcointalk.org/index.php?board=159.0'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    posts = []
    for post in soup.find_all('div', class_='subject'):
        post_title = post.get_text(strip=True)
        posts.append({'PostTitle': post_title, 'Sentiment': 'Neutral'})

    df = pd.DataFrame(posts)
    save_with_history(df, 'bitcointalk_sentiment.csv')


async def fetch_discord_data():
    client = Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        messages = []
        for guild in client.guilds:
            for channel in guild.text_channels:
                async for message in channel.history(limit=100):
                    messages.append({'Channel': channel.name, 'Message': message.content, 'Sentiment': 'Neutral'})

        df = pd.DataFrame(messages)
        save_with_history(df, 'discord_sentiment.csv')
        await client.close()

    await client.start(DISCORD_BOT_TOKEN)


def main():
    fetch_bitcointalk_data()
    asyncio.run(fetch_discord_data())


if __name__ == "__main__":
    main()
