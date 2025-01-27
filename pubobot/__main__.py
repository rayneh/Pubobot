#!/usr/bin/python3
# encoding: utf-8
import time
import asyncio
import argparse
import os

# my modules
from . import console, config, bot, client, scheduler, stats3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--config", default="config.cfg", help="configuration file"
    )
    parser.add_argument("-l", "--logs", default="logs", help="log directory")
    parser.add_argument(
        "-d", "--db", default="database.sqlite3", help="sqlite3 database"
    )

    args = parser.parse_args()

    console.init(args.logs)
    scheduler.init()
    bot.init()
    stats3.init(args.db)
    config.init(args.config)
    client.init()

    client.c.loop.create_task(bot_run())
    client.run()  # runs until ctrl+c


async def bot_run():  # background thinking
    while True:
        if console.alive:
            frametime = time.time()
            bot.run(frametime)
            scheduler.run(frametime)
            console.run()
            await client.send()
            await asyncio.sleep(0.5)
        else:
            await client.close()
            print("QUIT NOW.")
            os._exit(0)


if __name__ == "__main__":
    main()
