# variables to add:
# stuff for ai
# points for li->pg, li->rv, rv->pg

# rn the answers to the player's options is
# set to the ideal answer (mostly for rv ai) + its weight
# probably take them out and put them in a set
# and make ai choose the best from there

label scene7:

    image second_stage = Frame("second_stage.jpg")

    scene second_stage

    show rivchar rv

    "{i}Tomorrow is the show.{/i}"

    "{i}Everyone’s worked hard up until now, making sure that everything goes above and beyond, spendings hours upon hours perfecting their performances...you know how it goes.{/i}"

    "{i}And tomorrow, they’ll see the results of all their efforts.{/i}"

    rv "Alright, the last group’s music is queued."

    rv "...This is exhausting."


    menu:

        "You’re an athlete, though?":
            # points for rv->pg
            rv "Well, yeah, but..."
            rv "If you’re doing something new, of course it’ll be kind of tiring. No harm in that."
            rv "...On second thought, I’m not that tired, really. I could do this for two more hours if I had to!"
            rv "Wow, you’re something, [pg]. I’ll give you that."
            rv "It’s a different kind of work back here. I guess I’ve found some appreciation for the people that do this."


        "You got tired doing this sort of thing?":
            # points for rv->pg
            rv "Well, yeah, but..."
            rv "If you’re doing something new, of course it’ll be kind of tiring. No harm in that."
            rv "...On second thought, I’m not that tired, really. I could do this for two more hours if I had to!"
            rv "Wow, you’re something, [pg]. I’ll give you that."
            rv "It’s a different kind of work back here. I guess I’ve found some appreciation for the people that do this."


        "I kinda am, too.":
            rv "It’s a different kind of work back here. I guess I’ve found some appreciation for the people that do this."

    rv "...Where are they? [pg], when do they get on?"

    pg "In about two minutes."

    rv "Seriously...should I just go find them myself?"

    menu:

        # 1-2 points for rv->pg, some points for li->pg
        "I don’t think that’s a good idea...":
            $ pg_state[2] += 1

            $ rv_response = rival.findBestFit([[0,0,0,0,2,0,0,-2,0,0],[0,0,-2,0,0,0,0,2,0,0]])
            if(rv_response == 1):
                $ rv_state[7] -= 2
                $ rv_state[4] += 2
                show rivchar rv_crying
                rv "Ugh, you're right."

            elif(rv_response == 2):
                $ rv_state[7] -= 2
                $ rv_state[3] += 2
                rv "Even if this is a rehearsal, I want this to go well, but..."
                show rivchar rv_crying
                rv "Ugh, you're right."

        # 2-3 points for rv->pg, some points for li->pg
        "You shouldn’t leave your post, you need to be here when they do come.":
            $ pg_state[2] += 3


            $ rv_response = rival.findBestFit([[0,0,0,0,2,0,0,-2,0,0],[0,0,-2,0,0,0,0,2,0,0]])
            if(rv_response == 1):
                $ rv_state[7] -= 2
                $ rv_state[4] += 2
                show rivchar rv_crying
                rv "Ugh, you're right."

            elif(rv_response == 2):
                $ rv_state[7] -= 2
                $ rv_state[2] += 2
                rv "Even if this is a rehearsal, I want this to go well, but..."
                show rivchar rv_crying
                rv "Ugh, you're right."

        # best option, points for li->pg
        "You need to be here.":
            $ pg_state[2] += 2


            $ rv_response = rival.findBestFit([[0,0,0,0,2,0,0,-2,0,0],[0,0,-2,0,0,0,0,2,0,0]])
            if(rv_response == 1):
                $ rv_state[7] -= 2
                $ rv_state[4] += 2
                show rivchar rv_crying
                rv "Ugh, you're right."

            elif(rv_response == 2):
                $ rv_state[7] -= 2
                $ rv_state[2] += 2
                rv "Even if this is a rehearsal, I want this to go well, but..."
                show rivchar rv_crying
                rv "Ugh, you're right."

    rv "Or do you just not want me to leave?"

    menu:

        "That’s kind of...":
            show rivchar rv
            rv "I'm kidding."


        "I don’t know...":
            show rivchar rv
            rv "I'm kidding."

        # some points for rv->pg
        "What makes you say that...":
            show rivchar rv
            rv "I'm kidding."

    rv "Oh, here they come."

    rv "You’re all late, you know."

    rv "You were supposed to be here...three minutes ago."

    show rivchar rv_angry
    rv "If this was the real thing, there could be some serious delay."

    menu:

        "I think they get it, [rv].":

            $ rv_response = rival.findBestFit([[0,0,0,0,-2,0,0,2,0,0],[0,0,2,0,-2,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[7] -= 2
                $ rv_state[4] += 2
                show rivchar rv_sad
                rv "i guess I was a little harsh. Sorry about that."

            elif(rv_response == 2):
                $ rv_state[4] += 2
                $ rv_state[2] -= 2
                show rivchar rv_sad
                rv "...Right, right."
                rv "I guess I was a little harsh. Sorry about that."

        # points for li->pg
        "It’s fine, what matters is that they’re here.":
            $ pg_state[1] += 2
            # 1-2 points for li->rv

            $ rv_response = rival.findBestFit([[0,0,0,0,-2,0,0,2,0,0],[0,0,2,0,-2,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[7] -= 2
                $ rv_state[4] += 2
                show rivchar rv_sad
                rv "i guess I was a little harsh. Sorry about that."

            elif(rv_response == 2):
                $ rv_state[4] += 2
                $ rv_state[2] -= 2
                show rivchar rv_sad
                rv "...Right, right."
                rv "I guess I was a little harsh. Sorry about that."


        # points for li->pg
        "You don’t need to be so harsh.":
            $ pg_state[1] += 3

            $ rv_response = rival.findBestFit([[0,0,2,0,-2,0,0,0,0,0],[0,0,0,0,-3,0,0,2,0,0]])
            if(rv_response == 1):
                $ rv_state[4] -= 2
                $ rv_state[2] += 2
                show rivchar rv_sad
                rv "...Right, right."
                rv "I guess I was a little harsh. Sorry about that."

            elif(rv_response == 2):
                $ rv_state[4] -= 3
                $ rv_state[7] += 2
                rv "I’m not trying to be?"
                show rivchar rv_sad
                rv "...Does it seem that way?"
                rv "If it does, sorry."


    show rivchar rv
    pg "You guys are good to go in...3, 2, 1."

    rv "...And that’s the end of our jobs. At least for this rehearsal."

    rv "You know about the after-party, right?"

    menu:

        # 1-2 points for li->rv
        "After-party?":
            rv "Yeah...[li] said something about it a few days ago."

        # subtract 1-2 points from li->pg
        "Kind of...?":
            $ pg_state[2] -= 2

            $ rv_response = rival.findBestFit([[0,0,0,0,3,0,0,0,0,0],[0,0,1,0,2,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[4] += 3
                rv "Yeah...[li] said something about it a few days ago."

            elif(rv_response == 2):
                $ rv_state[2] += 1
                $ rv_state[4] += 2
                show rivchar rv_angry
                rv "Come on, at least pay a little attention."
                rv "[li] said something about it a few days ago."
                show rivchar rv

        # 2-3 points for li->rv
        "Did I miss something?":
            $ pg_state[2] -= 2


            $ rv_response = rival.findBestFit([[0,0,0,0,3,0,0,0,0,0],[0,0,1,0,2,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[4] += 3
                rv "Yeah...[li] said something about it a few days ago."

            elif(rv_response == 2):
                $ rv_state[2] += 1
                $ rv_state[4] += 2
                show rivchar rv_angry
                rv "Come on, at least pay a little attention."
                rv "[li] said something about it a few days ago."
                show rivchar rv

    rv "It’s going to be at...Ben Carson’s house?"

    rv "This dance group is one of his...interests? He’s an unofficial advisor?"

    menu:

        # 1-2 points for li->pg
        "Right, I think [li] told me about that.":
            $ pg_state[2] += 1
            rv "Anyway, he offered his house for...you know, the after-party."

        "Right...":
            rv "Anyway, he offered his house for...you know, the after-party."

        # points for rv->pg
        "If you say so...":
            rv "Anyway, he offered his house for...you know, the after-party."

    hide rivchar rv
    show luvint li_joy at right

    li "Good job everyone! You all did amazing!"

    li "The show looks great. I’m sure you’re all excited to show it off!"

    li "Alright, I won’t keep you guys long. Go home, get some rest, do whatever you need to do. See you tomorrow! Don’t forget -- you have to be here at 5PM!"

    show rivchar rv

    li "You guys have definitely got this down! You might be better than me when I had to do this, hahaha..."

    show luvint li_happy2 at right
    li "Doing what you did just now, we’ll definitely have a successful show tomorrow!"
    show luvint li_joy at right

    menu:

        # best option, points for li->pg
        "Then we’ll make sure to do our best.":
            $ pg_state[2] += 2
            $ pg_state[4] += 2
            $ pg_state[7] += 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,2,0,2,0,0,2,0,0]))
            "{i}[response]{/i}"
            # 1-2 points for li->rv

            $ rv_response = rival.findBestFit([[2,0,0,0,0,0,0,2,0,0],[3,0,0,0,0,0,0,1,0,0]])
            if(rv_response == 1):
                $ rv_state[7] += 2
                $ rv_state[0] += 2
                rv "Exactly. Though it wouldn’t hurt if we did better tomorrow."
                show rivchar rv_happy
                rv "Shoot for the moon, and if you fail, at least you’ll land among the stars -- that sort of thing."

            elif(rv_response == 2):
                $ rv_state[7] += 1
                $ rv_state[0] += 3
                rv "Oh, we’ll make sure it’ll be the best show it could possibly be. Though it wouldn’t hurt if we did better tomorrow."
                show rivchar rv_happy
                rv "Shoot for the moon, and if you fail, at least you’ll land among the stars -- that sort of thing."

        "Hopefully that’s the case.":
            # points for li->rv
            $ pg_state[4] += 1
            $ pg_state[2] += 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,1,0,1,0,0,0,0,0]))
            "{i}[response]{/i}"

            $ rv_response = rival.findBestFit([[3,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,2,0,0,0]])
            if(rv_response == 1):
                $ rv_state[7] += 1
                $ rv_state[0] += 3
                rv "Oh, we’ll make sure it’ll be the best show it could possibly be. Though it wouldn’t hurt if we did better tomorrow."
                show rivchar rv_happy
                rv "Shoot for the moon, and if you fail, at least you’ll land among the stars -- that sort of thing."

            elif(rv_response == 2):
                $ rv_state[6] += 2
                $ rv_state[0] += 1
                show rivchar rv_happy
                rv "Well, let's shoot for the moon, and if we fail, at least we’ll land among the stars."

        # 1-2 points for rv->pg
        "We’ll try.":
            # points for li->rv
            rv "Oh, we’ll make sure it’ll be the best show it could possibly be. Though it wouldn’t hurt if we did better tomorrow."
            rv "Shoot for the moon, and if you fail, at least you’ll land among the stars -- that sort of thing."

            $ rv_response = rival.findBestFit([[3,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,2,0,0,0]])
            if(rv_response == 1):
                $ rv_state[7] += 1
                $ rv_state[0] += 3
                rv "Oh, we’ll make sure it’ll be the best show it could possibly be. Though it wouldn’t hurt if we did better tomorrow."
                show rivchar rv_happy
                rv "Shoot for the moon, and if you fail, at least you’ll land among the stars -- that sort of thing."

            elif(rv_response == 2):
                $ rv_state[6] += 2
                $ rv_state[0] += 1
                show rivchar rv_happy
                rv "Well, let's shoot for the moon, and if we fail, at least we’ll land among the stars."

    show luvint li_happy2 at right

    li "Right!"

    li "Well, I’ll let you two go, too! Thanks for your hard work."

    jump after7
