import discord
from discord.ext import commands

# Define intents
intents = discord.Intents.default()

# Create a bot instance with intents and a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Define a command to get the latency
@bot.command()
async def ping(ctx):
    print('Ping command received!')
    # Calculate the latency
    latency = round(bot.latency * 1000)  # latency in milliseconds
    
    # Send a message with the latency
    await ctx.send(f'Pong! Latency is {latency}ms')

# Event to confirm when the bot is ready and online
@bot.event
async def on_ready():
    print('Bot is online!')

# Run the bot with your Discord bot token

bot.run('TOKEN HERE')
