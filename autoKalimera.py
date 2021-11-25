import requests
import re
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
import time

gettime = datetime.now()

subreddit = 'catpictures'
limit = 1
timeframe = 'hour'
listing = 'best'

while True:
	def get_reddit(subreddit,listing,limit,timeframe):
		try:
			base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
			request = requests.get(base_url, headers = {'User-agent': 'autoKalimera'})
		except:
			print('An Error Occured')
		return request.json()
 
	result = get_reddit(subreddit,listing,limit,timeframe)
	
	data = result['data']
	children = data['children']
	childrenstr="".join(map(str,children))

	url = re.search("'url_overridden_by_dest': '(.+?)',", childrenstr).group(1)
	print(url)
	
	r = requests.get(url)
	with open("cat.jpg", "wb") as f:
		f.write(r.content)
	
	original = Image.open("cat.jpg")
	title_font = ImageFont.truetype('Arial_Greek_Bold.ttf', 200)
	
	hournow = gettime.hour
	print(hournow)
	
	text = ""
	if hournow >= 21:
		text = "Καληνύχτα"
	elif hournow >= 17:
		text = "Καλό Απόγευμα"
	elif hournow >= 12:
		text = "Καλησπέρα"
	elif hournow >= 5:
		text = "Καλημέρα"
	elif hournow >= 0:
		text = "Καληνύχτα"
	print(text)
	
	image_editable = ImageDraw.Draw(original)
	image_editable.text((15,15), text, (242, 242, 242), font=title_font)
	original.save("kalimera.jpg")
	
	time.sleep(600)