import requests
import re
 
subreddit = 'catpictures'
limit = 1
timeframe = 'hour'
listing = 'best'
 
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

link = re.search("'url_overridden_by_dest': '(.+?)',", childrenstr).group(1)
print(link)