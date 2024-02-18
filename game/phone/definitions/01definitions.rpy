# /!\ default
# pc as in phone character :monikk:
default pc_sayori  = phone.character.Character("Sayori", phone.asset("sayori_icon.png"), "s", 21, "#22Abf8")
default pc_mc      = phone.character.Character("MC", phone.asset("mc_icon.png"), "mc", 35, "#484848")
default pc_yuri    = phone.character.Character("Yuri", phone.asset("yuri_icon.png"), "y", 20, "#a327d6")
default pc_monika  = phone.character.Character("Monika", phone.asset("monika_icon.png"), "m", 40, "#0a0")
default pc_natsuki = phone.character.Character("Natsuki", phone.asset("natsuki_icon.png"), "n", 45, "#fbb")
default pc_jlo     = phone.character.Character("Jlo", phone.asset("jlo.gif"), "j", 44, "#fbb")


default pov_key = "mc"

define phone_s  = Character("Sayori", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_mc = Character("MC", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")

init 100 python in phone.application:
    add_app_to_all_characters(message_app)
    add_app_to_all_characters(call_history_app)
    add_app_to_all_characters(calendar_app)

init 100 python in phone.calendar:
    add_calendar_to_all_characters(2023, 6, MONDAY)

init phone register:
    define "Welcome":
        add "s" add "mc" add "y" add "m" add "j" 
        icon phone.asset("default_icon.png")
        as thanks_for_using_my_framework key "ddu"

init phone register: 
    define "Jlo":
        add "mc" add "j"
        icon phone.asset("mc_icon.png")
        as my_first_con key "test"

label phone_discussion_test:
    phone discussion "ddu":
        time year 2023 month 6 day 5 hour 16 minute 30 delay -1 # exact date and time at which i wrote this. yes i am feeling quite silly and goofy
        label "'Sayori' has been added to the group" delay -1
        label "'MC' has been added to the group" delay -1
        label "'Yuri' has been added to the group" delay -1
        label "'Monika' has been added to the group" delay -1
        label "'JLo' has been added to the group" delay 0.2
        "j" "Hey there!"
        "m" "Thank you for using my framework."
        "m" "I mean {i}of course{/i} you're using {b}this{/b} framework."
        "m" "...not like there are any better ones out there~"
        "j" "natsuki!!!!! {emoji=EllenScream}"
        "j" "no being a meanie!!!!!!!{emoji=EllenScream}{emoji=EllenScream}{emoji=EllenScream}"
        "j" "If you are interested in DDLC mods, be sure to check out our mod {a=https://undercurrentsmod.weebly.com}Doki Doki Undercurrents{/a}! {emoji=Melody}"
        "mc" "In case you encounter an issue (or wanna make a suggestion),"
        "mc" "you can:"
        "mc" "DM me at {i}elckarow{/i} on Discord,"
        "mc" "open an issue on {a=https://github.com/Elckarow/Better-EMR-Phone}GitHub{/a},"
        "mc" "make a post on the phone's {a=https://elckarow.itch.io/better-emr-phone}Itch page{/a}."
        "s" "Happy coding!" 
    phone end discussion

    return

label phone_call_test:
    phone call "s"
    phone_s "Ohayouuu!!!!!!!!!!!!!!!!"
    phone_mc "Hey!"
    "Why is she always this energetic?"
    phone end call
    "..."

    return



# create two phone Character objects
default phone_sayori = phone.character.Character("Sayori", phone.asset("sayori_icon.png"), "s", 21,   "#22Abf8")
default phone_mc = phone.character.Character("MC", phone.asset("mc_icon.png"), "mc", 35, "#484848")

# create a group chat manually
default mc_sayo_gc = phone.group_chat.GroupChat("Sayori", phone.asset("sayori_icon.png"), "mc_sayo"). add_character("mc").add_character("s")
default mc_sayo_gc_j = phone.group_chat.GroupChat("Jlo", phone.asset("sayori_icon.png"), "mc_sayo_gc_j"). add_character("mc").add_character("j")

# create another group chat using `init phone register`
# and add a few messages
init phone register:
    define "goofy ahh chat":
        icon phone.asset("sayori_icon.png") key "goofy"
        add "mc" add "s" as goofy
        transient

    time month 1 day 26 year 2013 hour 14 minute 31
    "mc" "Ah!"
    "s" "Boo!"
    "mc" "Ah!"

label phone_discussion_testnew:
    scene expression "#fdfdfd"


    phone register mc_sayo_gc:  # using the group chat object directly
        image "s" Solid("#000", xysize=(50, 50))
        "s" "oops"

    "..."
    "Hmm?"
    "A message from Sayori?"

    phone discussion "mc_sayo": # using the gc's key
        pause

    "..."
    "... Really now?"

    phone discussion: # no gc. uses the one used before
        menu:
            "a square?":
                "mc" "a square?"
            "a black square?":
                "mc" "a black square?"
                "mc" "but why?"
     
    "..."
    
    

    "What an airhead..."
    phone end discussion
    return




label phone_jlo:
    phone discussion "test":
        time year 2023 month 6 day 5 hour 16 minute 30 delay -1 # exact date and time at which i wrote this. yes i am feeling quite silly and goofy
        label "'MC' has been added to the group" delay -1
        label "'JLo' has been added to the group" delay 0.2
        "j" "Hey there!"
        "mc" "you can:"
        "mc" "DM me at {i}elckarow{/i} on Discord,"
        "mc" "open an issue on {a=https://github.com/Elckarow/Better-EMR-Phone}GitHub{/a},"
        "mc" "make a post on the phone's {a=https://elckarow.itch.io/better-emr-phone}Itch page{/a}."
        "j" "Happy coding!" 
    phone end discussion

    return