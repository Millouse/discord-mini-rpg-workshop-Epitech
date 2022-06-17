import discord
from discord.ext import commands
from discord import app_commands, Interaction, Object, Embed
from discord.app_commands import Choice

from utils.Types import User

class buttonBattleHandler(discord.ui.View):
    # A completer pour les boutons

class Rpg(commands.Cog, description="Groupe de commande Divers"):
    def __init__(self, bot):
        self.bot = bot

    # Exemple de command ping
    @app_commands.command(name="ping", description="Répond avec \"Pong !\"")
    async def ping(self, ctx: Interaction):
        await ctx.response.send_message("Pong !")

    @app_commands.command(name="start", description="Créer votre personnage")
    async def start(self, ctx: Interaction):
        # code ici
        self.bot.save() # Sert à actualiser la database

    @app_commands.command(name="battle", description="Bats toi pour gagner de l'xp et de l'argent!")
    async def battle(self, ctx: Interaction):
        # code ici

    @app_commands.command(name="stats", description="Affiche vos stats")
    async def stats(self, ctx: Interaction):
        #code ici

    @app_commands.command(name="shop", description="Achete de l'équipement ici !")
    async def shop(self, ctx: Interaction):
        # code ici
        self.bot.save()

async def setup(bot):
    await bot.add_cog(Rpg(bot), guilds=[Object(id=bot.guild_id)])