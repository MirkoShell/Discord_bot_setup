# kill 1 to get new IP address
import os
import discord
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()


db["sui-vid"] = "https://replit.com/@kb0207/Encourage-bot#sui-siu.mp4"

sad_words = [
    "sad",
    "depressed",
    "unhappy",
    "angry",
    "miserable",
    "depressing",
    "awful",
    "pathetic",
    "heartbreak",
    "die",
    "loser",
    "fail",
]

starter_encouragements = [
    "Cheer up!", "Hang in there.", "You are a great person / bot!"
]

if "responding" not in db.keys():
    db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragment(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('#inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('#sui'):
      await message.channel.send('https://media.tenor.com/t3eKwU-odDgAAAPo/sui-siu.mp4')
      
      await message.channel.send("suiiiiiiiiiiiiiiiiii")
    if msg.startswith('#hello'):
        await message.channel.send('''Sup nerds?
Wanna get encouragement? Go ahead and try me.
Click here for detailed explanation for using me: 
https://github.com/kb0207/Encourage-bot_instructions#readme

Here are some of the things I listen to:

#inspire : To get a random encouraging quote
#new "your quote" : To add your own quote
#list : To view the added quoted
#del "number of the quote" : To delete a quote that is already added''')

    if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options = options + db["encouragements"]

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if msg.startswith("#new"):
        encouraging_message = msg.split("#new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if msg.startswith("#del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("#del", 1)[1])
            delete_encouragment(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("#list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    # if msg.startswith("#responding"):
    #     value = msg.split("#responding ", 1)[1]

    #     if value.lower() == "true":
    #         db["responding"] = True
    #         await message.channel.send("Responding is on.")
    #     else:
    #         db["responding"] = False
    #         await message.channel.send("Responding is off.")


keep_alive()

my_secret = os.environ['TOKEN']
client.run(my_secret)


