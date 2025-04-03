# DisNote Bot

Did you ever need to jott something down real quick be it in a family gathering , work meeting ,etc and you don't have obsidian in your phone! or it just doesn't sync right, well i intoduce to you the DisNote bot it is A Discord bot that automatically saves messages from a specific channel into your daily Notes using your template, organizing them by year and month. Perfect for jotting down that quick note.

## Features

- Automatically captures messages from a designated "notes" channel
- Organizes notes into a hierarchical folder structure (Year/Month/Day)
- Supports template-based daily note creation
- Uses Markdown format for note files
- Handles date placeholders in templates

## Requirements

- Python 3.12 or higher
- Discord.py library

## Installation

1. Clone this repository
2. Install dependencies:
```sh
pip install discord
```

## Configuration

Create a `.env` file in the project root with the following variables:

```env
DISCORD_BOT_TOKEN="your_bot_token_here"
notedir="/path/to/your/daily notes/directory"
template_dir="/path/to/your/template/file.md"
```
for the paths since the python os package supports spaces but parses bash backslashes as path slashes so just use a space instead of placing the "\" from bash
## Usage

1. Create a Discord bot in their [dev portal](https://discord.com/developers/applications/)
2. in installation choose the bot scope and add the send messages permission  
3. in Bot Enable Message Content Intent & Copy your Token
4. go to Installation & copy your installation link
5. Invite the bot to your Discord server
6. Create a channel named "notes"
7. Run the bot:
```sh
uv run main.py
```
1. Any message sent in the "notes" channel will be automatically saved to a daily note file

## File Structure

Notes are organized as follows:
```
notedir/
├── 2024/
│   ├── 01-January/
│   │   ├── 2024-01-01-Monday.md
│   │   └── 2024-01-02-Tuesday.md
│   └── 02-February/
│       └── ...
```

## Template Support

The bot supports templates with the following placeholders:
- `<%tp.file.creation_date()%>` - Replaced with current date and time
- `<%tp.date.now("YYYY-MM-DD")%>` - Replaced with current date

## Roadmap
- Support all Templatr shortcodes
- Customize the File Structure
- go rewrite ?