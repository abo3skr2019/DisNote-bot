import os
import sys

def load_env_file(filepath):
    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                key, sep, value = line.partition('=')
                if sep:  # Only proceed if '=' found
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    if key in ["DISCORD_BOT_TOKEN", "notedir", "template_dir"]:
                        os.environ[key] = value
    except FileNotFoundError:
        print(f".env file not found at {filepath}")

if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(__file__)

env_path = os.path.join(base_path, '.env')
load_env_file(env_path)
print("File path:", env_path)
print("Environment variables loaded from .env file.")
print("DISCORD_BOT_TOKEN:", os.environ.get("DISCORD_BOT_TOKEN"))
print("notedir:", os.environ.get("notedir"))
print("template_dir:", os.environ.get("template_dir"))