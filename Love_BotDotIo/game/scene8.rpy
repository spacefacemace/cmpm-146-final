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

    image second_stage = Frame("second_stage.jpg")
    image outside_second_stage = Frame("outside_second_stage.jpg")

    scene second_stage

    show rivchar rv

    pg "{i}No matter how many times we’ve rehearsed all this backstage stuff, being back here with [rv] is...interesting.{/i}"

    pg "{i}Especially when...{/i}"

    rv "[li], just in time. You’re up next."

    pg "{i}Of course we want this whole show to go well, but on [li]’s part, we’re extra competitive. And now that it’s the real thing, I think we’ve gone to our max.{/i}"

    menu:

        "Are you ready?":
            #points for li->rv
            $ pg_state[4] += 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,1,0,0,0,0,0]))
            "{i}[response]{/i}"


            $ rv_response = rival.findBestFit([[0,0,0,0,2,0,0,-1,0,0],[0,0,0,0,3,0,0,-2,0,0]])
            if(rv_response == 1):
                $ rv_state[4] += 2
                $ rv_state[7] -= 1
                show rivchar rv_happy
                rv "Of course, [li]’s worked hard up to this point. From all the sports I’ve played, I know that type of thing won’t go to waste. [li], you’ll do great."

            elif(rv_response == 2):
                $ rv_state[4] += 3
                $ rv_state[7] -= 2
                show rivchar rv_happy
                rv "Of course, [li]’s worked hard up to this point. From all the sports I’ve played, I know that type of thing won’t go to waste. [li], you’ll do great."
                show rivchar rv
                rv "But I can get where you're coming from, [pg]."

        "You think you’ll be okay?":
            #points for li->rv
            $ pg_state[1] += 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,1,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
           # rv "Of course, [li]’s worked hard up to this point. From all the sports I’ve played, I know that type of thing won’t go to waste. [li], you’ll do great."

            $ rv_response = rival.findBestFit([[0,0,0,0,2,0,0,-1,0,0],[0,0,0,0,3,0,0,-2,0,0]])
            if(rv_response == 1):
                $ rv_state[4] += 2
                $ rv_state[7] -= 1
                show rivchar rv_happy
                rv "Of course, [li]’s worked hard up to this point. From all the sports I’ve played, I know that type of thing won’t go to waste. [li], you’ll do great."

            elif(rv_response == 2):
                $ rv_state[4] += 3
                $ rv_state[7] -= 2
                show rivchar rv_happy
                rv "Of course, [li]’s worked hard up to this point. From all the sports I’ve played, I know that type of thing won’t go to waste. [li], you’ll do great."
                show rivchar rv
                rv "But I can get where you're coming from, [pg]."

        # best option, points for li->pg
        "You’re going to do great. You’ve worked really hard on this.":
            $ pg_state[0] += 1
            $ pg_state[4] += 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([1,0,0,0,1,0,0,0,0,0]))
            "{i}[response]{/i}"
            rv "Yeah, from all the sports I’ve played, I know that type of thing won’t go to waste."

    show rivchar rv
    show luvint li_happy at right

    li "Thanks! I’m nervous, but it’s nervous excitement. I think it’ll help...somehow, haha. But you’re right, I’ve worked hard on this! It’ll show, right?"

    menu:

        "I don’t see why not.":
            #points for li->rv
            rv "Oh for sure, we’ll make sure of it."

        "I think so.":
            #points for li->rv
            $ pg_state[0] -= 1
            rv "Oh for sure, we’ll make sure of it."

        # best option, points for li->pg
        "Of course it will, we’ll make sure of it.":
            $ pg_state[3] += 2
            $ pg_state[0] += 2
            $ pg_state[4] += 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([2,0,0,2,1,0,0,0,0,0]))
            "{i}[response]{/i}"


            $ rv_response = rival.findBestFit([[0,0,0,0,2,0,0,1,0,0],[0,0,0,0,3,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[4] += 2
                $ rv_state[7] += 1
                rv "[pg]’s right. It’s why we’re helping out."

            elif(rv_response == 2):
                $ rv_state[4] += 3
                rv "[pg]’s right. It’s why we’re helping out."
                rv "You gotta do your best while we're watching, too."
                show luvint li_happy2 at right
                li "Haha, of course!"

    rv "Anyway, your music’s queued up, [li]. Is she good to go, [pg]?"

    pg "Yep, in 5...4...3...2...1."

    show luvint li_joy at right
    li "Alright, here I go!"

    hide luvint li_joy at easeoutright

    "{i}We’ve seen this a million times, but it’s as captivating as the first time.{/i}"

    if LoveInterest.getResponse(rv_state) > LoveInterest.getResponse(pg_state):
        # rival's song is picked, rival gets some big points

        "{i}When [li] said she was picking [rv]'s song, he looked really proud.{/i}"

        "{i}I mean, I would be, too.{/i}"

        "{i}To be on [li]'s side is pretty critical at this point.{/i}"

        "{i}Well, even if it's not mine, it's fine. I mean, I'm here -- I still want to support her.{/i}"

    else: # player's song is picked, player gets some big points

        "{i}I'm glad she picked my song. It feels nice to be on [li]'s good side.{/i}"

        "{i}Although [rv] did seem a little bummed about it.{/i}"

        "{i}But we're rivals nonetheless. I think he understands.{/i}"

        "{i}And I like what she did with the song. Of course I do.{/i}"

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
            rv "...Wow. You’re pretty sure of yourself, [pg]."

        "I’m trying not to.":
            rv "You don’t so sure about yourself...or maybe it’s a strategy to make me think that."
            "...I dunno if I’ve thought that far ahead."
            rv "Then I guess I just gave you an idea...shit. Anyway."

    rv "Well, me neither."

    rv "I don’t really have much else to say."

    show rivchar rv_angry
    rv "But you know, [pg], you’re making it kind of hard."

    menu:

        "I'm sorry?":
            rv "Yeah, because normally people just quit by now...but not you."

        "Is that so?":
            rv "Yeah, because normally people just quit by now...but not you."

    rv "I mean, look at where we are."

    show rivchar rv
    rv "Honestly, that’s kind of commendable."

    menu:

        "Same with you.": # this one gives points for rv->pg
            rv "When this all comes to an end...no hard feelings?"

        "I guess it could be.":
            rv "When this all comes to an end...no hard feelings?"

    menu:

        "Yeah, no hard feelings.": # some points for rv->pg
            rv "Sweet. Don’t worry, that feeling’s mutual."

        "I’ll have to think about it.":
            rv "You know what? That’s fair. I would have said the same thing."

    rv "You’re not bad, [pg]. I wouldn’t mind you at all at any other point...but right now, you are my rival, so I do mind."

    # then like do a transition here?
    scene outside_second_stage

    show rivchar rv at right
    show luvint li_joy at left

    menu:

        "Congratulate [li].": # points for li->pg
            $ pg_state[7] += 3
            $ pg_state[4] += 4
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,4,0,0,3,0,0]))
            "{i}[response]{/i}"

            $ rv_response = rival.findBestFit([[0,0,0,0,1,0,0,2,0,0],[0,0,0,0,2,2,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[4] += 1
                $ rv_state[7] += 2
                pg "Congratulations, [li], the show was a success!"
                show rivchar rv_smiling at right
                rv "Yep, and from me and [pg] -- here you go."

            elif(rv_response == 2):
                $ rv_state[4] += 2
                $ rv_state[4] += 2
                pg "Congratulations, [li], the show was a success!"
                rv "You beat me to it."
                show rivchar rv_smiling at right
                rv "Anyway, congrats, [li]. From me and [pg] -- here you go."


        "Greet [li].":
            $ pg_state[4] -= 3
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,-3,0,0,0,0,0]))
            "{i}[response]{/i}"


            $ rv_response = rival.findBestFit([[0,0,0,0,1,0,0,2,0,0],[0,0,0,2,2,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[4] += 2
                $ rv_state[7] += 1
                rv "Congrats on the show, [li]. I’d say it went pretty well?"
                pg "Oh, here’s something for you."

            elif(rv_response == 2):
                $ rv_state[4] += 2
                $ rv_state[3] += 1
                rv "Congrats on the show, [li]. I’d say it went pretty well?"
                rv "[pg] and I have something for you."
                pg "Yup, here it is."

    li "Flowers? You shouldn’t have."

    show luvint li_happyblush at left
    li "No, really, I love flowers, but keeping them alive..."

    li "I’ll try my best, haha."

    show luvint li_happy2 at left
    li "I know I keep saying it, but thank you for your help! It’s thanks to you that the show was enjoyable. Everyone was less worried, me included. I think that ease of mind made our performances all the more better!"

    show rivchar rv at right
    show luvint li_joy

    menu:

        "If it meant the show was more enjoyable for you, then it was worth it.": # 1-2 points for li->rv
            rv "Yeah, what [pg] said. It’s nice that the last show went well."
            $ pg_state[1] += 3
            $ pg_state[6] += 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,3,0,0,0,0,1,0,0,0]))
            "{i}[response]{/i}"

            $ rv_response = rival.findBestFit([[0,0,0,0,1,0,0,1,0,0],[0,0,0,0,2,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[7] += 1
                $ rv_state[4] += 1
                rv "Yeah, what [pg] said. It’s nice that the last show went well."

            elif(rv_response == 2):
                $ rv_state[4] += 2
                rv "Yeah, no worries. You should enjoy your final show, after all."

        "It’s no big deal.":
            rv "Yeah, no worries. You should enjoy your final show, after all." # a lot of points for li->rv


    show cfimg cf_happy
    hide rivchar rv at easeoutright
    hide luvint li_joy at easeoutleft

    cf "Guys, you won’t believe who came to see the show! It’s two of my favorite teachers here, Pat and Sesh."

    show pat at left
    show sesh at right

    pat "[cf] said you were the leader, right?"

    li "That’s right."

    sesh "It was a really good show. I could see all the hard work that was put into it."

    pat "Right, and in a time crunch, too. Good thing you were able to make it -- if you ended up putting it off another week, I wouldn’t have been able to see it."

    sesh "Anyway, that’s all we wanted to say. And also, good job, [cf]."

    hide luvint li_joy
    show cfimg cf

    cf "Wow, thanks!"

    hide pat at easeoutleft
    hide sesh at easeoutright

    show rivchar rv at right
    show luvint li_joy at left

    show cfimg cf_disappointed
    cf "...I do good in this, but not so much his classes."

    show cfimg cf
    cf "Anyway!"

    cf "Did I miss anything?"

    rv "Not much."

    li "You guys are going to the after-party, right?"

    menu:

        "I wouldn’t miss it for the world.": # points for li->pg
            $ pg_state[7] += 2
            $ pg_state[5] += 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,0,1,0,2,0,0]))
            "{i}[response]{/i}"


            $ rv_response = rival.findBestFit([[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[7] += 1
                rv "Same here."

            elif(rv_response == 2):
                $ rv_state[4] += 1
                rv "You have a way with words, [pg]."
                rv "I have nothing to say except...well, same."

        "Right, the after-party...":
            cf "Did you forget? Good thing we’re going together, then."

        "That completely slipped my mind.":
            rv "You forgot? Don’t say you have something else planned. It’d suck if you weren’t there." # points for li->rv
            $ pg_state[2] -= 3
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,-3,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            "No, I don’t."
            show cfimg cf_disappointed
            cf "We literally made plans yesterday about going together! But with all the mayhem that was going on, I could see how it’d be easy to forget."
            "Of course, I wouldn’t miss it."

    show cfimg cf
    li "Awesome! See you guys later, then!"

    hide luvint li_joy at easeoutleft

    rv "Yeah, see you guys, too."

    hide rivchar rv at easeoutright

    cf "...Just you and me, [pg]."

    cf "That went well, don’t you think?"

    "Yep. I could tell you did your absolute best, [cf]."

    show cfimg cf_happy
    cf "Haha, well...I know [li]’s probably said it, but thanks for the help. We couldn’t have done it without you."

    show cfimg cf
    cf "Then should we get ready to head over to the after-party?"

    cf "Won’t matter if we’re late, but...you know how it is."

    jump after8
