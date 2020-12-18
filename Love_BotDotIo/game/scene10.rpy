# gonna assume there's going to be variables where there's booleans
# for player wins, player loses, rival->player?

label scene10:

    image quarry_amphitheatre = Frame("quarry_amphitheatre.jpg")

    scene quarry_amphitheatre

    show cfimg cf_happy at right
    show luvint li_joy at left
    show rivchar rv

    cf "We did it, [pg] -- we’ve finally graduated!"

    li "About time, too! We’ve all made it through college!"

    rv "Yeah, about that -- why are you guys last to graduate? Making us wait like this..."

    show cfimg cf at right

    menu:
        "We can’t really pick when we graduate...":
            cf "That’s true. Well, after all that time, we finally finished a big chapter of our lives. Thanks for coming, you guys. I appreciate it, and I’m sure [pg] does, too."

        "At least we made it through.":
            cf "That’s true. Well, after all that time, we finally finished a big chapter of our lives. Thanks for coming, you guys. I appreciate it, and I’m sure [pg] does, too."

        "We’re finally at the end, though.":
            cf "That’s true. Well, after all that time, we finally finished a big chapter of our lives. Thanks for coming, you guys. I appreciate it, and I’m sure [pg] does, too."

    rv "You went to ours. Wouldn’t be right if we didn’t go to yours."

    li "I’m glad we’re able to celebrate together! To think that we’re here like this...I’m grateful that I had you guys through the years. I wouldn’t have it any other way."

    cf "Don’t get so sappy, [li]."

    show luvint li_happyblush at left
    li "I can’t help it, though -- doesn’t everyone get sappy with this sort of thing?"

    show rivchar rv_smiling

    menu:

        "Yeah, it can’t be helped.":
            rv "I’m not good at that sort of stuff, but...today’s pretty special, so I’ll give you a pass, [li]."

        "It’s a once-in-a-lifetime thing, so it makes sense.":
            rv "I’m not good at that sort of stuff, but...today’s pretty special, so I’ll give you a pass, [li]."

        "I guess it’s fine?":
            rv "I’m not good at that sort of stuff, but...today’s pretty special, so I’ll give you a pass, [li]."

    cf "...Alright. Though we’ll still be neighbors for quite a bit, [li]. Our time at the apartment doesn’t end until August."

    show luvint li_joy at left
    li "Haha, I know!"

    rv "Right, mine is around that time, too. We’ll still be seeing each other quite a bit, huh?"

    li "Hmm, should I save the sappiness for when we all move out, then?"

    show cfimg cf_happy at right
    cf "Maybe. If it makes you feel better, you can be extra sappy then. I’ll allow it."

    show rivchar rv
    rv "...So what now?"

    cf "Hm. I know my family’s probably looking for me, so I should probably go to them."

    li "Oh, right, we shouldn’t keep you from them!"

    cf "Yep. See you guys in a bit."

    hide cfimg cf_happy at right with easeoutright

    if False == True:

        li "I have some other friends to go and congratulate, too. Let’s meet up back here, yeah?"

        rv "Sounds good."

        hide luvint li_joy at left with easeoutleft

        rv "Then it’s just you and me, [pg]."

        rv "..."

        show rivchar rv_embarassed
        rv "I don’t know how else to say this. I need to talk to you -- in private."

        "...Huh?"

        jump rv_pg_route


    else:

        rv "I should also go find some of my other friends and congratulate them too. You don’t mind, right?"

        li "Not at all!"

        hide rivchar rv with easeoutright
        hide luvint li_joy at left
        show luvint li_joy

        li "Just you and me, [pg]. Actually, that was perfect timing...if you have time, can I talk to you for bit? In private?"

        "Sure."

        if LoveInterest.getResponse(rv_state) < LoveInterest.getResponse(pg_state):
            jump li_pg_route
        else:
            jump li_rv_route

# branch if rival->pg route is true
label rv_pg_route:

    rv "You’re kind of annoying, you know?"

    menu:

        "Huh?":
            rv "I started this year hoping to get with [li], but..."

        "What?":
            rv "I started this year hoping to get with [li], but..."

    rv "For some reason, my plans have changed."

    rv "Have yours changed, too?"

    menu:

        "I’m not sure what you’re talking about.":
            rv "Hmph."

        "Maybe?":
            rv "Hmph."

    rv "I can’t tell if you’re playing or you’re actually that oblivious..."

    rv "Ignorance is bliss, I guess."

    rv "You know, I never thought I’d say this sort of thing. But, [pg]..."

    rv "I...I like you."

    rv "There, I said it."

    rv "After all this time, I ended up falling in love with my rival."

    menu:

        "I’m...":
            rv "You’re what? Speechless?"

    rv "Believe me, me too."

    rv "But...I can’t help it."

    rv "So...what about you?"

    menu:

        "I’m going to need some time to think about it...":
            rv "Fair enough. I guess I kinda just sprung it on you..."

    rv "But I want to know eventually."

    show rivchar rv_smiling
    rv "They’re coming back. Let’s meet up later, yeah?"

    show rivchar rv_smirking
    rv "Don’t think I’m letting you go easily."

    jump after10

# branch if player won
label li_pg_route:

    show luvint li_blush
    li "Umm...how should I start?"

    li "I’m a little nervous, haha..."

    li "I practiced this in my head so many times, but now that I’m doing it, my head is blanking."

    li "Should I just say it straight up? Maybe it’ll be easier than trying to figure out what I had planned before."

    show luvint li_happy2
    li "[pg], I think you’re a really cool person. You’re great! I don’t think I’ve ever seen you in any sort of bad light...especially during this last leg of our school year. You were such a great help during the show! And just a great shoulder to lean on. Really, there’s a lot of good things about you..."

    li "It led to a lot of things, and basically...what I’m trying to say is that after all that time..."

    show luvint li_happyblush
    li "I’m in love with you, [pg]."

    li "I think of you in that way."

    show luvint li_tsundere
    li "...Yeah. Yeah, that’s it. I like you, [pg]."

    menu:

        "I like you, too.":
            show luvint li_blush
            li "Woah, woah, woah -- am I hearing that right? You’re not playing with me?!"

        "I’ve had a crush on you since forever.":
            show luvint li_blush
            li "Woah, woah, woah -- am I hearing that right? You’re not playing with me?!"

    menu:

        "Nope.":
            show luvint li_happy2
            li "That’s...wow, this ended up going really well! I didn’t expect this at all!"

    li "...Didn’t expect this at all..."

    li "Um, then...what are we, then?"

    menu:

        "Dating?":
            show luvint li_happyblush
            li "...Seriously?!"

        "Together?":
            show luvint li_happyblush
            li "...Seriously?!"

    show luvint li_joy
    li "Wow, then I’m glad we have all summer to still be around. It’ll be kinda fun? Hahaha."

    li "We could go on dates, do couple stuff together, all that jazz! I mean, if that’s okay with you -- I’m just excited about the thought of it, that’s all."

    li "We could get a little closer..."

    show luvint li_happyblush
    li "Is that weird? Haha."

    show luvint li_happy2
    li "This is the best thing that’s ever happened to me! [pg]...I’m seriously so happy right now. You’ve made me really happy."

    li "Ah, they’re coming back right now -- let’s tell them the good news!"

    jump after10

# branch if rival won
label li_rv_route:

    show luvint li_blush
    li "Umm...how should I start?"

    li "I’m a little nervous, haha..."

    li "I practiced this in my head so many times, but now that I’m doing it, my head is blanking."

    li "Should I just say it straight up? Maybe it’ll be easier than trying to figure out what I had planned before."

    show luvint li_happy2
    li "I wanted to tell you that...later on, I’m going to tell [rv] that I like him."

    menu:

        "...Woah.":
            li "Seriously! I didn’t think he’d be my type, but...it just...kinda happened, haha."

        "Seriously?":
            li "Seriously! I didn’t think he’d be my type, but...it just...kinda happened, haha."

    show luvint li_happyblush
    li "He’s just...he’s something else. I can’t tell what it is, but...I like it. I like being around him. I just can’t help it."

    li "I know it might be weird telling you this first, but...it’s because I have a question to ask, too. I hope you don’t mind."

    li "It’s simple, really..."

    li "[pg]...do you think he’ll like me back?"

    menu:

        "I think he will.":
            show luvint li_joy
            li "Ah, that’s a relief..."

        "I don’t see why not.":
            show luvint li_joy
            li "Ah, that’s a relief..."

    li "Wish me luck later, okay?"

    menu:

        "For sure.":
            show luvint li_happy2
            li "Thank you, [pg]. You’re a really good friend."

    li "Ah, they’re coming back now. I can’t wait for later!"

    jump after10
