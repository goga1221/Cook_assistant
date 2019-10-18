import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, ConversationHandler, CommandHandler
from telegram.ext import MessageHandler, RegexHandler, Filters
from handler import welc_user, get_recipe, send_help, get_favorite, own_recipe_add, own_recipe_get_ingr, own_recipe_full, own_recipe_skip
from settings import PROXY, USER_EMOJI

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


USER_EMOJI = [':smiley_cat:',':smiling_imp:',':panda_face:',':dog:',  ':smile:']

def main():
    cook_bot = Updater('840072894:AAH3pR7cMN94E4SFwJNP6dMiUHAJefMvrm4', request_kwargs=PROXY)
    logging.info('Бот запускается')

    disp=cook_bot.dispatcher
    disp.add_handler(CommandHandler("start", welc_user))
    disp.add_handler(CommandHandler("recipe", get_recipe))
    disp.add_handler(RegexHandler('^(Получить случайный рецепт)$', get_recipe))
    disp.add_handler(RegexHandler('^(Избранное)$', get_favorite))
    disp.add_handler(RegexHandler('^(Справка)$', send_help))

    own_recipe=ConversationHandler(
        entry_points=[RegexHandler('^(Добавить свой рецепт)$', own_recipe_add)],
        states={
            "ingredient": [MessageHandler(Filters.text, own_recipe_get_ingr)],
            "formula": [MessageHandler(Filters.text, own_recipe_full),]},
        fallbacks=[]

    )
    disp.add_handler(own_recipe)
    

    cook_bot.start_polling()
    cook_bot.idle()

if __name__=="__main__":
    main() 
