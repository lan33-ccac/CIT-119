########################################################################
# Module: Use_pet_Class.py
# Exercise: Ch10_Exercise_1
# Purpose: Works with pet Class
# Last Update Date: 11/14/18
# Author: Lisa Nydick
########################################################################

import pet

def main():
    pet_name = ''
    pet_type = ''
    pet_age = ''

    mypet = pet.Pet(pet_name, pet_type, pet_age)

    pet_name = input("Enter your pet's name: ")
    pet_type = input("Enter your pet type: ")
    pet_age = input("Enter your pet's age: ")

    mypet.set_name(pet_name)
    mypet.set_animal_type(pet_type)
    mypet.set_age(pet_age)

    print("Your pet's name is", mypet.get_name(pet_name))
    print("Your pet's type is", mypet.get_animal_type(pet_type))
    print("Your pet's age is", mypet.get_age(pet_age))



main()