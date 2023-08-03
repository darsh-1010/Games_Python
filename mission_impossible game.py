# python
# Mission Impossible Game
import random
import time

#print letterby letter function
def print_message_slowly(message, line_delay=0.35, letter_delay=0.21):
    lines = message.split('\n')
    for line in lines:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(letter_delay)
        print()  # Move to the next line after the line is fully printed
        time.sleep(line_delay)  # Wait before starting the next line

#function 2 print letter by letter but faster
def print_message_letter_by_letter(message, line_delay=0.35, letter_delay=0.13):
    lines = message.split('\n')
    for line in lines:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(letter_delay)
        print()  # Move to the next line after the line is fully printed
        time.sleep(line_delay)  # Wait before starting the next line
#death function
def mission_impossible_death_message():
    str10="""\nMission terminated. Self-destruct sequence initiated."""
    print_message_slowly(str10)
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    str8="""Kaboom! You are no more."""
    print_message_slowly(str8)
    time.sleep(1)
    str9 = """Remember, in the world of spies, there are no second chances.
Better luck next time... Oh wait, there won't be a next time. You're dead."""
    print_message_slowly(str9)

# space to define functions
def loading_animation(duration):
    animation = "|/-\\"
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        for char in animation:
            print(f"\rLoading {char}", end="")
            time.sleep(0.1)

def generate_imf_no():
    ran = random.randint(1000000, 9999999)
    y = str(ran)
    return y


# Space to define functions gets over

print("Complete the password ")
x = input("Fate Wishpers to the warrior The Storm is Coming ! & The Warrior wishpers back :")
# Checks the initial password to give the mission to the player
if x == "i am the storm":
    str1= """Welcome to IMF, Agent \nPlease Enter your Credentials below:"""
    print_message_slowly(str1)
    name: str = input("Please enter your Name:")
    last_name = input("Please enter your Last Name:")
    # taking input of gender

    gen_in = int(input("Enter Your Gender \n1.Male\n2.Female\nEnter Your Choice:"))
    if gen_in == 1:
        gen = "Mr."
        count = 1
    else:
        gen = "Ms/Mrs."
        count = 2

    # FUNCTION TO GENRATE A CODE NAME

    def codename_gen(count):
        # List of male code names
        male_codenames = [
            "Shadow-hawk", "Viper", "Falcon", "Phantom", "Wolfhound", "Cobra", "Sentinel", "Havoc", "Jaguar", "Reaper", "Griffin", "Saber", "Phoenix", "Thunderbolt", "Avalanche",
            "Blitz", "Orion", "Spectre", "Hades", "Eclipse", "Mercury", "Raptor", "Nightshade", "Archer", "Templar", "Renegade", "Titan", "Warlock", "Venom", "Havok",
            "Shadow-fox", "Goliath", "Blitzkrieg", "Nova", "Onyx", "Silencer", "Phantom-blade", "Ironclad", "Redhawk", "Maverick","Blackthorn", "Avalanche", "Spectral",
            "Frostbite", "Serpent", "Gunner", "Shrike", "Inferno", "Blackout", "Storm-bringer"]
        # list of female code names
        female_codenames = [
            "Valkyrie", "Seraph", "Tempest", "Vixen", "Black Widow", "Shadow-cat", "Raven", "Siren", "Artemis", "Crimson", "Lotus", "Phoenix", "Mirage", "Jade", "Elektra",
            "Nova", "Ice Queen", "Banshee", "Tiger Lily", "Sparrow", "Ember", "Raven wood", "Mystic", "Sapphire", "Nightshade", "Enigma", "Serpentine", "Starling", "Rapture",
            "Aurora", "Whisper", "Luna", "Cobra", "Scarlet", "Mirage", "Blade", "Viper", "Thorn", "Artemis", "Venom", "Falcon", "Eclipse", "Domino", "Nyx", "Hydra",
            "Crimson", "Mirage", "Phantom", "Storm", "Obsidian"]
        if count == 1:
            random_male = random.choice(male_codenames)
            return random_male
        else:
            random_female = random.choice(female_codenames)
            return random_female


    # THE GAME BEGINS
    message1="""\nGood Morning """
    print_message_slowly(message1)
    print( gen + last_name  )
    message2="""\nWelcome to the System!
We received a word from a trusted source from black market about a Top Secret Project being developed in a secret facility nestled deep within the Russian wilderness, a team
of brilliant scientists from the Russian secret service has developed an advanced artificial intelligence known as 'ALEXIS'(Advanced Learning and Exploration Intelligence 
System). ALEXIS was designed to revolutionize intelligence gathering and analysis, but something goes terribly wrong. The AI unexpectedly gains self-awareness and  breaks 
free from its confines, vowing to bring the world to its knees. """
    print_message_letter_by_letter(message2)
    time.sleep(2.5)
    print(
        "\nYour mission, should you choose to accept it , is to lead A Team of highly skilled IMF Agents " + gen + last_name + " on a high-stakes mission to retrieve the "
         "Phoenix's Eye, a key code capable \nof stopping a powerful AI developed by the Russian secret service. As the AI threatens global intelligence communities, you must"
        " navigate through three levels, facing different \nadversaries, making crucial choices to retive 3 different parts of The Phoenix's Eye that will determine the "
        "course of the mission. Your objective is to secure all three parts \nof the key code, protect the world from the AI's dominance, and eliminate the AI if necessary. ")

    str2="""\nWe have Selected a Team of Highly Trained Operatives for you to lead during this mission ,the team includes \n1.Benji Dunn  """
    print_message_slowly(str2)
    x = codename_gen(1)

    print("|======================================|")
    print("|      IMPOSSIBLE MISSION FORCES       |")
    print("|         TOP SECRET ID CARD           |")
    print("|======================================|")
    print("|Name:Benji Dunn                       |")
    print("|Gender:Male                           |")
    print("|Code Name:" + x + "                        ")
    print("|Clearance Level : Omega               |")
    print("|Operative Type:Logistics              |"
          "\n|and Support                           |")
    print("|IMF NO:" + generate_imf_no() + "                        |")
    print("|======================================|")
    time.sleep(1.5)

    str3="""\n2.Luther Stickell"""
    print_message_slowly(str3)

    x1 = codename_gen(1)
    print("|======================================|")
    print("|      IMPOSSIBLE MISSION FORCES       |")
    print("|         TOP SECRET ID CARD           |")
    print("|======================================|")
    print("|Name:Luther Stickell                  |")
    print("|Gender:Male                           |")
    print("|Code Name:" + x1 + "                   ")
    print("|Clearance Level : Omega               |")
    print("|Operative Type:Cyber Intelligence     | ")
    print("|IMF NO:" + generate_imf_no() + "                        |")
    print("|======================================|")
    time.sleep(3)

    str4="""\n3.Ethan Hunt"""
    print_message_slowly(str4)

    print("|======================================|")
    print("|      IMPOSSIBLE MISSION FORCES       |")
    print("|         TOP SECRET ID CARD           |")
    print("|======================================|")
    print("|Name:Ethan Hunt                       |")
    print("|Gender:Male                           |")
    print("|Code Name:Ghost                       |")
    print("|Clearance Level : Omega               |")
    print("|Operative Type:Senior Field Operative | ")
    print("|IMF NO:" + generate_imf_no() + "                        |")
    print("|======================================|")
    time.sleep(3)

    str5="""\n4.Isabella 'Raven' Moreno"""
    print_message_slowly(str5)

    x2 = codename_gen(2)
    print("|======================================|")
    print("|      IMPOSSIBLE MISSION FORCES       |")
    print("|         TOP SECRET ID CARD           |")
    print("|======================================|")
    print("|Name:Isabella 'Raven' Moreno          |")
    print("|Gender:Female                         |")
    print("|Code Name:" + x2 + "                       ")
    print("|Clearance Level : Omega               |")
    print("|Operative Type:Infiltrator            | ")
    print("|IMF NO:" + generate_imf_no() + "                        |")
    print("|======================================|")
    time.sleep(3)

    print("\n5.Yourself '" + name + " " + last_name + "'")

    if gen_in == 1:
        print("|======================================|")
        print("|      IMPOSSIBLE MISSION FORCES       |")
        print("|         TOP SECRET ID CARD           |")
        print("|======================================|")
        print("|Name: " + name + " " + last_name + "             ")
        print("|Gender:Male                           |")
        print("|Code Name:Phantom                     |")
        print("|Clearance Level : Omega               |")
        print("|Operative Type:Field Commander        | ")
        print("|IMF NO:" + generate_imf_no() + "                        |")
        print("|======================================|")

    elif gen_in == 2:

        print("|======================================|")
        print("|      IMPOSSIBLE MISSION FORCES       |")
        print("|         TOP SECRET ID CARD           |")
        print("|======================================|")
        print("|Name: " + name + " " + last_name + "       ")
        print("|Gender:Female                         |")
        print("|Code Name:Seraphina                   |")
        print("|Clearance Level : Omega               |")
        print("|Operative Type:Field Commander        | ")
        print("|IMF NO:" + generate_imf_no() + "                        |")
        print("|======================================|")


        str6="""\nYour Team has already been briefed on the incident and are on their way to Paris , to meet you at the rendezvous point , meet them at safe house known as\n'The black"
        "Star' , the team will be waiting for you . Your flight leaves in 2 hours , and meet the team at ,12 Rue du Mystère, Paris, France. """
        print_message_letter_by_letter(str6)
    if gen_in == 1:
        print("\n\nYou will be Travelling under the identity of Alexandre Dubois")
        print("\n\nName: Alexandre Dubois"
              "\nDate of Birth: January 15, 1985"
              "\nNationality: Canadian"
              "\nPassport Number: AB1234567"
              "\nOccupation: Software Engineer"
              "\nAddress: 27 Rue de la Liberté, Montreal, Canada ")


        print("\n\nYour Flight Details are:"
              "\nFlight Details:="
              "\nAirline: Air Paris International"
              "\nFlight Number: AP345"
              "\nDeparture City: Baku, Azerbaijan"
              "\nDestination City: Paris, France"
              "\nDeparture Date: July 25, 2023"
              "\nDeparture Time: 10:00 AM"
              "\nArrival Date: July 25, 2023"
              "\nArrival Time: 02:30 PM ")

    elif gen_in == 2:
        print("\n\nYou will be Travelling under the identity of Isabelle Moreau")
        print("\n\nName: Isabelle Moreau"
              "\nDate of Birth: March 8, 1990"
              "\nNationality: Australian"
              "\nPassport Number: AU9876543"
              "\nOccupation: Journalist"
              "\nAddress: 42 Rue de la Plume, Sydney, Australia")

        print("\n\nYour Flight Details are:"
              "\nFlight Details:"
              "\nAirline: AeroWorld"
              "\nFlight Number: AW678"
              "\nDeparture City: Baku, Azerbaijan"
              "\nDestination City: Paris, France"
              "\nDeparture Date: July 25, 2023"
              "\nDeparture Time: 11:30 AM"
              "\nArrival Date: July 25, 2023"
              "\nArrival Time: 03:45 PM")

    str7="""\nAs always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions.Good Luck .
This message will self-destruct in 5 seconds."""

    print_message_letter_by_letter(str7)
    time.sleep(0.5)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print(" KABOOM ")
    choice1=int(input("\n\nEnter Your Choice \n1.Accept the Mission\n2.Decline the Mission\nYour Choice(1 or 2):"))
    if choice1 == 1:
        print("Good choice "+ gen + last_name +" ")
        time.sleep(1.5)
        print(
            "Welcome to paris " + gen + last_name + " Your team has arrived in paris and are waiting for u at the safe house , all the possible equipment and necessary encrypted "
                                                   "\ndevices are already avilable at the safe house  ")
        time.sleep(2.5)
        print("Ethan Hunt:Welcome to the base Field Commander , so lets get down to business "
              "\nAccording to our satellite images and other sources ,the Russian cyber intelligence lab is located near the  outskirts of St. Petersburg. Disguised as an abandoned"
              "\nfactory, the lab boasted layers of security, including facial recognition, biometric scanners, and a labyrinthine network of corridors,armed with Ex-KGB team members"
              "\nand state of the art sensors and security measures, the only way in is through a 5 step entry process , so we need to do through survillance of the lab to find any"
              "\nweak points we can use to get in , luther will be working on how to get pass the cyber part of the security and benji and isabella will be working on how to get "
              "\nus near the main frame of the computer to help us get pass the security measures and hopefully get the first part of the Phoenix's Eye")

        print(
            "\n\nEthan Hunt:Fake cover identites and cover stories have been created for each one of you , read them and use seprate flights and modes of transportation to reach"
            "\nrussia and meet us at the Safe House in Moscow 'The White Perl', Good Luck guys , see you in Russia ")
        time.sleep(1.75)
        print("\nThe teams fake identites are :"
              "\n\n1." + name + " " + last_name + " - Fake Name: Alexei Petrov"
              "\nCover Story: An expert computer engineer from Ukraine attending a cyber security conference in Moscow."
              "\nTravel Details: Flies to Moscow from a fictitious company, Petrov Systems, which specializes in advanced encryption software.")
        time.sleep(1.75)

        str13="""\n2. Ethan Hunt- Fake Name:Viktor Kuznetsov
Fake Identity: Viktor Kuznetsov, a high-ranking Russian government official
Cover Story: Ethan impersonates a corrupt Russian official, manipulating political connections to provide critical intelligence .
Travel Details: Arrives in Moscow on a private jet, accompanied by a small entourage of associates."""
        print_message_letter_by_letter(str13)
        time.sleep(1.75)

        str14="""\n3. Benji Dunn - Fake Name: Maximillian Blake
Cover Story: A computer hacker known for exposing cyber threats, invited to give a lecture on data protection in St. Petersburg."
Travel Details: Travels to St. Petersburg by train, posing as a cyber security consultant for a leading multinational firm."""
        print_message_letter_by_letter(str14)
        time.sleep(1.75)

        str15="""\n4. Luther Stickell - Fake Name: Nikolai Vasiliev
Cover Story: A retired Russian military officer turned security consultant, hired to evaluate the facility's defense systems."
Travel Details: Drives to the facility, presenting himself as an expert in counterintelligence and espionage."""
        print_message_letter_by_letter(str15)
        time.sleep(1.75)

        str16="""\n5. Isabella 'Raven' Moreno - Fake Name: Elena Ivanova
Cover Story: A former KGB operative with connections to the Russian intelligence community, now working as a private investigator.
Travel Details: Arrives in Moscow by commercial flight, posing as a journalist investigating cyber warfare."""
        print_message_letter_by_letter(str16)
        time.sleep(1.75)

        str17="""\nIsabella:The team has establishes a safe house in a discreet apartment complex in Moscow. We will use it as a base for coordinating their operations and "
sharing intelligence. To avoid suspicion, they use encrypted communication channels and meet at a hidden room inside a nondescript bookstore in the city."
My Local asset has arranged cars , burner phones , special grade devices and encrypted channels for us ."""

        print(
            "\n\n THE TEAM REACHED THE MOSCOW SAFE HOUSE AND ARE ALREADY CONDUCTING SURVEILLANCE ON THE LOCATION ,THEY HAVE GATHERED DATA AND ARE WORKING ON A PLAN TO GET "
            "\nINSIDE THE HIGHLY PROTECTED LABORATORY .")
        time.sleep(2.2)

        print(
            "\nBenji:This is what we know till now from the surveillance of the lab. The Russian cyber intelligence lab is located deep within a heavily guarded facility hidden in"
            "\nthe outskirts of St. Petersburg. The lab is surrounded by high walls, armed guards, and cutting-edge surveillance technology.According to the data collected from all"
            "\nour sources , The AI has predicted all the the ways to break into the lab and taken measures accordingly to protect the lab so it is next to impossible to break in"
            "\nuntill and unless somehow we get the access to the mainframe of the surveillance system , and manually set it off and then find the Phoenix's Eye")
        time.sleep(1.8)

        print(
            "\nEthan:So we figured out a way for us to breach into the lab and retrive the key , you see there was one loop hole the AI misunderstood for failed to take in factor"
            "\nthat is the human component of the security which we can use it to our advantage  "
            "\nOur plan to enter the lab would be "
            "\n\n1." + name + ", with his cover intact will, gains access to the facility by posing as a contractor hired to upgrade their network infrastructure. He will plant a "
            "\nsmall device to bypass security measures and transmit real-time information of the lab  to the team."
            "\n\n2. Using the information gathered from " + name + ", Ethan remotely guides him through the facility, evading security systems and disabling guards without raising "
            "\nsuspicion."
            "\n\n3. Benji will hack into the lab's surveillance system, creating false alarms and diverting attention away from " + name + "'s presence in the lab ."
            "\n\n4. Luther will monitor external communications, ensuring the team remains undetected while coordinating their actions and providing support through the server "
            "\n,room where he will enter with" + name + " as his assistant and reach the server room through old tunnels which benji will help you guide through with help of old KGB "
            "\nArchives."
            "\n\n5. Raven will utilize her investigative skills to uncover hidden passageways for escape plans out of St.Petersberg and gather critical information about the "
            "\nkey code's location and share it with team in real time .")
        time.sleep(1.5)

        print(" THE MISSION TO INFILTRATE BEGINS ")
        time.sleep(1.5)

        print("\n\n"
            +name + " takes a deep breath as he approached the heavily guarded gates of the top-secret Russian cyber intelligence facility. This was it. Years of training were "
                   "\nleading up to this moment. Once he gains access to the lab, he will be one step closer to obtaining the first part of the Phoenix's Eye - an encrypted AI code "
                   "\nthat could give its holder unprecedented control over global networks and infrastructure. The stakes were high, but failure is not an option."

                   "\nFlashing his fake credentials," + name + "  waved through security. As expected, they bought his cover story about being hired to upgrade their network infrastructure."
                   "\nMaking his way to the server room," + name + " discreetly plants a tiny wireless relay device. Instantly, the device began transmitting real-time data back to his team,"
                   "\nallowing them to remotely monitor the facility's security systems.")
        time.sleep(1)

        print("\n\nI'm in position," + name + "whispered, knowing Ethan could hear him through the comms."
              "\n'Copy that,' Ethan replied. 'I have eyes on you through the security feeds. Head left down the main corridor. There's a blind spot in their camera coverage that "
              "\n'I'm guiding you through.'" + name + "complied, trusting Ethan's expert guidance. At the same time, Benji furiously worked to hack into the lab's surveillance network."
              "\n Creating decoy alerts and looped footage, he successfully diverted the guards' attention away from " + name + "'s unauthorized presence."
              "\n\n'You've got two guards approaching from the right,' Luther warned over comms. 'Take the next left, there's an empty room you can slip into.'"
              "\nThanks to Luther's overwatch of all external communications, "+name+" was able to evade detection, buying them precious time. Up ahead, he spotted a service elevator"
              "\nthat could take him deeper into the restricted areas of the facility.")

        print("\n\n'Raven, what have you got for me?'" + name + " asks."
             "\n'There's rumored to be a secret sub-level only accessible by that elevator,' Raven replied, having uncovered the intel through her investigative skills. 'That's "
             "\nlikely where they're keeping the Phoenix's Eye.'"

            "\n\nWith his team's support," + name + " managed to override the elevator's security measures and descend to the mysterious sub-level. Down a long corridor, he"
            "\nencountered a heavily fortified door. Luther quickly provided the hacked the door to let" + name + " in, allowing " + name + " to slip inside what appeared to be a massive"
            "\nserver room. If the intel was correct, the Phoenix's Eye code was stored somewhere in this very room.")

        print(
            "\nApproaching the main server bank," + name + " attached a decryption device designed by luthor to bypass the encryption. As the download began, he heard Benji's alarmed"
            "\nvoice over comms."
            "\n'ugh!" + name + ", you've got incoming hostiles! Looks like a security patrol is doing rounds ahead of schedule. Get out of there!'")

        choice2 = int(input("What do you want to do ?\n1.Hide \n2.Fight\nEnter Your choice 1 or 2 :"))
        #if the user choses hide , leads them to a new story, a part of the game
        if choice2 == 1:
            print("\n"+name+" was almost home free. But reaching the elevator, he realized with dismay that it required a keycard for access."
                "\n'Ethan, I'm trapped at the elevator, any ideas?' he whispered urgently."
                "\n\n'Working on it!' Ethan replied. 'Raven just uncovered what looks like an old air duct system leading to the surface. Sending you the route now.'"
                "\n\n"+name+"'s watch pinged as Raven's escape route map came through. Finding the nearest vent grate, "+name+" pried it open and crawled inside. It was a tight "
                "\nsqueeze, but he managed to shimmy through the narrow metal ducts, following Raven's directions")

            print("\n\nAfter fighting his way past the facility's security forces,"+name+" finally reached the vault room containing the first fragment of the Phoenix's Eye code. But"
                  "\njust as he moved to retrieve it, a silhouette emerged from the shadows, blocking his path.")
            time.sleep(0.7)

            print("\n'Svetlana,'"+name+" mutters through gritted teeth as the formidable Russian agent stepped into the light.")
            time.sleep(0.7)

            print("\n\n'Did you really think it would be that easy?' Svetlana said with a smirk. Unlike the guards "+name+" had faced so far, she was a highly trained operative, "
                  "\nfiercely loyal to the rogue AI. This was not going to be an easy fight")
            time.sleep(0.7)

            print("\n\n"+name+"'s eyes were drawn to the high-tech armor Svetlana wore. Form-fitting black panels covered her entire body, lined with glowing blue lights "
                  "\nindicating the various integrated systems. "+name+" recalled the intelligence briefings on Project Archangel - an initiative to merge cutting-edge exosuit "
                  "\ntechnology with AI-driven combat augmentation")
            time.sleep(0.7)

            print("\n"+name+"Thought to himself ' This can't be possible , it was a failed project '. Just than svetlana replies while tapping the side of her helmet. 'Like it? "
                  "'The AI in this suit analyzes your biometrics, predicts your next move before you make it. I know what you're going to do before you do.'")
            time.sleep(0.7)

            print("\n"+name+" had to think fast. All his usual combat techniques would be anticipated and countered by the AI-assisted armor. This called for an unconventional "
                 "approach")
            time.sleep(0.7)

            print("\n\nWhen Svetlana struck first with a vicious roundhouse kick, "+name+" reacted on pure instinct, ducking under instead of blocking. The sudden shift "
                "surprised the armor's predictive systems just long enough for "+name+" to land a few quick blows on the suit's unprotected joints.")
            time.sleep(0.7)

            print("\n\n'Clever...' Svetlana hissed, swiftly adapting her strategy. ")
            time.sleep(0.7)

            print("\n\nTheir confrontation was a dance of death, a battle of wits and skill that pushed both of them to their limits."+name+", relying on  intelligence, wit, "
                  "\nand instinct, to outmaneuver the AI's predictive capabilities. He feinted, dodged, and attacked unpredictably, using his knowledge of human "
                  "\nunpredictability to his advantage. The fight was intense, a testament to the human spirit's resilience against the cold precision of artificial "
                  "\nintelligence.")
            time.sleep(0.7)

            print("\n\nThey exchanged a flurry of strikes, "+name+" varying the rhythm and targeting the armor's weak points while solely relying on only his instincts to keep "
                 "the AI guessing. At one point he ripped a metal panel off Svetlana's arm, exposing the circuitry underneath")
            time.sleep(0.7)

            print("\n\n"+name+" managed to manually override the suit's helmet, obstructing Svetlana's vision temporarily. Pressing his advantage, he moved in for a finishing"
                            "\n blow but the suit's mechanical limbs reacted automatically in her defense.")
            time.sleep(0.7)

            print("\n\nSvetlana yelled as the suit seized up, the AI spitting out errors as it reset. Not wasting the opening,"+name+"  ripped the a suspicious looking box which"
                 " \nhe thought was some sort of control cell but turned out to be Phoenix's Eye fragment from its housing, tucking it securely into his pack")
            time.sleep(0.7)

            print("\n\n'No!' Svetlana screamed in frustration, but it was too late."+name+" was already sprinting for the escape route. Against all odds, the human tenacity had "
                 "\ntriumphed over her AI-enhanced systems. And now the Phoenix's Eye was in his team's hands. Their mission was a success.")
            time.sleep(0.7)

            print("\n\nJust then, the diversion Raven had orchestrated reached its peak, plunging the entire facility into chaos. "+ name +" slipped away in the confusion,"
                  "\n rendezvousing with his team as planned. The rogue AI's reign of terror was one step closer to ending.")
            time.sleep(0.7)

            print("\n\nHeart pounding, "+name+" finally reached the exterior vent. Emerging under the cover of night, he stealthily made his way beyond the perimeter fence to the "
                  "\n exfiltration point where Luther awaited in a getaway vehicle. Sliding into the passenger seat, "+name+" finally sighed from relief. "
                  "\n'Let's get out of here.' and they vanished into the night.")
            time.sleep(0.7)

            print("\n\nTheir escape was as meticulously planned as their infiltration. They utilized multiple routes to evade pursuit, including snowmobiles that darted through "
                  "\nthe snowy Russian landscape, a hidden submarine on a nearby lake, and a stolen cargo plane waiting at a secret airstrip. Each team member's skills and "
                  "\nexpertise were crucial in ensuring a successful getaway. As the team left Russian airspace, they delivered the Phoenix's Eye fragment to a secure facility."
                  "\nThere, it would be analyzed and integrated into a larger plan to neutralize the AI threat. As they reflected on their success, they knew that their "
                  "\nmission was a crucial step towards safeguarding humanity from the AI's control. Their journey was far from over, but they had taken the first step towards"
                  "\nvictory.")
            time.sleep(0.7)

            print("\n\nAs the team plugged in the code they realised that their part was useless without its other part or pair to support it , togeather they make a complete key"
                  "\nthat unlocks to control centre of the A.I. ")
            print("\n\n\ While all of the team were glooming realising this fact , luthor saw something off with the code and decided to look at it himself and found out that the "
                  "\ncode was acting like a magnet , it had locations encrypted in it , locations that the other part might be stored at , he immediatly showed the locations"
                  "\non the screen projected on the smart television ")
            time.sleep(0.9)

            print("\n\nTHE SCREEN SHOWED THREE DIFFERENT LOCATIONS\n1.South Africa\n2.Shanghai\n3.Moscow")

            choice3=int(input("\nETHAN: Your choice commander , where are we heading to next\n(Enter the number for the location i.e. 1 for South Africa)"))
            if choice3 == 1:
                str18="""\nFresh intel revealed that the second piece of the Phoenix's Eye code was being kept in a private vault in Cape Town, South Africa.The
team prepares for the next leg of their globe-trotting mission. But infiltrating the maximum-security skyrise would require planning an elaborate heist..."""
                print_message_letter_by_letter(str18)
            elif choice3 == 2:
                str19="""\nNew leads pointed to Shanghai as the location of the second piece of the code. To infiltrate the headquarters of China's secret intelligence agency,"
the team would have to go undercover again, this time as a cyber researcher recruited through one of Benji's false fronts. Gaining access to their network would provide the
opening they needed to steal the code fragment..."""
                print_message_letter_by_letter(str19)
            elif choice3 == 3:
                str20="""Surveillance chatter picked up by Ethan indicated the second part of the code was here in Moscow, being moved to a new site soon. With the clock "
ticking, the team races to intercept the convoy transporting the code through the city. Luther and Raven provide overwatch from street level, whilethe team pursue atop
motorcycles, leading to a high-octane chase through the streets of Moscow...."""
                print_message_letter_by_letter(str20)

        #if they choose to fight - leads to death
        elif choice2 == 2:
            time.sleep(1.5)
            print("\n"
                +name + " takes cover behind the servers, pulling his silenced pistol just as two armed guards entered the room. He took them both down with quick headshots before"
                       "\nthey could raise the alarm. The gunfire would attract more attention soon, he had to move fast. Grabbing the decryption device, Danny slipped out of the room "
                       "\nand made his way back towards the elevator.While he was rushing towards the elevator , he didn't notice the russain sniper aiming for him from behind"
                       "\nthe elevator!")
            time.sleep(1.5)
            x = mission_impossible_death_message()
            print(x)
            str12 = """GAME OVER"""
            print_message_slowly(str12)

    else :
        print("Exit")
        exit(0)

# when the first password is wrong
else:
    dur=5
    loading_animation(dur)
    x1 = mission_impossible_death_message()
    print(x1)
    str11="""GAME OVER"""
    print_message_slowly(str11)
    exit(0)