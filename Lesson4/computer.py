
#All Answers that are suppose to display
#answer_match = ["Match", "match", "MATCH"]
#answer_flashlight = ["Flashlight", "flashlight", "FLASHLIGHT"]
answer_run = ["RUN", "Run", "run"]
answer_hide = ["Hide", "hide", "HIDE"]
answer_follow = ["Follow", "follow", "FOLLOW"]
answer_look = ["look", "LOOK", "Look"]

#Beginning of story
print("\nWelcome Adventure. You are walking through a dark forest tand find two items: a MATCH and a FLASHLIGHT")

print("\nWhich one will you pick?")

ans1 = input(">>")

#You pick up a match it will display the following print
if ans1.lower() == "match":

    print("\nYou pick up the match and strike it, and for an instant, the forest around you is illuminated."
     "You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?"
    )

#If you choose to run instead
    ans2 = input(">>")
    if ans2 in answer_run:
        print("\nYou start to run. Game Over!")

#If you choose to hide instead
        ans2 = input(">>")
    elif ans2 in answer_hide:
        print("\nYour start hiding behind a tree")

    
 #You pull a flashlight
elif ans1.lower() == "flashlight":
    print(
        "You pick up the flashlight and turn it on. You see the pathway lit up in front of you,"
        "\nbut you though you also heard sometthing off to the side. Do you want to FOLLOW the "
        "\npath or LOOK in the trees for the thing that made the noise?"
    )
#        print("\nYou pick up the flashlight and turn it on. You see the pathway lit up in front of you,")
#        print("but you though you also heard sometthing off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")

#You start following the path
    ans4 = input(">>")
    if ans4 in answer_follow:
        print("\nYou start following the path")
else: 
    print("Trash")





	
