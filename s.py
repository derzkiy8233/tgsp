from config import *
from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
import sys
client = Client('ghoul-session', api_id, api_hash)

client.start()

client.stop()

print('Бот запущен. Пиши старт в тг')


@client.on_message(filters.regex('ez|Ez|EZ|eZ') & filters.me)
def ghoul_spam_handler(client, message):
    i = 1000
    while i > 0:
        try:
            client.send_message(message.chat.id, f'Only {i-1}for end! (FE3R)')
        except FloodWait as e:
            sleep(e.x)

        i -= 1
        sleep(0)        

    if(end_message != ''):
        client.send_message(message.chat.id, end_message)


@client.on_message(filters.regex('no|nO|No|NO') & filters.me)
bkb = 99
while bkb < 100:
    sleep(999999)

@client.on_message(filters.command(ghoul_table_command, prefixes=command_prefixes) & filters.me)
def ghoul_table_handler(client, message):
    i = 1000
    while i > 62:
        try:
            text = f'{i} - 7 = {i-7}'
            for j in range(1,10):
                text += f'\n{i-7*j} - 7 = {i-7*(j+1)}'
            message.edit_text(f'`{text}`')
            sleep(sleep_time_ghoul)
        except FloodWait as e:
            sleep(e.x)

        i -= 7

    if(end_message != ''):
        client.send_message(message.chat.id, end_message)


client.run()
