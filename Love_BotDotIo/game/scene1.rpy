


label scene1:

    image that_one_food_truck = Frame("that_one_food_truck.png")
    image picnic_tables = Frame("picnic_tables.jpg")

    scene that_one_food_truck

    show cf

    cf "There you are, [pg]! I already got the sandwich you like to get. Let’s go meet them!"

    "{i}Wow, [cf] got my order correct. Not that I’m surprised about that. We’ve known each other since we were kids -- nah, since the womb.{/i}"

    "{i}...Which is why I’m tagging along. You’d think that since we’re neighbors we’d get sick of seeing each other and not meet up on campus, but here we are.{/i}"

    "{i}This friend group is all [cf]’s doing. It’s alright, though, since that means that --{/i}"


    scene picnic_tables

    show cf at right
    show li at left
    show rv

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

        "I forgot we were meeting up.":

            $ pg_state[2] = pg_state[2] - 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,-2,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"

            rv "Should I move for someone that forgot about meeting their friends?"

            rv "..."

            rv "Well since you’re here, I might as well."



        "I got distracted admiring all the scenery on the way here.":

            $ pg_state[3] = pg_state[3] = 3
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,3,0,0,0,0,0,0]))
            "{i}[response]{/i}"

            rv "That’s incredibly...cheesy."

            li "I totally understand! I’d do the same thing."


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

        "Yeah, there’s really no point.":

            $ pg_state[1] = pg_state[1] - 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,-2,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"

            li "Hmm, then I guess living in the present is some sort of bliss."

            rv "Besides, you might be missing something around you right now."

            pg "That’s too on the nose."

        "I haven’t really thought about that.":

            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"

    cf "Well, no matter what, [li], you’ve got to think somewhat ahead. How’s the planning for the last show?"

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

            rv "That’s a good idea. I’m a big, strong guy -- I could help out some heavy-lifting."

            pg "Just that?"

            rv "Well...anything else, too."

        "We could help -- I was going to go anyway to watch it, but why not support you guys behind-the-scenes as well?":

            $ pg_state[4] = pg_state[4] + 4
            $ pg_state[3] = pg_state[3] + 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,2,4,0,0,0,0,0]))
            "{i}[response]{/i}"

            rv "Um...yeah, same with me. That’s a good idea. I’m a big, strong guy -- I could help out some heavy-lifting."

            pg "Just that?"

            rv "Well...anything else, too."

        "...":

            rv "Well maybe we could do something to help out? Since it’s so important to you, I’m sure we could take some time out of our lives to do so -- right, [pg]?"

            menu:
                "Yeah, I’m more than happy to help.":

                    $ pg_state[2] = pg_state[2] + 1
                    $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,1,0,0,0,0,0,0,0]))
                    "{i}[response]{/i}"

                "I guess I could help out.":

                    $ pg_state[2] = pg_state[2]



        "That seems like a lot.":

            $ pg_state[1] = pg_state[1] + 1

            rv "Well maybe we could do something to help out? Since it’s so important to you, I’m sure we could take some time out of our lives to do so -- right, [pg]?"

            menu:
                "Yeah, I’m more than happy to help.":

                    $ pg_state[2] = pg_state[2] + 1
                    $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,1,1,0,0,0,0,0,0,0]))
                    "{i}[response]{/i}"

                "I guess I could help out.":

                    $ pg_state[2] = pg_state[2]



    li "Are you sure about this?"

    menu:
        "Absolutely! Anything to make the show run smoothly.":

            $ pg_state[3] = pg_state[3] + 2
            $ pg_state[4] = pg_state[4] + 3
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,2,3,0,0,0,0,0]))
            "{i}[response]{/i}"

        "Well since I got roped into it, I have no choice now.":

            $ pg_state[4] = pg_state[4] - 2
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,0,0,0,-2,0,0,0,0,0]))
            "{i}[response]{/i}"



    rv "Yup, I'm sure."

    li "Thanks, guys! I really appreciate it. Wow, I’m glad we’re doing something together before moving on. It’ll be fun!"

    jump after1
