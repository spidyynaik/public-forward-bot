import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "20349869"))
    API_HASH = os.environ.get("API_HASH", "875652bb0c7032c857d30ece89d13786")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6118227179:AAGbIDxYzRs5yMPGYGV5_STCO9c6Y0JT5-U")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "6050947612")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://tempvfy:MongoDB1432@vrfy.wbu5nnw.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "AQBCW23C6MQlLSVQbaw6YTLOiCzQ5MRyREYBWFemHIEtXnZNmSPR8V7XySC1AyFcoVTL6BxvOUoPs6mOzCdo_bYyqMFSq8nm60VMJ1rhbUDUP03sIQmOI_0q6z41QWFWeg2jytegXzFFX0AfGRqFIMj4sb-CLGPANu_tF4o2FMB3RP5cb4QfFu41RD1oYbnEIzuh-k2E91TCWTjHDRM5I2lTKdPoY5w_F_NfpZu7nubdtBdxWXdwkZUbkL98rSn_NTyE5acAwtePNPwFStjG3TYrwNxGwCFuUSBpbq7_DZ__Fjp_CfxHZQcZGMzu_2zY9xK9h_wCpTiAg6LQXt96sk-tAAAAAWiqIhwA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001954388479"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "SpidyForwarderBot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
