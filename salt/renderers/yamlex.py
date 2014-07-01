# -*- coding: utf-8 -*-
from __future__ import absolute_import

# Import python libs
import logging
import warnings

# Import salt libs
from salt.utils.serializers.yamlex import deserialize

log = logging.getLogger(__name__)


def render(sls_data, saltenv='base', sls='', **kws):
    '''
    Accepts YAML_EX as a string or as a file object and runs it through the YAML_EX
    parser.

    :rtype: A Python data structure
    '''
    with warnings.catch_warnings(record=True) as warn_list:
        data = deserialize(sls_data) or {}

        for item in warn_list:
            log.warn(
                '{warn} found in salt://{sls} environment={saltenv}'.format(
                    warn=item.message, sls=sls, saltenv=saltenv
                )
            )

        log.debug('Results of SLS rendering: \n{0}'.format(data))

    return data