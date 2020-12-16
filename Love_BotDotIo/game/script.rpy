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
    import numpy as np 
    from sklearn.linear_model import LinearRegression
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

    class Rival(object):
        def __init__(self):
            self.sceneResults = list()

            '''
            Rival needs to start _somewhere_. So let's set it up like
            the love interest and pair it up with a random responseValue
            '''
            initChoice =   [random.randrange(-5, 5, 1), #Confidence
                            random.randrange(-5, 5, 1), #Empathy
                            random.randrange(-5, 5, 1), #Responsibility
                            random.randrange(-5, 5, 1), #Romantic
                            random.randrange(-5, 5, 1), #Caring
                            random.randrange(-5, 5, 1), #Humor
                            random.randrange(-5, 5, 1), #Intelligence
                            random.randrange(-5, 5, 1), #Cool
                            random.randrange(-5, 5, 1),
                            random.randrange(-5, 5, 1)]

            responseValue = random.randrange(-10, 10, 1)
            initSceneResult = (initChoice, responseValue)

            self.appendSceneResult(initSceneResult)

        def appendSceneResult(self, sceneResult):
            if !isinstance(sceneResult, tuple):
                raise ValueError("Scene Result must be a tuple")
            self.sceneResults.append(sceneResult)

        def findBestFit(self, dialogueOptions):
            '''
            Will attempt to find the best response using the most recent responseValues
            of the Love Interest, and previous sceneResults data.

            dialogueOptions - List of the values associated with available dialogue options
            '''
            
            '''
            Multivariate linear regression.

            This reconstructs the best fit each call to findBestFit().

            Data organization: [([dialogueVal, ...], responseVal), ...]
            '''
            dialogueValues = [i[0] for i in self.sceneResults] 
            responseValues  = [j[1] for j in self.sceneResults]
            if len(dialogueOptions) != len(responseValues):
                raise ValueError("Data in dialogueValues and responseValues not the same size")
            x, y = np.array(dialogueValues).reshape(-1,1), np.array(responseValue)

            model = LinearRegression().fit(x, y)

            prediction = model.predict(x)

            '''
            Choose the option that is closest in pairwise value to the Rival's predictions.

            Note that order matters here, so the list comprehension accounts for that.
            '''
            bestOption = []
            prevDiffs = []
            for option in dialogueOptions:
                diffs = [abs(i - j) for i, j in zip(prediction, option)]
                if len(bestOption) == 0: # First iteration bestOption is empty
                    bestOption = [i for i in option]
                    prevDiffs = [j for j in diffs]
                else:
                    '''
                    Change bestOption if current diffs are greater pairwise than prevDiffs.

                    If there are a majority of greater values in `prevDiffs`, keep current
                    bestOption as it is "greater", and hence closer to the best option.
                    '''
                    comparison = zip(diffs, prevDiffs)
                    total, other = 0
                    for a, b in comparison:
                        if a >= b:
                            total += 1
                        else:
                            other += 1
                    if other > total:
                        continue
                    else:
                        bestOption = [i for i in option]
                        prevDiffs = [j for j in diffs]
            
            # Return the best choice corresponding to an available dialogue option for Rival
            return bestOption

    Rival = Rival()



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
