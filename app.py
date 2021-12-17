from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext, Filters
from telegram.update import Update
from telegram.files.inputmedia import InputMediaVideo
from telegram.bot import Bot
import random
import os
from moviepy.editor import *
import time



def medianame():
    mylist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
              "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    randomname = random.choices(mylist, k=12)
    global Vname
    global Fname
    Vname = ""
    for i in randomname:
        Vname += i
    Fname = Vname+".mp4"


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Send the video which you want to Edit...")



def downloader(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Please wait Processing the video...")
    medianame()
    downloader.videoname=Fname
    with open(Fname, 'wb') as f:
        try:
            context.bot.get_file(update.message.video).download(out=f)
        except:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Server failed to download Because media is large size Apology for that please send me one more time")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Send a video cutting duration in seconds ex. '5-10' this format ")




def replywithvideo(update: Update, context:CallbackContext):
    time=update.message.text
    string=""
    for i in time:
        try:
            if type(int(i)) == int:
                pass
            else:
                String+="j"
        except:
            string+=i
    if len(string) == 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Working on it...")
        duration=time.split("-")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Just Wait 10 to 15 Second" )
        start = duration[0]
        end = duration[1]
        try:
            video = VideoFileClip(downloader.videoname).subclip(start, end)
            video.write_videofile(downloader.videoname, codec='libx264')
        except:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry Server is Down!!")
        bot.send_video(chat_id=update.message.chat_id, video=open(downloader.videoname, 'rb'), supports_streaming=True, timeout=10000)
        os.remove(downloader.videoname)
        bot.send_message(chat_id=update.effective_chat.id, text="If you like my work you can follow me for more bots 😊")
        bot.send_message(chat_id=update.effective_chat.id, text="https://www.instagram.com/mahendrakaperavenollu/?hl=en")

    else:
        directories=os.listdir()
        Winput=0
        for i in directories:
            if i.endswith(".mp4"):
                Winput=1
            else:
                pass

        if Winput == 1:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Something wrong in your input bro...")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Format should be 0-10, 10-20 like this.")
        elif Winput == 0:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Send me a video for Edit...")



if __name__ == '__main__':

    BOT_TOKEN = <telegram bot token>
    bot = Bot(<telegram Bot token>)

    updater = Updater(BOT_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.video, downloader))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, replywithvideo))

    updater.start_polling()
    updater.idle()