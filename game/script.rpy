# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
#define mc = Character("MC")
define mc = Character("[maname]", color="#f3e40e", image="man.png" , callback=name_callback, cb_name="[maname]") # Main

#
image joe = im.Scale("intro/assets/joe_2_free.png", 1920,1080)
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
            jump office99
        "I'm NOT":
            return
# Story intro

label testroom:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.


label joeishere:
    scene office_lobby_2
    mc "hi welcome"
    
    mc "How is that guy?"
    
    show joe at right
    
    mc "HI Joe"


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

return