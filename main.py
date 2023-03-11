import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
token='5473856646:AAEX7xcjLKmsyhmOowhsG6X_TvvemSbkxTI'
bot=telebot.TeleBot(token)



@bot.message_handler(commands=["start"])
def any_msg(message):    
    start_keyboard = InlineKeyboardMarkup()
    callback_button = InlineKeyboardButton(text="Каталог", callback_data="Каталог")
    start_keyboard.add(callback_button)
    user_first_name = str(message.chat.first_name)
    bot.reply_to(message, f"Привет {user_first_name} ✌️ ты попал в RussianShop, переходи к покупкам!", reply_markup=start_keyboard)

def show_item(call, path_to_picture, cb_data, price):
    name = cb_data.split('|')[1]
    buy_keyboard = InlineKeyboardMarkup(row_width=1)
    callback_button = InlineKeyboardButton(text="Купить", callback_data=cb_data)
    callback_button2 = InlineKeyboardButton(text="Назад", callback_data="Назад")
    buy_keyboard.add(callback_button, callback_button2)
    photo = open(path_to_picture, 'rb')
    msg = bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=f'{name}\nЦена:{price}', reply_markup=buy_keyboard)



def providing_name_callback(msg, name):
    print(msg)
    str = f'username={msg.from_user.username}, text={msg.text}, item_name={name}'
    chat_id='-1001592487569'
    bot.send_message(chat_id=chat_id, text=str)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "Каталог":
            button_keyboard = InlineKeyboardMarkup(row_width=2)
            callback_button = InlineKeyboardButton(text="Табак", callback_data="Табак")
            callback_button2 = InlineKeyboardButton(text="Сигареты", callback_data="Сигареты")
            callback_button3 = InlineKeyboardButton(text="Сумки", callback_data="Сумки")
            callback_button4 = InlineKeyboardButton(text="Кисет для табака", callback_data="Кисет для табака")
            callback_button5 = InlineKeyboardButton(text="Гель для душа", callback_data="Гель для душа")
            callback_button6 = InlineKeyboardButton(text="Дождевики", callback_data="Дождевики")
            callback_button7 = InlineKeyboardButton(text="Презервативы", callback_data="Презервативы")  
            callback_button8 = InlineKeyboardButton(text="Glo", callback_data="Glo")
            callback_button9 = InlineKeyboardButton(text="Жевательная Резинка", callback_data="Жевательная Резинка")          
            button_keyboard.add(callback_button,
                         callback_button2,
                         callback_button3,
                         callback_button4,
                         callback_button5,
                         callback_button6,
                         callback_button7,
                         callback_button8,
                         callback_button9)
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Выбери Категорию",
                reply_markup=button_keyboard)

        
        
        
        
        if call.data == 'Табак':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)          
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Bali Shag.jpg', "ITEM|Bali Shag Halfzware", 8500)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Bali Nature.jpg', "ITEM|Bali Nature", 8500)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Dark Chocolate.jpg', "ITEM|Dark Chocolate", 6500)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Vanilla Choice.jpg', "ITEM|Vanilla Choice", 6500)            
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Aromatic Choice.jpg', "ITEM|Aromatic Choice", 6500)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Virginia Blend.jpg', "ITEM|Virginia Blend", 6500)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Cherry.jpg', "ITEM|Cherry", 6500)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Pandan.jpg', "ITEM|Pandan", 6500)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Exotic.jpg', "ITEM|Exotic", 6500)

        if call.data == 'Сигареты':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Captain Black Grape.jpg', "ITEM|Captain Black\nGrape", 4000)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Chapman.jpg', "ITEM|Chapman", 3500)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Parlament Silver.jpg', "ITEM|Parlament Silver", 3000)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Kent Switch.png', "ITEM|Kent Switch", 2500)
            
        if call.data == 'Сумки':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)          
            show_item(call, '/Users/artemarestov/Documents/russhop/img/bag black.jpg', "ITEM|Сумка Поясная\nЧерная", 6000)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/bag grey.jpg', "ITEM|Сумка Поясная\nСерая", 6000)     

        if call.data == 'Кисет для табака':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)     
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Кисет.jpg', "ITEM|Кисет для табака", 7000)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Black.jpg', "ITEM|Кисет для табака\nBlack", 7000)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Grey.jpg', "ITEM|Кисет для табака\nGrey", 7000)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Brown.jpg', "ITEM|Кисет для табака\nBrown", 7000)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Dark Blue.jpg', "ITEM|Кисет для табака\nDark Blue", 7000)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/White.jpg', "ITEM|Кисет для табака\nWhite", 7000)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Dark Grey.jpg', "ITEM|Кисет для табака\nDark Grey", 7000)

        
        if call.data == 'Дождевики':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)     
            show_item(call,'/Users/artemarestov/Documents/russhop/img/Дождевик.jpg', "ITEM|Дождевик", 1000)


        if call.data == 'Гель для душа':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)     
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Old Spice Astronaut.jpg', "ITEM|Old Spice\nAstronaut\n400ml", 5000)  
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Old Spice KrakenGard.jpg', "ITEM|Old Spice\nKrakenGard\n400ml", 5000)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Old Spice TigerClaw.jpg', "ITEM|Old Spice\nTigerClaw\n400ml", 5000)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Old Spice WhiteWater.jpg', "ITEM|Old Spice\nWhiteWater\n400ml", 5000) 


        if call.data == 'Презервативы':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)     
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Contex Lights.jpg', "ITEM|Contex Lights\n12шт", 7000)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Contex Relief.jpg', "ITEM|Contex Relief\n12шт", 7000)
            show_item(call, '/Users/artemarestov/Documents/russhop/img/Durex Elite.jpg', "ITEM|Durex Elite\n12шт", 9000)  

                

        if call.data == 'Glo':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)     
            show_item(call,'/Users/artemarestov/Documents/russhop/img/Glo Black.png', "ITEM|Glo Black", 10000)
            show_item(call,'/Users/artemarestov/Documents/russhop/img/Glo Blue.jpg', "ITEM|Glo Blue", 10000)

        
        if call.data == 'Жевательная Резинка':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)     
            show_item(call,'/Users/artemarestov/Documents/russhop/img/Orbit.jpg', "ITEM|Orbit", 500)
            show_item(call,'/Users/artemarestov/Documents/russhop/img/Eclipse Ice Berry.jpg', "ITEM|Eclipse Ice Berry", 500)            
            show_item(call,'/Users/artemarestov/Documents/russhop/img/Eclipse Mint.jpg', "ITEM|Eclipse Mint", 500)
            show_item(call,'/Users/artemarestov/Documents/russhop/img/Mentos.jpg', "ITEM|Mentos", 3000)

        if call.data.split('|')[0] == 'ITEM':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            msg=bot.send_message(
                chat_id=call.message.chat.id,
                text="Оставьте контактные данные, с вами свяжутся",
                parse_mode='Markdown')
            bot.register_next_step_handler(msg, providing_name_callback, call.data.split('|')[1])


        elif call.data == 'Назад':            
            # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        
            
            button_keyboard = InlineKeyboardMarkup(row_width=2)
            callback_button = InlineKeyboardButton(text="Табак", callback_data="Табак")
            callback_button2 = InlineKeyboardButton(text="Сигареты", callback_data="Сигареты")
            callback_button3 = InlineKeyboardButton(text="Сумки", callback_data="Сумки")
            callback_button4 = InlineKeyboardButton(text="Кисет для табака", callback_data="Кисет для табака")
            callback_button5 = InlineKeyboardButton(text="Гель для душа", callback_data="Гель для душа")
            callback_button6 = InlineKeyboardButton(text="Дождевики", callback_data="Дождевики")
            callback_button7 = InlineKeyboardButton(text="Презервативы", callback_data="Презервативы")  
            callback_button8 = InlineKeyboardButton(text="Glo", callback_data="Glo")
            callback_button9 = InlineKeyboardButton(text="Жевательная Резинка", callback_data="Жевательная Резинка")          
            button_keyboard.add(callback_button,
                         callback_button2,
                         callback_button3,
                         callback_button4,
                         callback_button5,
                         callback_button6,
                         callback_button7,
                         callback_button8,
                         callback_button9)                                       
            bot.edit_message_reply_markup(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,                                
                reply_markup=button_keyboard)
                
if __name__ == '__main__':
 bot.infinity_polling(timeout=10, long_polling_timeout = 5)




