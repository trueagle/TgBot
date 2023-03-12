import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
token='your bot token'
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
    chat_id='your id chat'
    bot.send_message(chat_id=chat_id, text=str)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "Каталог":
            button_keyboard = InlineKeyboardMarkup(row_width=2)
            callback_button = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button2 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button3 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button4 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button5 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button6 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button7 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")  
            callback_button8 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button9 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")          
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

        
        
        
#note that the price parameter is passed without quotes
        if call.data == 'Табак':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)          
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")            
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")

        if call.data == 'Сигареты':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            
        if call.data == 'Сумки':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)          
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")     

        if call.data == 'Кисет для табака':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)     
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")

        
        if call.data == 'Дождевики':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)     
            show_item(call,'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")


        if call.data == 'Гель для душа':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)     
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")  
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price") 


        if call.data == 'Презервативы':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)     
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call, 'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")  

                

        if call.data == 'Glo':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)     
            show_item(call,'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call,'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")

        
        if call.data == 'Жевательная Резинка':            
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)     
            show_item(call,'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call,'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")            
            show_item(call,'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")
            show_item(call,'the path to the directory where the file is located file.jpg', "ITEM|product name", "price")

        if call.data.split('|')[0] == 'ITEM':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            msg=bot.send_message(
                chat_id=call.message.chat.id,
                text="Оставьте контактные данные, с вами свяжутся",
                parse_mode='Markdown')
            bot.register_next_step_handler(msg, providing_name_callback, call.data.split('|')[1])


        elif call.data == 'Назад':            
            button_keyboard = InlineKeyboardMarkup(row_width=2)
            callback_button = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button2 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button3 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button4 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button5 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button6 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button7 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")  
            callback_button8 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")
            callback_button9 = InlineKeyboardButton(text="your category name", callback_data="name of the category button")          
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
                
if __name__ == '__main__':
 bot.infinity_polling(timeout=10, long_polling_timeout = 5)




