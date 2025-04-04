import discord
import os
import datetime

# Replace with your bot token and desired notes directory
TOKEN = os.environ.get("DISCORD_BOT_TOKEN")  # Make sure to set this environment variable
if TOKEN is None:
    raise ValueError("Please set the DISCORD_BOT_TOKEN environment variable.")
BASE_DIR = os.environ.get("notedir") # Base directory for notes
template_dir = os.environ.get("template_dir") # Directory for templates
if BASE_DIR is None:
    raise ValueError("Please set the notedir environment variable.")

# Set up the Discord client with required intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # Avoid processing messages sent by the bot itself
    if message.author == client.user:
        return

    # Optionally, filter for a specific channel
    if message.channel.name != "notes":
        return

    # Get the current date and time
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m-%B")  # e.g., "04-April"
    date_str = now.strftime("%Y-%m-%d")
    weekday = now.strftime("%A")

    # Create the directory structure
    year_dir = os.path.join(BASE_DIR, year)
    month_dir = os.path.join(year_dir, month)
    
    # Create directories if they don't exist
    os.makedirs(month_dir, exist_ok=True)

    # Define the file name with the full date and weekday
    file_name = f"{date_str}-{weekday}.md"
    file_path = os.path.join(month_dir, file_name)

    # If the file does not exist yet, create it with the template
    if not os.path.exists(file_path):
        if os.path.exists(template_dir):        
            # Read the template content and replace the date placeholder
            with open(template_dir, "r", encoding="utf-8") as f:
                template_content = f.read()
            
            # Replace the date placeholders
            current_date = now.strftime("%Y-%m-%d %H:%M:%S")
            template_content = template_content.replace("<% tp.file.creation_date() %>", current_date)
            template_content = template_content.replace("<%tp.date.now(\"YYYY-MM-DD\")%>", date_str)
            
            # Write the modified template back to the file
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(template_content)

    # Append the new note with a timestamp header
    note_content = message.content
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"{note_content}\n")

    # Optionally, send a confirmation message back to the channel
    await message.channel.send("Note appended to today's file!")
# Start the bot
client.run(TOKEN)