import requests
import re
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
import time

gettime = datetime.now()

subreddit = 'cats'
limit = 10
timeframe = 'hour'
listing = 'new'

def get_reddit(subreddit,listing,limit,timeframe):
	try:
		base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
		request = requests.get(base_url, headers = {'User-agent': 'autoKalimera'})
	except:
		print('An Error Occured')
	return request.json()

def geturl():
	result = get_reddit(subreddit,listing,limit,timeframe)
	
	data = result['data']
	children = data['children']
	childrenstr="".join(map(str,children))

	url = re.search("'url_overridden_by_dest': '(.+?)',", childrenstr).group(1)
	return url
	
def find_font_size(text, font, image, target_width_ratio):
    tested_font_size = 100
    tested_font = ImageFont.truetype(font, tested_font_size)
    observed_width, observed_height = get_text_size(text, image, tested_font)
    estimated_font_size = tested_font_size / (observed_width / image.width) * target_width_ratio
    return round(estimated_font_size)

def get_text_size(text, image, font):
    im = Image.new('RGB', (image.width, image.height))
    draw = ImageDraw.Draw(im)
    return draw.textsize(text, font)

def makepic():
	r = requests.get(url)
	with open("cat.jpg", "wb") as f:
		f.write(r.content)

	original = Image.open("cat.jpg")
	#title_font = ImageFont.truetype('Arial_Greek_Bold.ttf', 200)
		
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
	
	width_ratio = 0.8
	font_family = 'Arial_Greek_Bold.ttf'
	font_size = find_font_size(text, font_family, original, width_ratio)
	font = ImageFont.truetype(font_family, font_size)
	
	image_editable = ImageDraw.Draw(original)
	image_editable.text((25,25), text, (25, 25, 25), font=font)
	image_editable.text((30,30), text, (25, 25, 25), font=font)
	image_editable.text((29,29), text, (242, 242, 242), font=font)
	original.save("kalimera.jpg")

while True:
	url = geturl()
	#url = "https://static.wixstatic.com/media/2cd43b_aa75cdffb0744e888d948bfac42f12dc~mv2_d_1600_1415_s_2.png/v1/fill/w_1600,h_1415,fp_0.50_0.50/2cd43b_aa75cdffb0744e888d948bfac42f12dc~mv2_d_1600_1415_s_2.png"
	
	if ".jpg" not in url:
		subreddit = 'catpictures'
		url = geturl()
	if ".jpg" not in url:
		subreddit = 'catpics'
		url = geturl()
	if ".jpg" not in url:
		subreddit = 'cat'
		url = geturl()
	if ".jpg" not in url:
		subreddit = 'catssittingdown'
		url = geturl()
	if ".jpg" not in url:
		subreddit = 'SupermodelCats'
		url = geturl()
	if ".jpg" not in url:
		subreddit = 'tuckedinkitties'
		url = geturl()
	if ".jpg" in url:
		print(subreddit)
		print(url)
		makepic()
	else:
		print("No jpg found")
	
	time.sleep(600)