from hashlib import sha1
import hmac
import httplib
import json
import pprint
import re

pp = pprint.PrettyPrinter(indent=4)

key =  "Get it from the admin panel, in the API icon"
secret = "Get it from the admin panel, in the API icon"
debug = 1
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

	# X-Gcmp-Application MUST be 'provisioning-1'
	# X-Gcmp-Acting MUST be set to the user which will be loged as performing the action.
	#   You can create a "fake" user in your GroupCamp account for this purpose. Her
	#   privileges are not checked - this user is *only* loged as the user who did
	#   perform the action.
	# Authorization is the string "GCMP <key>:<signature>", the secret MUST NEVER BE SENT.
	#   It should be kept secret.
	# Content-Type is application/json, since the body is a json object.

	headers = {
		'X-Gcmp-Application': 'provisioning-1',
		'X-Gcmp-Acting': acting,
		'Authorization': 'GCMP '+key+':'+sig,
		'Content-Type': 'application/json'
	}

	if debug :
		print "The text to be signed <"+text+'>'
		print "The obtained signature "+sig

	if method == 'GET' and q_string != '':
		path = path + '?' + q_string

	cnx = httplib.HTTPSConnection('api.mustrum.groupcamp.test', 443)
	cnx.request(method, path, body, headers)
	res = cnx.getresponse()
	return res

def do_call_url ( uri ) :
	res = re.match(r"^(https?)://([^/]+)([^?]+)?(.*)$",uri)
	if not res :
		print "No match"
		return None
	protocol = res.group(1)
	domain   = res.group(2)
	path     = res.group(3)
	args     = res.group(4)
	print "Protocol ", protocol
	print "Domain   ", domain
	print "Path     ", path
	print "Q-string ", args
	return do_call('GET', path, '', args)




def new_orga(name, description):
	data = {
		'name' : name,
		'description' : description,
	}
	body = json.dumps(data)

	print body

	res = do_call('POST', '/core/v1/orga/invited', body)
	status = res.status
	body = res.read()
	data = json.loads(body)

	if debug :
		print "Status ",status
		print "Raw answer ",body

	if status != 200 :
		print "Failed"
		if data['error'] == 'bad_request' :
			print "Bad request";
			if data['errors'][0]['field'] == 'name' and data['errors'][0]['error'] == 'already_use' :
				print "Duplicate name"
		return 'failed'
	else :
		print "Creation successful, orga ID is " + data['result']['id']
		return data['result']['id']

def change_orga(uuid, name, description):
	data = {
		'name' : name,
		'description' : description,
	}
	body = json.dumps(data)

	res = do_call('POST', '/core/v1/orga/invited/'+uuid, body)
	status = res.status
	body = res.read()
	data = json.loads(body)

	if debug :
		print "Status ",status
		print "Raw answer ",body

	if status != 200 :
		print "Failed"
		if data['error'] == 'bad_request' :
			print "Bad request"
			if data['errors'][0]['field'] == 'name' and data['errors'][0]['error'] == 'already_use' :
				print "Duplicate name in orga modification"
		return 'failed';
	else :
		print "Modification successful, organization ID is " + data['result']['id']
		return data['result']['id']



def get_orga(uuid) :
	res = do_call('GET', '/core/v1/orga/'+uuid, '', '')
	body = res.read()
	data = json.loads(body)
	pp.pprint(data)
	return data['result']

def get_orgas() :
	res = do_call('GET', '/core/v1/orgas/invited', '', '')
	body = res.read()
	data = json.loads(body)
	pp.pprint(data)


new_uuid = new_orga('API 1', 'A company created via API')
change_orga(new_uuid, 'API 1 renamed', 'New description for the organization')
get_orga(new_uuid)

get_orgas()
