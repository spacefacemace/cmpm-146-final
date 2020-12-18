


label scene1:

    image that_one_food_truck = Frame("that_one_food_truck.png")
    image picnic_tables = Frame("picnic_tables.jpg")

    scene that_one_food_truck

    show cfimg cf

    cf "There you are, [pg]! I already got the sandwich you like to get. Let’s go meet them!"

    "{i}Wow, [cf] got my order correct. Not that I’m surprised about that. We’ve known each other since we were kids -- nah, since the womb.{/i}"

    "{i}...Which is why I’m tagging along. You’d think that since we’re neighbors we’d get sick of seeing each other and not meet up on campus, but here we are.{/i}"

    "{i}This friend group is all [cf]’s doing. It’s alright, though, since that means that --{/i}"


    scene picnic_tables

    show cfimg cf at right
    show luvint li_happy at left
    show rivchar rv

    "{i}There she is, [li]. Who knows how long I’ve had a crush on her -- well, I moved into the apartment complex we’re all at during the summer, so it’s some time in-between.{/i}"

    "{i}I really don’t know when I realized I liked her, but when I did, it felt like I was in the middle of that feeling before I even knew it began.{/i}"

    li "Yay, you’re here at last!  What took you so long?"

    menu:
        "Sorry, my last class went over a little bit.":

            $ pg_state[2] = pg_state[2] + 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,2,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"

            li "I guess that sort of thing happens. At least you’re here now. Come on, [rv], make room for them to sit down. You can’t eat standing up!"

            "{i}[li] is nice, funny, and endearing. Pretty upbeat. Pretty in general. She’s all the good cliches of any love interest in a visual novel. It’s nice hanging out with her, but...{/i}"

            $ rv_response = rival.findBestFit([[0,2,1,0,0,0,0,0,0,0],[0,-2,-1,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[1] += 2
                $ rv_state[2] += 1
                rv "That kind of thing happens."

            elif(rv_response == 2):
                $ rv_state[1] -= 2
                $ rv_state[2] -= 1
                rv "Then just leave early?"
                "It was an important lecture, though?"
                rv "...Sure."

            elif(rv_response == 3):
                $ rv_state[5] += 1
                rv "I think it'd be a power move if you just left early. The professor will never see it coming."
                li "Power move?"
                rv "Yeah?"
                li "Hm...haha, I guess I can see it."

        "I forgot we were meeting up.":

            $ pg_state[2] = pg_state[2] - 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,-2,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"

            li "I guess that sort of thing happens. At least you’re here now. Come on, [rv], make room for them to sit down. You can’t eat standing up!"

            "{i}[li] is nice, funny, and endearing. Pretty upbeat. Pretty in general. She’s all the good cliches of any love interest in a visual novel. It’s nice hanging out with her, but...{/i}"

            $ rv_response = rival.findBestFit([[1,-1,0,0,0,0,0,0,0,0],[0,-1,0,0,0,1,0,0,0,0],[0,2,0,0,0,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[0] += 2
                $ rv_state[1] -= 1
                rv "Should I move for someone that forgot about meeting their friends?"
                rv "..."
                rv "Well since you’re here, I might as well."

            elif(rv_response == 2):
                $ rv_state[1] -= 1
                $ rv_state[5] += 1
                rv "Hmm...don't want to."
                li "Aw, come on, [rv]."
                rv "..."
                rv "I'm kidding, I'm kidding."

            elif(rv_response == 3):
                $ rv_state[1] += 2
                rv "Sure, sure. Just don't do it again, okay?"



        "I got distracted admiring all the scenery on the way here.":

            $ pg_state[3] = pg_state[3] = 3
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,3,0,0,0,0,0,0]))
            "{i}[response]{/i}"

            li "I guess that sort of thing happens. At least you’re here now. Come on, [rv], make room for them to sit down. You can’t eat standing up!"

            "{i}[li] is nice, funny, and endearing. Pretty upbeat. Pretty in general. She’s all the good cliches of any love interest in a visual novel. It’s nice hanging out with her, but...{/i}"

            $ rv_response = rival.findBestFit([[0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,-1,0,0,0,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[3] += 1
                rv "That’s incredibly...cheesy, but I get it."
                li "I totally understand! I’d do the same thing."

            elif(rv_response == 2):
                $ rv_state[1] += 1
                rv "You know what? I get it."

            elif(rv_response == 3):
                $ rv_state[1] -= 1
                rv "Well next time, speed it up."


    "{i}[rv] is something else. We’re ‘friends’, but more so than that, we’re enemies. Rivals. We both like the same person, and we’re both friends with [li]. It’s kind of tricky.{/i}"

    li "Wow, time really goes by fast, huh. We’re so close to graduation! We’ve only got a limited amount of days to just hang out like this and chill."

    cf "Come on, it’s not that close..."

    li "But it will be soon with each day passing by. We’ll be there before we know it!"

    "{i}She’s right, we’ll be graduating really soon. There’s only so much time left to make some sort of move on [li]. If I don’t, I’ll probably regret it. It’ll be one of those ‘what could have been’ situations.{/i}"

    "{i}But of course there’s [rv] to worry about. He’s known her longer, probably has some advantage...I can’t let that get to me, though! Maybe I’m just some stubborn protag, but it’s better to try than to not try at all.{/i}"

    rv "There’s no point in thinking about that sort of thing. It’s better to live in the now, enjoy what’s going on around us."

    li "Not even a little bit?"

    menu:
        "We can’t avoid the future. It’s natural that we think about it.":

            $ pg_state[1] = pg_state[1] + 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,2,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"

            li "See! [pg] agrees with me. Thanks for the backup."

            $ rv_response = rival.findBestFit([[0,0,0,0,0,0,-1,0,0,0],[0,1,0,0,0,0,0,1,0,0]])
            if(rv_response == 1):
                $ rv_state[6] -= 1
                rv "...Maybe I'm just missing something. Whatever."

            elif(rv_response == 2):
                $ rv_state[1] += 1
                $ rv_state[7] += 1
                rv "I may be missing something, but I won't argue with it."

        "Yeah, there’s really no point.":

            $ pg_state[1] = pg_state[1] - 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,-2,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"

            $ rv_response = rival.findBestFit([[0,-2,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,2,0,0]])
            if(rv_response == 1):
                $ rv_state[1] -= 2
                $ rv_state[7] -= 1
                li "Hmm, then I guess living in the present is some sort of bliss."
                show rivchar rv_smirking
                rv "Besides, you might be missing something around you right now."
                "{i}That’s too on the nose.{/i}"

            elif(rv_response == 2):
                $ rv_state[1] += 1
                $ rv_state[7] += 2
                show rivchar rv_smirking
                rv "If it makes you feel better, [li], if you live in the present, you might notice something."
                "{i}That’s too on the nose.{/i}"

        "I haven’t really thought about that.":

            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"

            $ rv_response = rival.findBestFit([[0,2,0,0,0,0,0,2,0,0],[0,3,0,0,0,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[1] += 2
                $ rv_state[7] += 1
                show rivchar rv_smirking
                rv "Well, if it makes you feel better, [li], if you live in the present, you might notice something."
                "{i}That’s too on the nose.{/i}"

            elif(rv_response == 2):
                $ rv_state[1] += 3
                pg "...But I will now."
                rv "Good for you, [pg]."
                show  rivchar rv_smirking
                rv "Well, if it makes you feel better, [li], if you live in the present, you might notice something."

    show rivchar rv

    cf "Well, no matter what, [li], you’ve got to think somewhat ahead. How’s the planning for the last show?"

    show luvint li_tired at left
    li "Don’t even get me started!"

    "{i}[cf] and [li] are in one of the dance groups on campus. It’s how they met. [li] was actually the one to recommend [cf] our current living situation.{/i}"

    "{i}While [cf] is more of just a regular member, [li] is actually the current leader of the group. She’s got a lot of responsibilities because of it. One of them is the last show for their group, the one where they go all-out for.{/i}"

    "{i}Everyone performs in it since it’s the last one for the entire school year. And for those graduating, it’s their last show in the group ever. Needless to say, it’s a pretty big deal.{/i}"

    rv "Procrastinating again?"

    li "Just a little bit... It’s the behind-the-scenes stuff I’m worried about. Not a lot of people in the group want to perform and do that at the same time. I don’t blame them -- it’s a lot."

    menu:
        "Maybe we could help out?":

            $ pg_state[2] = pg_state[2] + 2
            $ pg_state[4] = pg_state[4] + 4
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,2,0,4,0,0,0,0,0]))
            "{i}[response]{/i}"

            $ rv_response = rival.findBestFit([[0,0,0,0,-3,0,0,1,0,0],[0,0,0,0,2,0,0,2,0,0],[0,0,0,0,2,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[4] -= 3
                $ rv_state[7] += 1
                rv "Do we have to?"
                pg "Hey, come on..."
                rv "..."
                rv "Well if there's that sort of pressure, I might as well."

            elif(rv_response == 2):
                $ rv_state[4] += 2
                $ rv_state[7] += 2
                rv "Yeah, I was going to go and watch it anyway to support you guys."
                rv "But helping is also support, right?"

            elif(rv_response == 3):
                $ rv_state[4] += 2
                show rivchar rv_happy
                rv "Yeah, I'm with [pg]. We could help."

        "We could help -- I was going to go anyway to watch it, but why not support you guys behind-the-scenes as well?":

            $ pg_state[4] = pg_state[4] + 4
            $ pg_state[3] = pg_state[3] + 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,2,4,0,0,0,0,0]))
            "{i}[response]{/i}"

            $ rv_response = rival.findBestFit([[0,0,0,0,1,0,0,2,0,0],[0,0,0,0,-2,0,0,2,0,0],[0,0,0,0,-3,0,0,1,0,0]])
            if(rv_response == 1):
                $ rv_state[4] -= 3
                $ rv_state[7] += 1
                show rivchar rv_happy
                rv "That’s a good idea. I’m a big, strong guy -- I could help out some heavy-lifting."

            elif(rv_response == 2):
                $ rv_state[4] += 2
                $ rv_state[7] += 2
                rv "We?"
                pg "Don't you want to?"
                show rivchar rv_happy
                rv "...Of course! That’s a good idea. I’m a big, strong guy -- I could help out some heavy-lifting."

            elif(rv_response == 3):
                $ rv_state[4] -= 3
                $ rv_state[7] += 1
                show rivchar rv_sad
                rv "Do we have to?"
                pg "Hey, come on..."
                rv "..."
                rv "Well if there's that sort of pressure, I might as well."

        "...":

            $ rv_response = rival.findBestFit([[0,3,3,0,0,0,0,3,0,0],[0,2,2,0,0,0,0,4,0,0],[-2,0,0,0,0,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[7] += 3
                $ rv_state[1] += 3
                $ rv_state[2] += 3
                rv "Well maybe we could do something to help out? Since it’s so important to you, I’m sure we could take some time out of our lives to do so -- right, [pg]?"

            elif(rv_response == 2):
                $ rv_state[7] += 4
                $ rv_state[1] += 2
                $ rv_state[2] += 2
                rv "Well maybe we could do something to help out? Since it’s so important to you, I’m sure we could take some time out of our lives to do so -- right, [pg]?"
                show rivchar rv_happy
                rv "We'd get to hang out quite a bit, too."

            elif(rv_response == 3):
                $ rv_state[0] -= 2
                show rivchar rv_sad
                rv "Yep, seems a little difficult."
                cf "You guys could, I dunno...help out?"
                rv "Could we?"
                cf "It would be greatly appreciated."
                rv "...I guess we could."

            menu:
                "Yeah, I’m more than happy to help.":

                    $ pg_state[2] = pg_state[2] + 1
                    $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,1,0,0,0,0,0,0,0]))
                    "{i}[response]{/i}"

                "I guess I could help out.":

                    $ pg_state[2] = pg_state[2]



        "That seems like a lot.":

            $ pg_state[1] = pg_state[1] + 1

            $ rv_response = rival.findBestFit([[0,3,3,0,0,0,0,3,0,0],[0,2,2,0,0,0,0,4,0,0],[-2,0,0,0,0,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[7] += 3
                $ rv_state[1] += 3
                $ rv_state[2] += 3
                rv "Well maybe we could do something to help out? Since it’s so important to you, I’m sure we could take some time out of our lives to do so -- right, [pg]?"

            elif(rv_response == 2):
                $ rv_state[7] += 4
                $ rv_state[1] += 2
                $ rv_state[2] += 2
                rv "Well maybe we could do something to help out? Since it’s so important to you, I’m sure we could take some time out of our lives to do so -- right, [pg]?"
                show rivchar rv_happy
                rv "We'd get to hang out quite a bit, too."

            elif(rv_response == 3):
                $ rv_state[0] -= 2
                show rivchar rv_sad
                rv "Yep, seems a little difficult."
                cf "You guys could, I dunno...help out?"
                rv "Could we?"
                cf "It would be greatly appreciated."
                rv "...I guess we could."

            menu:
                "Yeah, I’m more than happy to help.":

                    $ pg_state[2] = pg_state[2] + 1
                    $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,1,1,0,0,0,0,0,0,0]))
                    "{i}[response]{/i}"

                "I guess I could help out.":

                    $ pg_state[2] = pg_state[2]


    show rivchar rv
    show luvint li_blush at left
    li "Are you sure about this?"

    menu:
        "Absolutely! Anything to make the show run smoothly.":

            $ pg_state[3] = pg_state[3] + 2
            $ pg_state[4] = pg_state[4] + 3
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,2,3,0,0,0,0,0]))
            "{i}[response]{/i}"

            $ rv_response = rival.findBestFit([[0,0,1,0,2,0,0,0,0,0],[0,0,0,0,-1,0,0,-2,0,0],[0,0,0,0,0,0,0,3,0,0]])
            if(rv_response == 1):
                $ rv_state[2] += 1
                $ rv_state[4] += 2
                rv "Agreed. If it all helps out, I'm fine with that."

            elif(rv_response == 2):
                $ rv_state[4] -= 1
                $ rv_state[7] -= 2
                rv "That's a little extra, don't you think?"
                rv "...I guess I agree."

            elif(rv_response == 3):
                $ rv_state[3] += 3
                rv "Yep, with us there, we might just make it the best show yet."

        "Well since I got roped into it, I have no choice now.":

            $ pg_state[4] = pg_state[4] - 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,-2,0,0,0,0,0]))
            "{i}[response]{/i}"

            $ rv_response = rival.findBestFit([[0,-2,0,0,0,0,0,-2,0,0],[0,1,2,0,0,0,0,0,0,0],[0,0,2,0,-2,0,0,0,0,0]])
            if(rv_response == 1):
                $ rv_state[1] -= 2
                $ rv_state[7] -= 2
                rv "Saying it like that...well, I might agree a bit."
                rv "But a team effort isn't always bad, I guess."

            elif(rv_response == 2):
                $ rv_state[1] += 1
                $ rv_state[2] += 2
                show rivchar rv_happy
                rv "The more the merrier, right?"
                rv "A team effort is always better."

            elif(rv_response == 3):
                $ rv_state[2] += 2
                $ rv_state[4] -= 2
                show rivchar rv_sad
                rv "What a...choice set of words, [pg]."
                show rivchar rv
                rv "Even if you've been roped in, you'll do your best, right?"
                rv "I would hope so."


    show rivchar rv
    show luvint li_happy2 at left
    li "Thanks, guys! I really appreciate it. Wow, I’m glad we’re doing something together before moving on. It’ll be fun!"

    jump after1
