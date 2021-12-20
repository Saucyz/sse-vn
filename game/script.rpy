# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Erikku", color="#ffffff")
define g = Character("Gigi", color="#ffdafe")
define jes = Character("Chadica", color="#ff94ff")
define c = Character("Christine", color="#9fc5e8")
define john = Character("Johnhanna", color="#ff1100")
define jer = Character("Jerrinu", color="#ff5200")
define d = Character("Diannya", color="#ffdd4f")
define mon = Character("Monster", color="#b76228")
define johan = Character("Johannason", color="#ff5733")
define o = Character("Professor Oliver", color="#daf7a6")
define p = Character("DJ Phimari", color="94ff33")
define mar = Character("Martin Onii-chan", color="#daf7a6")
define y = Character("Yvonne", color="#a933ff")
define ed = Character("Eddiena, Hobo Mask", color="#600000")

default johanFlag = False
default oFlag = False
default marFlag = False
default yFlag = False
default keepFlag = False
default giveTo = "Nobody"

# The game starts here.

label start:

    # show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "audio/rain.mp3"
    scene city_night_bg

    "Another stormy night in Rain City..."

    "A seemingly endless torrent bombards the streets, creating a melancholic melody with the cars that race by, and the dissonance of disgruntled pedestrians."

    "In the heart of the downpour permeates a foreboding aura, the rain itself turning black with the sky. As the sky grows darker with ghostly clouds, so too do the hearts and minds of the citizens."

    play music "audio/sailor_moon_op.mp3"
    "However"
    "Unbeknownst to the masses, there's a ray of light fighting to sweep away the darkness. A shining beacon to lead the masses to love, and righteousness!"

    "Their name: Sailor Senshi [e]!"

    show e_sailor
    e "In the name of justice and light, we vow to put a stop to your tirade monster of darkness!"
    hide e_sailor
    
    show mon
    mon "GWUAAAAAAAH!!!"
    hide mon

    show g_sailor
    g "We've finally cleaned up your shadow minions around the city!"
    hide g_sailor

    show c_sailor
    c "There's still so many here, and we're surrounded!"
    hide c_sailor
    
    show john_sailor
    john "And the exhaustion from running around all night's starting to catch up to my delicate, fragile body UwU."    
    hide john_sailor

    show jes_sailor
    jes "It's ok [john], we'll protect each other, always."
    hide jes_sailor

    show jer
    jer "[e]-chan, we have enemies on all fronts! Should we split up and divide and conquer? Or stick together?"
    hide jer

    menu:
        "Fight together!":
            jump choice_together

        "Let's split up!":
            jump choice_apart

    label choice_apart:
        show e_sailor
        e "Let's split up! Everyone spread out! I'll handle this monster myself!"
        play music "audio/trouble.mp3"
        "We split up to take on groups of shadowy enemies on our own, however even spread out, the monster was able to strike at all of us."
        "My attacks on the creature weren't effective enought to hold it's attention, and in the next moments, we were overwhelmed."
        hide e_sailor
        show mon
        mon "Bwahahaha you fools, as if anyone could defeat us!"
        hide mon
        "We were defeated soon after, we were stronger together..."

        show text "Bad End" with dissolve        
        $ renpy.pause(4.0)
        return

    label choice_together:

    show e_sailor
    e "We've been chasing you down all night, your control over the city ends tonight! All together!"
    hide e_sailor

    show jer
    jer "You can do it guardians! Believe in your selves, and in the friends who believe in you!"
    hide jer

    show d
    d "Ya f*** this little b**** a** downer b**** up!"
    hide d

    show g_sailor
    play sound "audio/water.mp3"
    g "Sailor [g]! Joyous river blast!"    
    hide g_sailor
    with hpunch

    # screen shake, river sound
    show jes_sailor
    play sound "audio/earth.mp3"
    jes "Sailor [jes]! Avalanche of justice!"
    hide jes_sailor
    with hpunch

    # screen shake, earthquake sound
    show c_sailor
    play sound "audio/wind.mp3"
    c "Sailor [c]! Winds of fervor!"
    hide c_sailor
    with hpunch

    # screen shake, wind sound
    show john_sailor
    play sound "audio/kamehameha.mp3"
    john "Sailor [john]! Burning passion, Kamehameha!"
    hide john_sailor
    with hpunch

    show e_sailor
    play sound "audio/love_cannon.mp3"
    e "Sailor [e]! Elemental love cannon!"
    hide e_sailor
    with hpunch

    show mon with hpunch
    mon "AAACK, so much friendship!"

    mon "But this pathetic amount of energy from the five of you, will never be enough to defeat me! I'll engulf the whole greater metro area in sorrow! You haven't seen the last of me!"

    hide mon with dissolve

    "Our combined attack began to break the monster apart, however a piece flew off into the sky before any of us could react. Though we had won the battle, the war against this evil had just begun."
    "I knew we needed a plan to free the city of this gloom for good. As the clouds began parting to the dawn, I turned to face my fellow guardians, and realized..."

    show e_sailor
    e "OH MY GOSH! I'M GOING TO BE LATE FOR CLASS!"
    hide e_sailor
    
    "After saying my goodbyes to my friends, I rushed home to get ready for morning classes. While fighting the forces of despair, during the day I was an ordinary student at BCU."
    
    scene my_room_bg with fade
    play music "audio/casual.mp3"

    "I snuck back through my window, and transformed back into my pjs"
    "What an exhausting night." 
    
    show d
    d "That was awesome, you were like the motha-f*****g avatar!"
    hide d
    show jer
    jer "I hope you have a good day at school [e]-mmmmgghf!"
    hide jer
    show d
    d "Hey watch it, oh fu-mmrgrgr!"
    hide d

    "I crammed [jer] and [d], my magical animal companions, into my school bag to their discomfort."
    "I cleaned myself up and grabbed a piece of toast for breakfast, while waving goodbye to my parents and step brother, tripping over myself as I made a mad dash for the bus."

    scene bus_bg with fade
    "The bus driver graciously waited for me to board. I thanked them and skirted my way to have a seat in the back."
    "This was a good time to study up."

    menu:
        "Japanese": 
            jump choice_japanese
        "Russian":             
            jump choice_russian
        "Spanish": 
            jump choice_spanish

    label choice_japanese:
        $ lang = "Japanese"
        "The inner weeb in me couldn't resist, as I delved through my bag past Jerrinu and Diannya to my latest manga."
        jump choice_2_done

    label choice_russian:
        $ lang = "Russian"
        "Счастливого Рождества!"
        jump choice_2_done

    label choice_spanish:
        $ lang = "Spanish"
        "Feliz Navidad!"
        jump choice_2_done

    label choice_2_done:
    ""
    show jer
    jer "[e]-chan, wake up, we're almost there!"
    hide jer
    show d
    d "Shhh not so loud dumb ass someone's gonna hear us."
    hide d

    "I'd fallen sleep, I bolted awake as the bus pulled up to campus, my book sliding off my face, and my bag wreathing around on my lap."
    "I sprinted off the platform towards the lecture hall, but between fixing up my hair, and arguing with my schoolbag I wasn't fully aware of what I was sprinting into."

    scene campus_bg with fade
    
    show e_neutral with vpunch
    e "Aiya!"
    hide e_neutral

    show johan
    johan "[e]-chan, are you ok? Late to class again eh?"

    "I had crashed into the arms of my childhood friend, who also was attending BCU. Even though I fell with full force, full bag and all, his strong, toned arms gently caught me like a human pillow."

    e "I'm alright, oh my gosh, I'm so sorry, are you ok?!"

    johan "I'm fine haha, you were really motoring, you seem busy, don't let me slow you down."

    menu:
        "Stay and catch up for a minute": 
            jump choice_catchup
        "Gotta hurry to class!":             
            jump choice_hurrytoclass

    label choice_catchup:
        e "It's alright, I want to catch up for a minute, what were you up to this morning?"

        johan "I just finished my first lecture, I think we're taking the same elective, if you need any help my doors always open. If you ever need anything else, day or night, I'll be a call away."
        johan "But we should both get going, I'll catch up with you later ok?"
        e "Thanks I'd love to catch up more, see you later!"
        $ johanFlag = True
        jump choice_hurrytoclass

    label choice_hurrytoclass:
    hide johan
    scene lecture_bg with fade

    "I sprinted to my lecture, stealing a seat at the back without a minute to spare."
    "Though I was eager to get to class on time in part due to my interest in the subject, and my natural need to be punctual, what really made the lecture interesting, was the professor."
    "He was so young for a professor at this university, an unrivalled prodigy in his field with a passion for teaching."
    "So engaging it was hypnotic, the way he commanded the room with his passion and charisma."

    show o
    o "Alright class that's all for today, the exam is next week, please feel free to stop by my office anytime if you have any questions."
    hide o
    "I could attend office hours, though I already studied a bit of [lang]"

    menu:
        "Attend office hours":
            jump choice_officehours
        "Head to lunch":
            jump choice_lunch

    label choice_officehours:
        "On occasion I would sheepishly walk by the professor's office, nervously saying hello in passing or making small talk from the doorway."
        "Today I decided to visit office hours, and have a real conversation"
        e "Uhm, hello professor, I was wondering if you had a moment to answer some questions?"
        show o
        o "Of course, anything for my best student. Come have a seat, what can I help you with?"
        "We began discussing the intricacies of the language and culture"
        "He regaled me with stories of his travels and the extradinary people and places all over the world"
        o "Ah how the time flies, apologies for running you ear off, I need to leave to my next lecture, but do come by my office anytime, my door is always open"
        "I snapped out of my stupor, thanked him and scurried out of his office to meet the gang for lunch."
        $ oFlag = True
        jump choice_lunch
         
    label choice_lunch:
    hide o
    scene lunch_bg with fade
    play music "audio/lunch.mp3"

    "We all decided to meet for lunch at the bubble tea cafe on campus for lunch."
        
    show jer
    jer "Your [lang] is really improving Erikku-chan, I'm so proud of you!"
    hide jer

    show d
    d "What're those freaky ball things you're drinkin'?"
    hide d

    show c_neutral
    c "Here [d], you can try some of mine, it's a boba, or bubble tea."
    hide c_neutral

    show d
    d "Holy f*** this is some good a** s***"
    hide d

    show c_neutral
    c "You need to watch your little tongue or you're not getting anymore."
    hide c_neutral

    show jes_neutral
    jes "We should discuss the beast that escaped, and formulate our next plan of attack."
    hide jes_neutral

    show john_neutral
    john "Oh lighten up [jes]! We beat up that big ol' baddy once and we'll do it again >w<!"
    hide john_neutral

    show g_neutral
    g "We can celebrate our victory at the rave tonight! Shots!"
    hide g_neutral

    "There was a huge rave going on tonight, everyone in town would be showing up to see [p]."
    "After such a gloomy week of monsters and rain, this rave should re-energize the whole city!"

    scene front_door_bg with fade
    play music "audio/casual.mp3"
    "After lunch and my afternoon classes, I headed home to prep for the rave"
    "On my way inside, my brother was waiting to confront me."

    e "Onii-chan... Is everything ok?"
    "My step brother seemed to be suspicious of me recently. When we first met he was so indifferent to me I thought I was invisible at home."
    "After an incident at school when he caught a class bully picking up me, he stood up for me, and ever since has been protective of me."

    show mar
    mar "Did you sneak out last night?"
    "Blunt, to the point, that was Onii-chan for ya."

    menu:
        "Try to explain myself":
            jump choice_explain
        "Avoid eye contact and head for my room":
            jump choice_myroom

    label choice_explain:
        e "Hehe I uhm..."
        "Whenever I was nervous I would just giggle and dart my eyes around the room, a clear tell."
        "[mar] had a steely stare, as if he already knew I'd been sneaking out transforming using magic and fighting monsters."
        "Though he may seem cold on the outside, he always had a calming collected presence that reassured me at times, and intimidated me at others."

        mar "Just don't get into any trouble, I don't want you to get hurt."
        mar "I know we're only step siblings, and I used to give you a hard time, but we're family."
        mar "If anyone ever gives you any trouble, you come to me ok, I'll take care of it."
        e "Thanks Onii-chan, I'll always have your back too!"
        $ marFlag = True
        jump choice_myroom

    label choice_myroom:
    hide mar
    scene my_room_bg with fade
    "Stepping back into my room, let out [d] and [jer] from my bag to help me get ready for the rave."
    "As excited as I was, I couldn't help be a bit on edge recalling the monster's promise..."

    scene stage_bg with fade
    play music "audio/rave.mp3"

    show p
    p "Thanks for coming everyone, I love you all!"
    p "Hands up, I want you to all go crazy!"
    p "Ready, let's, go!"
    hide p

    scene rave_bg with fade
    "The rave was in the largest stadium around. A sea of ravers crashed against the enormous stage in the centre of the field."
    "All with the purpose of singing, dancing, and spreading love."

    "I danced my way through, at some point I knew I should find my friends, but the push and pull of the music drew me into the centre."
    "A crowd began forming, a dancer was pushing the limits of human physical ability, becoming one with the bass."
    "I became one of the many mesmerized bystanders, screaming and cheering at the dazzling moves this raver demonstrated."
    show y
    "This raver captivated me, at first metaphorically, and then literally as they grabbed my hand and tried pulled me in to their wicked dance."

    menu:
        "Dance with them":
            jump choice_dance
        "I should find my friends":
            jump choice_findfriends

    label choice_dance:
        "I was a leaf caught in the wind, helpless to the ebb and flow of the music and this force of nature dancing with me."
        y "Amazing moves, I'm [y], you're like, so good, wooooow"
        e "Oh my gosh no you're the amazing one, I'm [e], I'm so impressed by you!"
        y "Aaaaawe, thanks, I'm gonna take a break before I have a heart attack, I hope we can dance together again soon!"
        e "O M G I'd love to, thanks!"
        $ yFlag = True
        jump choice_findfriends

    label choice_findfriends:
    hide y
    show g_neutral
    g "Found you [e]-chan! Oh your kandi is so cute! Who're you going to trade with first?"
    hide g_neutral
    with fade
    "I had made a quite a few bracelets, and was very proud of how they turned out. Everyone I knew was here, all of my precious friends and colleagues."
    "But I had one kandi that was particularly special, for a particularly special person..."

    menu:
        "Give the bracelet to..."
        "[johan]" if johanFlag :
            $ giveTo = johan
            jump choice_giveTo
        "[o]" if oFlag == True :
            $ giveTo = o
            jump choice_giveTo
        "[mar]" if marFlag == True :
            $ giveTo = mar
            jump choice_giveTo
        "[y]" if yFlag == True :
            $ giveTo = y
            jump choice_giveTo
        "Keep it for now" :
            $ giveTo = mon
            jump choice_keep

    label choice_giveTo:
        "I decided that I'd give it to [giveTo]"
        "I blushed and mumbled incoherently to [g], far too embarassed to confess aloud."
        jump raveDisturbance
    label choice_keep:
        "I'll hang onto it for now, I was in no rush."
        $ keepFlag = True
        jump raveDisturbance

    label raveDisturbance:
    stop music
    play sound "audio/explosion.mp3"
    "At the height of the beat drop, an explosion cut music, and a dark cloud began enveloping the stage and [p]!"
    "The lights and music of the rave were slowly encroached by smoky tendrils, and shadow minions appeared throughout the venue."
    play music "audio/trouble.mp3"
    "The shadows drained the life from the citizens around, leaving mounds of unconscious party goers."
    "Gigi and I sprinted for backstage against the waves of fleeing patrons, with the rest of the Guardians following close behind."
    "Once we reached backstage, it was time to transform! Imbuing ourselves with the power love we readied ourselves to put an end to this party pooper."

    scene stage_bg with fade
    show e_sailor
    play music "audio/battle.mp3"
    e "Lunar gem energy dress up!"
    hide e_sailor

    show g_sailor
    g "[e]-chan! We've got your back!"
    hide g_sailor

    show jes_gun
    play sound "audio/reload.mp3"
    jes "This time we're going to put you away for good you beast!"
    hide jes_gun

    show c_sailor
    c "Uh oh, it looks like it's way bigger this time, and we don't have [jer] and [d] for support! Wait [jes], do you have a gu-"
    hide c_sailor

    show john_sailor
    john "[john]-chan was just starting to get in the groove too! Now I'm mad !>_<!"
    hide john_sailor

    show mon
    mon "Bwahahaha, I've returned to feast on your spirits!"
    mon "With this much food gathered here there's no way you could defeat me!"

    "The monster roared, a black mist tsunami washing over the rave stage."
    "We used our magic to shield ourselves and as many civilians as we could, but the sheer weight of the dread mist scattered us across the stage."
    "The monster inhaled, preparing another attack."
    "I began preparing another shield for myself, when I spotted [p] in some nearby rubble, she must have taken the brunt for the initial attack, and could be in bad shape."

    menu:
        "Shield yourself" :
            jump choice_shieldEnd
        "Protect [p]" :
            jump choice_protect

    label choice_shieldEnd:
        "I braced myself for the next attack. I was barely standing from the first one, I would need to conserve my strength."
        play music "audio/trouble"
        "We tried to regroup, struggling through the night to keep the hoards of shadow monsters and tendrils at bay."
        "Mustering up the last of our strength, we attempted our combined attack once again, but to no avail."
        "The monster was ready, absorbing our final blast, and exploding into dark mist, blanketing the entire city."
        "The raving music was a distant memory quickly replaced by mad laughter as I blacked out..."

        show text "Bad End" with dissolve
        $ renpy.pause(4.0)
        return

    label choice_protect:
    hide mon
    "[p] was in danger! I dove to protect her from the blast, burning pain flaying my back as I cradled her"

    show p
    p "You saved me, thank you! Wait are you ok?"
    p "One minute we were all having the times of our live, next we're exploding!"
    
    "I had an idea, [p] was right!"

    e "[p], are you able start the music again?"
    e "This is a creature of immense negativity, but if we inspire everyone with music and love, we can do anything!"

    p "Truuu, you right!"
    hide p

    "I protected [p] from the monsters as she made her way back onto the podium."
    play music "audio/rave2.mp3"
    "Music, and light blared across the entire city. The monsters taken off guard as their victims rose to their feet in defiance."
    "As the beat built up, so did the hearts and spirits of the city, as the rave began anew."

    show e_sailor
    e "Everyone, please, lend me your energy!"
    "The crowds hands jumped to the sky, light funneled back from the crowd towards the stage, converging on me."
    e "You see monster, the people and feelings you came to feed on will be your undoing!"
    e "In the name of the moon, I will punish you!"

    "I let loose of the love infused energy on the bass drop, the sky turned to day in a flash, and the monsters were eradicated."
    "All except, a tiny blob in the corner of the stage"
    hide e_sailor

    show mon_small
    mon "I never knew so much energy could be generated like that..."
    e "Love can empower us all, even you..."
    if keepFlag : 
        menu : 
            "Give kandi bracelet to monster" :
                "I handed my special kandi to the droplet, and spotted an even smaller droplet run down their cheek as they gently absorbed the bracelet"
                mon "Thank you..."                
                hide mon_small with dissolve
                jump choice_end
            "Keep kandi bracelet" :
                jump choice_fade

    label choice_fade:
    hide mon_small with dissolve
    "The monster faded away, in a final shimmer of light. The sun began to rise bathing the city in cleansing light."
    "My friends and I rushed backstage to transform back and avoid discovery."
    "We managed to sneak through fallen structures back into the crowd as if we'd never left"
    "Even though the monster was gone, and the night was over, the party had just begun!"

    if giveTo != "Nobody" :
        "The relief I felt quickly retreated, as I noticed [giveTo] running towards me."
        if giveTo == johan :
            show johan
        if giveTo == o :
            show o
        if giveTo == mar :
            show mar
        if giveTo == y :
            show y
        giveTo "Are you alright [e]? I've been looking all over for you, are you hurt, should I give you first aid or something?"
        hide johan
        hide o
        hide mar
        hide y

        e "Thank you [giveTo], actually there's something I want to give you..."
        jump choice_end

    label choice_end:
    scene sailor_moon_bg with fade
    play music "audio/sailor_moon_op.mp3"

    "Whether it's love, school, or fighting the forces of evil, you can count on them to give it their all, the guardians, and..."

    show e_sailor
    "Sailor Senshi, [e]!"
    ""
    hide e_sailor
    scene rave_bg with fade

    show ed
    ed "Great work everyone. We did it."
    hide ed

    show c_neutral
    c "... Didn't you just get here?"
    hide c_neutral

    show g_neutral
    g "... Aren't you that homeless person who lives in QE park?"
    hide g_neutral

    show ed
    ed "My job here is done."
    hide ed with moveoutright

    show e_neutral
    e "But you didn't do anything"
    hide e_neutral
    
    scene sailor_moon_bg with fade

    show text "{color=#000000}The End{/color}" with dissolve

    $ renpy.pause(2.0)

    show text "{color=#000000}Poorly Written by\n\nRichard Leong{/color}"
    $ renpy.pause(2.0)

    show text "{color=#000000}Piccrew Visuals by\n\nGigi Li{/color}"

    $ renpy.pause(2.0)

    show text "{color=#000000}Shoutouts to various YouTube and Anime Image sites that I couldn't find all the credits for...{/color}"

    $ renpy.pause(2.0)

    show text "{color=#000000}Happy holidays [e]!{/color}"

    $ renpy.pause(4.0)

    # This ends the game.
    return