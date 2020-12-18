# need to add:
# pg_state and rival_state, points for that
# ai choices
label scene2:

    image parking_lot = Frame("parking_lot.jpg")

    scene parking_lot

    show luvint li_sad

    li "Hmmmm...Maybe...No no no..."

    menu:

        "Hey there.":
            show luvint li_joy
            li "Oh. Hey. Good timing."

        "Is anything troubling you?": # best option for li->pg
            $ pg_state[1] = pg_state[1] + 1
            $ response = LoveInterest.textResponse(LoveInterest.getResponse([0,1,0,0,0,0,0,0,0,0]))
            "{i}[response]{/i}"
            show luvint li_tired
            li "It's nothing much. A bit silly, really."

    pg "What’s up?"

    show luvint li_tired
    li "I’m just not sure about what song to use for my segment of the dance show. I mean, I do have ideas in my head, but I just can’t decide on just one."

    pg "Can you list them out for me? Maybe I can help."

    li "Oh sure. So I’m torn between two choices. On one hand, there’s ‘Can’t Stop Me’. Since it’s our last performance, it would be nice to end things with a bang. But on the other hand there’s ‘Always with You’, which is more emotional and heartfelt. I’ve been thinking about this for days. Do you have any ideas?"

    pg "Well-."

    show rivchar rv at right

    rv "Hey. What’s going on over here?"

    pg "Gah!"

    show luvint li_happy2
    li "Oh hi, [rv]!"

    pg "Where did you come from?"

    rv "Chill. I just saw you two as I was driving through. So I decided to stop by and say hi."

    menu:

        "Could you have done so without sneaking up on us?":
            show rivchar rv_sad at right
            rv "Geez. Sorry. I’ll be more careful next time."

        "Cool. Maybe you could help us with something.":
            rv "Um, sure. What do you need my help with?"

    show luvint li_joy
    show rivchar rv at right
    li "Oh right. [pg] and I were just talking about which song I should use for the dance."

    rv "I’m listening."

    rv "I see. So you need help deciding on a song."

    li "Yeah. That’s about it."

    rv "Gotcha."

    pg "So what do we do now?"

    rv "Well, you were here first. How about you take the first pick?"

    menu:

        "Can’t Stop Me.":
            pg "Let’s end it all with a bang. No way to go out like a party."
            rv "Hmm. You make a good point, but I disagree. ‘Always with You’ is the better choice. Since this is the dance group’s last performance, it would make sense for it to feature a heartfelt goodbye."


        "Always with You.":
            pg "A heartfelt goodbye should be more than enough to resonate with the audience. Let’s make this last performance something everyone will continue to carry in their hearts."
            rv "Hmm. You make a good point, but I disagree. I’ll stand by ‘Can’t Stop Me’. An emotional goodbye is nice, but what would stick with the audience more is a performance where the performers go all out."

    menu:

        "On second thought...":
            pg "After listening to [rv]’s reasoning, I’m inclined to agree."
            rv "Wait...You are?"

        "Double down.":
            pg "Well, I still believe my choice is better. I won’t change my mind."
            rv "Suit yourself, then."

    pg "So what do you think, [li]?"

    show luvint li_serious
    li "Umm...I still don’t know. You both made very good points."

    rv "Well you have to decide on one."

    show luvint li_tired
    li "I know, but I think I still need time to think it over. Thanks anyway. You both have given me a lot to think about."

    pg "So who won?"

    rv "Guess we’ll just have to wait and see."

    jump after2
