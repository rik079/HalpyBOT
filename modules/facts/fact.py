import main
from typing import List
import re
import mysql.connector
import logging

from config import Database

facts = {}

fact_index = []
basic_facts = []


cnx = mysql.connector.connect(user=Database.user,
                              password=Database.password,
                              host=Database.host,
                              database=Database.database)
print("Database connection established")

cursor = cnx.cursor()

async def on_connect():
    await get_facts()


async def update_fact_index():
    global fact_index
    factnames = facts.keys()
    regexp = re.compile("-")
    for name in factnames:
        if "_no_args" in name:
            continue
        else:
            fact_index.append(str(name))
            if not regexp.search(name):
                basic_facts.append(str(name))


# TODO function to get all facts from database

async def add_fact(factname: str, facttext: str, author: str, reqdm: bool):
    add_query = (f"INSERT INTO facts (FactName, FactText, FactAuthor, FactReqDM) "
                 f"VALUES (%s, %s, %s, %s);")
    add_data = (str(factname), str(facttext), str(author), reqdm)
    try:
        cursor.execute(add_query, add_data)
        cnx.commit()
        logging.info(f"FACT ADDED {factname} by {author}")
    except mysql.connector.Error as er:
        print(f"ERROR in registering fact {factname} by {author}: {er}")


async def get_facts():
    # TODO clear list when invoked and db cnx OK, add manual trigger
    get_query = (f"SELECT factName, factText, factReqDM "
                 f"FROM facts")
    try:
        cursor.execute(get_query)
    except mysql.connector.Error as er:
        print(f"ERROR in getting facts from DB: {er}")
    for (factName, factText, factReqDM) in cursor:
        facts[str(factName)] = [bool(factReqDM), factText]
    await update_fact_index()

async def recite_fact(bot: main, channel: str, sender: str, args: List[str], in_channel: bool, fact: str):

    # Check if fact is DM only
    req_dm = False
    if facts[str(fact)][0] is True:
        req_dm = True
    elif facts[str(fact)][0] is False:
        req_dm = False
    else:
        bot.reply(channel, sender, in_channel, "Fact not properly registered! Contact a Cyberseal")

    # Check if fact is present
    if str(fact) not in facts:
        bot.reply(channel, sender, in_channel, "Couldn't find fact! contact a Cyberseal")

    # PM only, noargs and args
    if f"{fact}_no_args" in facts and in_channel is False and req_dm is True:
        if len(args) == 0:
            return await bot.message(sender, facts[str(f"{fact}_no_args")][1])
        else:
            return await bot.message(sender, f"{' '.join(str(seal) for seal in args)}: {facts[str(fact)][1]})")

    # PM only, 1 version
    if f"{fact}_no_args" not in facts and in_channel is False and req_dm is True:
        return await bot.message(sender, facts[str(fact)][1])

    # Public and PM, 1 version
    if f"{fact}_no_args" not in facts and req_dm is False:
        if len(args) == 0:
            return await bot.reply(channel, sender, in_channel, facts[str(fact)][1])
        else:
            return await bot.reply(channel, sender, in_channel,
                                   f"{' '.join(str(seal) for seal in args)}: {facts[str(fact)][1]})")

    # Public and PM, args and noargs
    if in_channel and req_dm is False:
        if len(args) == 0:
            await bot.message(channel, facts[f"{str(fact)}_no_args"][1])
        else:
            await bot.message(channel, f"{' '.join(str(seal) for seal in args)}: {facts[str(fact)][1]}")
    elif in_channel is False:
        if len(args) == 0:
            await bot.message(sender, facts[f"{str(fact)}_no_args"][1])
        else:
            await bot.message(sender, f"{' '.join(str(seal) for seal in args)}: {facts[str(fact)][1]}")
    else:
        return
