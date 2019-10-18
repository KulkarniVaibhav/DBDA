import webapp2


class arun(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello All. Cloud Computing weclomes you')
	self.response.write('Hola seniorita..! This is from PC 29')

app = webapp2.WSGIApplication([
    ('/', arun),
], debug=True)
