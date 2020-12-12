# variables to add:
# stuff for ai
# points for li->pg, li->rv, rv->pg

# rn the answers to the player's options is
# set to the ideal answer (mostly for rv ai) + its weight
# probably take them out and put them in a set
# and make ai choose the best from there

label scene7:

    # first elem: li->pg, second elem: li->rv, third elem: rv->pg
    $ arr = [0, 0, 0]

    scene second_stage

    show rv
    
    "{i}Tomorrow is the show.{/i}"

    "{i}Everyone’s worked hard up until now, making sure that everything goes above and beyond, spendings hours upon hours perfecting their performances...you know how it goes.{/i}"

    "{i}And tomorrow, they’ll see the results of all their efforts.{/i}"

    rv "Alright, the last group’s music is queued."

    rv "...This is exhausting."


    menu:
        
        "You’re an athlete, though?":
            # points for rv->pg
            $ arr[2] += 3
            rv "Well, yeah, but..."
            rv "If you’re doing something new, of course it’ll be kind of tiring. No harm in that."
            rv "...On second thought, I’m not that tired, really. I could do this for two more hours if I had to!"
            rv "Wow, you’re something, [pg]. I’ll give you that."
            rv "It’s a different kind of work back here. I guess I’ve found some appreciation for the people that do this."


        "You got tired doing this sort of thing?":
            # points for rv->pg
            $ arr[2] += 3
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
            $ arr[0] += 3
            $ arr[2] += 2
            rv "Ugh, you're right."

        # 2-3 points for rv->pg, some points for li->pg
        "You shouldn’t leave your post, you need to be here when they do come.":
            $ arr[2] += 3
            $ arr[0] += 3
            rv "Ugh, you're right."

        # best option, points for li->pg
        "You need to be here.":
            $ arr[0] += 3
            rv "Ugh, you're right."

    rv "Or do you just not want me to leave?"

    menu:
        
        "That’s kind of...":
            rv "I'm kidding."


        "I don’t know...":
            rv "I'm kidding."

        # some points for rv->pg
        "What makes you say that...":
            $ arr[2] += 3
            rv "I'm kidding."

    rv "Oh, here they come."

    rv "You’re all late, you know."

    rv "You were supposed to be here...three minutes ago."

    rv "If this was the real thing, there could be some serious delay."

    menu:
        
        "I think they get it, [rv].":
            rv "I guess I was a little harsh. Sorry about that."

        # points for li->pg
        "It’s fine, what matters is that they’re here.":
            $ arr[0] += 3
            # 1-2 points for li->rv
            $ arr[1] += 2
            rv "...Right, right."
            rv "I guess I was a little harsh. Sorry about that."


        # points for li->pg
        "You don’t need to be so harsh.":
            $ arr[0] += 3
            # some points for li->rv
            $ arr[1] += 2
            rv "I’m not trying to be?"
            rv "...Does it seem that way?"
            rv "If it does, sorry."



    pg "You guys are good to go in...3, 2, 1."

    rv "...And that’s the end of our jobs. At least for this rehearsal."

    rv "You know about the after-party, right?"

    menu:
        
        # 1-2 points for li->rv
        "After-party?":
            $ arr[1] += 2
            rv "Yeah...[li] said something about it a few days ago."

        # subtract 1-2 points from li->pg
        "Kind of...?":
            $ arr[0] -= 2
            rv "Yeah...[li] said something about it a few days ago."

        # 2-3 points for li->rv
        "Did I miss something?":
            $ arr[1] += 3
            rv "Yeah...[li] said something about it a few days ago."

    rv "It’s going to be at...Ben Carson’s house?"

    rv "This dance group is one of his...interests? He’s an unofficial advisor?"

    menu:
        
        # 1-2 points for li->pg
        "Right, I think [li] told me about that.":
            $ arr[0] += 2
            rv "Anyway, he offered his house for...you know, the after-party."

        "Right...":
            rv "Anyway, he offered his house for...you know, the after-party."

        # points for rv->pg
        "If you say so...":
            $ arr[2] += 1
            rv "Anyway, he offered his house for...you know, the after-party."

    hide rv
    show li at right

    li "Good job everyone! You all did amazing!"

    li "The show looks great. I’m sure you’re all excited to show it off!"

    li "Alright, I won’t keep you guys long. Go home, get some rest, do whatever you need to do. See you tomorrow! Don’t forget -- you have to be here at 5PM!"

    show rv

    li "You guys have definitely got this down! You might be better than me when I had to do this, hahaha..."

    li "Doing what you did just now, we’ll definitely have a successful show tomorrow!"

    menu:
        
        # best option, points for li->pg
        "Then we’ll make sure to do our best.":
            $ arr[0] += 5
            # 1-2 points for li->rv
            $ arr[1] += 2
            rv "Exactly. Though it wouldn’t hurt if we did better tomorrow."
            rv "Shoot for the moon, and if you fail, at least you’ll land among the stars -- that sort of thing."

        "Hopefully that’s the case.":
            # points for li->rv
            $ arr[1] += 3
            rv "Oh, we’ll make sure it’ll be the best show it could possibly be. Though it wouldn’t hurt if we did better tomorrow."
            rv "Shoot for the moon, and if you fail, at least you’ll land among the stars -- that sort of thing."

        # 1-2 points for rv->pg
        "We’ll try.":
            $ arr[2] += 2
            # points for li->rv
            $ arr[1] += 3
            rv "Oh, we’ll make sure it’ll be the best show it could possibly be. Though it wouldn’t hurt if we did better tomorrow."
            rv "Shoot for the moon, and if you fail, at least you’ll land among the stars -- that sort of thing."

    li "Right!"

    li "Well, I’ll let you two go, too! Thanks for your hard work."

    return arr

