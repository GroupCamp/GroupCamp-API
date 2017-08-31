from hashlib import sha1
import hmac
import httplib
import json
import pprint
import re

pp = pprint.PrettyPrinter(indent=4)

key    = "Get a key, for interface 'reporting', from the admin panel, in the API icon"
secret = "Get the secret associated with the key, in the same place"
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

	cnx = httplib.HTTPSConnection('api.groupcamp.com', 443)
	cnx.request(method, path, body, headers)
	res = cnx.getresponse()
	return res

def do_call_url ( uri ) :
	# When an API is paginated, the next_page and previous_page provides
	# links to the sibbling pages.
	# The python httplib library needs to split this URI into various
	# pieces (host, path, query string, etc). So we de rely on the same
	# do_call as before, since we need to split the URI anyway. Can probably
	# be written in a better way in your usual framework :)
	res = re.match(r"^(https?)://([^/]+)([^?]+)\?(.*)$",uri)
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

	# Protocol will always be https. Domain will always be the same as the domain
	# of the first request.
	return do_call('GET', path, '', args)


def get_all_lines(method, path, body, query_string) :
	res = do_call(method, path, body, query_string)
	status = res.status
	body = res.read()

	if debug :
		print "Status ",status
		print "Raw answer ",body

	data = json.loads(body)

	if status != 200 :
		print "Failed"
		if data['error'] == 'bad_request' :
			print "Bad request";
			if data['errors'][0]['field'] == 'name' and data['errors'][0]['error'] == 'already_use' :
				print "Duplicate name"
		return 'failed'
	else :
		print "Request successful, number of pages:", data["page_count"]
		result = data['result']

	count = data['page_count']
	print "There are", count, "pages of result"
	# pp.pprint(data)
	while 'next_page' in data :
		res = do_call_url(data['next_page'])
		if not res :
			return 'failed on a page'
		body = res.read()
		data = json.loads(body)
		result.extend(data['result'])
		# pp.pprint(data)

	print "Obtained", len(result), "records :"
	return result

def get_tlogs(start_date, end_date):
        res = do_call('GET', '/track/v1/timelogs', '', 'start='+start_date+'&end='+end_date)
        body = res.read();
        data = json.loads(body)
        pp.pprint(data)

# Get logs for precisely one week
get_tlogs('2016-10-24','2016-10-30')


