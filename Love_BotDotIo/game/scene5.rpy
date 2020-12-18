# variables to add:
# points for li->pg, li->rv, rv->pg

# rn the answers to the player's options is
# set to the ideal answer (mostly for rv ai) + its weight
# probably take them out and put them in a set
# and make ai choose the best from there

label scene5:

    image second_stage = Frame("second_stage.jpg")

    scene second_stage

    show cfimg cf at right
    show luvint li_joy at left
    show rivchar rv

    li "Here’s where we’ll be having our show! It’s enough space for us and we’ve already done some stuff here in the past, so we’re pretty well acquainted with that stage!"

    show cfimg cf_disappointed at right
    cf "Ahh, I remember performing here freshman year like it was just yesterday..."

    pg "Didn’t your group get delayed five minutes because you got so nervous you had to go to the bathroom?"

    rv "Hey, some people just get those nervous bowel movements."

    show cfimg cf at right
    cf "Alright...I’m a changed person now. That won’t happen again -- hopefully."

    li "I remember that, too...well, [rv], [pg], what do you think? You’ll be okay?"

    menu:

        # best option, points for li->pg
        "Of course.":
            $ pg_state[0] += 2
            $ pg_state[2] += 2
            $ pg_state[7] += 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([2,0,2,0,0,0,0,2,0,0]))
            "{i}[response]{/i}"
            # maybe some points for li->rv

            $ rv_response = rival.findBestFit([[3,0,0,0,0,0,0,1,0,0],[2,0,0,0,0,0,0,3,0,0]])
            if(rv_response == 1):
                $ rv_state[0] += 3
                $ rv_state[7] += 1
                show rivchar rv_smiling
                rv "Yup. I’m not the type to back down from a challenge."

            elif(rv_response == 2):
                $ rv_state[0] += 2
                $ rv_state[7] += 3
                show rivchar rv_smirking
                rv "And I agree with [pg]. I’m not the type to back down from a challenge."


        "It could take some getting used to...":
            # best option for rv, points for li->rv
            $ pg_state[7] -= 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,0,0,0,-2,0,0]))
            "{i}[response]{/i}"

            $ rv_response = rival.findBestFit([[2,0,0,0,-2,0,0,0,0,0],[2,0,0,0,3,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[0] += 2
                $ rv_state[4] -= 2
                show rivchar rv_smiling
                rv "I’ll be fine, 100% -- I’m not the type to back down from a challenge."

            elif(rv_response == 2):
                $ rv_state[0] += 2
                $ rv_state[4] += 3
                show rivchar rv_smiling
                rv "Hey, I'm here for support, [pg]."
                rv "Besides, I’m not the type to back down from a challenge."


        "Maybe?":
            # best option for rv, points for li->rv
            $ pg_state[0] -= 3
            $ pg_state[2] -= 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([-3,0,-2,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            $ rv_state[0] += 2
            show rivchar rv_smiling
            rv "I’ll be fine, 100%% -- I’m not the type to back down from a challenge."

    rv "I’ve got a high level of tolerance with all the sports I’ve played, believe me."
    show rivchar rv_happy
    # some points for li->rv for this one
    rv "Don’t worry, [li] -- with me around, this show will be like a well-oiled machine!"

    menu:

        # best option, points for li->pg
        "Don’t count me out, [rv]. I’ll do my best to help, too.":
            $ pg_state[0] += 3
            $ pg_state[4] += 1
            $ pg_state[7] += 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([3,0,0,0,1,0,0,2,0,0]))
            "{i}[response]{/i}"
            # some points for li->rv

            $ rv_response = rival.findBestFit([[0,0,0,0,-2,0,0,1,0,0],[0,0,0,0,2,0,0,1,0,0]])
            if(rv_response == 1):
                $ rv_state[4] -= 2
                $ rv_state[7] += 2
                show rivchar rv
                rv "...Well I guess I might have left you out there for a bit. Sorry."
                rv "I don’t doubt that you can put in the work."

            elif(rv_response == 2):
                $ rv_state[4] += 2
                $ rv_state[7] += 1
                show rivchar rv
                rv "Didn't mean to leave you out. I don't doubt that you can put in the work."
                rv "I like the confidence, though."


        "I’m here too, [rv].":

            $ rv_response = rival.findBestFit([[0,0,0,0,-2,0,0,1,0,0],[0,0,0,0,2,0,0,1,0,0]])
            if(rv_response == 1):
                $ rv_state[4] -= 2
                $ rv_state[7] += 2
                show rivchar rv
                rv "...Well I guess I might have left you out there for a bit. Sorry."
                rv "I don’t doubt that you can put in the work."

            elif(rv_response == 2):
                $ rv_state[4] += 2
                $ rv_state[7] += 1
                show rivchar rv
                rv "Didn't mean to leave you out. I don't doubt that you can put in the work."
                rv "I like the confidence, though."


        "It looks like [rv]’s got this whole show covered...":
            # maybe lower li->rv points for this one?
            $ pg_state[0] -= 3
            $ pg_state[7] -= 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([3,0,0,0,0,0,0,-2,0,0]))
            "{i}[response]{/i}"

            $ rv_state[0] += 3
            show rivchar rv_crying
            rv "...Are backing out of this?"
            rv "No, you just made it seem like you got it, you know. I’m here too."
            rv "...Well I guess I might have left you out there for a bit. Sorry."
            show rivchar rv
            rv "I don’t doubt that you can put in the work."

    li "The good news is that you don’t have to be in view of the audience -- if that worried you, at least."

    li "And also, there’s people to do all the lights and technical stage stuff, so that won’t be a problem, either! Perks of renting this space out."

    li "That really only leaves making sure everyone’s in their place, getting this in order, that sort of thing. Managing the show."

    li "Of course I’d do it, but..."

    show luvint li_happy2 at left
    li "Fortunately, you guys are here!"

    li "It’s mostly making sure the music is queued up and that people are ready to go on their cue, as well as making sure people are getting on quickly enough for the next performance."

    show luvint li_joy at left
    li "I think there’s about...20 performances in total?"

    li "Not too bad, right?"

    menu:

        # best option, points for li->pg
        "Not at all.":
            $ pg_state[2] += 2
            $ pg_state[7] += 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,2,0,0,0,0,2,0,0]))
            "{i}[response]{/i}"
            # some points for li->rv

            $ rv_response = rival.findBestFit([[2,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[0] += 2
                $ rv_state[7] += 1
                rv "We’d help if it were 100, right, [pg]?"

            elif(rv_response == 2):
                $ rv_state[0] += 1
                rv "I agree, it's not bad."


        "20 is...":
            # best option for rv, points for li->rv

            $ rv_response = rival.findBestFit([[3,0,0,0,0,0,0,2,0,0],[0,0,0,0,3,0,0,2,0,0]])
            if(rv_response == 1):
                $ rv_state[0] += 3
                $ rv_state[7] += 2
                rv "We’d help if it were 100, right, [pg]?"

            elif(rv_response == 2):
                $ rv_state[4] += 3
                $ rv_state[7] += 2
                rv "Don't be so down on yourself, [pg]. We can do it."


        "It’s a lot.":
            # best option for rv, points for li->rv
            $ pg_state[2] -= 2
            $ pg_state[7] -= 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,-2,0,0,0,0,-2,0,0]))
            "{i}[response]{/i}"

            $ rv_response = rival.findBestFit([[3,0,0,0,0,0,0,2,0,0],[0,0,0,0,3,0,0,2,0,0]])
            if(rv_response == 1):
                $ rv_state[0] += 3
                $ rv_state[7] += 2
                rv "We’d help if it were 100, right, [pg]?"

            elif(rv_response == 2):
                $ rv_state[4] += 3
                $ rv_state[7] += 2
                rv "Don't be so down on yourself, [pg]. We can do it."

    cf "We’ll make sure the group listens to you guys, too. They can get...rowdy, but I’m sure you two can handle it."

    li "And of course, we won’t just throw you into the job! We’ll be doing rehearsals, easing you into the flow of the show."

    li "[pg], [rv]...thank you for helping. I really, really, really mean it."

    show luvint li_happy2 at left
    li "It’s making me so much more excited for the show knowing some of my friends are helping out!"

    "{i}...Friends. Right.{/i}"

    "{i}And judging from [rv]’s face, the word stings for him, too.{/i}"

    "{i}We’ll change it somehow.{/i}"

    jump after5
