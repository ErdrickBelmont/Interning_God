#diable close project confirmation
init python:
    config.quit_action = None

#image resize
image bg temple = im.Scale("temple.png", 1980, 1080)
image bg grassy field = im.Scale("House in front of a tea field.png", 1980, 1080)
image bg school = im.Scale("elementary school.png", 1980, 1080)
image bg market = im.Scale("market.png", 1980, 1080)
image bg street = im.Scale("town.png", 1980, 1080)
image bg river = im.Scale("riverside.png", 1980, 1080)
image bg grave = im.Scale("grave.png", 1980, 1080)

image i ancient = im.Scale("intern-ancient.png", 225 * 1.6, 280 * 1.6)
image gl = im.Scale("child-normal.png", 200 * 1.6, 280 * 1.6)
#image gl mad = im.Scale("child-mad.png", 200 * 1.6, 280 * 1.6)
image gp = im.Scale("grandpa-normal.png", 200 * 1.6, 280 * 1.6)
image gm = im.Scale("granny-normal.png", 200 * 1.6, 280 * 1.6)
image i normal = im.Scale("intern-modern.png", 210 * 1.6, 280 * 1.6)

#character definition
define i = Character("Intern God")
define gp = Character("Grandpa")
define gm = Character("Grandma")
define gl = Character("Guoliang")

#character art position definition
define middle = Position (yalign = 0.7)
define left = Position (xalign = 0.15, yalign = 0.7)
define right = Position (xalign = 0.85, yalign = 0.7)
define lower_middle = Position (yalign = 0.75)
define lower_left = Position (xalign = 0.15, yalign = 0.75)
define lower_right = Position (xalign = 0.85, yalign = 0.75)


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
    "Taking on my human form, I made my way to a tea farm tended by an old couple. The couple is currently hard at work harvesting tea leaves."
    show i normal at middle
    "These two have been praying every single day for the well-being of their grandson, Guoliang. "
    "From what I’ve observed, this kid is one of those troublemakers. Always pulling pranks on the townsfolk, and getting caught every single time. He doesn’t even try to talk to his grandparents"
    "How exactly am I supposed to help this old couple? Hm…"
    #show i smile at above_box
    "Ah, got it! I just have to figure out what he really wants, and give it to him. Easy peasy!…Now, how I figure that out is the real question…"
    hide i
    gm "You there, young man!"
    show gm at lower_left
    show gp at right
    "I look up to see the grandfather and grandmother marching towards me. She helped her husband walk while she carried a basket full of tea leaves on her back."
    "The grandmother has this stern look on her face, but the grandfather looks rather confused."
    hide gp
    #show i annoyed at right
    show i normal at right
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
    show i normal at right
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
    show i normal at middle
    "Talk about perfect timing. I can use this as an opportunity to get something for their grandchild. Problem solved!"
    hide i at fadeout(1.0)
    "Once the couple resumes picking more leaves, I transform into a bird and fly off to the school."

    scene bg school with fade
    "After flying for a bit, I arrived at the elementary school. I land in a nearby alley where no one will see me turn back into a human."
    show i normal at middle
    "Before picking up Guoliang, I fix myself up a little so I don’t look suspicious. Then, I start walking over to the school. I look for a clock on my way to check the time."
    i "3:05pm. Guoliang should be out by now."
    hide i
    "I head to the entrance of the elementary school."
    show gl at middle
    "There, I find a little boy waiting with a teacher. That must be Guoliang. He definitely has the appearance of a troublemaker, alright."
    show gl at right
    show i normal at left
    i "Hi, hello! I’m here to pick up Guoliang."
    "Teacher" "Ah~ You’re the one Guoliang’s grandmother called about."
    "Teacher" "Okay, Guoliang. Off you go, and don’t cause trouble for this young man."
    "The teacher nudges Shūzhēn forward to me. I reach out my hand for Guoliang to grab, but he doesn’t take it."
    #show i shocked at left
    "Instead he just scoffs and walks next to me, without so much as a glance in my direction."
    hide gl
    "Teacher" "You two take care!"
    show i normal at left
    "I waved back to the teacher as she saw us out with a smile."
    hide i

    scene bg market with fade
    "As I walked Guoliang through the market, I ask him about anything he wants to have."
    show i normal at left
    show gl at right
    i "So, Guoliang… is there anything in particular you want? Something you’re in the mood for? You name it, I can get it for you!"
    gl "What do you care?"
    #show i shocked at left
    i "I’m just asking. Thought I’d get you a treat so you’re more comfortable around me."
    gl "Hah! Like that’ll win me over."
    i "So… is that a no…?"
    gl "Why did my grandparents even send you to get me? I can get back on my own like I always do."
    show i normal at left
    i "Apparently you’ve been getting yourself into a lot of trouble, young man."
    gl "Have not!"
    #show i annoyed at left
    i "Don’t deny it. I’ve seen you being all mischievous."
    i "Setting animals loose, shooting rubber bands, kicking shuttlecocks at people…"
    gl "Hmph. They got what they deserved."
    i "{i}Some kid.{/i}"
    show i normal at left
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
    show i normal at middle
    i "He sure has a lot of energy, even for a little kid."
    i "*sigh* This is becoming more of a hassle than I thought it would be."
    hide i
    "I begin searching around the area for him."
    "If it’s anything like those chase scenes in movies, he probably hid behind a corner and waited til I ran past him."
    "So I search behind every corner, and after a few minutes of looking around, I find him hiding behind some crates of fruits."
    show gl at middle
    "It looks like he’s about to shoot a rubber band at some fruit vendor."
    show gl at right
    show i normal at left
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
    show i normal at left
    gl "Agh! Let go of my hand!"
    i "So you can run away again? Not a chance."
    "I drag Guoliang along with me."
    #show i nervous at middle
    show i normal at middle
    hide gl
    "Maybe I should just bring him back to his grandparents and hope that that’s enough."
    "..."
    "..."
    show i normal at middle
    "No."
    "I made a vow to help the people of this town before their end, and I’ll see it through."
    #show i annoyed at middle
    "Even if it means dealing with this runt."
    show gl at right
    show i normal at left
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
    show i normal at left
    "Doesn’t look like Guoliang wants to talk anymore. He’s really giving me a tough time!"
    "I already spent a good amount of time trying to help this old couple, and I am not about to back out! They want their grandson to be happy, so I’m going to make him happy. I have to."
    #show i nervous at left
    "Before they all perish."
    show i normal at left
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
            show i normal at left
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
            show i normal at left
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
            show i normal at middle
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
            show i normal at left
            show gl at right
            i "{i}That’s it! Kids love toys! If I buy him a brand new toy, then he’ll surely be happy! …at least, until doomsday arrives…{/i}"
            i "You want a toy, don’t you?"
            gl "Huh? What? No I don’t."
            i "I see you staring at those toys over there. Don’t be shy."
            gl "I said I do- hey!"
            "I take Guoliang to the toy store so he can pick out a toy."

            scene bg store
            #show i smile at left
            show i normal at left
            show gl at right
            i "Go on and pick any toy you want."
            gl "I told you I don’t want any toys."
            gl "Besides, toys are for little kids."
            show i normal at left
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
            show i normal at middle
            i "Excuse me. One [toy] for my little boy here, please."
            "The clerk hands me the [toy]."
            #show i smile at midddle
            i "Thank you!"
            show i normal at left
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
            show i normal at middle
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
    show i normal at middle
    #show i tired at middle
    i "*sigh* I guess this is one prayer I won’t be able to answer…"
    i "I just hope they don’t come back and haunt this place after they die."
    hide i
    gp "What was that, lad?"
    show i normal at left
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
    show i normal at left
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
    show i normal at left
    i "I… I can imagine."
    gp "We’re…"
    gp"We’re not gonna be around much longer… I know it."
    #show i shocked at left
    i "I… how do you-"
    gp "But at the very least, I want our grandson to experience the love of a parent before our time comes."
    gp"Can you grant us this last wish?"
    show i normal at left
    "I don’t know if this old man is delusional, or he saw right through me."
    "Regardless, I assure him that I’ll do what I am allowed to do for him."
    #show i smile at left
    i"Of course."
    gp"Mmm, good."
    "The grandfather slowly walks away."
    hide gp with fade
    #show i nervous at middle
    i"What a strange old man."
    show i normal at middle
    i"But now I know where to find Guoliang."
    hide i
    "After making sure I’m alone, I transform into a bird and fly over to the river to find Guoliang."
    "... ..."
    "... ..."
    gp"Haha… such a fine young man…"

    scene bg riverside
    "I fly overhead to the river, and after surveying the area, I find Guoliang crouching by the riverside. Just like the old man said."
    "I land on the road by the river, quickly transforming back into a human."
    show i normal at middle
    "I’m about to walk over to Guoliang, but then I stop myself."
    #show i nervous at left
    show i normal at left
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
    show i normal at left
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
    show i normal at middle
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
    show i normal at middle
    i"To experience all of this, and at such a young age too…"
    i"There’s only one thing to do now."
    hide i
    i"Gently, I rub Guoliang’s back."
    show i normal at left
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

    
    "To be continued"



    jump end

    
label Hana_arc:
    "Come here on a later date again!"


label end:
    return

