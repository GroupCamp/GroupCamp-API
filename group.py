from hashlib import sha1
import hmac
import httplib
import json

key =  "Get it from the admin panel, in the API icon"
secret = "Get it from the admin panel, in the API icon"
debug = 1
acting = 'big.boss@localhost'

def do_call (method, path, body) :

	# The text to be signed is a concatenation of
	# - the method (POST, PUT, GET, etc),
	# - the string '::'
	# - the path, with the leading /, without the trailing /
	# - the string '::'
	# - the body of the request (can be a json object, or an empty string)

	text = method + '::' + path + '::' + body
	signature = hmac.new(secret, text, sha1)
	sig = signature.digest().encode("base64").rstrip('\n')

	# X-Gcmp-Application MUST be 'provisionning-1'
	# X-Gcmp-Acting MUST be set to the user which will be logged as performing the action.
	#   you can create a "fake" user in your GroupCamp account for this purpose. Her
	#   privileges are not checked - this user is *only* loged as the user who did
	#   perform the action.
	# Authorization is the string "GCMP <key>:<signature>", the secret MUST NEVER BE SENT.
	#   It should be kept secret.
	# Content-Type is application/json, since the body is a json object.

	headers = {
		'X-Gcmp-Application': 'provisionning-1',
		'X-Gcmp-Acting': acting,
		'Authorization': 'GCMP '+key+':'+sig,
		'Content-Type': 'application/json'
	}

	if debug :
		print "The text to be signed <"+text+'>'
		print "The obtained signature "+sig

	cnx = httplib.HTTPSConnection('api.groupcamp.com', 443)
	cnx.request(method, path, body, headers)
	res = cnx.getresponse()
	return res





def new_project(name, description, access, guests, gcat_name, management_team):
	data = {
		'name' : name,
		'description' : description,
		'access' : access,
		'with_guests' : guests,
		'category_name' : gcat_name,
		'management_team' : team_uuid
	}
	body = json.dumps(data)

	res = do_call('POST', '/core/v1/group/project', body)
	status = res.status
	body = res.read()
	data = json.loads(body)

	if debug :
		print "Status ",status
		print "Raw answer ",body

	if status != 200 :
		print "Failed"
		if data['error'] == 'bad_request' :
			print "Bas request";
			if data['errors'][0]['field'] == 'name' and data['errors'][0]['error'] == 'already_use' :
				print "Duplicate name"
		return 'failed'
	else :
		print "Creation successful, groupe ID is " + data['result']['id']
		return data['result']['id']

def insert_user(group_id, email) :
	res = do_call('PUT', '/core/v1/group/'+group_id+'/user/'+email, '')
	status = res.status
	if status != 200 :
		print "Adding member failed"
	else :
		print "Added member in the group"


team_uuid = 'Get it from the GroupCamp user interface'
gcat_name = 'Main category'
group_id = new_project('The new group 3', 'This group have been created via the provisionning API', 'invite', False, gcat_name, team_uuid)
if group_id != 'failed' :
	insert_user(group_id, 'jean@localhost')

