# Authentication

Three special headers are used to authenticate every API request.

`X-Gcmp-Application` contains the name of the API (for now, `reporting` or
`provisioning`) and the version number:

> X-Gcmp-Application: reporting-1

`X-Gcmp-Acting`contains the reference of a user that will be used
when any action needs to be logged or traced in the history in your
account. For example, when a group is created, this user will be
recorded in the main history as the user who created the group. This
user is **not** used for any credential control. There is no need for
this user to be an administrator of the account, or to be membe of
any group. We suggest using a dedicated user, with an explicit name,
so having a user whose name is "Our API program" with an e-mail
"api@mycompany.com", and the HTTP header:

> X-Gcmp-Acting: `api@mycompany.com`

A signature, based on your key and the secret associated with it, will
prove the request have been issued by you. The text to be signed is a
string containing the http method (GET, POST, etc), the string '::',
the path of the request (including the in-path arguments), the string
'::', and the body of the request. This text is hashed, using SHA1,
with the secret. It is sent in the `Authorization` header, with the
key.

> Authorization: GCMP `key`:`signature`

See an example in python in [group.py](../../group.py)

# Possible errors

During authentication, whatever the reason that makes the request
is rejected, the error returned is always `unauthorized` with http
status 401.

Here are the usual problems:

* API is not enabled on your account: if you cannot access the API
  icon in the admin panel of your account, then, the authentication
  will consider the key/secret pair is invalid, please contact the
  GroupCamp support to re-enable the API access on your account.
* The key have been deleted: if you delete the key (and its associated
  secret, it will immediately be rejected.
* The key used is for another application: if you declare a key/secret
  pair for the `reporting` API, you cannot use it for the `provisioning`
  API, it will be rejected during the authentication, because the key
  and the `X-Gcmp-Application` do not match.
* The signature does not match, try using our python test code to
  make a signature on your request, and compare with the signature
  produced by your own code.
* The API used is not the right one: if a method is available in the
  API `reporting` it cannot be called in the API `provisioning`. If
  the `X-Gcmp-Application` and the key are coherent, but the method
  is not available, the final phase of the authentication will fail.

Once the authentication is a success, the possible errors will be the ones
associated with the method you call.



