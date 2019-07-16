from hashlib import sha1
import hmac
import httplib
import json
import pprint
import re

pp = pprint.PrettyPrinter(indent=4)

key    = "Get it from the admin panel, in the API icon"
secret = "Get it from the admin panel, in the API icon"
debug  = 1
acting = 'big.boss@localhost'


def do_call (method, path, body, q_string='') :

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
	# X-Gcmp-Acting MUST be set to the user which will be loged as performing the action.
	#   You can create a "fake" user in your GroupCamp account for this purpose. Her
	#   privileges are not checked - this user is *only* loged as the user who did
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

	cnx = httplib.HTTPSConnection('api.groupcamp.com', 443)
	cnx.request(method, path, body, headers)
	res = cnx.getresponse()
	return res


def get_report() :
	res = do_call('GET', '/track/v1/report/', '', 'search=Some%20text')
	status = res.status
	body = res.read()

	if debug :
		print "Status ",status
		print "Raw answer ",body

	data = json.loads(body)
	pp.pprint(data)

get_report()
