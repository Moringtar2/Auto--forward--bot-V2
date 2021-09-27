#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton('🗣️Group', url='t.me/AD_BOTZ'),
        InlineKeyboardButton('📢Updates', url='t.me/ONLY_CODES'),
        InlineKeyboardButton('📃Bot List', url='https://t.me/ONLY_CODES'),
    ],[
        InlineKeyboardButton('🖥️  Movie Groop 🖥️', url='https://t.me/ADMOVEIAD')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/684583157d50b4882ffc3.jpg",
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.private & filters.command(['help']))
async def help(client, message):
    buttons = [[
        InlineKeyboardButton('🗣️Group', url='t.me/AD_BOTZ'),
        InlineKeyboardButton('📢Updates', url='t.me/ONLY_CODES'),
        InlineKeyboardButton('🔐Close', callback_data='close_btn')
        ],[
        InlineKeyboardButton('🖥️ Movie Groop 🖥️', url='https://t.me/ADMOVEIAD')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/684583157d50b4882ffc3.jpg",
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.private & filters.command(['about']))
async def about(client, message):
    buttons = [[
        InlineKeyboardButton('🗣️Group', url='t.me/AD_BOTZ'),
        InlineKeyboardButton('📢Updates', url='t.me/ONLY_CODES'),
        InlineKeyboardButton('🔐Close', callback_data='close_btn')
        ],[
        InlineKeyboardButton('🖥️ Movie Groop 🖥️', url'https://t.me/ADMOVEIAD')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/684583157d50b4882ffc3.jpg",
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
