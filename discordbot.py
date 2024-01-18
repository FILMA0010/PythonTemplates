# Simple Discord.py example
# Required packages: discord
# pip install discord.py
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is connected to Discord as {bot.user.name}")

@bot.slash_command(description="Simple Message Test Command") # Creates the slash command and add a description
async def hello(ctx): # after the "def" select the name of the slash command
    await ctx.send("Hello, world!")

@bot.slash_command(description="Simple Message Embed Test Command") # Creates the slash command and add a description
async def embed(ctx): # after the "def" select the name of the slash command
    embed = discord.Embed(
        title="Example Embed", # Embed Title
        description="This is an example embed.", # Embed Description
        color=discord.Color.blue() # Embed Color
    )
    embed.add_field(name="Field 1", value="Value 1", inline=False) # Adds a Field
    embed.add_field(name="Field 2", value="Value 2", inline=False) # Adds a field, inline=False = its below eachother, True means next to eachother
    await ctx.send(embed=embed) # Sends defined Embed

bot.run("YOUR_BOT_TOKEN") # Enter your discord bot token