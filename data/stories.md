
## good story
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "datharajgdr@gmail.com"}
    - slot{"email": "datharajgdr@gmail.com"}
    - utter_goodbye

## no greet story
* restaurant_search{"cuisine": "mexican", "location": "delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "delhi"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "datharajgdr@gmail.com"}
    - slot{"email": "datharajgdr@gmail.com"}
    - utter_goodbye

## no greet story 2
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
## story 
* restaurant_search{"price": "mid", "cuisine": "american", "location": "bangalore"}
    - slot{"cuisine": "american"}
    - slot{"location": "bangalore"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye

## story 2
* restaurant_search{"price": "mid", "cuisine": "chinese", "location": "bengaluru", "email": "divyagaripelly@gmail.com"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bengaluru"}
    - slot{"price": "mid"}
    - slot{"email": "divyagaripelly@gmail.com"}
    - action_send_email
    - slot{"email": "divyagaripelly@gmail.com"}
    - utter_goodbye
## story 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "nizamabad"}
    - slot{"location": "nizamabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye

## story 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "agra"}
    - slot{"location": "agra"}
    - utter_ask_cuisine
* cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - action_send_email
    - slot{"email": "pgdmlupgrad@gmail.com"}
    - utter_goodbye

## story 5
* restaurant_search{"price": "mid", "cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "datharajgdr@gmail.com"}
    - slot{"email": "datharajgdr@gmail.com"}
    - action_send_email
    - utter_goodbye

## story 6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* email{"email": "datharajgdr@gmail.com"}
    - slot{"email": "datharajgdr@gmail.com"}
    - action_send_email
    - utter_goodbye
	
## story 7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* email{"email": "xxxx@gmail.com"}
    - slot{"email": "xxxx@gmail.com"}
    - action_send_email
    - utter_goodbye

## story 8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* email{"email": "yyy@gmail.com"}
    - slot{"email": "yyy@gmail.com"}
    - action_send_email
    - utter_goodbye

## story 8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "new delhi"}
    - slot{"location": "new delhi"}
    - utter_ask_cuisine
* cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* email{"email": "zzzz@gmail.com"}
    - slot{"email": "zzzz@gmail.com"}
    - action_send_email
    - utter_goodbye


## story 9
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "agra"}
    - slot{"location": "agra"}
    - utter_ask_cuisine
* cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* email{"email": "datharajgdr@gmail.com"}
    - slot{"email": "datharajgdr@gmail.com"}
    - action_send_email
    - utter_goodbye

## story 10
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* cuisine{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* email{"email": "datharajgdr@gmail.com"}
    - slot{"email": "datharajgdr@gmail.com"}
    - action_send_email
    - utter_goodbye

## story 11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* email{"email": "pgdml@gmail.com"}
    - slot{"email": "pgdml@gmail.com"}
    - action_send_email
    - utter_goodbye

## story 12
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* email{"email": "cccc@gmail.com"}
    - slot{"email": "cccc@gmail.com"}
    - action_send_email
    - utter_goodbye

## story 13
* greet
    - utter_greet
* restaurant_search{"price": "mid", "cuisine": "chinese", "location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "hyderabad"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye

## story 15
* restaurant_search{"price": "mid", "cuisine": "american", "location": "delhi"}
    - slot{"cuisine": "american"}
    - slot{"location": "delhi"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* email{"email": "ggg@gmail.com"}
    - slot{"email": "ggg@gmail.com"}
    - action_send_email
    - utter_goodbye
	
## story 13
* greet
    - utter_greet
* restaurant_search{"price": "mid", "cuisine": "chinese", "location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "hyderabad"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye

## story 14
* restaurant_search{"price": "mid", "cuisine": "american", "location": "delhi"}
    - slot{"cuisine": "american"}
    - slot{"location": "delhi"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* email{"email": "ggg@gmail.com"}
    - slot{"email": "ggg@gmail.com"}
    - action_send_email
    - utter_goodbye
