# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
#define mc = Character("MC")
define mc = Character("[maname]", color="#f3e40e") # Main Character
define joe = Character("Joe", color="#0e57f3")
define mic = Character("Micheal", color="#0ef3a7")

#
#image joe = im.Scale("intro/assets/joe_2_free.png", 1920,1080)
#image scale = im.Scale("imagenacme", 1920,1080)
# The game starts here.


# Beginning
label start:
    menu optional_name:
        #"Hi! Are you 18 or above?"
        "Hi, are you ready"
        "Yes!":
            $ maname = renpy.input("What your name?(Default: Bill)")
            $ maname = maname.strip()
            if not maname:
                $ maname = "Bill"
            jump testroom
        "I'm NOT":
            return
# Story intro

label testroom:
#to Do : Anpassen
    show bg_home_table
    "Hello fellow gaming intusiast "
    extend "Thank you for downloading the game. "
    extend "This game is under active and continous development. "
    extend "This is an early stage build wich purpose is to present the basics of the game." 
    "There are many missing contents right now which are to be added in the future builds. " 
    extend "In the next stages the development focuses on the story writing and filling all the gaps that has been left open." 
    "If you find any bug or glitch please don't hesitate to contact the Dev Team on the F95 site or leave a comment on the thread."
    extend " Thank you for your understanding and I wish you a great day."
    "Have fun."
    hide bg_home_table

    # This ends the game.


label joeishere:
    scene office_lobby_2
    mc " Uhhhh, what a week. \n" 
    extend "I cant wait when this week is over"
    
    mc "Wow, how is that guy?"
    
    show joe_mic at right with moveinright
    
    joe "HI my friend, i would love to introduce myself"
    joe "I am Joe, i bought the company resently"

    hide joe_mic with moveoutright

    jump introjoe


#label handytest:
#    scene bg room
#
#    call phone_jlo


#label handytest2:
#    scene bg beach
#
#    call phone_pics

#label phone_jlo_with:
#    scene bg room
#    
#    call phone_jlo_again


#rename any character
#    $ niname = renpy.input("What is her name?(Default: Nicolette)")
#    $ niname = niname.strip()
#    if not niname:
#        $ niname = "Nicolette"

return