import discord
import random

# Create an instance of a client, used to interact with Discord
intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content
client = discord.Client(intents=intents)

# Replace with your bot's token from Discord Developer Portal
TOKEN = 'MTI4OTkzNjExMjkyMzQ0NzM2OA.GGdnM3.C3UBXIOGm7EEu2wUb5ettgm7dSADkD4LCY3NF0' 

# Function to calculate the attack and defense result
def calculate_attack_result(active_percentage, passive_percentage):
    X = active_percentage + 50 - passive_percentage
    crit_value = X // 4

    # Roll 1d100
    roll = random.randint(1, 100)

    # Determine success, crit, and crit fail
    if roll <= crit_value:
        result = "Critical Success"
    elif roll <= X:
        result = "Success"
    elif roll >= 95:
        result = "Critical Fail"
    else:
        result = "Fail"

    return X, crit_value, roll, result

# Event for when the bot is ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Event for when a message is sent
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    print(f'Received message: {message.content}')  # Debugging line

    # Respond to specific command
    if message.content.startswith('!dr'):
        try:
            # Example command format: !dr 70 30
            parts = message.content.split()
            active_percentage = int(parts[1])
            passive_percentage = int(parts[2])

            # Calculate results
            X, crit_value, roll, result = calculate_attack_result(active_percentage, passive_percentage)

            # Create a response
            response = (
                f"**Crit Value**: {crit_value}\n"
                f"**Roll (1d100)**: {roll}\n"
                f"**Result**: {result}"
            )

            await message.channel.send(response)

        except (IndexError, ValueError):
            await message.channel.send("Please provide valid input. Example: `!dr (active) (passive)`")

# Run the bot
client.run(TOKEN)
