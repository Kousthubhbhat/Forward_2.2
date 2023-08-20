import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "18274091"))
    API_HASH = os.environ.get("API_HASH", "97afe4ab12cb99dab4bed25f768f5bbc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2108427614:AAFgNBxwh8kOAAWu8Jyaqy1Puv3O5XCT7K8") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "BQAKhYPH1j5sgnYjq_Kus6I2rj70yd3QgIfkAsqLr2Ka_URaJy_69fFUYqWxc5yi_z8toVQZOSfM6jS1hyQ8VevVwSpBJipCUZtlbkZCimSKtRtPKK1IZc7SrXJaxWgc8EWdjnrMI7BNpVX5R8-3POtdauUoXRW2bpAy5KzP_XKrVu-4p2FWPe9w7djvb_buYeSrlLUhhHRjQ6Zyx2lY-AKxqqsnfGfDNst1RSVzXz18I_RW22iAkeFRGtb4k074j6Jb6xrkQ_PyzJ84GzmBUoBArurIw9I1fk8zbd34R0Hq3tJNg51Sxltcr7Wu84eIhSImsrKnJDQIDFogZbmgRfu9Tr70rAA") 
    OWNER_ID = os.environ.get("OWNER_ID", "1321137324")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://123:123@cluster0.jqrrqvh.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "Forward_Session")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001796986025"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
