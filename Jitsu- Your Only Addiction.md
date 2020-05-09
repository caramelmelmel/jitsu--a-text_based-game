# Jitsu- Your Only Addiction
How to play your game
Describe your code
This game is a text-based IDE game that is developed solely only by Melody Yun and is solely for the purpose of enjoyment for stress relief. This game is about a ninja who wants to win the war against herbert or his one admired shifu sensei known as the enemy will this ninja be able to rise up to his ranks? or will he not? 

## More about this game 
### How to play?
1. Run in the terminal or IDE that contains jupyter notebook or a pipvenv 
2. Create a gmail account or if you have a gmail account, please only answer "yes" or "no" in this form only. No caps and whatnots. 

    Example:

    ![](https://i.imgur.com/3ZItMFc.png)

3. Follow the instructions down below. Input accordingly like the green ones.

    ![](https://i.imgur.com/crongPd.png)


4. Only key in 'f','s' or 'w' or else you will automatically be exited out of the game.

    ![](https://i.imgur.com/QudzlJO.png)
    
5. You would be able to see your data in the firebase as the data accumulates.
    ![](https://i.imgur.com/x1blye0.png)
6. If you win and lose, you would be able to see the following in your firebase.
7. If you win, you earn 7 coins, if you lose, you earn 3 coins and if you_draw, you win nothing


## Code explanation
Please install the following libraries and environments with the following commands:
```
pip install libdw
```
```
pip install pyrebase
```
```
pip install jupyter notebook 
```
or install anaconda 
```
sudo apt install pipenv
```
### The code explanation
1. The following ensures that the user has created a signup account. This enables the user to go into the firebase.

3. The following classes are created for the pupose of the ninja class to battle against the enemy class.

5. The tutorial functions allow the code to be easily reusable and the writing of the code to be more efficient.


7. To proceed, the game is played as follows.
     a. win by element. We create a list to temporarily store variables of the enemy and the player for comparison purpose.
     b. To increase the complexity of the game, we actually use a random generator for the enemy and get_next_values for the player to update the state and also give an attack ouput that gives the player an advantage over the enemy.

5. Some statements are classified into functions to allow for modularity.
6. The classes are done so that instantiation can occur.

###The code
1.
```
# first part 1a.

already_created_gmail_account = input("Have you created a gmail account? please enter yes or no: ")
if already_created_gmail_account == "NO" or already_created_gmail_account == "No" or already_created_gmail_account == "no" or already_created_gmail_account == "nO":
    print("you might want to register at"+"https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgmail.com%26oq%3Dgmai%26aqs%3Dchrome.1.69i57j69i59j69i61l2j69i60.5101j0j1%26sourceid%3Dchrome%26ie%3DUTF-8&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    ask_user = input("Have you created a gmail account? please enter yes or no: ")
   
    if ask_user == "yes":
        print("Ok please sign in with an email and a password")
        email = input("Gmail: ")
        print("You have entered an email")
        pwd = input("Password: ")
        print("you have entered a password")
        user = auth.create_user_with_email_and_password(email,pwd)
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
        print("You have signed in successfully")'''

#2.
class elemental(sm.SM):
    def __init__(self):
        self.attack = rand.choice(5,12) 
        self.defence = 1
        self.health = 1
        
    def elemental_attack(self,enemy):
        damage = self.attack
        enemy.health -= damage//4
        return enemy_health
    
    def get_next_values(self,state,inp): #the input should be between 1 to 5
        if state >=9 :
            if inp < 5:
                next_state = 6
                self.attack -= 5
        elif state < 9 :
            if inp <= 5:
                self.attack += inp * 1.5
                next_state = 8
                
```#2. class Ninja(elemental):
    def __init__(self,name,val):
        self.name = name
        self.health = 7 
        self.attack = 10
        self.start_state = int(input("choose a number you would like to put in "))
        
    def quit_game(self):
        self.health = 0
        return "You have quit the game and you will not earn any of the values even from the saved game."
    
    def elemental_posession(self,enemy):
        self.health -= 1
        
    def elemental_check(self,value):
        self.attack = value *1.5 + 7
        return self.attack 
    
    def get_next_values(self,state,inp): #the input should be between 1 to 5
        if state >=9 :
            if inp < 5:
                next_state = 6
                self.attack -= 5
        elif state < 9 :
            if inp <= 5:
                self.attack += inp * 1.5
                next_state = 8
            
        return self.attack #output
        

```

``` #Q3.
def try_tutorial():
    print("You have the following elements available to you!")
    el_list = ["fire",'water',"snow"]
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
    el_list = ["fire","water","ice"]
    for i in el_list:
        print(i)
    print("You can win by elements: fire beats snow, snow beats water and water beats fire")
    print("You get it? Now, you can challenge our very own sensei and herbert the polar bear!")
    print("Let's try!")
    try_tutorial()
    print("Now that you have managed to try and play the elements, let's head back!")
```

```
#4a.
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
                
```
```
#4b. 
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
```

 ## Youtube Link Demo
 https://youtu.be/wMQONLl8DGg
