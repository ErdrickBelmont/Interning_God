#diable close project confirmation
init python:
    config.quit_action = None

#image resize
image bg temple = im.Scale("temple.avif", 1980, 1080)
image bg tea house = im.Scale("House in front of a tea field.avif", 1980, 1080)
image bg school = im.Scale("elementary school.avif", 1980, 1080)
image bg market = im.Scale("market.avif", 1980, 1080)
image bg cat = im.Scale("cat.avif", 1980, 1080)
image bg bridge = im.Scale("bridge.avif", 1980, 1080)
image bg food stall = im.Scale("food stall.avif", 1980, 1080)

image i ancient = im.Scale("intern-ancient.png", 225 * 1.6, 280 * 1.6)
image gl = im.Scale("child-normal.png", 200 * 1.6, 280 * 1.6)
image gp = im.Scale("grandpa-normal.png", 200 * 1.6, 280 * 1.6)
image gm = im.Scale("granny-normal.png", 200 * 1.6, 280 * 1.6)
image i normal = im.Scale("intern-modern.png", 210 * 1.6, 280 * 1.6)
#prompt for future use: image  = im.Scale(".png",  * 1.6,  * 1.6)

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
        jump arc2

label Guoliang_arc:

    scene bg tea house
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
    menu:
        "Buy some street food":
            scene bg food stall
            "buy food"
        
        "Buy a toy for them":
            "buy toy"
    
    "write this tomorrow"



    jump end

    
label arc2:
    "Come here on a later date again!"



label end:
    return

label dClockUpdate:


