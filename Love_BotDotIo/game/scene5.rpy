# variables to add:
# points for li->pg, li->rv, rv->pg

# rn the answers to the player's options is
# set to the ideal answer (mostly for rv ai) + its weight
# probably take them out and put them in a set
# and make ai choose the best from there

label scene5:

    scene second_stage

    show cf at right
    show li at left
    show rv

    li "Here’s where we’ll be having our show! It’s enough space for us and we’ve already done some stuff here in the past, so we’re pretty well acquainted with that stage!"

    cf "Ahh, I remember performing here freshman year like it was just yesterday..."

    pg "Didn’t your group get delayed five minutes because you got so nervous you had to go to the bathroom?"

    rv "Hey, some people just get those nervous bowel movements."

    cf "Alright...I’m a changed person now. That won’t happen again -- hopefully."

    li "I remember that, too...well, [rv], [pg], what do you think? You’ll be okay?"

    menu:

        # best option, points for li->pg
        "Of course.":
            $ state[0] += 5
            # maybe some points for li->rv
            $ state[1] += 3
            rv "Same with me. I’m not the type to back down from a challenge."


        "It could take some getting used to...":
            # best option for rv, points for li->rv
            $ state[1] += 5
            rv "I’ll be fine, 100% -- I’m not the type to back down from a challenge."


        "Maybe?":
            # best option for rv, points for li->rv
            $ state[1] += 5
            rv "I’ll be fine, 100% -- I’m not the type to back down from a challenge."

    rv "I’ve got a high level of tolerance with all the sports I’ve played, believe me."

    # some points for li->rv for this one
    rv "Don’t worry, [li] -- with me around, this show will be like a well-oiled machine!"

    menu:

        # best option, points for li->pg
        "Don’t count me out, [rv]. I’ll do my best to help, too.":
            $ state[0] += 5
            # some points for li->rv
            $ state[1] += 3
            rv "Of course I won’t count you out."
            rv "...Well I guess I might have left you out there for a bit. Sorry."
            rv "I don’t doubt that you can put in the work."


        "I’m here too, [rv].":
            rv "...Well I guess I might have left you out there for a bit. Sorry."
            rv "I don’t doubt that you can put in the work."


        "It looks like [rv]’s got this whole show covered...":
            # maybe lower li->rv points for this one?
            $ state[1] -= 2
            rv "...Are backing out of this?"
            rv "No, you just made it seem like you got it, you know. I’m here too."
            rv "...Well I guess I might have left you out there for a bit. Sorry."
            rv "I don’t doubt that you can put in the work."

    li "The good news is that you don’t have to be in view of the audience -- if that worried you, at least."

    li "And also, there’s people to do all the lights and technical stage stuff, so that won’t be a problem, either! Perks of renting this space out."

    li "That really only leaves making sure everyone’s in their place, getting this in order, that sort of thing. Managing the show."

    li "Of course I’d do it, but..."

    li "Fortunately, you guys are here!"

    li "It’s mostly making sure the music is queued up and that people are ready to go on their cue, as well as making sure people are getting on quickly enough for the next performance."

    li "I think there’s about...20 performances in total?"

    li "Not too bad, right?"

    menu:

        # best option, points for li->pg
        "Not at all.":
            $ state[0] += 5
            # some points for li->rv
            $ state[1] += 2
            rv "We’d help if it were 100, right, [pg]?
            "I don’t doubt that you can put in the work."


        "20 is...":
            # best option for rv, points for li->rv
            $ state[1] += 5
            rv "Not bad at all. We’d help if it were 100, right, [pg]?
            "I don’t doubt that you can put in the work."


        "It’s a lot.":
            # best option for rv, points for li->rv
            $ state[1] += 5
            rv "Not bad at all. We’d help if it were 100, right, [pg]?
            "I don’t doubt that you can put in the work."

    cf "We’ll make sure the group listens to you guys, too. They can get...rowdy, but I’m sure you two can handle it."

    li "And of course, we won’t just throw you into the job! We’ll be doing rehearsals, easing you into the flow of the show."

    li "[pg], [rv]...thank you for helping. I really, really, really mean it."

    li "It’s making me so much more excited for the show knowing some of my friends are helping out!"

    "{i}...Friends. Right.{/i}"

    "{i}And judging from [rv]’s face, the word stings for him, too.{/i}"

    "{i}We’ll change it somehow.{/i}"

    jump after5
