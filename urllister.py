from HTMLParser import HTMLParser

class URLLister(HTMLParser):

	def reset(self):
		HTMLParser.reset(self)
		self.urls = []
		
	def handle_starttag(self, a, attrs):
		href = [v for k, v in attrs if k.lower() =='href']
		if href:
			self.urls.extend(href)
