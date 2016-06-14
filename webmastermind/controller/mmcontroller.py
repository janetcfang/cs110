# [START imports]
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

# session code from this example:
# url: http://webapp-improved.appspot.com/api/webapp2_extras/sessions.html

import jinja2
import webapp2
from webapp2_extras import sessions

# import your mastermind functions
import mmFuncs

# boiler plate code for sessions
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

# more boiler plate code, just leave it as is
class BaseHandler(webapp2.RequestHandler):  # Copied from Google's doc
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

# [START main_page]
class MainPage(BaseHandler):

    def get(self):
        secret = mmFuncs.generateSecret() 
    	self.session['secret'] = secret  # store secret in session
    	feedbackList = []
    	self.session['history'] = feedbackList
    	
        template_values= {'secret':secret}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
# [END main_page]


class GuessController(BaseHandler):

    def get(self):
        guess = self.request.get('guess')
    	secret = self.session.get('secret')
    	print(guess, secret)
    	# here is where you should compute exacts and partials by
    	#   calling functions you put in mmFuncs.py
    	# then display result using feedback in template
    	
	if len(guess) == 4:
    	
    		partials = 0
    		
    		exacts = mmFuncs.computeExacts(secret, guess)
    	
    		if exacts == 4:
    			results = "Congrats, you won!"
    		else:
    			partials = mmFuncs.computePartials(secret, guess)
    			results = "Please try again."
    			
    		feedback = guess + " " + "Exacts:" + str(exacts) + "Partials:" + str(partials)
    		
    		feedbackList = str(self.session['history'])
    		#feedbackList.append(feedback)
    		feedbackList = feedbackList + "\n" + feedback
    		self.session['history'] = feedbackList	
    	
   		# set up the template_values with the list of people returned.
    	template_values= {'guess':guess, 'secret':secret, 'feedback':feedbackList}
    	

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

# boiler plate, leave as is
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}


# here is where you map your url requests to handlers
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/on_guess', GuessController),
], config=config, debug=True)
