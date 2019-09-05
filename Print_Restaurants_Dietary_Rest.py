###########################################################################
# Module: Print_Restaurants_Dietary_Rest.py
# Exercise: Ch 3 Exercise 18
# Purpose: Prints a list of restaurants that meet dietary restrictions
# Author: Lisa Nydick
# Last Update: 09/28/2018
###########################################################################

# Define named constants for prompt and output text
VEGIT_PROMPT = "Is anyone in your party a vegetarian? "
VEGAN_PROMPT = "Is anyone in your party a vegan? "
GLUTEN_PROMPT = "Is anyone in your party gluten-free? "
REST_CHOICES = "Here are your restaurant choices:"

# Make a list of restaurants
restaurants = ["Joe's Gourmet Burgers", "Main Street Pizza Company", "Corner Cafe", "Mama's Fine Italian", "The Chef's Kitchen"]

#Read in dietary restrictions
vegit = str(input(VEGIT_PROMPT)) # Ask about vegetarian restrictions
vegan = str(input(VEGAN_PROMPT)) # Ask about vegan restrictions
gluten = str(input(GLUTEN_PROMPT)) # Ask about vegan restrictions

print(REST_CHOICES) # Print restaurant choices line

if vegit == 'no':
    if gluten == 'no': # No one is vegitarian or gluten-free, so all restaurants are acceptable
        for i in [0, 1, 2, 3, 4]:
            print(restaurants[i])
    else: # No one is vegitarian, but someone is gluten-free, so eliminate non-gluten-free choices
        for i in [1, 2, 4]:
            print(restaurants[i])
else:
    if vegan == 'no': # No vegetarians are vegan
        if gluten == 'no': # No vegetarians are gluten-free
            for i in [1, 2, 3, 4]: # All vegetarian restaurants are acceptable
                print(restaurants[i])
        else:
            for i in [1, 2, 4]: # Only gluten-free, vegetarian restaurants are acceptable
                print(restaurants[i])
    else:
        for i in [2, 4]: # Only vegan restaurants are acceptable.  All vegan restaurants are also gluten-free, so no need to check for it
            print(restaurants[i])