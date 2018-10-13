#!/usr/bin/python

import random, pickle
import numpy as np

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
		self.default_profile()
	
	def default_profile(self):
		self.name = "default"
		self.vegetarian = False
		self.cheesepref = []
		self.cheese_dislike = []
		self.meatpref = []
		self.meat_dislike = []
		self.veggiepref = []
		self.veggie_dislike = []
		
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
		self.cheese_dislike.append(raw_input("Is there any cheese you hate?"))
		self.cheese_dislike.append(raw_input("Anything else, hater?"))
		#remember to code for idiots who answer bullshit
		if self.vegetarian:
			print "Here are some non-meat protein options, you hippie:"
			ingredient_print(NOT_MEAT)
			self.non_meatpref = raw_input("What is your favorite kind of fake dead animal?")
		else:
			print "Hey Carnivore, have some meat choices:"
			ingredient_print(MEAT)
			print "Did you win the lottery recently? Because premium meat is available for extra cash:"
			ingredient_print(FANCY_MEAT)
			self.meatpref = []
			self.meatpref.append(raw_input("What's your favorite meat? "))
			self.meatpref.append(raw_input("What's your next favorite meat? "))
			self.meat_dislike = []
			self.meat_dislike.append(raw_input("Is there any meat you hate? "))
			self.meat_dislike.append(raw_input("Anything else, hater? "))

		print """Vegetables are good for you. The veggies below are normal-priced, except for one. 
			If you wanna pay out the nose for an avocado and simultaneously cause the drought in Calfornia, you can do that, too. 
			Here's your options:"""
		ingredient_print(VEGGIES)
		self.veggiepref = []
		self.veggiepref.append(raw_input("What's your favorite vegetable? "))
		self.veggiepref.append(raw_input("What's your next favorite veggie? "))
		self.veggiepref.append(raw_input("How about one more? Michelle Obama will be proud. "))
		self.veggie_dislike = []
		self.veggie_dislike.append(raw_input("Which of these veggies do you hate? "))
		self.veggie_dislike.append(raw_input("Anything else? "))
		self.veggie_dislike.append(raw_input("One more: "))

		
			
		
def ingredient_print(c):
	for x in range(len(c)/3):
		print "%s    %s    %s" %(c[0+3*x],c[1+3*x],c[2+3*x])
	if len(c)%3 == 0:
		pass
	if len(c)%3 == 1:
		print "%s" %(c[-1])
	if len(c)%3 == 2:
		print "%s    %s" %(c[-2],c[-1])


def choose_with_probability(things, probs =[]):
	if len(probs) == 0: 
		my_choice = random.choice(things)
	else:
		my_choice = np.random.choice(things, p=probs)
		
	return my_choice
	
def get_yes_or_no_answer(text, reply):
	max_times_to_ask = 3
	times_asked = 0
	got_response = False
	acceptable_responses = ["yes", "yeah", "yah", "ya", "sure", "of course", "y", "uh huh", "yup"]
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
	
def save_profile(profile_dict):
	try:
		with open("Profiles.dat", "wb") as file:
			pickle.dump(profile_dict, file)
			print "profile saved"
	except IOError:
		print "didn't save file successfully."

def pizza_builder(Profile):
	global CHEESE
	global MEAT
	global NOT_MEAT
	global VEGGIES
	global FANCY_CHEESE
	global FANCY_MEAT
	global FANCY_VEGGIES

	toppings = raw_input("How many toppings do you want (in addition to cheese)? ")
	toppings = int(toppings)

	wants_fancy_cheese = get_yes_or_no_answer("Do you want to pay extra for fancy cheese? ",
											  "What are you talking about?")
	carnivore = get_yes_or_no_answer("Do you want meat on this pizza? ", "I was trying to be nice.")
	if carnivore:
		wants_fancy_meat = get_yes_or_no_answer("Do you want to pay extra for fancy meat? ",
												"Sir, you're making a scene.")
	else:
		wants_fancy_meat = False
	wants_fancy_veggies = get_yes_or_no_answer("Do you want to pay extra for avocados and single-handedly" \
											   " cause the drought in California, you monster? ",
											   "I think you know what I think about that.")

	pizza = []

	if Profile:
		cheese_probs = []
		if wants_fancy_cheese:
			base_probs = 1.0 / (len(CHEESE) + len(FANCY_CHEESE) - len(Profile.cheese_dislike) + len(Profile.cheesepref))
			for a in (CHEESE + FANCY_CHEESE):
				if a == Profile.cheese_dislike:
					cheese_probs.append(0)
				elif a == Profile.cheesepref:
					cheese_probs.append(base_probs * 2.0)
				else:
					cheese_probs.append(base_probs)
		else:
			base_probs = 1.0 / (len(CHEESE) - len(Profile.cheese_dislike) + len(Profile.cheesepref))
			for a in (CHEESE):
				if a == Profile.cheese_dislike:
					cheese_probs.append(0)
				elif a == Profile.cheesepref:
					cheese_probs.append(base_probs * 2.0)
				else:
					cheese_probs.append(base_probs)
		nonmeat_probs = []
		if Profile.vegetarian:
			base_probs = 1.0 / (len(NOT_MEAT) + len(Profile.non_meatpref))
			for a in NOT_MEAT:
				if a == Profile.non_meatpref:
					nonmeat_probs.append(base_probs * 2.0)
				else:
					nonmeat_probs.append(base_probs)
		else:
			meat_probs = []
			if wants_fancy_meat:
				base_probs = 1.0 / (len(MEAT) + len(FANCY_MEAT) - len(Profile.meat_dislike) + len(Profile.meatpref))
				for a in (MEAT + FANCY_MEAT):
					if a == Profile.meat_dislike:
						meat_probs.append(0) 
					elif a == Profile.meatpref:
						meat_probs.append(base_probs * 2.0)
					else:
						meat_probs.append(base_probs)
			else:
				base_probs = 1.0 / (len(MEAT) - len(Profile.meat_dislike) + len(Profile.meatpref))
				for a in (MEAT):
					if a == Profile.meat_dislike:
						meat_probs.append(0)
					elif a == Profile.meatpref:
						meat_probs.append(base_probs * 2.0)
					else:
						meat_probs.append(base_probs)

		veggie_probs = []
		if wants_fancy_veggies:
			base_probs = 1.0 / (len(VEGGIES) + len(FANCY_VEGGIES) - len(Profile.veggie_dislike) + len(Profile.veggiepref))
			for a in (VEGGIES + FANCY_VEGGIES):
				if a == Profile.veggie_dislike:
					veggie_probs.append(0)
				elif a == Profile.veggiepref:
					veggie_probs.append(base_probs * 2.0)
				else:
					veggie_probs.append(base_probs)
		else:
			base_probs = 1.0 / (len(VEGGIES) - len(Profile.veggie_dislike) + len(Profile.veggiepref))
			for a in (VEGGIES):
				if a == Profile.veggie_dislike:
					veggie_probs.append(0)
				elif a == Profile.veggiepref:
					veggie_probs.append(base_probs * 2.0)
				else:
					veggie_probs.append(base_probs)

	pizza = []

	# pizza.append(choose_with_probability(sauce, sauce_probs)) OOPS WE FORGOT ABOUT THE SAUCE OUR BAD
	if wants_fancy_cheese:
		cheese_list = CHEESE + FANCY_CHEESE
	else:
		cheese_list = CHEESE
		
	if wants_fancy_meat:
		meat_list = MEAT + FANCY_MEAT
	else: 
		meat_list = MEAT
		
	if wants_fancy_veggies:
		veggie_list = VEGGIES + FANCY_VEGGIES
	else: 
		veggie_list = VEGGIES
	
	pizza.append(choose_with_probability(cheese_list, cheese_probs))
	pizza.append(choose_with_probability(meat_list, meat_probs))

	for a in range(toppings - 1):
		pizza.append(
			choose_with_probability(veggie_list, veggie_probs))  # TODO exclude duplicate veggies

	print "CONGRATULATIONS! \nYour perfect personalized pizza is a delicious Mellow Mushroom pizza with:"

	my_pizza = ""
	for thing in pizza:
		my_pizza += "%s " % thing

	print pizza
	
if __name__ == "__main__":
	
	
	print "Fleens? You're not fleens! Hmph!... Whoever you are, MAKE ME A PIZZA!"
	#This is a reference to the Zoombinis, obviously
	print "(At Mellow Mushroom)"
	print "You can choose your favorite ingredients to make a pizza just for you or make a random pizza!"

	ProfileDict = get_profiles()
	Profile = TasteProfile()
	
	x = get_yes_or_no_answer("Have you been here before? ","Don't be a dick.")
	if x:
		y = get_yes_or_no_answer("Did you make a taste profile? ","Stop being difficult.")
		if y: 
			z = get_yes_or_no_answer("Do you want to use your taste profile today? ","Just answer the question.")
			# TODO: Select, load profile here 
	else: 
		a = get_yes_or_no_answer("Do you want to create a taste profile? ","Come on, man.")
		if a: 
			Profile.profile_build()
			# TODO: add new profile to ProfileDict
			save_profile(ProfileDict)
			
	pizza_builder(Profile)
	


