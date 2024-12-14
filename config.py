#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8012673189:AAFyG4TRkK_N33ngPA-12DEhEW_Xfi6sBBI")
    API_ID = int(os.environ.get("API_ID", "25318125"))
    API_HASH = os.environ.get("API_HASH", "b29fb6a928e8b8a3308f8c2d3ba9cfb0")
    AUTH_USERS = "7376514183"

