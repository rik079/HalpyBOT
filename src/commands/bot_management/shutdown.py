"""
HalpyBOT v1.2.2

shutdown.py - Will be with you shortly, please hold!

Copyright (c) 2021 The Hull Seals,
All rights reserved.

Licensed under the GNU General Public License
See license.md
"""


import os
import signal
import logging

from typing import List

from src.packages.checks.checks import require_permission, DeniedMessage, require_dm
from .. import Commands

@require_dm()
@require_permission("ADMIN", message=DeniedMessage.ADMIN)
@Commands.command("shutdown")
async def cmd_shutdown(ctx, args: List[str]):
    """
    Shut down the bot (restart if running as daemon)

    Usage: !shutdown
    Aliases: n/a
    """
    logging.critical(f"Shutdown has been ordered by {ctx.sender}")
    os.kill(os.getpid(), signal.SIGUSR2)
