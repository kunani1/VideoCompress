# (c) @AbirHasan2005

from bot.get_cfg import get_config

class Config(object):
    # You can keep this default
    SESSION_NAME = "AH_HVEC_CompressBot"
    # Put MongoDB URL
    DATABASE_URL = "mongodb+srv://ksai:ksai@cluster0.kayzwoi.mongodb.net/cluster0?retryWrites=true&w=majority"
    # get a token from @BotFather
    TG_BOT_TOKEN = "5459584173:AAH5gFxLV-hQkspxROAvnh9eYdBNXT10MKY"
    # The Telegram API things
    APP_ID = "4483436"
    API_HASH = "8702509bba70a3637777f76083b2c440"
    LOG_CHANNEL = "-1001505809090"
    UPDATES_CHANNEL = "COMPRESSORBOTLOGS1"
     # Without `@` LOL
     # Get these values from my.telegram.org
    # array to store the channel ID who are authorized to use the bot
    AUTH_USERS = "1319693201"
           
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "/app/downloads"
    # Telegram maximum file upload size
    BOT_USERNAME = "kscompressorbot"
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = "https://placehold.it/90x90"
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = "None"
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR =  "▓"
    UN_FINISHED_PROGRESS_STR = "░"
    LOG_FILE_ZZGEVC = "Log.txt"
      # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = "False"
