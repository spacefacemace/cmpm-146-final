# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define li = Character(_('Anabelle_Willow'))
define rv = Character(_('Aaron'))
define cf = Character(_('Joshua'))
define rm = Character(_('Vernon'))

define pat = Character(_('Prof._Pat'))
define sesh = Character(_('Prof._Sesh'))

# images under luvint tag
image luvint li_angry = "li_angry.png"
image luvint li_blush = "li_blush.png"
image luvint li_confused = "li_confused.png"
image luvint li_happy = "li_happy.png"
image luvint li_happy2 = "li_happy2.png"
image luvint li_happyblush = "li_happyblush.png"
image luvint li_joy = "li_joy.png"
image luvint li_judgement = "li_judgement.png"
image luvint li_sad = "li_sad.png"
image luvint li_sad2 = "li_sad2.png"
image luvint li_serious = "li_serious.png"
image luvint li_tired = "li_tired.png"
image luvint li_tsundere = "li_tsundere.png"
# images under roommate tag
image roommate rm = "rm.png"
image roommate rm_angry = "rm_angry.png"
image roommate rm_glad = "rm_glad.png"
image roommate rm_smile = "rm_smile.png"
image roommate rm_suspicious = "rm_suspicious.png"
# images under rivchar tag
image rivchar rv = "rv.png"
image rivchar rv_angry = "rv_angry.png"
image rivchar rv_crying = "rv_crying.png"
image rivchar rv_embarassed = "rv_embarassed.png"
image rivchar rv_happy = "rv_happy.png"
image rivchar rv_sad = "rv_sad.png"
image rivchar rv_smiling = "rv_smiling.png"
image rivchar rv_smirking = "rv_smirking.png"

image cfimg cf = "cf.png"
image cfimg cf_disappointed = "cf_disappointed.png"
image cfimg cf_happy = "cf_happy.png"
image cfimg cf_sad = "cf_sad.png"
image cfimg cf_serious = "cf_serious.png"
image cfimg cf_shocked = "cf_shocked.png"

init python:
    import random
    #import numpy as np
    #from sklearn.linear_model import LinearRegression
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

    interest = [random.randrange(-3, 5, 1), #Confidence
                random.randrange(0, 5, 1), #Empathy
                random.randrange(-3, 5, 1), #Responsibility
                random.randrange(-4, 5, 1), #Romantic
                random.randrange(-3, 4, 1), #Caring
                random.randrange(-5, 5, 1), #Humor
                random.randrange(-2, 3, 1), #Intelligence
                random.randrange(-3, 4, 1), #Cool
                random.randrange(-5, 5, 1),
                random.randrange(-5, 5, 1)]

    LoveInterest = LoveInterest(interest)

    '''
    class Rival:
        def __init__(self):
            self.sceneResults = list()
            self.iteration = 1 # For special case perfect squares


            #Rival needs to start _somewhere_. So let's set it up like
            #the love interest and pair it up with a random responseValue

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

            responseValue = random.randrange(-5, 5, 1)
            initSceneResult = (initChoice, responseValue)

            self.appendSceneResult(initSceneResult)

        def appendSceneResult(self, sceneResult):
            if not isinstance(sceneResult, tuple):
                raise ValueError("Scene Result must be a tuple (prediction, chosen dialogue)")


            #Extrapolate variables "x_i" of the (responseValue = a_1*x_1 + ... a_r*x_r)
            #linear combination given the constraints that bound the interest values: -5 <= i <= 5.

            coefficients = np.array([sceneResult[0]])
            responseValue = np.array([sceneResult[1]])

            # Dimensions must be square, so add 0-valued dimensions
            newDims = np.zeros((coefficients.shape[1]-1,coefficients.shape[1]))
            expCoefficients = np.concatenate((coefficients, newDims))
            newDims = np.zeros((1,coefficients.shape[1]-1))
            expResponseValues = np.append(responseValue, newDims)

            # Dirty the coefficient data to avoid singular matrix exception (it can't be a perfect fit)
            dirtyCoefficients = expCoefficients+0.00001*np.random.rand(coefficients.shape[1], coefficients.shape[1])

            x = np.linalg.solve(dirtyCoefficients, expResponseValues)

            self.sceneResults.append((dirtyCoefficients, x))

        def isPerfect(self, val):
            if (sqrt(val) - floor(sqrt(val)) != 0):
                return False
            return True

        def getPerfectSquare(self, val):

            #Returns the closest perfect square and the steps it took to
            #get there.

            if Rival.isPerfect(val):
                return val, 0

            n1 = val + 1
            while True:
                if self.isPerfect(n1):
                    steps = n1 - val
                    return n1, steps
                else:
                    n1 += 1

        def findBestFit(self, dialogueOptions):

            #Will attempt to find the best response using the most recent responseValues
            #of the Love Interest, and previous sceneResults data.

            #dialogueOptions - List of the values associated with available dialogue options



            #Multivariate linear regression.

            #This reconstructs the best fit each call to findBestFit().

            #Data organization: [([dialogueVal, ...], responseVal), ...]

            dialogueValues = [i[0] for i in self.sceneResults]
            responseValues  = [j[1] for j in self.sceneResults]
            if len(dialogueValues) != len(responseValues):
                raise ValueError("Data in dialogueValues and responseValues not the same size")

            npDiagVals, npRespVals = np.array(dialogueValues, dtype=object), np.array(responseValues, dtype=object)


            #This is silly, but either the shape of the data is a perfect square or we need
            #to add enough zero columns such that it can be a perfect square.

            diagSize = npDiagVals.shape[0] * npDiagVals.shape[1] * npDiagVals.shape[2]
            requiredSize, numDims = self.getPerfectSquare(diagSize)

            diagShape = 0
            respShape = 0
            if numDims == 0: # diagSize is already a perfect square (e.g. 100)
                diagShape = respShape = floor(sqrt(requiredSize))

                # Uhhmm.. Special case! Rival loses some data from prior responses on
                # perfect squares because the shaping is impossible to make work.
                # (e.g. (4,10) cannot shape (1,20)), (16,10) cannot shape to (1,40).A
                if requiredSize != 100:
                    numOfRemovedRows = -floor(sqrt(npRespVals.shape[0])) * self.iteration
                    npRespVals = npRespVals[:numOfRemovedRows:]
                    self.iteration += 1

            else:
                newDims = np.zeros(numDims)
                npDiagVals = np.concatenate((npDiagVals.flatten(), newDims))

                # We're going to lose some info here because I can't make, e.g., (2,10) shaped as (1,15)
                newSize = floor(sqrt(requiredSize))
                npRespVals = npRespVals.flatten()[:newSize]
                # npRespVals = np.concatenate((npRespVals.flatten(), newDims))

                diagShape = respShape = newSize
            breakpoint()
            x = np.squeeze(npDiagVals.reshape(1, diagShape, diagShape), axis=0)
            y = np.squeeze(npRespVals.reshape(1, respShape), axis=0)


            #Rival AI learns from the previous choices and makes a prediction.


            model = LinearRegression().fit(x, y)

            prediction = model.predict(x)


            #Choose the option that is closest in pairwise value to the Rival's predictions.

            #Note that order matters here, so the list comprehension accounts for that.

            bestOption = []
            prevDiffs = []
            for option in dialogueOptions:
                diffs = [abs(i - j) for i, j in zip(prediction, option)]
                if len(bestOption) == 0: # First iteration bestOption is empty
                    bestOption = [i for i in option]
                    prevDiffs = [j for j in diffs]
                else:

                    #Change bestOption if current diffs are greater pairwise than prevDiffs.

                    #If there are a majority of greater values in `prevDiffs`, keep current
                    #bestOption as it is "greater", and hence closer to the best option.

                    comparison = zip(diffs, prevDiffs)
                    total, other = 0, 0
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
            self.appendSceneResult((prediction[:10], LoveInterest.getResponse(bestOption)))
            return bestOption
    '''

    class Rivals(object):
        def __init__(self, interests):
            self.li_interests = interests

        def appendSceneResult(self, choice, response):
            count = 0
            while count < 10:
                self.li_interests[count] = self.li_interests[count] + (choice[count] * response)
                count += 1


        def findBestFit(self, dialogueOptions):
            optionsCount = 0
            count = 0
            bestResult = -100000
            bestResultIndex = -10
            currentResult = -1

            while optionsCount < len(dialogueOptions):
                currentResult = 0
                dialogue = dialogueOptions[optionsCount]
                while count < 10:
                    currentResult = currentResult + (self.li_interests[count] * dialogue[count])
                    count += 1
                if(currentResult >= bestResult):
                    bestResult = currentResult
                    bestResultIndex = optionsCount
                optionsCount += 1

            self.appendSceneResult(dialogueOptions[bestResultIndex], LoveInterest.getResponse(dialogueOptions[bestResultIndex]))

            return (bestResultIndex + 1)



    rival = Rivals([0,0,0,0,0,0,0,0,0,0])
    #rival = Rival()

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    $ pg_state = [0,0,0,0,0,0,0,0,0,0]
    $ rv_state = [0,0,0,0,0,0,0,0,0,0]

    #"This Love Interest has multipliers [interest]"

    # Prompt the player to enter a name
    $player_character = renpy.input("Type in a name.")
    $player_character = player_character.strip()
    # Or result to default name
    if player_character == "":
        $player_character = "Bobby Joe"

    define pg = Character(_("[player_character]"))

    jump scene1
label after1: #show this scene in demo
    #jump scene2
label after2:
    #jump scene3
label after3:
    #jump scene4
label after4:
    #jump scene5
label after5:
    #jump scene6
label after6:
    #jump scene7
label after7:
    #jump scene8
label after8:
    #jump scene9
label after9:
    jump scene10
label after10: #show this scene in demo
    "li interest is [interest]"
    "pg_state is [pg_state]"
    "rv_state is [rv_state]"



    # This ends the game.

    return
