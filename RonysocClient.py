# -*- coding: utf-8 -*-
import os
import random
import socket
import re
import time

import botpy
from botpy import logging,  BotAPI

from botpy.message import Message, C2CMessage
from botpy.ext.cog_yaml import read
from botpy.ext.command_util import Commands

from Ronycoc import os_info_message
from Ronycoc import McStatus
from Ronycoc import determine_img

config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()

NULL_CHARACTER = ""

@Commands("os")
async def reply_os_info(api: BotAPI, message: Message, params=None):
    _log.info(params)
    await api.post_message(message.channel_id, content=os_info_message())
    return True

@Commands("status")
async def reply_mc_status(api: BotAPI, message: Message, params=None):
    _log.info(params)
    try:
        server = McStatus(message)
        await api.post_message(message.channel_id, content=await server.mc_satus_message())
    except ValueError:
        await api.post_message(message.channel_id, content="invalid host")
    except socket.gaierror:
        await api.post_message(message.channel_id, content="No tasks were successful. Is server offline?")
    except Exception as e:
        print(e)
        await api.post_message(message.channel_id, content="internal error")
    return True
    
@Commands("randint")
async def random_int(api: BotAPI, message: Message, params=None):
    _log.info(params)
    await api.post_message(message.channel_id, content=f"random number is: {random.randint(-2147483648,2147483647)}")

@Commands("determine")
async def determine(api: BotAPI, message: Message, params=None):
    if params == NULL_CHARACTER:
        random.seed(time.time())
        await api.post_message(message.channel_id, content="determine randomly")
        await api.post_message(message.channel_id, content=(
        f"<@!{random.choice(await api.get_guild_members(message.guild_id, limit=400))['user']['id']}> determine that you are")
        )
        await api.post_message(message.channel_id, image=determine_img(int(message.author.id)))
    elif params != NULL_CHARACTER:
        if re.match(r'<@!(\d+)>', params):
            await api.post_message(message.channel_id, content=f"{params} determine that you are")
            await api.post_message(message.channel_id, image=determine_img(int(message.author.id)))
        else:
            await api.post_message(message.channel_id, content="@ the person you want to detremine or not to determine randomly")
    return True

@Commands("help")
async def help(api: BotAPI, message: Message, params=None):
    await api.post_message(message.channel_id, content=
    "help list:\n"
    "/os to get os information\n"
    "/status <ip/host:(port)> to get minecraft server status\n"
    "/randint to get a random 32-bit signed integer\n"
    "/determine (@someone) to determine or determine randomly a person is a 0 or 1")
    return True
        
class Client(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_at_message_create(self, message: Message):
        _log.info(f"{self.robot.name}receive message {message.content}")
        handlers = [
            reply_os_info,
            reply_mc_status,
            random_int,
            determine,
            help,
        ]
        for handler in handlers:
            if await handler(api=self.api, message=message):
                return
        

if __name__ == "__main__":
    intents = botpy.Intents(public_guild_messages=True)
    client = Client(intents=intents, is_sandbox=True)
    client.run(appid=config["appid"], secret=config["secret"])
