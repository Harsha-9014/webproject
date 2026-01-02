import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:\ml project\instagram.csv")
df['Date']=pd.to_datetime(df['Date'])
df['engagement']=df['Likes']+df['Comments']+df['Shares']
df['engagement_rate']=(df['engagement']/df['Impressions'])*100
print("average engagement rate by platform:")
print(df.groupby('Platform')['engagement_rate'].mean())
plt.figure()
for platform in df['Platform'].unique():
  data=df[df['Platform']==platform]
plt.plot(data['Date'],data['Followers'],label=platform)
plt.xlabel("Date")
plt.ylabel("Followers")
plt.title("Followers Growth")
plt.legend()
plt.show()
plt.figure()
plt.bar(df['Platform'],df['engagement'])
plt.title("engagement comparision")
plt.xlabel("Platform")
plt.ylabel("Total engagement")
plt.show()