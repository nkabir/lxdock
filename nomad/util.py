# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


def run_cmd(container, cmd):
    logger.debug("Running %s" % (' '.join(cmd)))
    stdout, stderr = container.execute(cmd)
    logger.debug(stdout)
    logger.debug(stderr)