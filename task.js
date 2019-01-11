/*
	This tiny test script is designed to be used in a browser.

	Include those in the HEAD of your HTML page:
	<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.9-1/crypto-js.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.9-1/hmac-sha1.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.9-1/enc-base64.min.js"></script>
 */

// This one is the key, declared for your API access in the GroupCamp admin interface.
var key    = 'The key';
// This one is the secret associated with the key, used to sign your request. Must not
// be sent to GroupCamp (or elsewhere).
var secret = 'The secret associated to the key';
// The main GroupCamp API server
var domain = 'api.groupcamp.com';
// The user acting
var acting = 'e-mail address of the acting user';

/*
	Will send a request to the GroupCamp API, and display the result in the web page.
*/
function send_request(method, path, body, q_string, on_success, on_error) {
	// Signing request
	var text = method + '::' + path + '::' + body
	var hash = CryptoJS.HmacSHA1(text, secret);
	var hashInBase64 = CryptoJS.enc.Base64.stringify(hash);

	// Sending request
	var url = 'https://'+domain+path;
	if ( q_string ) {
		url += '?'+q_string; 
	} 
	var xhr = new XMLHttpRequest();
	xhr.open(method, url, true);
	xhr.onload = function(res) { on_success(xhr.response); };
	xhr.onerror = on_error;
	xhr.withCredentials = false;
	xhr.responseType = 'json';
	xhr.setRequestHeader('Content-Type','application/json');
	xhr.setRequestHeader('X-Gcmp-Application','reporting-1');
	xhr.setRequestHeader('X-Gcmp-Acting',acting);
	xhr.setRequestHeader('Authorization','GCMP '+key+':'+hashInBase64);
	xhr.send(body);
}

function get_task(uuid, on_success, on_error) {
	var method = 'GET';
	var path = '/task/v1/task/' + uuid;
	var body = '';
	var q_string = ''
	send_request(method, path, body, q_string, on_success, on_error);
}

var uuid = 'Uuid of a task (you can get it from the information panel)';
get_task(uuid, function(res) {console.info(res);}, function(res) {console.error(res);});

