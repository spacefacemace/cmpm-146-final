# variables to add:
# stuff for ai
# points for li->pg, li->rv, rv->pg

# rn the answers to the player's options is
# set to the ideal answer (mostly for rv ai) + its weight
# probably take them out and put them in a set
# and make ai choose the best from there


label scene9:

    image bens_house = Frame("studentlounge.jpg")
    image out_bens_house = Frame("out_bens_house.jpg")

    scene bens_house

    show cfimg cf at right
    show roommate rm at left

    rm "This is...an odd venue, but I’ll take it. His vinyl collection is insane."

    cf "...Did you go through it?"

    show roommate rm_suspicious at left
    rm "What? Of course not. I have manners."

    cf "Why are you here again?"

    rm "Because [li] invited me?"

    hide roommate rm_suspicious
    hide cfimg cf
    show luvint li_tired
    show rivchar rv at right

    li "It’d be a shame if he was left in your apartment all by himself!"

    li "Besides, this sort of thing...it’s a last for most of us before graduating."

    rv "It really is about to end, huh?"

    rv "On one hand, thank god. On the other hand..."

    show luvint li_joy

    menu:

        # best option, points for li->pg
        "It’s a bit bittersweet.":
            $ pg_state[6] += 3
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,0,0,3,0,0,0]))
            "{i}[response]{/i}"
            li "I totally get it! You go through all this and then..."
            show rivchar rv_smiling at right
            rv "Just like that, it’s about to end." # (1-2 pts li->rv)
            li "Yep, exactly."


        "I’m glad it’s over.":
            $ pg_state[6] -= 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,0,0,-1,0,0,0]))
            "{i}[response]{/i}"
            $ rv_response = rival.findBestFit([[0,1,0,0,0,0,2,0,0,0],[0,1,0,3,0,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[6] += 2
                $ rv_state[1] += 1
                li "I totally get it! You go through all this and then..."
                show rivchar rv_smiling at right
                rv "Just like that, it’s about to end."
                li "Yep, exactly."

            elif(rv_response == 2):
                $ rv_state[1] += 1
                $ rv_state[3] += 3
                rv "Well if we're blanking..."
                rv "Wait, I got it."
                rv "It’s bittersweet, kind of."
                show rivchar rv_embarassed at right
                rv "...Geez, that was cheesy. Don’t tell anyone I said that."
                li "Haha, I won’t tell."


        "I’m not sure what to think.":
            $ rv_response = rival.findBestFit([[0,1,0,0,0,0,2,0,0,0],[0,1,0,3,0,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[6] += 2
                $ rv_state[1] += 1
                li "I totally get it! You go through all this and then..."
                show rivchar rv_smiling at right
                rv "Just like that, it’s about to end."
                li "Yep, exactly."

            elif(rv_response == 2):
                $ rv_state[1] += 1
                $ rv_state[3] += 3
                rv "Well if we're blanking..."
                rv "Wait, I got it."
                rv "It’s bittersweet, kind of."
                show rivchar rv_embarassed at right
                rv "...Geez, that was cheesy. Don’t tell anyone I said that."
                li "Haha, I won’t tell."

    show rivchar rv at right
    show luvint li_serious
    li "...I was going to say some more stuff, but I should probably save that spiel for later, huh?"

    menu:

        "Is it a lot?":
            $ pg_state[4] -= 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,-2,0,0,0,0,0]))
            "{i}[response]{/i}"
            $ rv_response = rival.findBestFit([[0,0,0,2,0,-1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[5] -= 1
                $ rv_state[3] += 3
                rv "Haha, very funny, [pg]...I think."
                pg "Yep, sarcasm."
                rv "Well, no matter how much, I’ll listen to it. You can count on that."

            elif(rv_response == 2):
                $ rv_state[3] += 1
                rv "Well, no matter how much, I’ll listen to it. You can count on that."

        # best option, points for li->pg
        "I’m looking forward to it.":
            $ pg_state[4] += 3
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,3,0,0,0,0,0]))
            "{i}[response]{/i}"
            $ rv_response = rival.findBestFit([[0,0,0,2,0,0,0,0,0,0],[0,0,0,0,2,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[3] += 2
                rv "Me too. No matter how much you’ll say, I’ll listen to it. You can count on that."

            elif(rv_response == 2):
                $ rv_state[4] += 2
                rv "Don't worry, we'll listen."

        # 1-2 points for li->pg
        "Wonder what it could be...":
            $ pg_state[5] += 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,0,2,0,0,0,0]))
            "{i}[response]{/i}"
            $ rv_response = rival.findBestFit([[0,0,0,0,2,0,0,0,0,0],[0,0,0,2,0,1,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[4] += 2
                rv "Don't worry, we'll listen."

            elif(rv_response == 2):
                $ rv_state[5] += 1
                $ rv_state[3] += 2
                rv "Hmm, I wonder, too."
                pg "Hmm."
                rv "Hmm."
                rv "Well, we'll listen. Don't worry."

    show luvint li_happy
    li "Oh, an audience? Then I’ll make sure it’s good."

    # (then fade to like later that night, li rv and pg are outside)
    scene out_bens_house
    show rivchar rv at right
    show luvint li_joy

    rv "I should get going. I want to wake up early tomorrow to go to the gym."

    li "Haha, always working hard on that, huh, [rv]? Well, we won’t keep you then."

    rv "Thanks. See you...well, we’re neighbors, so see you whenever."

    hide rivchar rv easeoutright

    li "...And then there were two."

    li "At least right here where we are. I think [cf] and [rm] went to go check out the vinyls again."

    li "I know I talk about just how eventful this year was...so I want to ask you this, [pg] -- what’d you think of this year?"

    menu:

        "It was a lot.":
            li "There’s a thought I always have, though...the thought of time moving forward."

        # best option, points for li->pg
        "You made it bearable.":
            $ pg_state[3] += 3
            $ pg_state[7] += 3
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,3,0,0,0,3,0,0]))
            "{i}[response]{/i}"
            show luvint li_blush
            li "Me...?"
            show luvint li_happyblush
            li "That’s the first time someone’s said that to me."
            li "Well then...I’m honored!"
            li "There’s a thought I always have, though...the thought of time moving forward."

        # 1-2 points for li->pg
        "I’m ready for what’s next.":
            $ pg_state[0] += 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([1,0,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            show luvint li_happy
            li "Me too! A new chapter in life is always exciting."
            li "There’s a thought I always have, though...the thought of time moving forward."

    show luvint li_joy
    li "There’s a lot to get in order when moving on."

    li "At this point, it’s the type where we have to get our life together."

    show luvint li_tired
    li "Though I’m sure [rv] has something figured out. He always does. He mentioned working at his dad’s business? That must be fun."

    menu:

        # subtract points for li->pg(?)
        "It’s only because his dad is the CEO.":
            $ pg_state[4] -= 3
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,-3,0,0,0,0,0]))
            "{i}[response]{/i}"
            li "Ah, what am I thinking? We’re just in our 20’s. In the end, there’s no rush."

        # 1-2 points for li->rv
        "He sure has his life figured out.":
            $ pg_state[0] -= 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([-1,0,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            li "Ah, what am I thinking? We’re just in our 20’s. In the end, there’s no rush."

        # 1-2 pts for li->rv but 3-4 for li->pg
        "He just has a head start, we still have time.":
            $ pg_state[1] += 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,2,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            li "Ah, what am I thinking? We’re just in our 20’s. In the end, there’s no rush."

    show luvint li_joy
    li "I’m sure we’ll be fine."

    menu:

        # best options, pts for li->pg
        "Yep, we will be.":
            $ pg_state[1] += 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,1,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            li "...What a mood we’re in. Let’s change that."

        # 1 pt for li->pg
        "I hope so.":
            li "...What a mood we’re in. Let’s change that."

        # 2 pts for li->pg
        "That’s the plan.":
            $ pg_state[0] += 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([1,0,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            li "...What a mood we’re in. Let’s change that."

    li "I’m going to check on the others. What about you?"

    "I’ll stay here for now."

    li "Alright! Feel free to come back inside whenever."

    hide luvint li_joy at easeoutleft

    "{i}In about a week, we’ll be graduating, one by one.{/i}"

    "{i}...Some system the university’s got.{/i}"

    "{i}But still, we’ll no longer be students here. That’s crazy to think about.{/i}"

    "{i}And yet [li] is just still a friend to both [rv] and me...{/i}"

    "{i}As close as we are, that’s all we are.{/i}"

    "{i}Is graduation the time to say something?{/i}"

    "{i}Will [rv] say something by then?{/i}"

    "{i}Will I?{/i}"

    "{i}As scary as it is, the only way to find out is to let time move forward.{/i}"

    "{i}I just hope I don’t end up regretting it.{/i}"

    jump after9
