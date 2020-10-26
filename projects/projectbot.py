import telebot        # program will work with "pytelegrambotapi" library

# special token from botfather
token = '1083328649:AAG_ePjYzgENPi6gNeKiB-ce9W8QYTg0P1k'
# creating example of bot
bot = telebot.TeleBot(token)
# getting id of chat(group) by the name
GROUP_ID = '@botnomattest'
# the list of filthy words which will be deleted
blacklist = ['далб', 'даун', 'ля', 'мал', 'бла', 'тупой', 'дурак']
# sorry for filthy woords, but I did it for the right way:)


# interception of other people's messages by 'message_handler' command
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # searching filthy words in order by function 'def'
    for x in blacklist:
        if(x in message.text):
            # if filthy words are found, it will delete them
            bot.delete_message(message.chat.id, message.message_id)
        else:
            pass
# programm works without stopping by 'infinity_polling' command
if __name__ == "__main__":
    bot.infinity_polling(none_stop=True)
