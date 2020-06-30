import GetOldTweets3 as got
region=["KL","MH","RJ","KA","GA","MP","UP","GJ","TN","TS","BH","JK","PY","HR","AP","WB","CT","OR","JH","AS","HP","NL","SK","MN","AR","TR","ME","MI","UT"] #state code corresponding to particular coordinates and radius
coordinates=["10.8505,76.2711","19.7515,75.7319","27.0238,74.2179","15.3173,75.7139","15.2993,74.1240","22.9734,78.6569","28.8467,80.9462","22.2587,71.1924","11.1271,78.6569","18.1124,79.0193","25.0961,85.3131","33.7782,76.5762","31.1471,75.3412","29.0588,76.0856","15.9129,79.7400","22.9868,87.8550","21.2787,81.8661","20.9517,85.0985","23.6102,85.2799","26.2006,92.9376","31.1048,77.1734","26.1584,94.5624","27.5330,88.5122","24.6637,93.9063","28.2180,94.7278","23.9408,91.9882","25.4670,91.3662","23.1645,92.9376","30.0668,79.0193"]
radius=["111.22","312.97","330.05","247.08","34.33","313.29","278.28","249.79","203.47","188.88","173.12","115.95","126.61","118.63","227.76","168.07","207.44","222.62","159.29","158.01","133.12","72.64","47.52","84.30","163.26","57.77","84.49","81.92","130.47"]
for i in range(0,len(region)):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#covid19 #coronavirus #lockdown').setSince("2020-03-01").setUntil("2020-05-31").setNear(coordinates[i]).setWithin(radius[i]+"km").setMaxTweets(10)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    
