# Workshop Discord RPG
Bonjour à tous et bienvenue dans ce workshop.
Aujourd'hui on va voir comment faire un petit RPG en python sur Discord

**LES FICHIERS SONT PRESENTS DANS LE REPO, NE PAS OUBLIER DE FORK ET CLONE POUR LES RÉCUPERER**

## Installation
### Python
pour l'installation, on va commencer par installer python si ce n'est pas déjà fait
```sh
sudo dnf install python3.8 (pour fedora)
sudo apt-get install python3.8 (pour ubuntu)
```
### Pip
De même pour pip (gestionnaire python) si ce n'est pas déjà fait

```
python -m ensurepip --upgrade
```
Si cela ne fonctionne pas, installer pip à l'aide du script :
 https://bootstrap.pypa.io/get-pip.py.

### Discord.py

Puis installer discord.py qui va nous servir a communiquer avec le serveur Discord

```sh
pip install discord.py @ git+https://github.com/Rapptz/discord.py@f6a74f74a7aed0879fc086805eae8873e745d0ea
```

On va donc pouvoir commencer !

## Setup du bot

Pour ceux qui n'était pas la ce matin, je vous dirige sur ce README.md afin de pouvoir setup votre bot sans difficulté : *lien du premier workshop*

Une fois cela fait, on va télécharger le fichier ```main.py``` et compléter avec les infos de votre bot

Une fois fini, on va créer notre database en JSON qui va permettre de stocker nos personnages

Télécharger le fichier ```db.json``` et placer le dans la racine du repo puis ```DBHandler.py``` ainsi que ```Types.py```

Ces fichiers vont servir à transformer notre base JSON en objet afin de faciliter l'accès au info que la database contient

Le fichier ```Types.py``` nous sert a définir ce que contient notre personnage, etc...

On va pouvoir commencer à créer nos premières fonctions !

## Start

Notre première fonction va nous permettre de créer un personnage si nous en avons pas. Le moyen de relier le personnage au compte discord qui le possède sera la variable ```owner``` qui va contenir l'identifiant du compte discord a qui appartient le personnage.

### Exercice 1 : /start

Ecrire une slash command qui va créer un personnage dans la db avec comme paramètres :  un nom et un genre. Ne pas oublier de gérer le cas ou il à déjà un personnage

![](https://cdn.discordapp.com/attachments/768415712498024448/986989287948029982/unknown.png)

![](https://cdn.discordapp.com/attachments/768415712498024448/986989578562961548/unknown.png)

> Pas obligatoire de faire les paramètres (choices) mais cela doit être une slash command

Pour s'aider :
https://discordpy.readthedocs.io/en/latest/api.html
ou exemple de slash command :
```py
import discord
from discord import app_commands
from discord.ext import commands

class your_command(commands.Cog):

    def __init__(self, bot : commands.Bot):
    self.bot = bot

    @app_commands.command(name = "your_command", description = "Returns Hello World!")
    @app_commands.describe(name = "Your name")
    async def your_command(self, interaction : discord.Interaction, name : str):
        await interaction.response.send_message(f"Hello World, {name}!", ephemeral = True)

async def setup(bot : commands.Bot):
    await bot.add_cog(your_command(bot), guilds = [discord.Object(id = 123)])
```

### /Stats

On va ensuite faire une fonction qui permet de consulter ses stats ainsi que son équipement

Elle prendra pas d'argument, il va juste falloir vérifier que l'auteur du message a bien un personnage et afficher celui ci

![](https://cdn.discordapp.com/attachments/768415712498024448/986992674013839371/unknown.png)


### /Battle

On attaque le gros morceau.
Dans chaque player sera stocké l'ennemie avec lequel il se bat.
On va créer un embed message (https://cog-creators.github.io/discord-embed-sandbox/) avec deux bouttons en dessous pour dire qu'on va l'attaquer ou non. Essayez de pensez à toute les éventualités (remettre un monstre lorsque celui ci est mort, verifier si le joueur est mort, ...)

![](https://cdn.discordapp.com/attachments/777229041736220703/987004716502368266/unknown.png)
![](https://cdn.discordapp.com/attachments/777229041736220703/987004896601591888/unknown.png)

> (L'affichage est buggé mais je vous fait confiance pour pas faire la même bétise)

### A vous !

On va devoir implementer les fonctions suivantes :
- Se soigner
- Augmenter ses caractéristiquess
- Ajouter des activités pour gagner de l'xp (aller miner par exemple, ...)


Et aussi tout ce qu'il vous passe par la tête !

Pour voius inspirer, je vous done le lien d'un discord qui est le meilleur (selon moi) bot "rpg" :
https://discord.gg/thesystemdungeons
