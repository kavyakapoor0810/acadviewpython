#question1

'''An access token is an object that describes the security context of a process or
thread. The information in a token includes the identity and privileges of the user account
associated with the process or thread. ... The security identifie r (SID) for the user's account.

access token for twitter
    Access_Token = "1011804483339341825-6Ng2c5i4OIBxOwFF8qt40zY8k4FVZ1"
access token for sendgrid
    SG.OZtBwMrES9aSPXfe29RESw.RMXq8wJYEl_5S2AfT2vhl - SHMdnwA0GJOoWeUOOEhD0

#question2
    in cmd
     by using--- tracert www.facebook.com
    google - [172.217.24.228]
    facebook - [157,240,13,38]
    '''
#question3

from twitterkeys import Consumer_Key,Consumer_Secret,Access_Token,Access_Token_Secret
import tweepy

oauth =tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
oauth.set_access_token(Access_Token,Access_Token_Secret)
api=tweepy.API(oauth)
print(api.search("#sanju"))
user=api.get_user('kavyakapoor0810')
print(user.screen_name)
print(user.followers_count)

#question4
''''
An API is a spec and a library is an implementation.
A library contains re-usable chunks of code where as  API is an
interface between two
software programs which facilitates the
interaction between them.

API is part of library that defines how it will interact
with external code. Every library has API, API is sum 
of all public/exported stuff. Nowadays meaning of API 
is widened. we might call the way web site/service interact 
with code as API also. You can also tell that some device 
has API - the set of commands you can call.

Sometimes this terms can be mixed together.
For example you have some server app.
It has API with it, and this API is implemented 
as a library. But this library is just a middle layer 
you and not the one who executes your calls. But if library
itself contains all action code then we can't say that this
library is API.
'''

#question5

import sendgrid
import os
from sendgrid.helpers.mail import *
sg = sendgrid.SendGridAPIClient(apikey='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')
from_email = Email("kavyakapoor0810@gmail.com")
to_email = Email("kavyakapoor0810@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print("response.status_code",response.status_code)
print("response.body",response.body)
print("response.headers",response.headers)