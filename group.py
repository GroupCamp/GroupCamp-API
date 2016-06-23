from hashlib import sha1
import hmac
import httplib
import json
import pprint

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

	# X-Gcmp-Application MUST be 'provisionning-1'
	# X-Gcmp-Acting MUST be set to the user which will be loged as performing the action.
	#   You can create a "fake" user in your GroupCamp account for this purpose. Her
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

	if method == 'GET' and q_string != '':
		path = path + '?' + q_string

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
			print "Bad request";
			if data['errors'][0]['field'] == 'name' and data['errors'][0]['error'] == 'already_use' :
				print "Duplicate name"
		return 'failed'
	else :
		print "Creation successful, groupe ID is " + data['result']['id']
		return data['result']['id']

def change_project(uuid, name, description, access, guests):
	data = {
		'name' : name,
		'description' : description,
		'access' : access,
		'with_guests' : guests
	}
	body = json.dumps(data)

	res = do_call('POST', '/core/v1/group/project/'+uuid, body)
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
				print "Duplicate name in project modification"
		return 'failed';
	else :
		print "Modification successful, groupe ID is " + data['result']['id']
		return data['result']['id']

def insert_user(group_id, email) :
	res = do_call('PUT', '/core/v1/group/'+group_id+'/user/'+email, '')
	status = res.status
	if status != 200 :
		print "Adding member failed"
		print "Raw answer ", res.read()
	else :
		print "Added member in the group"


def remove_user(group_id, email) :
	res = do_call('DELETE', '/core/v1/group/'+group_id+'/user/'+email, '')
	status = res.status
	if status != 200 :
		print "Removing member failed";
		print "Raw answer ", res.read()
	else :
		print "Removed member from the group"


def user_teams(email) :
	res = do_call('GET', '/core/v1/user/'+email+'/teams', '')
	if res.status != 200 :
		print "Failed"
		return 'failed'

	body = res.read()
	data = json.loads(body)
	for team in data['result'] :
		if team['is_tech'] :
			management = " is a management team"
		else :
			management = ""
		print "Team '"+team['name']+"' having UUID = "+team['id']+management
	return data


team_uuid = 'Get it from the GroupCamp user interface'
gcat_name = 'Main category'
user_email = 'jean@localhost'
group_id = new_project('The new group 3', 'This group have been created via the provisionning API', 'invite', False, gcat_name, team_uuid)
if group_id != 'failed' :
	insert_user(group_id, user_email)
	change_project(group_id, 'Another name', 'The description is modified', 'open', True)

print "The user '"+user_email+"' is a member of the following teams:"
user_teams(user_email)


