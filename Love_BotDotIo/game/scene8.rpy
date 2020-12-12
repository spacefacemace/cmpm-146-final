# variables to add:
# stuff for ai
# points for li->pg, li->rv, rv->pg

# this is the one with pat and sash
# pat = pat, sesh = sesh
# autocorrect keeps making path "path" and sesh "sash" so if it throws a fit...might be those.

# rn the answers to the player's options is
# set to the ideal answer (mostly for rv ai) + its weight
# probably take them out and put them in a set
# and make ai choose the best from there

label scene8:

    # first elem: li->pg, second elem: li->rv, third elem: rv->pg
    $ arr = [0, 0, 0]

    scene second_stage

    show rv
    
    pg "{i}No matter how many times we’ve rehearsed all this backstage stuff, being back here with [rv] is...interesting.{/i}"

    pg "{i}Especially when...{/i}"

    rv "[li], just in time. You’re up next."

    pg "{i}Of course we want this whole show to go well, but on [li]’s part, we’re extra competitive. And now that it’s the real thing, I think we’ve gone to our max.{/i}"

    menu:

        "Are you ready?":
            #points for li->rv
            $ arr[1] += 3
            rv "Of course, [li]’s worked hard up to this point. From all the sports I’ve played, I know that type of thing won’t go to waste. [li], you’ll do great."

        "You think you’ll be okay?":
            #points for li->rv
            $ arr[1] += 3
            rv "Of course, [li]’s worked hard up to this point. From all the sports I’ve played, I know that type of thing won’t go to waste. [li], you’ll do great."

        # best option, points for li->pg
        "You’re going to do great. You’ve worked really hard on this.":
            $ arr[0] += 5
            rv "Yeah, from all the sports I’ve played, I know that type of thing won’t go to waste."

    show li at right

    li "Thanks! I’m nervous, but it’s nervous excitement. I think it’ll help...somehow, haha. But you’re right, I’ve worked hard on this! It’ll show, right?"

    menu:

        "I don’t see why not.":
            #points for li->rv
            $ arr[1] += 3
            rv "Oh for sure, we’ll make sure of it."

        "I think so.":
            #points for li->rv
            $ arr[1] += 3
            rv "Oh for sure, we’ll make sure of it."

        # best option, points for li->pg
        "Of course it will, we’ll make sure of it.":
            $ arr[0] += 5
            rv "[pg]’s right. It’s why we’re helping out."


    rv "Anyway, your music’s queued up, [li]. Is she good to go, [pg]?"

    pg "Yep, in 5...4...3...2...1."

    li "Alright, here I go!"

    hide li at easeoutright

    "{i}We’ve seen this a million times, but it’s as captivating as the first time.{/i}"

    "{i}[li] is good. She’s very passionate about it, and that’s what makes it so interesting to watch.{/i}"

    "{i}You can really tell that this is one of her favorite things to do.{/i}"

    rv "...Psst. Hey."

    menu:

        "What?":
            rv "You’re thinking the same thing, aren’t you?"

        "Huh?": 
            rv "You’re thinking the same thing, aren’t you?"

        "(silence)":
            rv "You’re thinking the same thing, aren’t you?"

    menu:

        "Yeah, I don’t want to.":
            # points for rv->pg
            $ arr[2] += 3
            rv "...Wow. You’re pretty sure of yourself, [pg]."

        "I’m trying not to.":
            rv "You don’t so sure about yourself...or maybe it’s a strategy to make me think that."
            "...I dunno if I’ve thought that far ahead."
            rv "Then I guess I just gave you an idea...shit. Anyway."

    rv "Well, me neither."

    rv "I don’t really have much else to say."

    rv "But you know, [pg], you’re making it kind of hard."

    menu:

        "I'm sorry?":
            rv "Yeah, because normally people just quit by now...but not you."

        "Is that so?": 
            rv "Yeah, because normally people just quit by now...but not you."

    rv "I mean, look at where we are."

    rv "Honestly, that’s kind of commendable."

    menu:

        "Same with you.": # this one gives points for rv->pg
            $ arr[2] += 2
            rv "When this all comes to an end...no hard feelings?"

        "I guess it could be.": 
            rv "When this all comes to an end...no hard feelings?"

    menu:

        "Yeah, no hard feelings.": # some points for rv->pg
            $ arr[2] += 3
            rv "Sweet. Don’t worry, that feeling’s mutual."

        "I’ll have to think about it.":
            rv "You know what? That’s fair. I would have said the same thing."

    rv "You’re not bad, [pg]. I wouldn’t mind you at all at any other point...but right now, you are my rival, so I do mind."

    # then like do a transition here?
    scene outside_second_stage

    show rv at right
    show li at left

    menu:

        "Congratulate [li].": # points for li->pg
            $ arr[0] += 4
            "Congratulations, [li], the show was a success!"
            rv "Yep, and from me and [pg] -- here you go."
            $ arr[1] += 1

        "Greet [li].":
            $ arr[1] += 4
            rv "Congrats on the show, [li]. I’d say it went pretty well?" # points for li->rv
            "Oh, here’s something for you."
            $ arr[0] += 1

   li "Flowers? You shouldn’t have."

   li "No, really, I love flowers, but keeping them alive..."

   li "I’ll try my best, haha."

   li "I know I keep saying it, but thank you for your help! It’s thanks to you that the show was enjoyable. Everyone was less worried, me included. I think that ease of mind made our performances all the more better!"

    menu:

        "If it meant the show was more enjoyable for you, then it was worth it.": # 1-2 points for li->rv
            rv "Yeah, what [pg] said. It’s nice that the last show went well."
            $ arr[1] += 2

        "It’s no big deal.":
            rv "Yeah, no worries. You should enjoy your final show, after all." # a lot of points for li->rv
            $ arr[1] += 4

    show cf
    hide rv at easeoutright
    hide li at easeoutleft

    cf "Guys, you won’t believe who came to see the show! It’s two of my favorite teachers here, Pat and Sesh."

    show pat at left
    show sesh at right

    pat "[cf] said you were the leader, right?"

    li "That’s right."

    sesh "It was a really good show. I could see all the hard work that was put into it."

    pat "Right, and in a time crunch, too. Good thing you were able to make it -- if you ended up putting it off another week, I wouldn’t have been able to see it."

    sesh "Anyway, that’s all we wanted to say. And also, good job, [cf]."

    hide li
    show cf

    cf "Wow, thanks!"

    hide pat at easeoutleft
    hide sesh at easeoutright

    show rv at right
    show li at left

    cf "...I do good in this, but not so much his classes."

    cf "Anyway!"

    cf "Did I miss anything?"

    rv "Not much."

    li "You guys are going to the after-party, right?"

    menu:

        "I wouldn’t miss it for the world.": # points for li->pg
            $ arr[0] += 4
            rv "Same here." # give li->rv like one pity point he's trying
            $ arr[1] += 1

        "Right, the after-party...":
            cf "Did you forget? Good thing we’re going together, then."

        "That completely slipped my mind.":
            rv "You forgot? Don’t say you have something else planned. It’d suck if you weren’t there." # points for li->rv
            $ arr[1] += 4
            "No, I don’t." 
            cf "We literally made plans yesterday about going together! But with all the mayhem that was going on, I could see how it’d be easy to forget." 
            "Of course, I wouldn’t miss it." 

    li "Awesome! See you guys later, then!"

    hide li at easeoutleft

    rv "Yeah, see you guys, too."

    hide rv at easeoutright

    cf "...Just you and me, [pg]."

    cf "That went well, don’t you think?"

    "Yep. I could tell you did your absolute best, [cf]."

    cf "Haha, well...I know [li]’s probably said it, but thanks for the help. We couldn’t have done it without you."

    cf "Then should we get ready to head over to the after-party?"

    cf "Won’t matter if we’re late, but...you know how it is."

    return arr

