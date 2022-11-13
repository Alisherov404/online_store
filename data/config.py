from environs import Env

# use environs library
env = Env()
env.read_env()

# Read from .env file
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
