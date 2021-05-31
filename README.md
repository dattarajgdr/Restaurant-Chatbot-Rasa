# Restaurant-Chatbot-Rasa

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. 
We are using the Zomato API as the knowledge base to query upon and retrieve results.

Tech Stack Used : RASA NLU, Spacy, LSTM , RNN, Python

The bot takes the following inputs from the user:

## City: 
Take the input from the customer as a text field. For example:

Bot: In which city are you looking for restaurants?

User: anywhere in Delhi

## Cuisine Preference: 
Take the cuisine preference from the customer. Following is an example for the same:

Bot: What kind of cuisine would you prefer?

Chinese

Mexican

Italian

American

South Indian

North Indian

User: I’ll prefer Italian!

## Average budget for two people: 
Segment the price range (average budget for two people). For example:

Bot: What price range are you looking at?

Lesser than Rs. 300

Rs. 300 to 700

More than 700

User: in range of 300 to 700

Finally, the bot will ask the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot asks for user’s email id and then send it over email. Else, just reply with a 'goodbye' message. The mail should have the following details for each restaurant:

Restaurant Name

Restaurant locality address

The average budget for two people

Zomato user rating

 
