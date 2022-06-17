import discord
import aiohttp

from discord.ext import commands
from utils.DbHandler import DbHandler

class MyBot(commands.Bot, DbHandler):
    def __init__(self):
        super().__init__(
            command_prefix="?", intents=discord.Intents.all(), application_id= # id du bot
        )
        self.guild_id = # Your guild ID
        self.initial_extensions = [
            "cogs.Rpg",
        ]
        DbHandler.__init__(self, "db.json")

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)
        await bot.tree.sync(guild=discord.Object(id=self.guild_id))

    async def close(self):
        await super().close()

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")


bot = MyBot()
bot.run("TOKEN")