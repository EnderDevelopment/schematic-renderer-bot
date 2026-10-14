import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="render", description="Render a schematic file")
@app_commands.describe(file="The schematic file to render")
async def render(interaction: discord.Interaction, file: discord.Attachment):
    if not file.filename.endswith(('.lite', '.litematic', '.schematic')):
        await interaction.response.send_message("Invalid file type. Please upload a .lite, .litematic, or .schematic file.", ephemeral=True)
        return
    
    # Process the file and render the schematic
    await interaction.response.send_message("Rendering the schematic...", ephemeral=True)
    # Add your rendering logic here
    
@bot.tree.command(name="schematic_panel", description="Create a schematic panel")
async def schematic_panel(interaction: discord.Interaction):
    # Create a schematic panel
    await interaction.response.send_message("Creating a schematic panel...", ephemeral=True)
    # Add your panel creation logic here

@bot.tree.command(name="schematic_thread_create", description="Create a new schematic thread")
@app_commands.describe(name="Name of the thread")
async def schematic_thread_create(interaction: discord.Interaction, name: str):
    # Create a new schematic thread
    await interaction.response.send_message(f"Creating a new schematic thread: {name}", ephemeral=True)
    # Add your thread creation logic here

@bot.tree.command(name="schematic_add", description="Add a schematic to a thread")
@app_commands.describe(thread_name="Name of the thread", file="The schematic file to add")
async def schematic_add(interaction: discord.Interaction, thread_name: str, file: discord.Attachment):
    if not file.filename.endswith(('.lite', '.litematic', '.schematic')):
        await interaction.response.send_message("Invalid file type. Please upload a .lite, .litematic, or .schematic file.", ephemeral=True)
        return
    
    # Add the schematic to the specified thread
    await interaction.response.send_message(f"Adding schematic to thread: {thread_name}", ephemeral=True)
    # Add your schematic addition logic here

bot.run(TOKEN)
