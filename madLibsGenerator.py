from tkinter import *
from tkinter.ttk import Combobox

# Story Variable
noun = "----"
anoun = "----"
pnoun = "----"
adj = "----"
verb = "----"
adverb = "----"
potb = "----"
excl = "----"
surname = "----"
animal = "----"

class StoryGenerator:
    @staticmethod
    def dentist():
        story = Tk()
        story.title("A VISIT TO THE DENTIST")
        story.geometry('510x525')

        # Texts in 'dentist' Story
        Label(story, text=f'''\tA one-act play to be performed by two {pnoun} in this room.
        PATIENT: Thank you so very much for seeing me, Doctor {surname},
        \t  on such {adj} notice.

        DENTIST: What is your problem, young {noun}?

        PATIENT: I have a pain in my upper {anoun}, which is giving me
        \t  a severe {potb} ache.

        DENTIST: Let me take a look. Open your {potb} wide.
        \t  Good. Now I'm going to tap your {pnoun} with my {noun}.

        PATIENT: Shouldn't you give me a/an {anoun} killer?

        DENTIST: It's not necessary yet. {excl}! I think I see
        \t a/an {noun} in your upper {anoun}.

        PATIENT: Are you going to pull my {anoun} out?

        DENTIST: No, I'mgoing to {verb} your tooth and put in
        \t  a temporary {noun}.

        PATIENT: When do I come back for the {adj} filling?

        DENTIST: A day after I cash your {anoun}.''', font=("Arial Bold", 11), justify='left').pack()
        Button(story, text="Close", command=story.destroy).pack(pady=10)
    
    @staticmethod
    def sleep():
        story = Tk()
        story.title("A  GOOD  NIGHT'S  SLEEP")
        story.geometry('450x390')

        # Texts in 'sleep' Story
        Label(story, text=f'''\tHere are five {adj} suggestions to follow if you want a/an
        {adj} night's sleep:
        
        1. Open a window and fill your {potb} with fresh
        {noun} and then, exhale {adverb}.
        
        2. Exercise {adverb} at least 15 {pnoun} a day.
        Doctors and {adj} therapists suggest a combination
        of push-ups and {verb}-ups, jumping {pnoun},
        and, of course, deep {potb} bends.
        
        3. Drink a/an {potb} glass of warm {excl} a
        half hour before turning off your {anoun} and going to
        {noun}.
        
        4. If all else fails, count {animal} jumping over a/an
        {anoun}.
        
        5. WARNING: Never go to bed on a full {potb}.''', justify='left', font=("Arial Bold", 11)).pack()
        Button(story, text="Close", command=story.destroy).pack(pady=10)

    @staticmethod
    def picnic():
        story = Tk()
        story.title("FUN  FAMILY  PICNIC")
        story.geometry('510x325')

        # Texts in 'picnic' Story
        Label(story, text=f'''\tAs usual, our family {noun} was a/an {adj}
        disaster. Mom packed {anoun} sandwiches and {noun}
        salad, and Dad brought a volleyball and a/an {verb}.
        Once we got to the {anoun} grounds, my brother started
        shooting me with a water {animal}. But when I screamed, my
        mom got mad and said, \"You just calm down, young {surname}.\"
        Dad was having trouble setting up the {noun} net, so I
        offered to help, but he shouted at the top of his {pnoun}.
        \"Just stay out of the {anoun} !\" Then I went to lend a/an
        {potb} to Mom. \"Well, it's about time somebody
        offered to help,\" she said {adverb} as she rolled her
        {potb}. I spent the rest of the day eating Mom\'s
        roasted {pnoun} and watching Dad fight with the
        {adverb}. I wish we could be more like normal {pnoun}
        and spend weekends watching {adj} reruns.''', font=("Arial Bold", 11), justify='left').pack()
        Button(story, text="Close", command=story.destroy).pack(pady=10)

    @staticmethod
    def coaching():
        story = Tk()
        story.title("LIFE COACHING")
        story.geometry('510x435')

        # Texts in 'coaching' Story
        Label(story, text=f'''\tCoaching is a partnership between a/an {noun} and
        a/an {anoun} that is designed to help a disfunctional
        young {anoun} reach his or her {potb}.It
        is a step-by-{adverb} process that creates clarity and
        {noun}-filled moments. Here are some of the mental
        emotional, and {adj} benefits of coaching:

        • Discovering your inner {potb} and allowing it to play
        
        • Recovering from a traumatic {anoun} experience
        
        • Learning the art of \"{verb}\"
        
        • Learning how to change {adj} thinking
        
        • Learning how to protect yourself {adverb}
        
        The relationship between a/an {surname} and a coach
        transforms {pnoun}. Too bad it costs more money than
        you can shake a/an {animal} at. Maybe you could try
        squeezing one of those nice stress {pnoun} instead?''', font=("Arial Bold", 11), justify='left').pack()
        Button(story, text="Close", command=story.destroy).pack(pady=10)


main = Tk()
main.geometry("250x250")
main.title("Mad Libs Generator")
# main.wm_iconbitmap("Logo.ico") # Displays the custome logo instead of tkinter logo

def inputScreen(topic):
    def redirect():
        global noun
        global anoun
        global pnoun
        global adj
        global verb
        global adverb
        global potb
        global excl
        global surname
        global animal

        # Setting Values
        noun = val_noun.get()
        anoun = val_anoun.get()
        pnoun = val_pnoun.get()
        adj = val_adj.get()
        verb = val_verb.get()
        adverb = val_adverb.get()
        potb = val_potb.get()
        excl = val_excl.get()
        surname = val_surname.get()
        animal = val_animal.get()

        # make object of class
        story = StoryGenerator()

        if topic=="Dentist":
            story.dentist()
        elif topic=="Sleep":
            story.sleep()
        elif topic=="Picnic":
            story.picnic()
        elif topic=="Coaching":
            story.coaching()
        else:
            pass

    inputs = Tk()
    # Creating 'Talking' Input Screen
    inputs.title("Please Input Carefully!")
    inputs.geometry('380x350')

    Label(inputs, text="Select options related to the Story", font="Arial 14 bold", justify='left').pack(side=TOP, pady=7)
    # First Frame
    first = Frame(inputs)
    Label(first, text="Select one from these Nouns: ").pack(side=LEFT)
    val_noun = Combobox(first, state='readonly', width=20, values=(["grass", "bunny", "pine tree", "bumpit", "car", "table"]))
    val_noun.current(0)
    val_noun.pack(side=LEFT, padx=50)
    first.pack(side=TOP, pady=2)
    # Second Frame
    second = Frame(inputs)
    Label(second, text="Select another one from these Nouns: ").pack(side=LEFT)
    val_anoun = Combobox(second, state='readonly', width=20, values=["grass", "bunny", "pine tree", "bumpit", "car", "table"])
    val_anoun.current(1)
    val_anoun.pack(side=LEFT, padx=28)
    second.pack(side=TOP, pady=2)
    # Third Frame
    third = Frame(inputs)
    Label(third, text="Select one from these Plural Nouns: ").pack(side=LEFT)
    val_pnoun = Combobox(third, state='readonly', width=20, values=["lava lamps", "croissants", "masks", "exams"])
    val_pnoun.current(3)
    val_pnoun.pack(side=LEFT, padx=32)
    third.pack(side=TOP, pady=2)
    # Fourth Frame
    fourth = Frame(inputs)
    Label(fourth, text="Select one from these Adjectives: ").pack(side=LEFT)
    val_adj = Combobox(fourth, state='readonly', width=20, values=["sparkling", "voluptous", "groovy", "hot pink"])
    val_adj.current(3)
    val_adj.pack(side=LEFT, padx=38)
    fourth.pack(side=TOP, pady=2)
    # Fifth Frame
    fifth = Frame(inputs)
    Label(fifth, text="Select one from these Verbs: ").pack(side=LEFT)
    val_verb = Combobox(fifth, state='readonly', width=20, values=["boogie", "play"])
    val_verb.current(1)
    val_verb.pack(side=LEFT, padx=51)
    fifth.pack(side=TOP, pady=2)
    # Sixth Frame
    sixth = Frame(inputs)
    Label(sixth, text="Select one from these Adverbs: ").pack(side=LEFT)
    val_adverb = Combobox(sixth, state='readonly', width=20, values=["heartlessly", "expectantacy", "fearlessly"])
    val_adverb.current(2)
    val_adverb.pack(side=LEFT, padx=43)
    sixth.pack(side=TOP, pady=2)
    # Seventh Frame
    seventh = Frame(inputs)
    Label(seventh, text="Select one from these Parts of the body: ").pack(side=LEFT)
    val_potb = Combobox(seventh, state='readonly', width=20, values=["tonsils", "belly", "toes", "head", "mind"])
    val_potb.current(1)
    val_potb.pack(side=LEFT, padx=19)
    seventh.pack(side=TOP, pady=2)
    # Eighth Frame
    eighth = Frame(inputs)
    Label(eighth, text="Select one from these Exclamatories: ").pack(side=LEFT)
    val_excl = Combobox(eighth, state='readonly', width=20, values=["amaze", "awesome", "wow"])
    val_excl.current(1)
    val_excl.pack(side=LEFT, padx=28)
    eighth.pack(side=TOP, pady=2)
    # Nineth Frame
    nineth = Frame(inputs)
    Label(nineth, text="Select one from these Surnames: ").pack(side=LEFT)
    val_surname = Combobox(nineth, state='readonly', width=20, values=["Singh", "Sharma", "Singhal", "Dhoni", "Kholi", "Bumrah"])
    val_surname.current(3)
    val_surname.pack(side=LEFT, padx=37)
    nineth.pack(side=TOP, pady=2)
    # Tenth Frame
    tenth = Frame(inputs)
    Label(tenth, text="Select one from these Animals: ").pack(side=LEFT)
    val_animal = Combobox(tenth, state='readonly', width=20, values=["dogs", "cats", "humans", "kangaroos"])
    val_animal.current(3)
    val_animal.pack(side=LEFT, padx=42)
    tenth.pack(side=TOP, pady=2)
    # Eleventh Frame
    eleventh = Frame(inputs)
    Button(eleventh, text="Close", command=inputs.destroy).pack(side=RIGHT, padx=10, pady=10)
    Button(eleventh, text="Submit", command=redirect).pack(side=RIGHT, padx=10, pady=10)
    eleventh.pack(side=TOP, pady=5)

# text of main screen
# font="Arial 17 bold"
Label(main, text="Mad Libs Generator", font=("Arial Bold", 17), justify='center').pack(pady=10)

# buttons of main screen
btn = Frame(main)
Button(btn, text="A  VISIT  TO  THE  DENTIST", command=lambda clicked="Dentist": inputScreen(clicked), padx=8).pack(pady=5)
Button(btn, text="A  GOOD  NIGHT'S  SLEEP", command=lambda clicked="Sleep": inputScreen(clicked), padx=11).pack(pady=5)
Button(btn, text="FUN  FAMILY  PICNIC", command=lambda clicked="Picnic": inputScreen(clicked), padx=22).pack(pady=5)
Button(btn, text="LIFE  COACHING", command=lambda clicked="Coaching": inputScreen(clicked), padx=35).pack(pady=5)
Button(btn, text="Close", command=main.destroy, padx=7).pack(pady=8)
btn.pack()

main.mainloop()
