import cgi
import os
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


# main page appears on load
class MainPage(webapp.RequestHandler):
  def get(self):
    # put in default values for principal and rate
    template_values={'principal':'1000','rate':'10'}
    # render the page using the template engine
    path = os.path.join(os.path.dirname(__file__),'index.html')
    self.response.out.write(template.render(path,template_values))

class CalcController(webapp.RequestHandler):
  def get(self):
    principalString=self.request.get('principal')
    principal = int(principalString)
    rateString = self.request.get('rate')
    rate = int(rateString)
    yearsString = self.request.get('years')
    years = int(yearsString) 
    finalPrincipalString = self.request.get('finalPrincipal')
    finalPrincipal = str(finalPrincipalString)
    interest = self.request.get('interest')
    totalInterest = 0
    n = 0
    while n < years:
    	interest = (principal*rate/100)
    	finalPrincipal = interest+principal
    	totalInterest = totalInterest + interest
    	principal = finalPrincipal
    	n = n + 1
    interestString = str(totalInterest)
    
    # set up the template_values with the list of people returned.
    template_values= {'interest':interestString, 'principal':principalString, 'finalPrincipal':finalPrincipal, 'years': yearsString, 'rate':rateString}
   
    # render the page using the template engine
    path = os.path.join(os.path.dirname(__file__),'index.html')
    self.response.out.write(template.render(path,template_values))


# create this global variable that represents the application and specifies which class
# should handle each page in the site
application = webapp.WSGIApplication(
					# MainPage handles the home load
                                     [('/', MainPage),
					# when user clicks on add button, we call on_add action
					# check out index.html to see where on_add gets submitted
                                      ('/on_calculate', CalcController)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
