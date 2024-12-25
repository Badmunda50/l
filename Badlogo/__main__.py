import asyncio
import importlib
from Badlogo import LOGGER, app
from pyrogram import idle
from Badlogo.plugins import ALL_MODULES

loop = asyncio.get_event_loop()

async def main():
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Badlogo.plugins" + all_module)
    LOGGER.info("Successfully Imported All Modules")
    LOGGER.info("Badlogo Bot Started Successfully")
    await idle()

# Start the bot
if __name__ == "__main__":
    loop.run_until_complete(main())
    LOGGER.info("Stopping Bot! GoodBye")
