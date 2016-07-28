import tweepy

consumer_key='GF96szaWaipqWH0LtIkHqhe89'
consumer_secret='70vjD0UA2kSHilF3PJ3nAs03ncCMdzZmGu5cnqdo58Q4LwUm2E'
access_token_key='554304300-lcXN6CUmmfei5iKjxaEj4Pza42hREgoq8b4k1y74'
access_token_secret='kuQ6laDpjjqFqx4BkTGkkG8t7mElV6mec1fv9i1STWQ9m'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

f=open("stop_words.txt","r")
arr=f.read()
f.close()
arr=arr.split("\n")

statuses=[]
f=open("output.txt","w")
for word in arr:
	result1=api.search(q=word+" -filter:retweets AND -filter:replies",lang="en",show_user=True)
	for r in result1:
		if int(r.author.followers_count)>=1000:
			flag=0
			for obj in word.split("%20"):
				if obj in r.author.screen_name.lower():
					flag=1
					break
			if flag==0:
				f.write("@"+r.author.screen_name+"\n")
				f.write(str(r.created_at)+"\n")
				f.write(r.text.encode("utf-8"))
				f.write("\n")
				f.write("https://twitter.com/"+ r.author.screen_name +"/statuses/"+ str(r.id) )
				f.write("\n")
				f.write("\n")
f.close()