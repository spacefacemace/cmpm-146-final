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


    # the stuff for the chess stuff in this scene.
    $ chess_win = False
    $ best_move = 0

    scene pg_cf_rm_apartment

    show cf at right
    show li at left
    show rv
    
    cf "Don’t mind all the mess."

    menu:
        
        # best option, points for li->pg
        "Yeah, we’re gonna clean all this stuff tomorrow.":
            $ state[0] += 5
            rv "I sure hope so."
            cf "We have free time tomorrow, right, [pg]? We’ll get this sorted out."

        "Watch out for that pizza box.":
            # best option for rv, points for li->rv
            $ state[1] += 5
            rv "Don’t you think you should clean your place up a little?"

            menu:
                
                # 1-2 points for li->pg
                "Yeah, we'll clean it.":
                        $ state[0] += 2
                        cf "We have free time tomorrow, right, [pg]? We’ll get this sorted out."

                # lower points for li->pg
                "We’ll see about that.":
                        $ state[0] -= 4
                        cf "We have free time tomorrow, right, [pg]? We’ll get this sorted out."

        "(silence)":
            # best option for rv, points for li->rv
            rv "Don’t you think you should clean your place up a little?"
            $ state[1] += 5

            menu:
                
                # 1-2 points for li->pg
                "Yeah, we'll clean it.":
                    $ state[0] += 1
                    cf "We have free time tomorrow, right, [pg]? We’ll get this sorted out."

                # lower points for li->pg
                "We’ll see about that.":
                    $ state[0] -= 4
                    cf "We have free time tomorrow, right, [pg]? We’ll get this sorted out."

    cf "While we’re at it, let’s get [rm] in it, too."

    li "Yeah, where is he?"

    menu:
        
        # best option, points for li->pg
        "He’s playing Minecraft. I can go get him.":
            $ state[0] += 5
            li "Can’t have him missing out!"


        "He’s probably playing Minecraft.":
            # best option for rv, points for li->rv
            $ state[1] += 5
            rv "Why don’t you go get him, [pg]? See if he wants to hang out."


        "I dunno, his room?":
            # best option for rv, points for li->rv
            $ state[1] += 5
            rv "Why don’t you go get him, [pg]? See if he wants to hang out."

    hide cf
    show rm at right

    rm "Woah, there’s certainly more people here."

    li "[rm], are you good with sushi? Because we have a lot."

    rm "Yeah, if you don’t mind sharing."

    li "Not at all!"

    "{i}I should probably...{/i}"

    menu:
        
        # best option, points for li->pg
        "Clear the table.":
            $ state[1] += 5
            "Should I clear the table?"
            li "That'd be great!"


        "Set up the food.":
            # 1-2 points for li->pg
            $ state[0] += 2
            "Should I set up the food?"
            # 1-2 points for li->rv
            rv "Shouldn’t we clear the table first?"
            $ state[1] += 2
            li "Yeah, that first, then the food!"


        "Wait.":
            # best option for rv, points for li->rv
            rv "Shouldn’t we clear the table first?"
            $ state[0] += 5
            li "That’s a good idea!"

    li "All set. Alright, let’s dig in!"

    # fade here?

    hide rv
    show cf

    cf "Wow, that was exceptionally good."

    rm "It’s sushi, what did you expect?"

    pg "And all the soju [cf] drank."

    cf "I think we all had a bit."

    pg "But not as much as you."

    pg "[cf] usually doesn’t eat sushi, but I guess he couldn’t taste it considering he finished one and a half bottles of the cherry-flavored one?"

    cf "You know me too well, [pg]."

    cf "What was that?"

    rm "Oh, it’s my chess set. I was wondering where that went."

    cf "We had a chess set?"

    menu:
        
        # best option, points for li->pg
        "[rm] mentioned it when we first moved in.":
            $ state[0] += 3
            rm "Yes, we had a chess set. Though I don’t know how to play it {i}well{/i}."


        "I guess it was just hiding.":
            rm "Yes, we had a chess set. Though I don’t know how to play it {i}well{/i}."


        "I didn’t know that, either.":
            rm "Yes, we had a chess set. Though I don’t know how to play it {i}well{/i}."

    hide cf
    show rv

    rv "You’d be at some competition right now if you did."

    rm "...True."

    menu: 

        "Do you know how to play, [rv]?":
            # 1-2 points for li->rv
            $ state[1] += 2
            rv "Of course, and I’m good at it, too. My dad taught me how to play, and it was hard to beat him."


        "Are you good at it, [rv]?":
            # 1-2 points for li->rv
            $ state[1] += 2
            rv "Of course. I had to get good if I wanted to beat my dad, and he had a really high score."

        # some points for rv->pg, 1-2 points for li->pg
        "What are you to say that, [rv]?":
            $ state[0] += 2
            $ state[2] += 3
            # 2-3 points for li->rv
            $ state[2] += 3
            rv "Because I know how to play well? I had to get good if I wanted to beat my dad, and he had a really high score."


    li "Do you know how to play, [pg]?"

    "{i}Do I...?{/i}"

    menu: 

        "Of course, I’m not very good though.":
            # 1-2 points for li->rv
            $ state[1] += 2
            rv "Aren’t you modest? Why don’t we figure out how good you really are?"

        # 2-3 points for li->pg
        "Of course, I’m decent at it.":
            $ state[0] += 3
            # 2-3 points for li->rv
            $ state[1] += 3
            rv "Then you wouldn’t mind playing a game against me, would you?"

        # 2-3 points for li->pg and rv->pg
        "Of course, I might be even better than [rv].":
            $ state[0] += 3
            $ state[2] += 3
            # 2-3 points for li->rv
            rv "Those are some big words..."
            $ state[1] += 3
            rv "If that’s the case, then you wouldn’t mind playing a game against me, would you?"

    menu: 

        # 2-3 points for li->pg and rv->pg
        "Bring it on.":
            $ state[0] += 3
            $ state[2] += 3
            rv "Then let’s set up the board."

        # 2-3 points for li->pg, high points for rv->pg
        "Let’s see how good you really are.":
            $ state[0] += 3
            $ state[2] += 5
            rv "Then let’s set up the board."

        # 1-2 points for li->pg and rv->pg
        "I’ll try my best.":
            $ state[0] += 2
            $ state[2] += 2
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
    $ if best_move >= 2:
        $ chess_win = True

    if chess_win:

        rv "Bad move, [pg]. I win."

        #li->rv big points, some points for rv->pg
        $ state[1] += 5
        $ state[2] += 3

        rv "Good game, though. You caught me off guard a couple of times."


    else:

        rv "...I’m resigning. Good game, [pg]. You put up a good fight."

        $ state[0] += 5
        $ state[2] += 3

        # rv->pg some points, li->pg big points


    rm "That was...thrilling, yet not-so-thrilling at the same time."

    cf "Should have drank a bit more."

    li "It was! Even if I wasn’t sure what was going on...[rv], [pg], you were both pretty cool!"

    li "If I learned how to play, maybe I could play next time..."

    menu: 

        # best option, points for li->pg
        "I would love to teach you how to play.":
            $ state[0] += 5
            li "Awesome! You might have to go easy on me at first, haha."

        # maybe like 1-2 points for li->pg
        "Having a match would be fun.":
            $ state[0] += 2
            # best option for li->rv, points for li->rv
            $ state[1] += 5
            rv "I could teach you how to play."
            li "You will? Thanks!"
            "{i}Damn, I could have done that.{/i}"

        "Yeah, maybe next time.":
            # best option for li->rv, points for li->rv
            $ state[1] += 5
            rv "I could teach you how to play."
            li "You will? Thanks!"
            "{i}Damn, I could have done that.{/i}"

    "{i}But that was a good game overall.{/i}"

    "{i}...I should really try harder, and of course I shouldn’t let myself get too comfortable.{/i}"

    "{i}[rv] is a pretty set on getting [li]...{/i}"

    "{i}...but I’m just as determined.{/i}"

    jump after4

