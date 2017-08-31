from hashlib import sha1
import hmac
import httplib
import json
import pprint
import re

pp = pprint.PrettyPrinter(indent=4)

host   = 'api.groupcamp.com'
key    = "token from the API icon in the admin panel of your GroupCamp account"
secret = "the secret associated with the above key"
debug  = 1
acting = 'email address of the "acting" user (not that important for the reporting API)'


def do_call (method, path, body='', q_string='') :

	# The text to be signed is a concatenation of
	# - the method (POST, PUT, GET, etc),
	# - the string '::'
	# - the path, with the leading /, without the trailing /
	# - the string '::'
	# - the body of the request (can be a json object, or an empty string)

	text = method + '::' + path + '::' + body
	signature = hmac.new(secret, text, sha1)
	sig = signature.digest().encode("base64").rstrip('\n')

	# X-Gcmp-Application MUST be 'reporting-1'
	# X-Gcmp-Acting MUST be set to the user which will be logged as performing the action.
	#   You can create a "fake" user in your GroupCamp account for this purpose. User
	#   privileges are not checked - this user is *only* logged as the user who did
	#   perform the action.
	# Authorization is the string "GCMP <key>:<signature>", the secret MUST NEVER BE SENT.
	#   It should be kept secret.
	# Content-Type is application/json, since the body is a json object.

	headers = {
		'X-Gcmp-Application': 'reporting-1',
		'X-Gcmp-Acting': acting,
		'Authorization': 'GCMP '+key+':'+sig,
		'Content-Type': 'application/json'
	}

	if debug :
		print "The text to be signed <"+text+'>'
		print "The obtained signature "+sig

	if method == 'GET' and q_string != '':
		path = path + '?' + q_string

	cnx = httplib.HTTPSConnection(host, 443)
	cnx.request(method, path, body, headers)
	res = cnx.getresponse()
	return res



def get_element(method, path) :
	res = do_call(method, path)
	status = res.status
	body = res.read()

	if debug :
		print "Status ",status
		print "Raw answer ",body

	data = json.loads(body)

	if status != 200 :
		print "Failed"
		return 'failed'
	else :
		print "Request successful"
		result = data['result']
	return result


result = get_element('GET', '/task/v1/task/[UUID of a task]')
pp.pprint(result)
