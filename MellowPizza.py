#!/usr/bin/python

import random, pickle

#global variables are usually in all caps TODO change all these below
SAUCE = ["olive oil and garlic","pesto","Mellow Red Sauce"]

CHEESE = ["mozzarella","cheddar","feta cheese","parmesan","provolone","ricotta",
	"Follow Your Heart vegan cheese (GF, motherfucker)"]
FANCY_CHEESE = ["Bleu cheese", "MontAmore", "Mozzarella - FRESH!"]

MEAT = ["anchovies", "applewood smoked bacon", "ground beef", "ham", "meatballs","pepperoni","salami","sausage"]
FANCY_MEAT = ["all-natural grilled chicken", "all-natural grilled steak"]
NOT_MEAT = ["tofu","tempeh"]

VEGGIES = ["artichoke hearts","banana peppers", "basil", "black olives",
         "caramelized onions","garlic","green olives","green peppers",
         "jalapenos","Kalamata olives", "mushrooms", "onions", "pepperoncini", "pineapple", 
		 "pesto swirl","portobello mushrooms", "roasted mushroom trio", "roasted red peppers",
		 "roma tomatoes","spinach","roasted tomatoes"]
FANCY_VEGGIES = ["avocado because you're a dirty Millennial"]

class TasteProfile():
	def __init__(self):
		self.profile_build()
	def profile_build(self):
		self.name = raw_input("What's your name?" )
		self.vegetarian = get_yes_or_no_answer("Are you a vegetarian?" ,"Just answer me, dude.")
		print "Check out your cheese options:"
		ingredient_print(CHEESE)
		print "If you are independently weathly, they also offer these fancy cheeses for an additional fee:"
		ingredient_print(FANCY_CHEESE)
		self.cheesepref = []
		self.cheesepref.append(raw_input("What is your favorite cheese?"))
		self.cheesepref.append(raw_input("What is your second favorite cheese?"))
		self.cheese_dislike = []
		self.cheese_dislike.append(raw_input("Is there any cheese you hate?")
		self.cheese_dislike.append(raw_input("Anything else, hater?")
		#remember to code for idiots who answer bullshit
		if vegetarian:
			print "Here are some non-meat protein options, you hippie:"
			ingredient_print(NOT_MEAT)
			self.non_meatpref = raw_input("What is your favorite kind of fake dead animal?")
		else:
			print "Hey Carnivore, have some meat choices:"
			ingredient_print(MEAT)
			print "Did you win the lottery recently? Because premium meat is available for extra cash:"
			ingredient_print(FANCY_MEAT)
			self.meatpref = []
			self.meatpref.append(raw_input("What's your favorite meat?"))
			self.meatpref.append(raw_input("What's your next favorite meat?"))
			self.meat_dislike = []
			self.meat_dislike.append(raw_input("Is there any meat you hate?")
			self.meat_dislike.append(raw_input("Anything else, hater?")

		print """Vegetables are good for you. The veggies below are normal-priced. 
			If you wanna pay out the nose for an avocado and simultaneously cause the drought in Calfornia, you can do that, too. 
			Here's your options:"""
		ingredient_print(VEGGIES)
		self.veggiepref = []
		self.veggiepref.append(raw_input("What's your favorite vegetable?"))
		self.veggiepref.append(raw_input("What's your next favorite veggie?"))
		self.veggiepref.append(raw_input("How about one more? Michelle Obama will be proud."))
		self.veggie_dislike = []
		self.veggie_dislike.append(raw_input("Which of these veggies do you hate?")
		self.veggie_dislike.append(raw_input("Anything else?")

		
			
		
def ingredient_print(c):
	for x in range(len(c)/3):
		print "%s    %s    %s" %(c[0+3*x],c[1+3*x],c[2+3*x])
	if mod(len(c),3) == 0:
		pass
	if mod(len(c),3) == 1:
		print "%s" %(c[-1])
	if mod(len(c),3) == 2:
		print "%s    %s" %(c[-2],c[-1])


def choose_with_probability(things, probs = []):
	if len(probs) == 0: 
		my_choice = random.choice(things)
	else:
		my_choice = random.choice(things) #TODO: implement probability; probably use numpy.random.choice
		
	return my_choice
	
def get_yes_or_no_answer(text, reply):
	max_times_to_ask = 3
	times_asked = 0
	got_response = False
	acceptable_responses = ["yes", "yeah", "sure", "of course", "y", "uh huh", "yup"]
	negative_responses = ["no", "nah", "nope", "hell no", "no way", "n", "gross", "negative", "ew"]
	
	while got_response == False:
		
		response = raw_input(text)
		response = response.lower()
		
		if response in acceptable_responses: 
			choice = True
			got_response = True
			
		elif response in negative_responses:
			choice = False
			got_response = True
			
		else:
			print reply
		
		times_asked += 1
		
		if times_asked == 1: 
			reply = reply.upper()
		elif times_asked == 2:
			text = text.upper()
		
		if times_asked == max_times_to_ask and not got_response: 
			print "You're an asshole."
			got_response = True
			choice = False		
	return choice

def get_profiles():
	try: 
		f = pickle.load(open("Profiles.dat", "r"))
	except:
		f = {}
	return f
	
	
if __name__ == "__main__":
	
	
	print "Fleens? You're not fleens! Hmph!... Whoever you are, MAKE ME A PIZZA!"
	#This is a reference to the Zoombinis, obviously
	print "(At Mellow Mushroom)"
	print "You can choose your favorite ingredients to make a pizza just for you or make a random pizza!"

	ProfileDict = get_profiles()
	
	x = get_yes_or_no_answer("Have you been here before?")
	if x:
		y = get_yes_or_no_answer("Did you make a taste profile?")
		if y: 
			z = get_yes_or_no_answer("Do you want to use your taste profile today?")
		else:
			Profile = False
	else: 
		a = get_yes_or_no_answer("Do you want to create a taste profile?")
		if a: 
			Profile = TasteProfile()
	
	toppings = raw_input("How many toppings do you want? ")
	toppings=int(toppings)

	wants_fancy_cheese = get_yes_or_no_answer("Do you want to pay extra for fancy cheese? ",
		"What are you talking about?")
	carnivore = get_yes_or_no_answer("Do you want meat on this pizza? ", "I was trying to be nice.")
	if carnivore:
		wants_fancy_meat = get_yes_or_no_answer("Do you want to pay extra for fancy meat? ", 
		"Sir, you're making a scene.")
	wants_fancy_veggies = get_yes_or_no_answer("Do you want to pay extra for avocados and single-handedly"\
		" cause the drought in California, you monster? ", "I think you know what I think about that.")

	pizza = []

	if Profile:
		pass #TODO THIS
	else:
		
	
	pizza.append(choose_with_probability(sauce, sauce_probs))

	if wants_fancy_cheese:
		pizza.append(choose_with_probability(fancy_cheese))
	else: 
		pizza.append(choose_with_probability(cheese))

	if not carnivore:
		pizza.append(choose_with_probability(not_meat))
	elif wants_fancy_meat:
		pizza.append(choose_with_probability(fancy_meat))
	else:
		pizza.append(choose_with_probability(meat))

	if wants_fancy_veggies:
		pizza.append(choose_with_probability(fancy_veggies))
		toppings -= 1
		
	for a in range(toppings-1):
		pizza.append(choose_with_probability(veggies)) #TODO exclude duplicate veggies

	print "CONGRATULATIONS! \nYour perfect personalized pizza is a delicious Mellow Mushroom pizza with:"

	my_pizza = ""
	for thing in pizza: 
		my_pizza += "%s " % thing 
		
	print my_pizza

