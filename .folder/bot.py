from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import bot_command as b



updater = Updater('5835810655:AAHADFcvbV_LGtZ2TMxIEl4gq1ys5whAhj8')

updater.dispatcher.add_handler(CommandHandler("hi", b.hi_command))
updater.dispatcher.add_handler(CommandHandler("time", b.time_command))
updater.dispatcher.add_handler(CommandHandler("help", b.help_command))
# updater.dispatcher.add_handler(CommandHandler("sum", sum_command))


updater.start_polling()

updater.idle()