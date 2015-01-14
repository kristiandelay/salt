# -*- coding: utf-8 -*-
'''
An "Always Approved" eauth interface to test against, not intended for
production use

Enable MySQL authentication.

  .. code-block:: yaml

    external_auth:
      authrocket:
        administrator:
          - .*
          - test.*

'''
import requests
import simplejson
import logging

def auth(username, password):  # pylint: disable=unused-argument
#
    '''
    Authenticate!
    '''

	url = 'https://api.ops.sh/1/auth/login/'
	realmID = 'rl_0v8jTbB6yprKS3KFI6KRJb'

	data = {}
	data['realmID'] = realmID;
	data['loginName'] = username;
	data['password'] = password;

	json_data = json.dumps(data)

	payload = "userLoginStruct = %s" % json_data
	headers = {'Content-Type': 'application/json'}

	responseObject = requests.post(url, headers=headers, data=payload)
	
	if responseObject.text == 'true':
		print 'authentication success'
   		return True
	else:
		print 'authentication failed'
    	return False

    return False
#
