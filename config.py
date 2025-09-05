import os
from dotenv import load_dotenv
load_dotenv()
PROVIDER_MODEL = os.getenv("MODEL")
assert PROVIDER_MODEL, "Please set MODEL in your .env to a supported model id"