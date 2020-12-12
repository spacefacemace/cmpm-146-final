# Global variables:
# player_meter
# rival_meter

label scene6:
    $ interact_with_li = False

    # Define boardwalk image
    scene sc_boardwalk

    show cf at right
    show li
    show rv at left

    # Check rival meter against player's
    if state[1] > state[0]:
        jump rival_higher
    else:
        jump player_higher

    label rival_higher:   # Local label

        rv "Since the max for the gondola is two people, how about I ride with [li], and [pg] could ride with [cf]?"

        li "That sounds like a good idea!"

        pg "{i}Wow, he’s really trying to get her. It’s not his first time doing this, huh? Or maybe I’m just a really bad rival.{/i}"

        # Background change to inside gondola
        scene inside_gondola

        hide rv
        hide li
        show cf at center

        "[rv] and [li] get on the gondola. You and [cf] get on the next one."

        cf "You've got some work ahead of you, [pg]."

        menu:
            "I'm not giving up yet.":

                $ state[2] = state[2]

            "It's definitely going to be difficult.":

                $ state[2] = state[2]

            "I'm not sure what's going to happen...":

                $ state[2] = state[2]

        cf "What are you planning to do?"

        menu:
            "Just try to get on [li]'s good side even more?":

                $ state[2] = state[2]

            "I'm still not sure.":

                $ state[2] = state[2]

            "Do you have any advice?":

                $ state[2] = state[2]


        cf "Hmm, well, I'd try to be as forward -- no, try to be {i}more{/i} forward than [rv]. Play his game, but do it better."

        menu:
            "How do I do that?":
                label cf_advice:
                    cf "Take charge, think of what [li] would like to hear. Don’t let him take up all of [li]’s time! You have to get her to see you in a good way, too. Then I think you have more of a chance."
                    pg "Since when did you get so good at giving advice?"
                    cf "Haha... I'm not too sure."

            "Sounds like a good idea":
                cf "Are you sure?"
                menu:
                    "How can I do that better?":
                        jump cf_advice
                    "Yeah, I'm sure."

        cf "I'm here for moral support, buddy. Look, we're already at the other side of the boardwalk -- why don't you try and put that advice to use?"
        jump funnel_cake_scene


    label player_higher:
        $ interact_with_li = True

        li "It looks like the gondola only let's two people ride at a time. And there's four of us, so..."

        menu:
            "You could go with me.":
                li "Oh... that sounds good!"
                jump li_pg_gondola

            "...":
                jump pg_indifferent

            "How should we split up?":
                jump pg_indifferent

        label pg_indifferent:
            li "How about...me and [pg] go together, and [rv] could go with [cf]?"
            cf "That's alright with me."
            rv "...Yeah, I guess."

        label li_pg_gondola:
            pg "{i}Is it just me or is someone glaring at me? Someone behind me?{/i}"

            # fade in

            # Change characters on scene to rival and cf, rival is looking daggers at pg
            hide li
            show rv annoyed

            # fade out

            pg "{i}Well that makes sense. Can’t waste this opportunity, though!{/i}"

            # Change background to inside of gondola
            scene inside_gondola

            show li
            hide rv
            hide cf

            li "I used to be scared of this as a kid because of how high up we are, but it’s not so bad now."

            menu:
                "Is it because I’m here, too?":
                    li "Um, maybe? Hahaha..."
                    li "It does help that I’m with someone I trust."
                    jump smalltalk


                "Yeah, I guess you get used to it.":
                    jump smalltalk

            default menuset = set()
            menu smalltalk:
                set menuset
                "How's planning the show going so far?":
                    li "It’s going great! We’re getting ready for rehearsals of the full show soon. Got to make sure everyone’s on track!"
                    pg "Are you on track?"
                    li "...Sort of? Haha. I’d like to think I am. I’m still not satisfied, but it’s getting there."
                    menu:
                        "I’m sure all this dedication is going to amount to something great.":
                            $ state[2] = state[2]
                        "You’re close, just a little bit left.":
                            $ state[2] = state[2]

                    li "Thanks! And your help is definitely making the process easier. You picked up the needed skills really quick, it’s kind of impressive!"
                    menu:
                        "Got to make sure I’m on track, too.":
                            $ state[2] = state[2]
                        "Just a part of helping out.":
                            $ state[2] = state[2]

                    li "I really appreciate it. I haven’t figured it out yet, but when it’s over, I’ll make sure to make you guys some sort of meal. It’s the least I can do!"

                "You said you baked something the other day?":
                    li "I did! I made an apple pie. The apartment smelled so good while it was baking..."
                    li "Apple pie is my favorite...but I didn’t think you were the type to like it, too."
                    menu:
                        "I bet it tasted as good as it smelled.":
                            $ state[2] = state[2]
                        "I wish I could have some.":
                            $ state[2] = state[2]

                    li "I have a bit of it left! I could give you a slice when we head back."
                    menu:
                        "I’ve loved it since I was a kid!":
                            $ state[2] = state[2]
                        "I’ve warmed up to it.":
                            $ state[2] = state[2]
                    li "That’s good! Well, the recipe I used is one that runs in the family, so there’s some secret ingredients in there. Still apple pie, nonetheless!"
                    menu:
                        "Secret ingredients?":
                            li "Yeah...obviously I can’t say them, but don’t worry, they’re edible, and it makes the flavors way better!"
                            pg "Fair enough."

                        "I can’t wait to try it.":
                            li "Yeah, I’m confident you’ll like it!"

                "What're you thinking about?":
                    li "I’m thinking about how nice the weather is. Kind of cliche, isn’t it? But it’s not too hot, not too cold. The sky is blue. What’s not to appreciate?"
                    li "What about you, [pg]?"
                    menu:
                        "I’m thinking about...you?":
                            li "Me? Hahaha...what about me?"
                            menu:
                                "Just about how lucky I was to ride this with you.":
                                    $ state[2] = state[2]
                                "Well you’re my riding buddy, so why wouldn’t I be?":
                                    $ state[2] = state[2]
                            li "I guess that’s a given...should I think about you too, then?"
                            li "Though the only thought to come to mind is that I’m glad we’re riding this together. Definitely better than being by myself!"

                        "I’m thinking about the weather, too.":
                            li "Fair enough. The weather affects all of us."

            li "Looks like we’re getting off soon."

    label funnel_cake_scene:

        # Switch background to main scene
        scene sc_boardwalk

        show cf at right
        show li
        show rv at left

        rv "I’m hungry. Should we eat something?"

        if not interact_with_li:
            pg "{i}Be more forward. Alright, let’s do this.{/i}"
        menu:
            "What about those funnel cakes?":
                li "Funnel cakes sound good right now! I haven’t had those in forever."

            "Same here.":
                rv "What about that funnel cake place?"
                li "I haven’t had those in forever -- let’s get those."

        # Switch background to funnel cake shop
        scene funnel_cake_shop

        show cf at right
        show li
        show rv at left

        menu:
            "I can pay for you, [li].":
                li "Are you sure about that, [pg]?"
                pg "Yeah, I don’t mind."
                rv "Then count me in, too."
                cf "[pg] is paying? Nice."
                pg "...Alright, alright."
                pg "{i}I ended up paying for more than what I expected but...it’s fine.{/i}"

            "Wonder what I should get…":
                rv "I can pay for you, [li]."
                li "Woah, really? ...Thanks!"
                pg "{i}...Missed opportunity there.{/i}"

        li "Ah, we’re next. I’m still deciding…"
        rv "Me too."
        cf "Same here…[pg], you order first. Don’t you have a regular?"
        pg "{i}I do. I guess that’s convenient.{/i}"
        pg "{i}Well, this trip to the Boardwalk wasn’t all too bad.{/i}"

        if interact_with_li:
            pg "{i}[cf] gave me some good advice.{/i}"
        else:
            pg "{i}I got to spend some time with just [li]{/i}"

        pg "{i}And after all of that...this could be some sort of reward.{/i}"
        pg "{i}Alright, can I get...{/i}"
        jump after6
