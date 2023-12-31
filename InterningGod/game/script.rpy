#diable close project confirmation
init python:
    config.quit_action = None

#character definition
define i = Character("Intern God")
define h = Character("Hana")
define gp = Character("Grandpa")
define gm = Character("Grandma")
define gl = Character("Guoliang")
define s = Character("Spirit")


#image resize
<<<<<<< Updated upstream
image bg temple = im.Scale("temple.png", 1920, 1080)
image bg grassy field = im.Scale("House in front of a tea field.png", 1920, 1080)
image bg school = im.Scale("elementary school.png", 1920, 1080)
image bg market = im.Scale("market.png", 1920, 1080)
image bg street = im.Scale("town.png", 1920, 1080)
image bg river = im.Scale("riverside.png", 1920, 1080)
image bg grave = im.Scale("grave.png", 1920, 1080)
image bg cat = im.Scale("cat.jpg", 1920, 1080)
=======

image bg grassy field = "grass_field1.png"
image bg school = "school1.png"
image bg market = "market1.png"
image bg street = "town_street1.png"
image bg river = "river1.png"
image bg cat = "cat1.png"

>>>>>>> Stashed changes

#intern
image i ancient = im.Scale("intern-ancient.png", 225 * 1.6 , 280 * 1.6 )
image i mad = im.Scale("InGod_Angery.png",309 , 492 )
image i happy = im.Scale("InGod_Happy.png",307 , 506)
image i sad = im.Scale("InGod_Sad.png",306 , 496 )
image i neutral = im.Scale("InGod_Neutral.png", 306 , 497 )

#child
image gl = im.Scale("child_Neutral.avif", 169 , 392 )
image gl happy = im.Scale("child_happy.avif", 167 , 398 )
image gl sad = im.Scale("child_sad.avif", 169 , 393 )
image gl mad = im.Scale("child_angery.avif", 166 , 389 )

#spirit
image s neutral = im.Scale("child_Neutral.avif", 169 , 392 )
image s happy = im.Scale("child_happy.avif", 167 , 398 )
image s sad = im.Scale("child_sad.avif", 169 , 393 )
#image s mad = im.Scale("child_angery.avif", 166 , 389 )

#hana
<<<<<<< Updated upstream
image h happy = im.Scale("child_happy.avif", 200 , 280 )
image h neutral = im.Scale("child_Neutral.avif", 200 , 280 )
image h sad = im.Scale("child_sad.avif", 200 , 280 )
image h mad = im.Scale("child_angery.avif", 200 , 280 )
=======
image h happy = im.Scale("hana_happy.png", 277 , 453 )
image h neutral = im.Scale("hana_Neutral.png", 290 , 463 )
image h sad = im.Scale("hana_sad.png", 276 , 452 )
image h mad = im.Scale("hana_angery.png", 200 , 280 )
>>>>>>> Stashed changes


#image gl mad = im.Scale("child-mad.png", 200 , 280 )
image gp = im.Scale("grandpa-normal.png", 200 * 1.6 , 280 * 1.6 )
image gm = im.Scale("granny-normal.png", 200 * 1.6 , 280 *1.6 )






#character art position definition
define middle = Position (yalign = 0.7)
define left = Position (xalign = 0.15, yalign = 0.7)
define right = Position (xalign = 0.85, yalign = 0.7)
define lower_middle = Position (yalign = 0.75)
define lower_left = Position (xalign = 0.15, yalign = 0.75)
define lower_right = Position (xalign = 0.85, yalign = 0.75)
define upper_right = Position (xalign = 0.95, yalign = 0.05)

#time images
define currentTime = 6
image clockFace = "clockFace.svg"
image clockHands = ConditionSwitch(
    "currentTime == 1", "1.svg",
    "currentTime == 2", "2.svg",
    "currentTime == 3", "3.svg",
    "currentTime == 4", "4.svg",
    "currentTime == 5", "5.svg",
    "currentTime == 6", "6.svg",
    "currentTime == 7", "7.svg",
    "currentTime == 8", "8.svg",
    "currentTime == 9", "9.svg",
    "currentTime == 10", "10.svg",
    "currentTime == 11", "11.svg",
    "currentTime == 12", "12.svg"
)

label updateClock:
    $ currentTime += 1
    if currentTime == 13:
        $ currentTime = 1
    return

label showClock:
    show clockFace at upper_right
    show clockHands at upper_right
    return

label start:
    
    scene bg temple
    i "Day XXX. Only XXX more days until the town and its people meet their end. "
    show i ancient at middle
    i "I truly wish I could save them from this calamity, but even gods cannot intervene with the fate of mortals."
    i "*Sigh* The least I can do is grant them one final moment of happiness. Now, whose prayers should I answer today?"
    scene black with fade

menu:
    "Help out an old couple":
        jump Guoliang_arc
    "arc 2":
        jump Hana_arc

label Guoliang_arc:

    scene bg grassy field
    call showClock
    "Taking on my human form, I made my way to a tea farm tended by an old couple. The couple is currently hard at work harvesting tea leaves."
    show i neutral at middle
    "These two have been praying every single day for the well-being of their grandson, Guoliang. "
    "From what I’ve observed, this kid is one of those troublemakers. Always pulling pranks on the townsfolk, and getting caught every single time. He doesn’t even try to talk to his grandparents"
    "How exactly am I supposed to help this old couple? Hm…"
    #show i smile at above_box
    "Ah, got it! I just have to figure out what he really wants, and give it to him. Easy peasy!…Now, how I figure that out is the real question…"
    hide i
    gm "You there, young man!"
    call updateClock
    show gm at lower_left
    show gp at right
    "I look up to see the grandfather and grandmother marching towards me. She helped her husband walk while she carried a basket full of tea leaves on her back."
    "The grandmother has this stern look on her face, but the grandfather looks rather confused."
    hide gp
    #show i annoyed at right
    show i neutral at right
    "Shoot, was I staring? Do they think I'm a stalker?"
    i "Uh d-don’t mind me! I was just taking a look at the tea trees! Nothing else, I swear"
    show gm at lower_left
    gm "What are you babbling about? I just want you to do something for us."
    i "Huh? Oh, that’s it?"
    gm "You see, our grandson has been getting into a lot of trouble lately, so we don’t want him running around town without someone watching over him."
    hide i
    hide gm
    show gp at middle
    "The grandfather takes off his straw hat and wipes off his sweat."
    gp "No, there’s no need to trouble yourself, young man. Our daughter will pick him up."
    show gp at right
    show gm at lower_left
    gm "I told you, dear, she can’t."  
    gp "Why not?"
    gm "She’s gone, remember?"
    gp "Oh, right…"
    gp "When will she be back?"
    gm "*sigh* Just go sit over there on the porch and take your medicine."
    hide gp
    "The grandfather sauntered over to a seat on the porch."
    gm "I swear, sometimes I don’t know what to do with him."
    "The grandmother fixes the flower in her hair."
    gm "Anyway, please just bring back our grandson. Can you do that for us?"
    show i neutral at right
    i "Oh, uh, of course!"
    gm "Good."
    gm "Go ahead and buy him anything to keep him from going off. As for me, I have my own problems to take care of."
    hide i
    "She turns around to find her husband wandering off into the field"
    gp "Is it time to harvest the tea leaves already? Honey? Oh, where did you run off to?"
    gm "Oh for god’s sake."
    hide gm
    "The grandmother slowly chases after her wandering husband."
    #show i smile
    show i neutral at middle
    "Talk about perfect timing. I can use this as an opportunity to get something for their grandchild. Problem solved!"
    hide i at fadeout(1.0)
    "Once the couple resumes picking more leaves, I transform into a bird and fly off to the school."

    scene bg school with fade
    "After flying for a bit, I arrived at the elementary school. I land in a nearby alley where no one will see me turn back into a human."
    show i neutral at middle
    "Before picking up Guoliang, I fix myself up a little so I don’t look suspicious. Then, I start walking over to the school. I look for a clock on my way to check the time."
    i "3:05pm. Guoliang should be out by now."
    hide i
    "I head to the entrance of the elementary school."
    show gl at middle
    "There, I find a little boy waiting with a teacher. That must be Guoliang. He definitely has the appearance of a troublemaker, alright."
    show gl at right
    show i neutral at left
    i "Hi, hello! I’m here to pick up Guoliang."
    "Teacher" "Ah~ You’re the one Guoliang’s grandmother called about."
    "Teacher" "Okay, Guoliang. Off you go, and don’t cause trouble for this young man."
    "The teacher nudges Shūzhēn forward to me. I reach out my hand for Guoliang to grab, but he doesn’t take it."
    #show i shocked at left
    "Instead he just scoffs and walks next to me, without so much as a glance in my direction."
    hide gl
    "Teacher" "You two take care!"
    show i neutral at left
    "I waved back to the teacher as she saw us out with a smile."
    hide i

    scene bg market with fade
    "As I walked Guoliang through the market, I ask him about anything he wants to have."
    show i neutral at left
    show gl at right
    i "So, Guoliang… is there anything in particular you want? Something you’re in the mood for? You name it, I can get it for you!"
    gl "What do you care?"
    #show i shocked at left
    i "I’m just asking. Thought I’d get you a treat so you’re more comfortable around me."
    gl "Hah! Like that’ll win me over."
    i "So… is that a no…?"
    gl "Why did my grandparents even send you to get me? I can get back on my own like I always do."
    show i neutral at left
    i "Apparently you’ve been getting yourself into a lot of trouble, young man."
    gl "Have not!"
    #show i annoyed at left
    i "Don’t deny it. I’ve seen you being all mischievous."
    i "Setting animals loose, shooting rubber bands, kicking shuttlecocks at people…"
    gl "Hmph. They got what they deserved."
    i "{i}Some kid.{/i}"
    show i neutral at left
    i "Look, I’m just here to keep an eye on you until you get home. If you promise to behave, I’ll buy you whatever you want, okay?"
    gl "Anything?"
    #show i smile at left
    i "Yeah! Anything. You name it. I’ll buy it!"
    gl "Even if it’s expensive?"
    i "Of course! If it makes you happy, then by all means I’ll get it for you."
    gl "What makes me happy…"
    gl "Then, do you want to know what I want?"
    i "Tell me."
    gl "I want…"
    hide gl
    "Guoliang darts ahead trying to get away from me."
    gl "To get away from you!"
    #show i shocked at middle
    i "What- hey! Guoliang! Come back here!"
    hide i
    "I chase after Guoliang."

    scene bg bridge with fade
    " I follow him down the street, up and down stairs, across a bridge, and even through the gaps between buildings.Eventually, I lost sight of him…"

    scene bg market
    #show i tired at middle
    show i neutral at middle
    i "He sure has a lot of energy, even for a little kid."
    i "*sigh* This is becoming more of a hassle than I thought it would be."
    hide i
    "I begin searching around the area for him."
    "If it’s anything like those chase scenes in movies, he probably hid behind a corner and waited til I ran past him."
    "So I search behind every corner, and after a few minutes of looking around, I find him hiding behind some crates of fruits."
    show gl at middle
    "It looks like he’s about to shoot a rubber band at some fruit vendor."
    show gl at right
    show i neutral at left
    "I walk up behind him and pick him up."
    gl "Wha- Hey! Put me down!"
    "Guoliang shouts as he tries to free himself. The fruit vendor gives me a look of concern."
    #show i nervous at left
    i "Ehehe…"
    i "Sorry about that. This one loves to run off on his own."
    i "We were just on our way home and then he-"
    hide gl
    "Fruit Vendor" "Oh, it’s just you, Guoliang."
    "Fruit Vendor" "Found yourself a new caretaker, did you?"
    "Fruit Vendor" "Hehehe good luck. This little rascal’s a handful."
    #show i tired at left
    i "Oh he certainly is…"
    show gl at right
    "I carry a squirming Guoliang away in my arm."
    "But as I’m leaving, I can’t help but overhear the fruit vendor say something about Guoliang."
    hide gl
    hide i
    "Fruit Vendor" "Poor boy. A shame he doesn’t have any good role models in his life."

    scene bg cat
    show gl at right
    show i neutral at left
    gl "Agh! Let go of my hand!"
    i "So you can run away again? Not a chance."
    "I drag Guoliang along with me."
    #show i nervous at middle
    show i neutral at middle
    hide gl
    "Maybe I should just bring him back to his grandparents and hope that that’s enough."
    "..."
    "..."
    show i neutral at middle
    "No."
    "I made a vow to help the people of this town before their end, and I’ll see it through."
    #show i annoyed at middle
    "Even if it means dealing with this runt."
    show gl at right
    show i neutral at left
    gl "Ugh, fine! I won’t run away anymore. Just let go of my hand."
    i "Hmm… I don’t know…"
    gl "Come on. Please?"
    i "{i}It’s for the sake of his grandparents. Worst case scenario, I have to chase him all around town again. You just have to make him happy.{/i}"
    #show i tired at left
    i "Alright, but no funny business."
    "Guoliang nodded, though he was clearly annoyed."
    i "Okay good."
    #show i smile at left
    i "Now then, I said I’d get you something, and I’m a man of my word. What are you in the mood for?"
    gl "Nothing. Just take me home."
    i "You sure? Your grandparents said you could have anything."
    gl "I told you I don’t want anything!"
    show i neutral at left
    "Doesn’t look like Guoliang wants to talk anymore. He’s really giving me a tough time!"
    "I already spent a good amount of time trying to help this old couple, and I am not about to back out! They want their grandson to be happy, so I’m going to make him happy. I have to."
    #show i nervous at left
    "Before they all perish."
    show i neutral at left
    show gl at right
    i "{i}Okay. I’m just going to have to take a guess.{/i}"
    "As I’m thinking about what to buy for them, a mouthwatering scent permeates the air."
    "At the same time, I notice Guoliang staring in the direction of a small toy shop."
    hide i
    hide gl
    default gl_choice = "gua bao"
    menu:
        "Buy some street food":
            $ gl_choice = "gua bao"
            scene bg food stall
            "I decide to track down the scent, making sure to also keep Guoliang in my line of sight."
            "We eventually traced the source of the aroma to a stall that was selling gua bao."
            #show i smile at left
            show i neutral at left
            show gl at right
            i "That looks tasty!"
            i "What do you think, Guoliang? You like gua bao?"
            gl "They’re my favorite food."
            i "Well then, why don’t I get us a couple of bao?"
            gl "Okay, sure."
            i "Good."
            hide gl
            "I pull out a wallet from my pocket and hand the vendor some cash."
            i "We’ll take 2, please."
            "The vendor takes the cash and prepares us some fresh gua bao."
            "My mouth waters just watching them prepare it. The pork looks so tender and juicy. And the smell."
            #show i happy at left
            "*sniff* Ah~ Simply divine!"
            "Even though gods don’t need to eat, I find it a sin to not partake in human cuisine."
            "I eagerly take the two buns from the vendor."
            #show i smile at left
            i "Thank you!"
            show gl at right
            i "Here you go, Guoliang. Eat up!"
            #show i happy at left
            hide gl
            "After handing Guoliang his gua bao, I begin to dig into mine, savoring every bite."
            "Not even a minute goes by and I’ve already consumed my bao."
            #show i smile at left
            i "That was delicious."
            show gl at right
            "I look over to Guoliang, who had watched me devour the bao in seconds."
            "He had not taken a single bite of the bao."
            show i neutral at left
            i "What’s wrong?"
            i "You said they’re your favorite."
            show gl at right
            gl "Yeah, I did."
            i "So go ahead and eat it."
            gl "I can’t."
            i "Why not?"
            gl "Because I’m allergic to peanuts!"
            #show i shocked at left
            i "Oh! You are? You should have told me."
            gl "You should’ve asked."
            #show i nervous at left
            i "I… okay, fair point."
            i "Here, I’ll go buy you another one."
            i "Wait right here, okay?"
            gl "Okay."
            hide i
            hide gl
            "I go back to the vendor to buy another gua bao for Guoliang… and another one for myself. This time, without peanuts."
            "I wait behind a father and his son. They seem so happy to be eating together. Classic father-son bonding activities. The father carries his son on his shoulders as they walk away with their bao."
            "I’m up next."
            "After paying for the two bao, I return to the spot where I left Guoliang."
            #show i smile at middle
            show i neutral at middle
            i "Alrighty, I made sure to ask the guy not to put peanuts this ti-"
            #show i nervous at middle
            "I look, but Guoliang is not there."
            i "Guoliang?"
            hide i with fade
            "I look around the area, but there’s no sign of Guoliang."
            i "{i}Oh no{/i}"
            i "Me and my captivation for food!"
            i "{i}I gotta find Guoliang fast!{/i}"
            i "{i}I can’t make the old couple’s wish come true if I don’t have Guoliang with me!{/i}"
            hide i
            "Scarfing down the gua bao I bought, I search the entire area for Guoliang."
        
        "Buy a toy for him":
            scene bg market
            #show i smile at left
            show i neutral at left
            show gl at right
            i "{i}That’s it! Kids love toys! If I buy him a brand new toy, then he’ll surely be happy! …at least, until doomsday arrives…{/i}"
            i "You want a toy, don’t you?"
            gl "Huh? What? No I don’t."
            i "I see you staring at those toys over there. Don’t be shy."
            gl "I said I do- hey!"
            "I take Guoliang to the toy store so he can pick out a toy."

            scene bg store
            #show i smile at left
            show i neutral at left
            show gl at right
            i "Go on and pick any toy you want."
            gl "I told you I don’t want any toys."
            gl "Besides, toys are for little kids."
            show i neutral at left
            i "Last I checked, you are one."
            gl "Grrr."
            i "Alright, fine. I’ll pick for you."
            hide i 
            hide gl
            "There’s a wide variety of toys here. Which toy should I pick for Guoliang?"
            default toy = "chě líng"
            menu:
                "chě líng":
                    $ gl_choice = "chě líng"
                    $ toy = "chě líng"
                "Spinning top":
                    $ gl_choice = "Spinning top"
                    $ toy = "Spinning top"
            show i neutral at middle
            i "Excuse me. One [toy] for my little boy here, please."
            "The clerk hands me the [toy]."
            #show i smile at midddle
            i "Thank you!"
            show i neutral at left
            show gl at right
            "I give the [toy] to Guoliang."
            i "Here you go. Go on, play with it."
            gl "Seriously? These toys are so lame."
            #show i shocked at left
            i "What? I’ve seen kids your age love playing with these."
            gl "Yeah cause they’re babies. Only little kids would have fun playing with something so stupid."
            #show i smile at left
            i "It’s not stupid. If you know how to do tricks."
            gl "What tricks?"
            i "Hehe, watch and learn, kid."
            hide gl
            if toy == "chě líng":
                "I take the chě líng and begin doing all sorts of tricks with it."
                "I fiddle around with the sticks, making loops and pulling until I get the chě líng to make the shape of a sort of web."
            
            if toy == "spinning top":
                "I take the string from the top and start swinging it around."
                "Each time I swung it, I wrapped the string around my fingers, making loops until finally…"
                "The top was dangling in front of the web I made with the string."
            show gl at right
            gl "Mmm. Not bad."
            i "Impressive right? Now watch this."
            if toy == "chě líng":
                "I rotate my arms around, keeping the formation of the string."
                "Wherever I rotated, the chě líng would roll along, never leaving the string."
                "I heard a little girl laughing."
                "On my right, I see a little girl and her mom watching me in awe."
                hide gl
                i "{i}Time to give everyone the grand finale.{/i}"
                "To finish my performance, I give the sticks a pull, straightening the string and shooting the chě líng up in the air."
                "I give the mom and her daughter a smile, then catch the chě líng on the string without looking."
            if toy == "spinning top":
                "I sway the top gently a few times before giving it one big swing."
                "In an instant, my web unravels itself in a fashionable manner. "
                "I heard a little girl laughing."
                "On my left, I see a little girl and her mom watching me in awe."
                hide gl
                i "{i}Time to give everyone the grand finale.{/i}"
                "To finish my performance, I twirl the top around me before launching it into the air."
                "I give the mom and her daughter a smile, then catch the top on the palm of my hand without looking. The top is still spinning when I catch it."
            "The mom and her daughter clap for me, so I decide to give them a little bow."
            i "Thank you, thank you!"
            #shwo i smile at middle
            i "See that, Guoliang? That’s not so lame now, is it?"
            "I look around the area, but there’s no sign of Guoliang."
            show i neutral at middle
            i "Guoliang?"
            #show i nervous at middle
            i "{i}Probably should have stopped after the first trick.{/i}"
            hide i
            "Seeing as how the little girl was fascinated by my skills, I decide to give her the toy."
            "She and her mother thank me, and wave goodbye. Now back to the matter at hand."
            #show i nervous at middle
            i "{i}I gotta go find Guoliang!{/i}"
            i "{i}I can’t make the old couple’s wish come true if I don’t have the little rascal with me!{/i}"
            hide i 
        
    scene bg bridge
    "I spent hours searching the town."
    "I checked every alley, every store, even went back to the elementary school. No sign of him whatsoever."
    "I lean against the railing of a bridge in defeat."
    show i neutral at middle
    #show i tired at middle
    i "*sigh* I guess this is one prayer I won’t be able to answer…"
    i "I just hope they don’t come back and haunt this place after they die."
    hide i
    gp "What was that, lad?"
    show i neutral at left
    show gp at right
    "I turn around to find the grandfather standing right next to me."
    #show i shocked at left
    i "Oh! Sir, how long have you been here?"
    gp "Hah, not very long. I just got here."
    i "D-did uh, you hear anything I said."
    gp "What? Did you say something?"
    #show i nervous at left
    i "Uh nothing, nothing just… admiring the view."
    hide i
    hide gp

    scene bg town
    gp "Ah… It is a lovely view, ain’t it?"
    i "Yes. Yes it is."
    "The two of us stand there in silence."
    "I don’t want to bring up the fact that I lost their grandson after they trusted me to bring him back home."
    "But at the same time, it’s a little awkward not saying a word."

    scene bg bridge
    gp "Guoliang likes to sit by the river just outside of town."
    i "...what?"
    show gp at right
    show i neutral at left
    gp "Anytime he wants to be by himself, he goes outside of town and sits by the river."
    gp "It’s where he does all of his thinking."
    i "How… How do you know this?"
    gp "You came to us to bring Guoliang true happiness, didn’t you?"
    gp "The gods really did hear our prayers."
    #show i nervous at left
    i "I… I uh…"
    gp "Truth is, that boy misses his parents."
    gp "He never got to experience what it was like… to have a loving mama and baba."
    gp "My wife and I tried to love and care for him… as best we could but… there is only so much these old bones can do."
    show i neutral at left
    i "I… I can imagine."
    gp "We’re…"
    gp"We’re not gonna be around much longer… I know it."
    #show i shocked at left
    i "I… how do you-"
    gp "But at the very least, I want our grandson to experience the love of a parent before our time comes."
    gp"Can you grant us this last wish?"
    show i neutral at left
    "I don’t know if this old man is delusional, or he saw right through me."
    "Regardless, I assure him that I’ll do what I am allowed to do for him."
    #show i smile at left
    i"Of course."
    gp"Mmm, good."
    "The grandfather slowly walks away."
    hide gp with fade
    #show i nervous at middle
    i"What a strange old man."
    show i neutral at middle
    i"But now I know where to find Guoliang."
    hide i
    "After making sure I’m alone, I transform into a bird and fly over to the river to find Guoliang."
    "... ..."
    "... ..."
    gp"Haha… such a fine young man…"

    scene bg riverside
    "I fly overhead to the river, and after surveying the area, I find Guoliang crouching by the riverside. Just like the old man said."
    "I land on the road by the river, quickly transforming back into a human."
    show i neutral at middle
    "I’m about to walk over to Guoliang, but then I stop myself."
    #show i nervous at left
    show i neutral at left
    show gl at right
    "It’s faint, but I can hear Guoliang sniveling."
    i "{i}Is he crying? Why would he be…{/i}"
    i "{i}Oh…{/i}"
    hide gl
    hide i
    "I think back to what the old man said."
    gp "Truth is, that boy misses his parents."
    gp "He never got to experience what it was like… to have a loving mama and baba."
    "And the time when I bought him the [gl_choice]."
    "There was a kid who was spending quality time with their parent at the time."
    i "{i}I get it now.{/i}"
    "I approach Guoliang slowly until my shadow is cast over him."
    show i neutral at left
    show gl at right
    "Guoliang is still sobbing. He doesn’t seem to have noticed me yet."
    i "You miss them, don’t you?"
    gl "Huh!?"
    "Guoliang quickly turns his head around to see me standing right behind him."
    "His face was covered in tears, and snot was running from his nose."
    "Guoliang tries to wipe his face with his arm to hide the fact that he was crying, but it was already too late for that."
    gl "What are you…"
    i "Your parents. You just want to be with them, right?"
    "Guoliang looks away without giving a response."
    i "Your grandpa told me."
    "For once, Guoliang doesn’t say anything. He just goes back to staring at the river."
    "I take a seat next to Guoliang, not saying a word."
    "He doesn’t try to run away."
    i "It must be hard for you. Watching all of those kids happily skip around with their mamas and babas."
    gl "Be quiet!"
    gl"All those kids talk about how much they love their parents and how amazing they are."
    gl"Meanwhile I can’t even do much with {i}my{/i} grandparents."
    gl"Nothing like what I see all my classmates get to do with their parents."
    gl"I never even got much time with my parents!"
    gl"My mama died when I was only four, and my baba leaves me here soon after!"
    show i shocked at left
    i"He what!?"
    gl"He hasn’t even come to check in on me in three years."
    show i neutral at middle
    i"... ..."
    gl"I miss when baba would let me ride on his shoulders, or play with me. A-and when mama would cook her famous gua bao."
    gl"*sniff* I thought we would always be one happy family…"
    gl"Why did they have to leave me? *sniff*"
    gl"I…I…"
    hide i
    gl"I…I JUST WANT MY MAMA AND BABA!"
    hide gl
    "Guoliang wails into the setting sun. His cries echo across the valley."
    "All of the pain, sorrow, anger. Everything he had been holding in until now came flowing out like the river."
    #show i sad at middle
    show i neutral at middle
    i"To experience all of this, and at such a young age too…"
    i"There’s only one thing to do now."
    hide i
    i"Gently, I rub Guoliang’s back."
    show i neutral at left
    show gl at right
    i"I’m sure your father was just as heartbroken. I mean, he lost the love of his life, and maybe seeing you just brought too much pain for him to bear."
    "Guoliang continues to weep."
    i"Look, I don’t know what it’s like to lose both of my parents as a young boy…"
    i"But I do know that a kid should never have to go through what you experienced. Especially not alone."
    "Guoliang’s stops crying."
    i"Even if your parents aren’t here to be with you, there are people who can be."
    i"People who want nothing more than to see you be happy and live your life to the fullest. Your grandparents, your teacher, the kids at the school, even the fruit vendor." 
    #show i smile at left
    i"and me"
    i"A family doesn’t only have to be people who are related to you. A family can be the people who are there to see you shine in your happiest moments, and are there to lift you up in your darkest hours."
    i"But above all else, no matter what you do, whether you succeed or fail, they will always love you."
    i"You just have to let them in."
#the rest is wrote after the background change
    "I stand up and reach my hand out to Guoliang."
    i "So what do you say, Guoliang?"
    i "Are you ready to let me in?"
    "Guoliang stares at me, then looks back at my hand."
    "For a long moment, he just stares. I wasn’t sure if he was going to take it or not."
    "But soon enough, Guoliang takes my hand."
    "I help Guoliang up onto his feet, and pull out a cloth to wipe his face clean."
    i "Now, I may not be your father, but at the very least…"
    "I pick up Guoliang and place him on my shoulders."
    i "I can at least treat you like you were my own son!"
    i "Go on, take a look."

    scene bg street
    "Guoliang slowly opens his eyes, where the view of town meets his wondrous gaze."
    "The setting sun bathes the town in its rays, its light reflecting off of the surface of the river."
    gl "Whoa…"
    i "Do you like the view?"
    gl "It… It’s so pretty!"
    i "Yeah. It sure is."

    scene bg river

    i "Alright passengers, please fasten your seatbelts. The train is about to take off!"
    gl "Huh?"
    i "Right now!"
    "I begin light jogging back to the town with Guoliang on my shoulders."
    gl "Whoa!"
    i "Hold on tight!"
    "Guoliang holds onto my head."
    "I can hear Guoliang laugh as I continue to jog back to town."

    scene bg market

    "Me and Guoliang walk through the night market, both of us eating peanut free gua bao."
    i "You enjoying your gua bao, Guoliang?"
    "I hear a muffled “mhm” from him."
    gl "Ish sho good!"
    i "Haha! Don’t talk while you chew, kid."
    "As we’re walking, I notice a shop selling bào bīng on the side."
    i "Why don’t we get some bào bīng to cool off?"
    gl "*gasp* Yay!"
    "Guoliang and I sit down and enjoy a nice bowl of mango bào bīng together."
    gl "Mmm! Yummy!"
    i "Glad you like it!"
    i "{i}I wonder how long it’s been since Guoliang was like this.{/i}"
    i "{i}It's nice to see he's finally enjoying himself."
    i"{i}Now all I have to do is drop him off at his grandparents’ house, and this will all be over!{/i}"
    i"..."
    i"..."
    i "{i}It will all be over...{/i}"
    "I look over to Guoliang getting stuck in with the bào bīng."
    i "{i}Who knows how long he’ll have left until the town meets its end?{/i}"
    i "{i}He finally gets to experience happiness after so long, and it might be the only time he gets to be happy.{/i}"
    i "{i}Why? All because it’s supposed to be his fate to die?{/i}"
    i "{i}He deserves to live a long, happy life!{/i}"
    gl "Are you okay mister?"
    i "Huh?"
    gl "You look like you’re mad."
    i "O-oh. It’s nothing, don’t worry about it."
    i "Just make sure to finish the bào bīng before I drop you off."
    gl "If you say so."
    "Guoliang continues to eat the bào bīng."

    scene bg street
    i "Okay, we’re almost home."
    gl "*Yawn* Today was the best! I hope I can’t wait to have more days like this!"
    i "Yeah… yeah I hope you do…"
    i "..."
    i "{i}Am I really going to just let him die?{/il}"

    menu:
        "Drop him off":
            i "*sigh*"
            i "{i}No, I can’t change his fate.{/i}"
            i "{i}As much as I want nothing more than for this boy to live, I can’t.{/i}"
            i "{i}Even gods shouldn’t tamper with the fate of mortals… No matter how unfair it can be.{/i}"
            "I look down at Guoliang."
            "It looks like he’s starting to drift off."
            "I pick Guoliang up and carry him on my back."
            i "There you go. Just a little longer."
            gl "Mmmm… I love you… baba…"
            i "Baba?"
            "Guoliang begins to snore."
            i "Hah!"
            i "{i}As long as Guoliang is happy in his final moments, that’s enough for me.{/i}"
            i "I love you too…"

        "Save him":
            "I stop."
            gl "Huh? Why are we stopping?"
            i "Guoliang."
            gl "Yeah?"
            i "Have you ever thought about moving back to the city to find your father?"
            gl "W-why…?"
            i "Just answer yes or no."
            gl "Um… well I have, but I don’t have any money."
            i "I’ll give you money."
            gl "You will?"
            i "Yeah, enough money to last you a whole year."
            gl "H-how?"
            i "Don’t worry about it. I’m asking if you want to move to the city."
            i "I’ll take care of telling your grandparents and the school."
            gl "Um.. I uh-"
            i "Of course you do! Come on, I’ll take you to the train station."
            "I turn around and try to take Guoliang to the train station."
            i "{i}This is the only way to save the boy.{/i}"
            i "{i}He deserves a chance to live a happy life!{/i}"
            "But Guoliang doesn’t move."
            i "Huh? Guoliang?"
            gl "... I… I don’t want to."
            i "What?"
            gl "I don’t want to go. I want to stay here."
            i "But… but why?"
            gl "I don’t know, but I want to start living my life here in town."
            i "You can have a better life in the city. Have a fresh start! LIVE a happier life!"
            "Guoliang backs away, and I realized I started raising my voice at him."
            i "I-I’m sorry. I’m so sorry."
            i "I don’t know what came over me."
            gl "I-it’s okay, mister."
            i "I just… I don’t understand."
            i "Don’t you want to be reunited with your father?"
            i "If you’re worried he might bring you back here, just talk with him. He probably just needs someone to help him, like you and me today."
            gl "I {i}do{/i} want to be with him."
            gl "But I’m not ready to face him yet."
            gl "There are a lot of things I want to do here, and things I have to fix."
            gl "Once I’ve done all that, then I think I’ll be ready to see baba again."
            i  "{i}But, you won’t have the chance to do any of that…{/i}"
            gl "Besides, mister, you taught me something today."
            i "Oh? What’s that?"
            gl "My family’s been here this entire time! And I need to make things right with them."
            i "!"
            i "..."
            i "{i}Whatever makes him happy.{/i}"
            i "You’re right. Your family has been here all along."
            "Guoliang and I smile at each other."
            i "Now come on. Just a little further to home."

            scene bg grassy field
            gm "Thank you again for bringing Guoliang back."
            i "It was nothing, really."
            gm "I must say, I haven’t seen Guoliang happy in forever."
            gm "Whatever you did for him, thank you, truly."
            i "Haha. I’m always glad to bring a smile to anyone’s face!"
            i "Now then, I’ll be off now."
            gm "Take care!"
            "I wave goodbye to the old lady, but before I go, Guoliang runs up to me."
            gl "Hey! Mister!"
            i "Huh? What’s up?"
            "Out of the blue, Guoliang gives me a big hug."
            gl "Thank you for everything!"
            "Guoliang hugs me tightly."
            i "You’re welcome."
            "I see Guoliang run back to his grandmother before she closes the door."
            "Taking the form of a bird, I circle above Guoliang’s house to take one good look at it."
            i "{i}Goodbye, Guoliang.{/i}"
            i "{i}May you be reunited with your mother in the afterlife.{/i}"
            "With a heavy heart, I say one final goodbye to Guoliang and his folks before flying off to the temple."
            "Unknown to me, the grandfather watched me fly off from the window of his room."
            gp "Thank you, for answering our prayers, my lord."

    jump end

    
label Hana:
    "Come here on a later date again!"



    jump end

    
label Hana_arc:
<<<<<<< Updated upstream
=======
    play music "maintheme.wav" volume 0.5 loop
    scene bg street with fade
    i "(Walking among the townspeople in disguise, I watch mothers traveling with their children, some men working on fixing up an older house, and a single old lady sitting on her porch. Her name is Hana, I believe, and from what I’ve observed of her, she was
alone.)"
    show i neutral at lower_right
    i "(In my short time here, I’ve only gotten one or two prayers from her, once asking me to
send a message to a loved one. I’m not sure how successful those kinds of messages
are, or how often they reach their departed loved ones, but I sent it on anyway, as is the
standard.)"
    i "(Looking over at her, she has a quite disheartened expression painted all over her face.
Her eyes are closed, and I can feel that she’s quite deep in thought, and as I focus, I
can sense that she’s in the middle of sending me a prayer!
Maybe I will be able to help?)"
>>>>>>> Stashed changes
    show i happy at lower_right
    i "Uh… hello ma’am! Is there anything I can help you with?"
    show h neutral at lower_left
    "At this, Hana turns to look at you up and down, examining you while making little comments. At this, you look briefly at your human form, checking that you didn’t make any part of it too strange or unordinary."
    h "Hmm, well you’re a little thin, but you should do well enough!"
    show i neutral at lower_right
    i "Huh, ok note for next time, make sure my muscles are accurate."
    show h happy at lower_left
    h "Young man, do you think you would be able to help me with a few errands today?"
    i "(Should I really be running errands? I could be doing so much more with my time here…) "
    "(Looking over at Hana, her house is very quaint, and more than that, she’s the only one in it. There are some photos framed around the house, and while most of them are covered in dust, there’s one exception. Two girls stand arm in arm in a field, their smiles bright and wide.)"
    i "(Maybe I’m the only one that can help her…)"
    i "Yes! I would love to help ma’am! What can I do? "
    "(Hana chuckles after hearing your response.) "
    h "So enthusiastic! Well, here, I need help getting some things for someone very close to me. It’s a special occasion, so it’s really important that I get everything by the end of today."
    i "Oh! Is it their birthday, perhaps?"
    show h sad at lower_left
    "(The smile falls from her face.) "
    h "Ah…I guess you could say that…"
    show i neutral at lower_right
    i "(Ah…did I say something to upset her?)"
    i "…Anyway, what exactly do you need?"
    show h neutral at lower_left
    "( She shakes herself out of whatever was affecting her, and starts picking some things up while talking to you.)"
    h "Well, that’s the thing. I can handle one of these things, but they’re both pretty time consuming, so I don’t think I can do both. I need to get True Lilies from one of the fields nearby, but my knees make getting there more complicated than it really should be."
    show i happy at lower_right
    i "Oh, that shouldn’t be too hard. What’s the other thing?"
    h "Some ingredients for a famous dish of mine, Braised Pork and Dumplings! I’ve made a list of everything I need to get at the market, and it’s fairly close, but I often need to take multiple trips so I don’t carry too much."
    show h happy at lower_left
    h "I already get chewed out by my doctor too much for pushing myself, I don’t want to add more fuel to that fire!"
    i "Got it! You said you need all of this by the end of today, yes?"
    h "Correct!"
    i "Well, I can take care of one of these, while you take care of the other, and that way we’ll have both done relatively soon!"
    show i neutral at lower_right
    i "(Now… which one to choose…)"
    # hana split 1
    menu:
        "Gather some Pure Lilies":
            call lillies from _call_lillies
        "Gather ingredients at the market":
            call market from _call_market

    show i happy at lower_right
    show h happy at lower_left
    "As soon as you arrive back on Hana’s front porch she turns around, smiling."
    h "Ah! You got everything! Thank you so much."
    i "Of course! Now, what else can I help you with?"
    show h neutral at lower_left
    h "Oh no, you’ve done enough! Sit down, I’ll take care of the cooking."
<<<<<<< Updated upstream
=======
    "(She takes the ingredients and starts making the dough for the dumplings, then
moving onto getting the pork cooked. All the while, I try my best to arrange
the flowers somewhat neatly, but end up packing way too many flowers in one
single vase.)"
    h "Alright, almost done on the food over here, and those flowers are...
passable."
    show i sad at lower_right
    i "I tried my best!"
    show h happy at lower_left
    h "That you did! I didn’t exactly hire a florist for this, now did I?"
    "(She laughs, and I sit down with a pout, slightly embarrassed by this mortal
mocking my work. Silence fills the air as Hana packs up some of the food into a
small box, and ties a neat bow onto the top of it. She looks like she has
something to say, but she’s staying silent.)"
    show i neutral at lower_right
    i "Is everything alright, Hana?"
    show h neutral at lower_left
    h "...I want to tell you about her."
    i "Hm?"
    show h happy at lower_left
    h "Kuniko, I mean."
    show i happy at lower_right
    i "Kuniko? Is that who we’re preparing this for?"
    "(She nods briefly.)"
    show h neutral at lower_left
    h "We grew up together here in this town, to be honest it didn’t look too
much different from it does now."
    "(Hana laughs at that and I smile as well.)"
    h "We were inseparable, but for one reason or another she had to move
away to the city."
    show h happy at lower_left
    h "In that absence my heart ached for her, even if I could not put it into
words yet."
    "(She looked at me with a smile, but I can tell there’s a sadness in her voice. I
offer a smile back, and she continues.)"
    h "When she finally moved back I was the happiest I’ve ever been, and she
was delighted to see me again as well! We spent years at each other’s
sides being best friends, I was even at her side during her wedding but..."
    show h sad at lower_left
    h "I knew I wanted more."
    show i sad at lower_right
    i "Ah... I see so-"
    h "I was envious, that day, that I wasn’t the one up there with her. And I
thought about telling her but- I didn’t want to ruin her perfect life."
    "(She takes a slightly shaky breath.)"
    show h happy at lower_left
    h "So... I kept it to myself. I figured that being there by her side was better
than sacrificing our friendship over something that could never be. She eventually divorced, and at one point it even seemed like- maybe a
life with her was possible but..."
    "(Hana’s eyes welled up with tears, a few stray ones falling to the ground as she
took a deep breath.)"
    show h sad at lower_left
    i "...What happened to her?"
    h "She...caught some kind of illness"
    "(A pause fills the air as Hana takes her time wiping her tears.)"
    h "I don’t know if the doctors ever found out what it was, but she was in pain.
I was there for her, along every step of the way but- In the end it didn’t
matter."
    "Hana tries to wipe away the last of her tears, and quietly continues."
    h "She passed away a few years ago."
    i "Oh... oh I’m so sorry Hana..."
    h "It’s...alright, I’ve learned to live life in her absence. But, I can’t lie and say
that I don’t miss her, miss the space where she used to be, by my side.
Everyday just feels so- heavy without her."
    show i happy at lower_right
    i "I know it’s not been easy but, it’s beautiful you still honor her."
    "I offered her a tissue, and she takes it with a weak smile."
    h "I used to beat myself up, wishing that I could’ve done something to help
her- maybe then, we could’ve had a nice life together-"
    i "I promise, you did everything you could."
    "Hana wiped the last of her tears."
    show h neutral at lower_left
    h "I know you’ve already done so much, just being here listening, but can
you help me out with one last thing?"
    show i happy at lower_right
    i "Yes. What do you need?"
    h "On the other side of town, there's a small memorial set up for her. Can
you help me get the last of the things ready for Kuniko?"
    i "Of course! What needs to be done?"
    h "Well, I like to get everything done by sunset, and I’m already running out
of time, can you help me choose? I need to get a gift for Kuniko, but I also
need to get candles for her memorial. I think I can only do one, but if we
get it together we can still make it!"
    menu:
        "Buy some decorations for the memorial":
            call decorations from _call_decorations
        "Pick out a gift for Kuniko":
            call gift from _call_gift
>>>>>>> Stashed changes

    "WIP"
    jump end
        
label lillies:
    show i happy at lower_right
    i "Here, how about I go and gather those flowers, and bring them back to you as soon as I can?"
    show h happy at lower_left
    h "Yes, thank you! I guess I’ll gather up my basket for the market then!"
    hide h
    "You start to walk away, watching as Hana gathers her things and heads into the town center. As soon as she’s out of eyesight, you transform into a small bird, and fly towards the lily field."
    hide i
    scene Grassy Field
    "(You fly over, looking for a good patch of lilies, until you find a beautiful group of white lilies, shining like the moonlight.)"
    "Perfect! Whoever she’s giving these two will love them!"
    show i neutral at lower_right
    "(Landing close to them, you lightly dust off your clothes, and start picking a few of them. As you gather a few of them, you feel a voice from behind you.) "
    s "Oh… Hana still gets those?"
    "(If you were a mortal, the spirit’s voice would’ve made you jump. Thankfully, you’re fairly used to the deceased and their behavior.)"
    show i happy at lower_right
    i "Ah! Hello, you know Hana?"
    s "Mmm… I do. Or, I did."
    "(The spirit’s voice echoes around you, a hollow, faint sound. Then there’s a quiet laugh that echoes for a moment.)"
    s "How in the world did she get a god to do her errands for her?"
    i "Ah! Well, I was tasked with helping the people of this town, and answering their prayers. I guess her prayer was to prepare for some special event today, and it must be pretty important!"
    s "So she… she still-"
    "(The spirit pauses, thinking for a moment, and then looks at you and speaks a single word.)"
    s "Oh."
    show i neutral at lower_right
    i "Is…everything ok?"
    hide s
    "(You look around, but the spirit is already disappearing.)"
    i "(Hmm, frustrating. I should check in with Hana when I get back.)"
    "Gathering your things, you make sure you’ve gathered plenty of lilies, and start to fly back to Hana."
    hide i
    return


label market:
    show i happy at lower_right
    i "Well, what if I got the stuff for Braised Pork and Dumplings and you got the lilies?"
    show h happy at lower_left
    h "Sure! I’ll start heading out to the fields."
    hide h
    "You wave goodbye to Hana, gather some of her baskets and bags, and start to head out to the town center."
    scene market
    show i neutral at lower_right
    i "(Hmm, so the list here should have everything, now if I can just actually find it all…)"
    "You look over the list, trying to make a mental map of where you would find everything and what to get first."
    i "I think I’ll start with getting the stuff for the dough!"
    return

<<<<<<< Updated upstream

=======
label decorations:
    show i happy at lower_right
    i "Let’s get some decorations!"
    "(Getting my things, Hana and I head to the market in search of candles, flowers,
and other decorations.)"
    hide i
    hide h
    scene bg market
    show i neutral at lower_right
    show h neutral at lower_left
    "(Hana and I arrive at the market, picking up a few candles that look good enough
for a proper memorial.)"
    i "Do these look good so far Hana?"
    show h happy at lower_left
    h "Yes, they look lovely!"
    i "What else do you think we should get for the memorial?"
    "(Hana thinks for a moment, and then smiles and leads me towards some stationary supplies.)"
    h "What if I wrote her a letter?"
    show i happy at lower_right
    i "That would be beautiful!"
    "(Picking up some supplies and paper that looks sufficiently elegant, Hana and I head back to her house.)"
    scene bg street
    show h neutral at lower_left
    h "What should I write- where do I even begin?"
    i "You could tell her how you feel?"
    "(Hana laughs and smiles.)"
    show h happy at lower_left
    h "My entire life I couldn’t tell her, and only now that she’s gone I finally tell her, that seems like a sick joke."
    show i sad at lower_right
    i "Ah! Apologies I didn’t mean to-"
    h "No, no, I think it would be nice! It would maybe give me a little closure with this. Thank you."
    "(I sit and watch as Hana writes down a letter to Kuniko, offering little bits of advice and encouragement. And when she’s done, we get ready to head to the memorial.)"
    scene bg grassy field 
    show h neutral at lower_left
    h "Thank you, again. Can you hand me the rest of what we’ve brought?"
    "I handed over the candles and decorations we bought. Hana sets them down,
and organizes them around Kuniko’s memorial. Very gently, she takes out the
letter she wrote to her, and holds it to her heart."
    h "Are you... sure that it’s not too much? Leaving a love letter like this for
her?"
    show i happy at lower_right
    i "Of course not."
    "(Reassured, Hana places a single kiss on the letter, and places it down on the
memorial.)"
    return 

label gift:
    show i happy at lower_right
    i "What if I helped you pick out a gift?"
    show h happy at lower_left
    h "That sounds lovely, thank you."
    "Getting my things, Hana and I head to the market to find a perfect gift for Kuniko."
    hide i
    hide h
    scene bg market
    show i neutral at lower_right
    show h neutral at lower_left
    "(Hana and I arrive at the market, bouncing from store to store to find something good for Kuniko, but Hana is very specific with what the item needs to be. I pick up a nice necklace with a green gemstone being offered, and show it to Hana.)"
    show i happy at lower_right
    i "Here, what about this?"
    h "Hmm, no she never really liked green. Or most jewelry, for that matter... but maybe something simple would be nice?"
    "(Hana stands there, thinking for a moment, before muttering something barely audible.)"
    show h happy at lower_left
    h "Well... we had matching bracelets as kids... what if-"
    "(An idea pops into my head, and I give Hana an excuse as I start heading towards the fancier side of the jewelry section of the market. I stumble upon a stand with matching rings meant for couples, and quickly call Hana over.)"
    h "Again, I don’t know if jewelry is really her style- oh."
    show i happy at lower_right
    i "Is this a fitting gift?"
    "(Tears form in Hana’s eyes as she places a hand over her mouth and nods, and with her confirmation I buy a pair from the salesclerk. With the gift bought, we head out towards Kuniko’s memorial.)"
    scene bg grassy field
    "Hana and I stand at Kuniko’s memorial, getting everything we’ve brought ready."
    show i neutral at lower_right
    show h sad at lower_left
    h "Thank you, again. Can you hand me the rest of what we’ve brought?"
    "(I finish getting the food and flowers placed down near the memorial, and Hana
takes out the little gift box containing her and Kuniko’s rings. With shaky hands,
she opens it, takes out the ring meant for her, and closes the box.)"
    h "Is this truly alright? What if this is too forward or strange? I mean I haven’t
even... confessed to her?"
    show i happy at lower_right
    i "Isn’t this gesture enough of a confession? I think she would understand
what you’re saying."
    show h happy at lower_left
    h "Hmm... you’re right!"
    "(Hana closes the box, and places it down in the center of Kuniko’s memorial. )"
    return


label transition:
    play music "once_upon_a_time_loop.ogg" volume 0.3 loop
    if not Guoliang or not Hana:
        scene bg street with fade
        show i ancient at middle
        i "Only 2 more days until the town and its people meet their end."
        i "If only I could do more for them to change their fate…"
        i "*Sigh* The least I can do is grant them one final moment of happiness."
        i "Now then, time to go answer [arc]’s prayers."
        hide i
        if Guoliang == True and Hana == False :
            jump Hana_arc
        else:
            jump Guoliang_arc
    else:
        jump end
>>>>>>> Stashed changes







label end:
    return

