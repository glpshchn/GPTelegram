import os
import sys

try:
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession
except Exception as err:
    print(err)
    print('Failed to import. Please install Telethon.')
    print('Run: pip install telethon')
    sys.exit()

print('You are now going to login, and the session string will be displayed on screen.')
print('You need to copy that for future use.')

input('Press [ENTER] to proceed')

api_id = input('Enter API ID: ')
api_hash = input('Enter API Hash: ')
phone = input('Enter your phone number in international format: ')

if not api_id or not api_hash or not phone:
    print('Missing required inputs. Quitting.')
    sys.exit()

with TelegramClient(StringSession(), int(api_id), api_hash).start(phone=phone) as client:
    print('\nSession string:\n')
    print(client.session.save())
    print('\nSave this string securely.')

print('To deactivate this session, go to Telegram App -> Settings -> Devices -> Active sessions.')
