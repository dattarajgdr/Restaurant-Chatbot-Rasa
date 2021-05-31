from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json

import smtplib 
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']
weoperate= list(map (lambda x:x.lower(),WeOperate))
def RestaurantSearch(City,Cuisine,Price):
    TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
    if Price=='mid':    
        TEMP=TEMP.loc[(TEMP['Average Cost for two']>= 300)&(TEMP['Average Cost for two']<= 700)].sort_values(by='Aggregate rating',ascending=False)
    if Price=='low':
        TEMP=TEMP.loc[TEMP['Average Cost for two']<300].sort_values(by='Aggregate rating',ascending=False)
    if Price=='high':
        TEMP=TEMP.loc[TEMP['Average Cost for two']>700].sort_values(by='Aggregate rating',ascending=False)
    return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']].head(10)

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		if loc == None:
			return dispatcher.utter_message('Location got is None')
		if loc.lower() not in weoperate:
			dispatcher.utter_message("We don't operate in your location")
		results = RestaurantSearch(City=loc,Cuisine=cuisine,Price=price)
		response=""
		if results.shape[0] == 0:
			response= "no results"
		else:
			for restaurant in RestaurantSearch(loc,cuisine,price).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Aggregate rating']} with avg cost {restaurant['Average Cost for two']} \n\n"
				
		dispatcher.utter_message("-----"+response)
		#return [SlotSet('location',loc)]

class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'
	
	def run(self,dispatcher,tracker,domain):
		loc=tracker.get_slot('location')
		cuisine=tracker.get_slot('cuisine')
		price=tracker.get_slot('price')
		results= RestaurantSearch(City=loc,Cuisine=cuisine,Price=price)
		email=tracker.get_slot('email')
		if email == None:
			email = 'pgdmlupgrad@gmail.com'
		msg = MIMEMultipart()
		msg['Subject'] = "The details of all the restaurants you inquired"
		msg['From'] = 'pgdmlupgrad@gmail.com'
		html = """\
		<html>
          <head></head>
          <body>
            {0}
          </body>
        </html>
        """.format(results.to_html())
		part1 = MIMEText(html, 'html')
		msg.attach(part1)
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login("pgdmlupgrad@gmail.com", "pgdml@1960")
		server.sendmail(msg['From'], email , msg.as_string())
		dispatcher.utter_message("email has been sent succesfully")
		# return [SlotSet('email',email)]