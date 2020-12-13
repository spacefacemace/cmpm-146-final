# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(_('Eileen'))
define li = Character(_('Love_Intrest'))
define rv = Character(_('Rival'))
define cf = Character(_('Childhood_Friend'))
define rm = Character(_('Roommate'))
define pg = Character(_('player_character'))
define pat = Character(_('Prof._Pat'))
define sesh = Character(_('Prof._Sesh'))


init python:
    import random
    scenes = []

    class Scene(object):
        def __init__(self, label, title):
            self.kind = "scene"
            self.label = label
            self.title = title

            scenes.append(self)

    Scene("scene1", _("Scene1 Name"))
    Scene("scene2", _("Scene1 Name"))
    Scene("scene3", _("Scene1 Name"))
    Scene("scene4", _("Scene1 Name"))
    Scene("scene5", _("Scene1 Name"))
    Scene("scene6", _("Scene1 Name"))
    Scene("scene7", _("Scene1 Name"))
    Scene("scene8", _("Scene1 Name"))
    Scene("scene9", _("Scene1 Name"))
    Scene("scene10", _("Scene1 Name"))

    class LoveInterest(object):
        def __init__(self, interests):
            self.interests = interests

        def getResponse(self, statement):
             rating = 0
             count = 0
             while count < len(self.interests):
                 rating = rating + (self.interests[count]*statement[count])
                 count = count + 1
             return rating

        def textResponse(self, rate):
            if(rate <= -7):
                return "She really didn't like that response"
            elif(rate <= -2):
                return "She doesn't look happy"
            elif(rate < 2):
                return "She looks indifferent"
            elif(rate < 7):
                return "She looks happy"
            elif(rate >= 7):
                return "She loved that response"

    interest = [random.randrange(-5, 5, 1), #Confidence
                random.randrange(-5, 5, 1), #Empathy
                random.randrange(-5, 5, 1), #Responsibility
                random.randrange(-5, 5, 1), #Romantic
                random.randrange(-5, 5, 1), #Caring
                random.randrange(-5, 5, 1), #Humor
                random.randrange(-5, 5, 1), #Intelligence
                random.randrange(-5, 5, 1), #Cool
                random.randrange(-5, 5, 1),
                random.randrange(-5, 5, 1)]

    LoveInterest = LoveInterest(interest)




# The game starts here.

label start:

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


    $ pg_state = [0,0,0,0,0,0,0,0,0,0]
    $ rv_state = [0,0,0,0,0,0,0,0,0,0]

    "This Love Interest has multipliers [interest]"

    jump scene1
label after1:
    jump scene2
label after2:
    jump scene3
label after3:
    jump scene4
label after4:
    jump scene5
label after5:
    jump scene6
label after6:
    jump scene7
label after7:
    jump scene8
label after8:
    jump scene9
label after9:
    jump scene10
label after10:
    "state is [pg_state]"



    # This ends the game.

    return
