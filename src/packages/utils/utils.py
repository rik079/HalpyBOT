"""
HalpyBOT v1.4.2

utils.py - miscellaneous utility functions

Copyright (c) 2021 The Hull Seals,
All rights reserved.

Licensed under the GNU General Public License
See license.md
"""

import re
import json

def language_codes():
    """Get a dict of ISO-639-1 language codes

    Returns:
        (dict): A dictionary {2 letter abbreviation: name}

    """
    with open("data/languages/iso639-1.json") as file:
        langs = json.load(file)
        return langs

def strip_non_ascii(string: str):
    """Strip non-ASCII characters from a string

    Args:
        string (str): String that needs to be sanitized

    Returns:
        (tuple): A tuple with the values:

            - string (str): Stripped string
            - has_stripped (bool): True is characters were removed, else False

    """
    res = re.subn(r'[^\x00-\x7f]', r'', string)
    if res != (string, 0):
        # Return new string and True if characters were removed
        return res[0], True
    else:
        return res[0], False


async def get_time_seconds(time: str):
    """Get time in seconds from a hh:mm:ss format

    Args:
        time (str): Time, in a hh:mm:ss format

    Returns:
        (int): Time in seconds

    Raises:
        ValueError: String does not match required format

    """
    pattern = re.compile("(?P<hour>\d+):(?P<minutes>\d+):(?P<seconds>\d+)")
    if not re.match(pattern, time):
        raise ValueError("get_time_seconds input does not match hh:mm:ss format")
    res = pattern.search(time)
    counter = 0
    conversionTable = {
        "hour": 3600,
        "minutes": 60,
        "seconds": 1
    }
    for unit in conversionTable.keys():
        value = int(res.group(unit))
        counter += value * conversionTable[unit]
    return str(counter)
