#!/usr/bin/env python
# coding: utf-8

# # Libraries and Modules
#

# In[13]:


# install the following libraries used using the pip command above in the anaconda environment on the macbook air and macbook pro
import libdw
from libdw import sm

# push to firebase using the python wrapper
import pyrebase

# import the relevant libraries to operate in other ways
import numpy

# import the relevant libraries
import random

# # Firebase authentication and signup phase
# ensure that you have created a firebase project authentication
# firebase authentication and configuration in the following dictionary
config = {"apiKey": "",
          "authDomain": "",
          "databaseURL": "",
          "projectId": "",
          "storageBucket": "",
          "messagingSenderId": "720730224613",
          "appId": "",
          "measurementId": ""}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# allow the user to signup and pass firebase authentication
already_created_gmail_account = input("Have you created a gmail account? please enter yes or no: ")
if already_created_gmail_account == "NO" or already_created_gmail_account == "No" or already_created_gmail_account == "no" or already_created_gmail_account == "nO":
    print(
        "you might want to register at" + "https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgmail.com%26oq%3Dgmai%26aqs%3Dchrome.1.69i57j69i59j69i61l2j69i60.5101j0j1%26sourceid%3Dchrome%26ie%3DUTF-8&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    ask_user = input("Have you created a gmail account? please enter yes or no: ")

    if ask_user == "yes":
        print("Ok please sign in with an email and a password")
        email = input("Gmail: ")
        print("You have entered an email")
        pwd = input("Password: ")
        print("you have entered a password")
        user = auth.create_user_with_email_and_password(email, pwd)
        print("Your user account has been created for jitsu. Now you will sign in")
        email = input("Gmail: ")
        pwd = input("Password : ")
        signin = auth.sign_in_with_email_and_password(email, pwd)

else:
    sub_times = input("Have you already created a jitsu account?")
    if sub_times == 'yes':
        email = input("Gmail: ")
        pwd = input("Password : ")
        signin = auth.sign_in_with_email_and_password(email, pwd)
        print("You have signed in successfully")


# Note: The above print statements are also meant for debugging puposes.


#
# # Elemental Introduction and Game

# define the elemental rules for the user and the following game tutorial for the user

def try_tutorial():
    print("You have the following elements available to you!")
    el_list = ["fire", 'water', "snow"]
    for i in el_list:
        user_inp = input("What elements would you like to play: ")
        if user_inp == 'fire':
            print("Well Done, you have played fire")
        if user_inp == 'water':
            print("Well done, you have played water")
        if user_inp == 'snow':
            print('you have unleashed the snow jitsu in you.')


def jitsu_tutorial():
    print("First the elements that you can play are only these few:")
    el_list = ["fire", "water", "ice"]
    for i in el_list:
        print(i)
    print("You can win by elements: fire beats snow, snow beats water and water beats fire")
    print("You get it? Now, you can challenge our very own sensei and herbert the polar bear!")
    print("Let's try!")
    try_tutorial()
    print("Now that you have managed to try and play the elements, let's head back!")


class SM:
    def start(self):
        self.state = self.start_state  # set state as startState

    def step(self, input):
        # print("Step function called")
        (next_state, output) = self.get_next_values(self.state, input)
        self.state = next_state  # updates the current state to be equal to the next state
        return output

    def transduce(self, inputs):
        self.start()
        outputs = []
        for input_value in inputs:
            output = self.step(input_value)
            if (self.done(self.state)):
                break
            else:
                outputs.append(output)

        return outputs

    def done(self, inp):
        pass


class elemental(sm.SM):
    def __init__(self):
        self.attack = rand.choice(5, 12)
        self.defence = 1
        self.health = 1

    def elemental_attack(self, enemy):
        damage = self.attack
        enemy.health -= damage // 4
        return enemy_health

    def get_next_values(self, state, inp):  # the input should be between 1 to 5
        if state >= 9:
            if inp < 5:
                next_state = 6
                self.attack -= 5
        elif state < 9:
            if inp <= 5:
                self.attack += inp * 1.5
                next_state = 8

        return self.attack  # output


# define the character involve in the game
# states will be passed in form of integer values between 5 and 12
# the idea across is to regenerate the next value of the card elements
# let the card numbers range in the form of

# Every player starts as a ninja character

class Ninja(elemental):
    def __init__(self, name, val):
        self.name = name
        self.health = 7
        self.attack = 10
        self.start_state = int(input("choose a number you would like to put in "))

    def quit_game(self):
        self.health = 0
        return "You have quit the game and you will not earn any of the values even from the saved game."

    def elemental_posession(self, enemy):
        self.health -= 1

    def elemental_check(self, value):
        self.attack = value * 1.5 + 7
        return self.attack

    def get_next_values(self, state, inp):  # the input should be between 1 to 5
        if state >= 9:
            if inp < 5:
                next_state = 6
                self.attack -= 5
        elif state < 9:
            if inp <= 5:
                self.attack += inp * 1.5
                next_state = 8

        return self.attack  # output


# define the 2 key players that the user can play with
class enemy:
    def __init__(self):
        self.health = 7
        self.attack = 12

    def element_choice(self):
        elements = ['fire', 'snow', 'water']
        self.element = random.choice(elements)
        return self.element

    def element_magnitude(self):
        self.attack -= random.randrange(1, 5)
        return self.attack


# the following enables the function to be reused
def print_win():
    print("you win!")


def print_lose():
    print("you lose :<")


def print_draw():
    print("you draw")


def play_the_game():
    user_tut = input("Would you like a jitsu tutorial?")
    if user_tut == 'yes':
        jitsu_tutorial()
        player_in_game()
    else:
        player_in_game()


def player_in_game():
    name = input("what is your name?")
    player = Ninja(name, 5)
    challenger = enemy()
    # this happens for the first time
    el = ['fire', 'water', 'snow']
    el_dict = {"f": 'fire', 's': 'snow', 'w': 'water'}
    # following lists are to compare the elements between the players and attack magnitudes between the players
    player_lst = []
    enemy_lst = []

    num_turns = 7
    enemy_num_turns = 7

    inp = int(input("choose a random number between 5 to 12 to start with"))
    # instantiate what happens next
    st = int(inp)

    print("you have just started the game")
    print("choose from the following elements available to you.")

    for i in el:
        print(i)

    start_el = input("type f for fire, w for water and s for snow ")
    player_lst.append(el_dict[start_el])
    enemy_lst.append(challenger.element_choice)

    next_card_val = player.get_next_values(inp, inp)

    print("the next value is {}".format(next_card_val))  # this confirms the next card played

    while num_turns > 0 and enemy_num_turns > 0:

        next_card_val = player.get_next_values(next_card_val, next_card_val)
        player_list = []
        enemy_list = []
        print("the enemy has attacked, yet again.")
        print("Now choose an element")
        el = input("type f for fire, w for water and s for snow ")
        try:
            player_list.append(el_dict[el])
        except KeyError:
            el = input("please type only f, w or s")
            player_list.append(el_dict[el])

        enemy_list.append(challenger.element_choice())

        if player_list[0] != enemy_list[0]:
            if player_list[0] == el_dict['f'] and enemy_list[0] == el_dict['w']:
                print_lose()
                num_turns -= 1
                enemy_num_turns += 1

            elif player_list[0] == el_dict['w'] and enemy_list[0] == el_dict['f']:
                print_win()
                num_turns += 1
                enemy_num_turns -= 1

            elif player_list[0] == el_dict['w'] and enemy_list[0] == el_dict['s']:
                print_lose()
                num_turns -= 1
                enemy_num_turns += 1

            elif player_list[0] == el_dict['s'] and enemy_list[0] == el_dict['w']:
                print_win()
                num_turns += 1
                enemy_num_turns -= 1

            elif player_list[0] == el_dict['f'] and enemy_list[0] == el_dict['s']:
                print_win()
                num_turns += 1
                enemy_num_turns -= 1

            elif player_list[0] == el_dict['s'] and enemy_list[0] == el_dict['f']:
                print_lose()
                num_turns -= 1
                enemy_num_turns += 1

            elif player_list[0] == el_dict['f'] and enemy_list[0] == el_dict['w']:
                print_lose()
                num_turns -= 1
                enemy_num_turns += 1

        if player_list[0] == enemy_list[0]:
            if next_card_val > challenger.element_magnitude():
                print_win()
                num_turns += 1
                enemy_num_turns -= 1

            elif next_card_val < challenger.element_magnitude():
                print_lose()
                num_turns -= 1
                enemy_num_turns += 1

            elif next_card_val == challenger.element_magnitude():
                print_draw()
                num_turns += 0
                enemy_num_turns += 0

    # compute the number of coins earned based on who lost their life first
    if enemy_num_turns == 0 and num_turns > 0:
        num_coins = 7
        write_to_fb(name, num_coins)
    if num_turns == 0 and enemy_num_turns > 0:
        num_coins = 3
        write_to_fb(name, num_coins)
    if num_turns == 0 and enemy_num_turns == 0:
        num_coins = 0

    print("You have won {} for today! Come back next time!".format(num_coins))
    num_try = 1
    # end the game from firebase
    write = write_from_fb()
    print("You have a total of {} today".format(write))

    return num_coins


# write to firebase


def write_to_fb(name, l):
    db = firebase.database()
    user_p = {name: l}
    db.child("users").push(user_p)
    db.child("users").child("name").set(user_p)
    # for subsequent games
    db.child("name").child("name").update(user_p)
    return user_p


def write_from_fb():
    db = firebase.database()
    users = db.child("users").get()
    return users.val()


play_the_game()




