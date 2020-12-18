# variables to add:
# chess_win = False
# best_move = 0
# stuff for ai
# points for li->pg, li->rv, rv->pg

# rn the answers to the player's options is
# set to the ideal answer (mostly for rv ai) + its weight
# probably take them out and put them in a set
# and make ai choose the best from there

label scene4:

    image pg_cf_rm_apartment = Frame("pg_cf_rm_apartment.jpg")

    # the stuff for the chess stuff in this scene.
    $ chess_win = False
    $ best_move = 0

    scene pg_cf_rm_apartment

    show cfimg cf at right
    show luvint li_joy at left
    show rivchar rv

    cf "Don’t mind all the mess."

    menu:

        # best option, points for li->pg
        "Yeah, we’re gonna clean all this stuff tomorrow.":
            $ pg_state[2] = pg_state[2] + 3
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,3,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"

            $ rv_response = rival.findBestFit([[0,-2,0,0,0,0,0,0,0,0],[0,2,-2,0,0,0,0,0,0,0],[0,-2,2,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,3,0,0]])
            if(rv_response == 1):
                $ rv_state[1] -= 2
                show rivchar rv_sad
                rv "...I sure hope so."

            elif(rv_response == 2):
                $ rv_state[1] += 2
                $ rv_state[2] -= 2
                rv "Well if it makes you feel better, my place kinda looks like this, too."

            elif(rv_response == 3):
                $ rv_state[1] -= 2
                $ rv_state[2] += 2
                show rivchar rv_angry
                rv "I'd never let my place get to this point."

            elif(rv_response == 4):
                $ rv_state[7] += 3
                rv "Maybe I could come over and help. We are sorta neighbors, after all."
                show rivchar rv_happy
                rv "Just not in the morning. I'm at the gym during that time."

        "Watch out for that pizza box.":
            $ pg_state[2] = pg_state[2] - 2
            $ pg_state[5] = pg_state[5] + 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,-2,0,0,2,0,0,0,0]))
            "{i}[response]{/i}"
            # best option for rv, points for li->rv

            $ rv_response = rival.findBestFit([[0,-2,2,0,0,0,0,0,0,0],[0,2,-2,0,0,0,0,0,0,0],[0,2,0,0,0,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[1] -= 2
                $ rv_state[2] += 2
                show rivchar rv_angry
                rv "Don’t you think you should clean your place up a little?"

            elif(rv_response == 2):
                $ rv_state[1] += 2
                $ rv_state[2] -= 2
                rv "Well if it makes you feel better, my place kinda looks like this, too."
                rv "But don't you think you should clean up a bit?"

            elif(rv_response == 3):
                $ rv_state[1] += 2
                rv "Well...we've all been there with this sort of thing."
                rv "Don't you think you should clean up, though?"

            menu:

                # 1-2 points for li->pg
                "Yeah, we'll clean it.":
                        $ pg_state[2] += 1
                        $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,1,0,0,0,0,0,0,0]))
                        "{i}[response]{/i}"
                        cf "We have free time tomorrow, right, [pg]? We’ll get this sorted out."

                # lower points for li->pg
                "We’ll see about that.":
                        $ pg_state[2] -= 3
                        $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,-3,0,0,0,0,0,0,0]))
                        "{i}[response]{/i}"
                        cf "We have free time tomorrow, right, [pg]? We’ll get this sorted out."

        "(silence)":
            # best option for rv, points for li->rv


            $ rv_response = rival.findBestFit([[0,-2,2,0,0,0,0,0,0,0],[0,2,-2,0,0,0,0,0,0,0],[0,2,0,0,0,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[1] -= 2
                $ rv_state[2] += 2
                show rivchar rv_angry
                rv "Don’t you think you should clean your place up a little?"

            elif(rv_response == 2):
                $ rv_state[1] += 2
                $ rv_state[2] -= 2
                rv "Well if it makes you feel better, my place kinda looks like this, too."
                rv "But don't you think you should clean up a bit?"

            elif(rv_response == 3):
                $ rv_state[1] += 2
                rv "Well...we've all been there with this sort of thing."
                rv "Don't you think you should clean up, though?"

            menu:

                # 1-2 points for li->pg
                "Yeah, we'll clean it.":
                        $ pg_state[2] += 1
                        $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,1,0,0,0,0,0,0,0]))
                        "{i}[response]{/i}"
                        cf "We have free time tomorrow, right, [pg]? We’ll get this sorted out."

                # lower points for li->pg
                "We’ll see about that.":
                        $ pg_state[2] -= 3
                        $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,-3,0,0,0,0,0,0,0]))
                        "{i}[response]{/i}"
                        cf "We have free time tomorrow, right, [pg]? We’ll get this sorted out."

    show rivchar rv
    cf "While we’re at it, let’s get [rm] in it, too."

    li "Yeah, where is he?"

    menu:

        # best option, points for li->pg
        "He’s playing Minecraft. I can go get him.":
            $ pg_state[4] += 3
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,3,0,0,0,0,0]))
            "{i}[response]{/i}"
            li "Can’t have him missing out!"


        "He’s probably playing Minecraft.":
            # best option for rv, points for li->rv


            $ rv_response = rival.findBestFit([[0,0,0,0,1,0,0,2,0,0],[0,0,0,0,2,0,0,2,0,0],[0,0,0,0,3,0,0,2,0,0]])
            if(rv_response == 1):
                $ rv_state[4] += 1
                $ rv_state[7] += 2
                rv "Why don’t you go get him, [pg]? See if he wants to hang out."

            elif(rv_response == 2):
                $ rv_state[4] += 2
                $ rv_state[7] += 2
                rv "You know him well, don't you?"
                rv "Why don’t you go get him, [pg]? See if he wants to hang out."

            elif(rv_response == 3):
                $ rv_state[4] += 3
                $ rv_state[7] += 2
                rv "Has he been at it all day?"
                pg "Yep, I don't think I've seen him at all."
                rv "Then why don’t you go get him, [pg]? See if he wants to hang out."


        "I dunno, his room?":
            # best option for rv, points for li->rv


            $ rv_response = rival.findBestFit([[0,0,0,0,1,0,0,2,0,0],[0,0,0,0,2,0,0,2,0,0],[0,0,0,0,3,0,0,2,0,0]])
            if(rv_response == 1):
                $ rv_state[4] += 1
                $ rv_state[7] += 2
                rv "Why don’t you go get him, [pg]? See if he wants to hang out."

            elif(rv_response == 2):
                $ rv_state[4] += 2
                $ rv_state[7] += 2
                rv "You know him well, don't you?"
                rv "Why don’t you go get him, [pg]? See if he wants to hang out."

            elif(rv_response == 3):
                $ rv_state[4] += 3
                $ rv_state[7] += 2
                rv "Has he been at it all day?"
                pg "Yep, I don't think I've seen him at all."
                rv "Then why don’t you go get him, [pg]? See if he wants to hang out."

    hide cfimg cf
    show roommate rm at right

    rm "Woah, there’s certainly more people here."

    li "[rm], are you good with sushi? Because we have a lot."

    rm "Yeah, if you don’t mind sharing."

    li "Not at all!"

    "{i}I should probably...{/i}"

    menu:

        # best option, points for li->pg
        "Clear the table.":
            $ pg_state[2] += 3
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,3,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            pg "Should I clear the table?"
            li "That'd be great!"


        "Set up the food.":
            # 1-2 points for li->pg
            $ pg_state[2] += 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,1,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            pg "Should I set up the food?"
            # 1-2 points for li->rv


            $ rv_response = rival.findBestFit([[0,0,3,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,1,0,0],[0,0,2,0,0,5,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[2] += 3
                show rivchar rv_angry
                rv "Shouldn't we clear the table first?"

            elif(rv_response == 2):
                $ rv_state[2] += 2
                $ rv_state[7] += 1
                rv "We should probably clear the table first."

            elif(rv_response == 3):
                $ rv_state[2] += 2
                $ rv_state[5] += 1
                rv "Nice try. We should probably clear the table first."


        "Wait.":

            $ pg_state[2] -= 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,-2,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            # best option for rv, points for li->rv


            $ rv_response = rival.findBestFit([[0,0,3,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,1,0,0],[0,0,2,0,0,5,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[2] += 3
                rv "Shouldn't we clear the table first?"

            elif(rv_response == 2):
                $ rv_state[2] += 2
                $ rv_state[7] += 1
                rv "We should probably clear the table first."

    show rivchar rv
    li "All set. Alright, let’s dig in!"

    # fade here?

    hide rivchar rv
    show cfimg cf_happy

    cf "Wow, that was exceptionally good."

    rm "It’s sushi, what did you expect?"

    pg "And all the soju [cf] drank."

    cf "I think we all had a bit."

    pg "But not as much as you."

    pg "[cf] usually doesn’t eat sushi, but I guess he couldn’t taste it considering he finished one and a half bottles of the cherry-flavored one?"

    show cfimg cf_disappointed
    cf "You know me too well, [pg]."

    show cfimg cf
    cf "What was that?"

    rm "Oh, it’s my chess set. I was wondering where that went."

    show cfimg cf_shocked
    cf "We had a chess set?"
    show cfimg cf

    menu:

        # best option, points for li->pg
        "[rm] mentioned it when we first moved in.":
            $ pg_state[4] += 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,2,0,0,0,0,0]))
            "{i}[response]{/i}"
            rm "Yes, we had a chess set. Though I don’t know how to play it {i}well{/i}."


        "I guess it was just hiding.":
            rm "Yes, we had a chess set. Though I don’t know how to play it {i}well{/i}."


        "I didn’t know that, either.":
            rm "Yes, we had a chess set. Though I don’t know how to play it {i}well{/i}."

    hide cfimg cf
    show rivchar rv

    rv "You’d be at some competition right now if you did."

    rm "...True."

    menu:

        "Do you know how to play, [rv]?":
            # 1-2 points for li->rv
            $ pg_state[6] = pg_state[6] + 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,0,0,2,0,0,0]))
            "{i}[response]{/i}"


            $ rv_response = rival.findBestFit([[2,0,0,0,0,0,2,0,0,0],[2,0,0,0,0,0,-1,0,0,0],[-2,0,0,0,0,0,1,0,0,0]])
            if(rv_response == 1):
                $ rv_state[0] += 2
                $ rv_state[6] += 2
                rv "Of course, and I’m good at it, too. My dad taught me how to play, and it was hard to beat him."

            elif(rv_response == 2):
                $ rv_state[0] += 2
                $ rv_state[6] -= 1
                rv "Well, my dad taught me, and he was a pretty good player."
                rv "He beat me a lot, but I got better because of it."


            elif(rv_response == 3):
                $ rv_state[0] += 2
                $ rv_state[6] += 1
                rv "Huh. Didn't expect you to ask me."
                rv "Of course, and I’m good at it, too. My dad taught me how to play, and it was hard to beat him."


        "Are you good at it, [rv]?":
            # 1-2 points for li->rv
            $ pg_state[6] = pg_state[6] + 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,0,0,2,0,0,0]))
            "{i}[response]{/i}"


            $ rv_response = rival.findBestFit([[2,0,0,0,0,0,2,0,0,0],[2,0,0,0,0,0,-1,0,0,0],[-2,0,0,0,0,0,1,0,0,0]])
            if(rv_response == 1):
                $ rv_state[0] += 2
                $ rv_state[6] += 2
                rv "Of course, and I’m good at it, too. My dad taught me how to play, and it was hard to beat him."

            elif(rv_response == 2):
                $ rv_state[0] += 2
                $ rv_state[6] -= 1
                rv "Well, my dad taught me, and he was a pretty good player."
                rv "He beat me a lot, but I got better because of it."


            elif(rv_response == 3):
                $ rv_state[0] += 2
                $ rv_state[6] += 1
                rv "Huh. Didn't expect you to ask me."
                rv "Of course, and I’m good at it, too. My dad taught me how to play, and it was hard to beat him."

        # some points for rv->pg, 1-2 points for li->pg
        "What are you to say that, [rv]?":
            $ pg_state[6] = pg_state[6] + 2
            $ pg_state[0] = pg_state[0] + 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([1,0,0,0,0,0,2,0,0,0]))
            "{i}[response]{/i}"


            $ rv_response = rival.findBestFit([[0,0,0,0,-2,0,2,0,0,0],[0,0,0,0,0,0,2,-2,0,0]])
            if(rv_response == 1):
                $ rv_state[4] -= 2
                $ rv_state[6] += 2
                rv "Because I know how to play well? I had to get good if I wanted to beat my dad, and he had a really high score."

            elif(rv_response == 2):
                $ rv_state[4] -= 2
                $ rv_state[6] += 2
                rv "Woah."
                show rivchar rv_happy
                rv "You're right though..."
                rv "I know how to play. I had to get good if I wanted to beat my dad, and he had a really high score."


    show rivchar rv
    li "Do you know how to play, [pg]?"

    "{i}Do I...?{/i}"

    menu:

        "Of course, I’m not very good though.":
            # 1-2 points for li->rv
            $ pg_state[0] = pg_state[0] - 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([-1,0,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            rv "Aren’t you modest? Why don’t we figure out how good you really are?"

        # 2-3 points for li->pg
        "Of course, I’m decent at it.":
            $ pg_state[0] = pg_state[0] + 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([2,0,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            rv "Then you wouldn’t mind playing a game against me, would you?"

        # 2-3 points for li->pg and rv->pg
        "Of course, I might be even better than [rv].":
            $ pg_state[0] = pg_state[0] + 4
            $ pg_state[1] = pg_state[1] - 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([4,-1,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            rv "Those are some big words..."
            rv "If that’s the case, then you wouldn’t mind playing a game against me, would you?"

    menu:

        # 2-3 points for li->pg and rv->pg
        "Bring it on.":
            $ pg_state[0] = pg_state[0] + 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([2,0,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            rv "Then let’s set up the board."

        # 2-3 points for li->pg, high points for rv->pg
        "Let’s see how good you really are.":
            $ pg_state[0] = pg_state[0] + 4
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([4,0,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            rv "Then let’s set up the board."

        # 1-2 points for li->pg and rv->pg
        "I’ll try my best.":
            $ pg_state[0] = pg_state[0] - 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([-1,0,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            rv "Then let’s set up the board."

    rv "Alright. White or black?"

    menu:

        "White.":
            rv "Go ahead, make your move."


        "Black.":
            rv "Alright, I’ll make my first move."

    "..."

    rv "..."

    "..."

    rv "..."

    "..."

    rv "..."

    rm "...This is my chess set, but I don’t know what’s going on."

    "{i}[rv] is better than I thought. You wouldn’t expect it, but he’s got a strategy.{/i}"

    "{i}Aside from being naturally competitive, I don’t want to lose in front of [li]. Of course it’s just a chess game with no risks, but somehow, it’s way more intense than that.{/i}"

    "{i}It’s not just a game of chess, but a battle of wits. A silent game to win [li]’s hand.{/i}"

    "{i}...Did I just say that?{/i}"

    "{i}Well, it’s like we’re trying to see who has a better chance right now, who’s in the right mindset to give it their all to get [li]. I guess that’s the feeling.{/i}"

    "{i}In that case, I should fight really hard. If I put in the work, I won’t entirely lose.{/i}"

    "{i}But I’m in a pretty tricky spot...he’s attacking from all sides of the board. If I’m not careful, he’ll get my king.{/i}"

    "{i}What should I do?{/i}"

    menu:

        "Attack.":
            rv "...Interesting."
            li "Is it good or bad?"
            rv "It might end the game sooner."

        # best_move +1
        "Defend.":
            $ best_move += 1
            rv "...Huh."
            li "Is it good or bad?"
            rv "It was unexpected."

    "{i}I can’t make out what he’s thinking with all these moves. Where are we at right now? Over 40 moves?{/i}"

    "{i}Well it’s not like we’re playing super-competitive chess that we’ve got those rules. Still...I wonder if the end is in sight?{/i}"

    "{i}My turn again. This time...{/i}"

    menu:

        # best_move +1
        "Attack.":
            $ best_move += 1
            rv "Hm."

        "Defend.":
            rv "Hm."

    "What does that mean?"

    rv "Well I can’t say, can I?"

    "{i}That’s the thing about chess. A part of it is psychological warfare.{/i}"

    "{i}Geez, then how long will it go on with [li], then?{/i}"

    "{i}I guess it doesn’t matter...I like her so much that I’d go through a lot of it if it means some sort of chance.{/i}"

    "{i}I’m sure [rv] is like that, too.{/i}"

    "{i}Our mindset is kind of alike, right?{/i}"

    "{i}If that’s the case, then...I should know what moves he’ll do next, right? Looking at the board...{/i}"

    menu:

        # best_move +1
        "Move queen.":
            $ best_move += 1
            rv "Oh wow."

        "Move rook.":
            rv "oh wow."

    # not sure if we have to put dollar sign or not for this one?
    if best_move >= 2:
        $chess_win = True

    if chess_win:

        rv "Bad move, [pg]. I win."
        show rivchar rv_smirking

        #li->rv big points, some points for rv->pg
        $ pg_state[0] = pg_state[0] - 2
        $ pg_state[7] = pg_state[7] - 5
        $ response = LoveInterest.textResponse(LoveInterest.getResponse([-2,0,0,0,0,0,0,-5,0,0]))
        "{i}[response]{/i}"

        show rivchar rv_happy
        rv "Good game, though. You caught me off guard a couple of times."


    else:

        rv "...I’m resigning. Good game, [pg]. You put up a good fight."

        $ pg_state[0] = pg_state[0] + 2
        $ pg_state[7] = pg_state[7] + 5
        $ response = LoveInterest.textResponse(LoveInterest.getResponse([2,0,0,0,0,0,0,5,0,0]))
        "{i}[response]{/i}"

        # rv->pg some points, li->pg big points

    show rivchar rv
    rm "That was...thrilling, yet not-so-thrilling at the same time."

    cf "Should have drank a bit more."

    show luvint li_happy at left
    li "It was! Even if I wasn’t sure what was going on...[rv], [pg], you were both pretty cool!"

    li "If I learned how to play, maybe I could play next time..."

    menu:

        # best option, points for li->pg
        "I would love to teach you how to play.":
            $ pg_state[4] += 3
            $ pg_state[7] += 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,3,0,0,2,0,0]))
            "{i}[response]{/i}"
            show luvint li_happy2 at left
            li "Awesome! You might have to go easy on me at first, haha."

        # maybe like 1-2 points for li->pg
        "Having a match would be fun.":
            # best option for li->rv, points for li->rv

            $ rv_response = rival.findBestFit([[0,0,0,0,2,0,0,2,0,0],[0,0,0,0,3,0,0,1,0,0]])
            if(rv_response == 1):
                $ rv_state[4] += 2
                $ rv_state[7] += 2
                rv "I could teach you how to play."
                show luvint li_happy2 at left
                li "You will? Thanks!"
                "{i}Damn, I could have done that.{/i}"

            elif(rv_response == 2):
                $ rv_state[4] += 1
                $ rv_state[7] += 3
                rv "Woah."
                rv "Yeah, it'll be fun once you know how to play. I could teach you."
                show luvint li_happy2 at left
                li "You will? Thanks!"
                "{i}Damn, I could have done that.{/i}"


        "Yeah, maybe next time.":
            # best option for li->rv, points for li->rv
            $ pg_state[4] -= 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,-2,0,0,0,0,0]))
            "{i}[response]{/i}"


            $ rv_response = rival.findBestFit([[0,0,0,0,2,0,0,2,0,0],[0,0,0,0,3,0,0,1,0,0]])
            if(rv_response == 1):
                $ rv_state[4] += 2
                $ rv_state[7] += 2
                rv "I could teach you how to play."
                show luvint li_happy2 at left
                li "You will? Thanks!"
                "{i}Damn, I could have done that.{/i}"

            elif(rv_response == 2):
                $ rv_state[4] += 1
                $ rv_state[7] += 3
                rv "Woah."
                rv "Yeah, it'll be fun once you know how to play. I could teach you."
                show luvint li_happy2 at left
                li "You will? Thanks!"
                "{i}Damn, I could have done that.{/i}"

    "{i}But that was a good game overall.{/i}"

    "{i}...I should really try harder, and of course I shouldn’t let myself get too comfortable.{/i}"

    "{i}[rv] is a pretty set on getting [li]...{/i}"

    "{i}...but I’m just as determined.{/i}"

    jump after4
