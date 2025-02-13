"""
HalpyBOT v1.4.2

rank_change.py - Handler for Seal vhost changes requested by the API

Copyright (c) 2021 The Hull Seals,
All rights reserved.

Licensed under the GNU General Public License
See license.md

"""

from typing import Dict
from aiohttp import web

from .server import APIConnector, HalpyClient
from .auth import Authenticate
from ..packages.database import DatabaseConnection, NoDatabaseConnection

routes = web.RouteTableDef()

@routes.post('/tail')
@Authenticate()
async def tail(request):
    if request.body_exists:
        request = await request.json()
    # Parse arguments
    rank = request["rank"]
    subject = request["subject"]
    result = None
    try:
        vhost = f"{subject}.{rank}.hullseals.space"
        with DatabaseConnection() as db:
            cursor = db.cursor()
            cursor.execute(f"SELECT nick FROM ircDB.anope_db_NickAlias WHERE nc = %s;", (subject,))
            result = cursor.fetchall()
            for i in result:
                await HalpyClient.client.rawmsg("hs", "SETALL", i[0], vhost)
            raise web.HTTPOk
    except NoDatabaseConnection:
        raise

APIConnector.add_routes(routes)
