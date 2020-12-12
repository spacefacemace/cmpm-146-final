# variables to add:
# stuff for ai
# points for li->pg, li->rv, rv->pg

# rn the answers to the player's options is
# set to the ideal answer (mostly for rv ai) + its weight
# probably take them out and put them in a set
# and make ai choose the best from there


label scene9:

    scene bens_house

    show cf at right
    show rm at left

    rm "This is...an odd venue, but I’ll take it. His vinyl collection is insane."

    cf "...Did you go through it?"

    rm "What? Of course not. I have manners."

    cf "Why are you here again?"

    rm "Because [li] invited me?"

    li "It’d be a shame if he was left in your apartment all by himself!"

    li "Besides, this sort of thing...it’s a last for most of us before graduating."

    rv "It really is about to end, huh?"

    rv "On one hand, thank god. On the other hand..."

    menu:
        
        # best option, points for li->pg
        "It’s a bit bittersweet.":
            $ state[0] += 5
            li "I totally get it! You go through all this and then..."
            rv "Just like that, it’s about to end." # (1-2 pts li->rv)
            $ state[1] += 1
            li "Yep, exactly."


        "I’m glad it’s over.":
            $ state[2] += 2
            rv "Well, yeah, but also...it’s bittersweet, kind of."
            rv "...Geez, that was cheesy. Don’t tell anyone I said that."
            li "Haha, I won’t tell."
            $ state[1] += 3

        "I’m not sure what to think.":
            li "I totally get it! You go through all this and then..."
            rv "Just like that, it’s about to end."
            $ state[1] += 3
            li "Yep, exactly."

    li "...I was going to say some more stuff, but I should probably save that spiel for later, huh?"

    menu:
        
        "Is it a lot?":
            rv "Well, no matter how much, I’ll listen to it. You can count on that." # a lot of points for li->rv
            $ state[1] += 4

        # best option, points for li->pg
        "I’m looking forward to it.":
            $ state[0] += 5
            rv "Me too. No matter how much you’ll say, I’ll listen to it. You can count on that." # (maybe like 2-3 li->rv)
            $ state[1] += 3

        # 1-2 points for li->pg
        "Wonder what it could be...":
            rv "Me too. No matter how much you’ll say, I’ll listen to it. You can count on that." # (maybe like 2-3 li->rv)
            $ state[1] += 3

    li "Oh, an audience? Then I’ll make sure it’s good."

    # (then fade to like later that night, li rv and pg are outside)
    scene out_bens_house
    show rv at right
    show li

    rv "I should get going. I want to wake up early tomorrow to go to the gym."

    li "Haha, always working hard on that, huh, [rv]? Well, we won’t keep you then."

    rv "Thanks. See you...well, we’re neighbors, so see you whenever."

    hide rv easeoutright

    li "...And then there were two."
 
    li "At least right here where we are. I think [cf] and [rm] went to go check out the vinyls again."

    li "I know I talk about just how eventful this year was...so I want to ask you this, [pg] -- what’d you think of this year?"

    menu:
        
        "It was a lot.":
            li "There’s a thought I always have, though...the thought of time moving forward."

        # best option, points for li->pg
        "You made it bearable.":
            $ state[0] += 5
            li "Me...?"
            li "That’s the first time someone’s said that to me."
            li "Well then...I’m honored!"
            li "There’s a thought I always have, though...the thought of time moving forward."

        # 1-2 points for li->pg
        "I’m ready for what’s next.":
            $ state[0] += 2
            li "Me too! A new chapter in life is always exciting."
            li "There’s a thought I always have, though...the thought of time moving forward."

    li "There’s a lot to get in order when moving on."

    li "At this point, it’s the type where we have to get our life together."

    li "Though I’m sure [rv] has something figured out. He always does. He mentioned working at his dad’s business? That must be fun."

    menu:
        
        # subtract points for li->pg(?)
        "It’s only because his dad is the CEO.":
            $ state[0] -= 2
            li "Ah, what am I thinking? We’re just in our 20’s. In the end, there’s no rush."

        # 1-2 points for li->rv
        "He sure has his life figured out.":
            $ state[1] += 2
            li "Ah, what am I thinking? We’re just in our 20’s. In the end, there’s no rush."

        # 1-2 pts for li->rv but 3-4 for li->pg
        "He just has a head start, we still have time.":
            $ state[1] += 2
            $ state[0] += 4
            li "Ah, what am I thinking? We’re just in our 20’s. In the end, there’s no rush."

    li "I’m sure we’ll be fine."

    menu:
        
        # best options, pts for li->pg
        "Yep, we will be.":
            $ state[0] += 5
            li "...What a mood we’re in. Let’s change that."

        # 1 pt for li->pg
        "That’s the plan.":
            $ state[0] += 1
            li "...What a mood we’re in. Let’s change that."

        "2 pts for li->pg":
            $ state[0] += 2
            li "...What a mood we’re in. Let’s change that."

    li "I’m going to check on the others. What about you?"

    "I’ll stay here for now."

    li "Alright! Feel free to come back inside whenever."

    hide li at easeoutleft

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
