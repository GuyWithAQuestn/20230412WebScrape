# for Discord
import requests
import os
import discord
import asyncio



def sendDiscordMessage(message_to_user):
    from discord import SyncWebhook
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#    webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/957773195652513823/NLyDChYImOy-XIzuMNJEhhtAM1u2L-edgNgT1QqvAFL1IzZ5OHJr7-69TigLr513Buw1", adapter=RequestsWebhookAdapter())
    webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/957773195652513823/NLyDChYImOy-XIzuMNJEhhtAM1u2L-edgNgT1QqvAFL1IzZ5OHJr7-69TigLr513Buw1")
    webhook.send("Haircut Bot: " + message_to_user)

    return 0

def mainBody(message_to_user):

    sendDiscordMessage(message_to_user)

    return 0