# 05 Dec 2017 | Timerbot | Sourced from GitHub

#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Simple Bot to send timed Telegram messages.
# This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot and the JobQueue to send
timed messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Alarm Bot example, sends a message after a set time.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler
import logging

def callback_minute(bot, job):
    bot.send_message(chat_id='294207804', text='One message every minute')

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='I am a Bot!')
    bot.send_message(chat_id='294207804', text='I am a Bot!')

def main():
    """Run bot."""
    updater = Updater("470966108:AAFCiXEBTy_acBVSZ31tKAObEcbC6I9ug9Q")
    #dispatcher = updater.dispatcher

    #start_handler = CommandHandler('start', start)
    #dispatcher.add_handler(start_handler)

    updater.start_polling()

    j = updater.job_queue

    jb = j.run_repeating(callback_minute, interval=10, first=0)
    #jb = j.run_once(callback_minute, 10)
    #print(jb)

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    #updater.idle()


if __name__ == '__main__':
    main()
