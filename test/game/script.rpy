# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define e = Character("Eileen")

init python:

    class Rival(object):
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
                    currentResult = currentResult + (self.li.interests[count] * dialogue[count])
                    count += 1
                if(currentResult >= bestResult):
                    bestResult = currentResult
                    bestResultIndex = optionsCount
                optionsCount += 1

            appendSceneResult(dialogueOptions[bestResultIndex], LoveInterest.getResponse(dialogueOptions[bestResultIndex]))

            return (bestResultIndex + 1)





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

    # This ends the game.

    return
