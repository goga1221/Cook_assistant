import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, ConversationHandler, CommandHandler
from telegram.ext import MessageHandler, RegexHandler, Filters
from handler import welc_user, get_recipe, send_help, get_favorite, own_recipe_add, own_recipe_get_ingr, own_recipe_full, own_recipe_skip,get_rec_by_name
from settings import USER_EMOJI
from proxy import TOKEN, PROXY
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    cook_bot = Updater(TOKEN, request_kwargs=PROXY)
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

    find_rec_by_name=ConversationHandler(
        entry_points=[RegexHandler('^(Найти рецепт по названию)$', get_rec_by_name)],                  
        states={},
        fallbacks=[]
    )
    disp.add_handler(find_rec_by_name)
 
    cook_bot.start_polling()
    cook_bot.idle()

if __name__=="__main__":
    main() 
#TODO Функция поиска рецепта по ингредиентам
'''
 find_rec_by_ingr=ConversationHandler(
        entry_points=[RegexHandler('^(Найти рецепт по ингредиентам)$', get_rec_by_ingr)],
        states={
            "ingredient": [MessageHandler(Filters.text, get_ingr),]},            
        fallbacks=[]
    )
    disp.add_handler(find_rec_by_ingr)
'''  