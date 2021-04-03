"""
HalpyBOT v1.4

announcer.py - Client announcement handler

Copyright (c) 2021 The Hull Seals,
All rights reserved.

Licensed under the GNU General Public License
See license.md

This module is due for a rewrite, and not documented

"""

import pydle
import logging

from . import message_builder as mb


annList = {
    # Cases
    "CODEBLACK": mb.codeblack,
    "PC": mb.pc,
    "XB": mb.xb,
    "PS4": mb.ps,
    "PLTERR": mb.plterr,
    "XBFISH": mb.kingfisher_xb,
    "PCFISH": mb.kingfisher_pc,
    "PSFISH": mb.kingfisher_ps,
    "PLTERRFISH": mb.kingfisher_plterr,
    # Other
    "PPWK": mb.ppwk,
}

class AnnouncerContext:
    def __init__(self, bot: pydle.Client, channel: str, sender: str):
        self.bot = bot
        self.channel = channel
        self.sender = sender

async def on_channel_message(bot: pydle.Client, channel: str, sender: str, message: str):
    # Seperate arguments
    parts = message.split(" -~~- ")
    anntype = parts[0]
    args = parts[1:]
    ctx = AnnouncerContext(bot, channel, sender)
    if anntype in annList:
        logging.info(f"NEW ANNOUNCER WEBHOOK PAYLOAD FROM {sender}: {message}")
        return await annList[anntype](ctx, args)
    else:
        return
