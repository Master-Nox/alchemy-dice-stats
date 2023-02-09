
# This is a proof of concept file for the Alchemy Dice Statistics extension.
# The Main goals of this project are as follows:
# Track each individual player's dice rolls.
# Track the DM's dice rolls.
# Output statistics when requested. Statistics include: Average number rolled, Number of times rolled, A breakdown of how many times each number was rolled using both whole numbers and percentages, How lucky/unlucky you are compared to the average, etc.
# Options for the DM to not have their dice rolls tracked/output.
# Option for the entire party's stats to be pooled/compared against one another.
# Separate statistics by session while also allowing for campaign wide statistics.
# Graphs
# Tracking who did the most/least damage, who crited/fumbled the most, who took the most/least damage, etc.
# More?

# TO BE WORKED ON
# Saving and Importing statistics to json/csv files.
# Party-wide Stats (Adding everyone's stats together and taking data/ Comparing party members.)
# DM-side statistics
# Options galore!
# Actually making it work with alchemy lmao(?)

import random as r

# OPTIONS
Output_DM_Stats = False
Allow_Player_Comparison = True
Allow_Player_Stat_Pooling = True

# Start

# Have a constantly running while loop for when a session starts/gameplay is occuring.

class Character_Intake:
    Characters = []
    # Initializes statistics for this particular character. Will need to save these to a file and reload them later.
    def __init__(self, Character_Name):
        self.__class__.Characters.append(self)
        
        self.Character_Name = Character_Name
        
        # Die rolls
        self.Total_Rolls = 0
        self.Total_Average = 0
        
        self.D100_Rolls = []
        self.D20_Rolls = []
        self.D12_Rolls = []
        self.D10_Rolls = []
        self.D8_Rolls = []
        self.D6_Rolls = []
        self.D4_Rolls = []
        
        self.Attacks = []
        self.Skills = []
        self.Saves = []
        self.Misc = []
        
        self.Nat20_Counter = 0
        self.Nat1_Counter = 0
        
        self.Damage_Recieved_Tracker = {"acid": [], "bludgeoning": [], "cold": [], "fire": [], "force": [], "lightning": [], "necrotic": [], "piercing": [], "poison": [], "psychic": [], "radiant": [], "slashing": [], "thunder": []}
        self.Total_Damage_Recieved = 0
        self.Highest_Single_Hit_Damage_Recieved = 0
        
        self.Damage_Dealt_Tracker = {"acid": [], "bludgeoning": [], "cold": [], "fire": [], "force": [], "lightning": [], "necrotic": [], "piercing": [], "poison": [], "psychic": [], "radiant": [], "slashing": [], "thunder": []}
        self.Total_Damage_Dealt = 0
        self.Highest_Single_Hit_Damage_Dealt = 0

        self.Highest_Single_Hit_Healing = 0
        self.Total_Healing_Dealt = 0
        self.Total_Healing_Recieved = 0
        self.Healing_Dealt = []
        self.Healing_Recieved = []

# Intakes rolls to be counted for statistics.
# Any roll that you want to be counted should follow the format of (DieType, Number, Attribute) and example would be (20, 15, attack) for someone rolling a d20, rolling the number 15, and for the roll to be an attack roll.
# If you want to add an attribute you have to add it as a case below.
# Text formatting is done entirely around the output, so look for that there.    
    def Intake(self, DieType, Number, Attribute):
        self.Total_Rolls += 1
        if DieType == 20 and Number == 20:
            self.Nat20_Counter += 1
        elif DieType == 20 and Number == 1:
            self.Nat1_Counter += 1

        match DieType:
            case 100:
                self.D100_Rolls.append(Number)
            case 20:
                self.D20_Rolls.append(Number)
            case 12:
                self.D12_Rolls.append(Number)
            case 10:
                self.D10_Rolls.append(Number)
            case 8:
                self.D8_Rolls.append(Number)
            case 6:
                self.D6_Rolls.append(Number)
            case 4:
                self.D4_Rolls.append(Number)
            case "NA":
                pass
        
        match Attribute:
            case "attack":
                self.Attacks.append(Number)
            case "skill":
                self.Skills.append(Number)
            case "save":
                self.Saves.append(Number)
            case "misc":
                self.Misc.append(Number)
            case "acid R":
                self.Damage_Recieved_Tracker["acid"].append(Number)
            case "bludgeoning R":
                self.Damage_Recieved_Tracker["bludgeoning"].append(Number)
            case "cold R":
                self.Damage_Recieved_Tracker["cold"].append(Number)
            case "fire R":
                self.Damage_Recieved_Tracker["fire"].append(Number)
            case "force R":
                self.Damage_Recieved_Tracker["force"].append(Number)
            case "lightning R":
                self.Damage_Recieved_Tracker["lightning"].append(Number)
            case "necrotic R":
                self.Damage_Recieved_Tracker["necrotic"].append(Number)
            case "piercing R":
                self.Damage_Recieved_Tracker["piercing"].append(Number)
            case "poison R":
                self.Damage_Recieved_Tracker["poison"].append(Number)
            case "psychic R":
                self.Damage_Recieved_Tracker["psychic"].append(Number)
            case "radiant R":
                self.Damage_Recieved_Tracker["radiant"].append(Number)
            case "slashing R":
                self.Damage_Recieved_Tracker["slashing"].append(Number)
            case "thunder R":
                self.Damage_Recieved_Tracker["thunder"].append(Number)
            case "acid D":
                self.Damage_Dealt_Tracker["acid"].append(Number)
            case "bludgeoning D":
                self.Damage_Dealt_Tracker["bludgeoning"].append(Number)
            case "cold D":
                self.Damage_Dealt_Tracker["cold"].append(Number)
            case "fire D":
                self.Damage_Dealt_Tracker["fire"].append(Number)
            case "force D":
                self.Damage_Dealt_Tracker["force"].append(Number)
            case "lightning D":
                self.Damage_Dealt_Tracker["lightning"].append(Number)
            case "necrotic D":
                self.Damage_Dealt_Tracker["necrotic"].append(Number)
            case "piercing D":
                self.Damage_Dealt_Tracker["piercing"].append(Number)
            case "poison D":
                self.Damage_Dealt_Tracker["poison"].append(Number)
            case "psychic D":
                self.Damage_Dealt_Tracker["psychic"].append(Number)
            case "radiant D":
                self.Damage_Dealt_Tracker["radiant"].append(Number)
            case "slashing D":
                self.Damage_Dealt_Tracker["slashing"].append(Number)
            case "thunder D":
                self.Damage_Dealt_Tracker["thunder"].append(Number)
            case "healing D":
                self.Healing_Dealt.append(Number)
            case "healing R":
                self.Healing_Recieved.append(Number)
          
    def Output_Criticals(self):
        return self.Nat20_Counter, self.Nat1_Counter
       
# Outputs for Damage
# Recieved  
    def Output_Highest_Single_Hit_Damage_Recieved(self):
        try:
            self.Highest_Single_Hit_Damage_Recieved = max(max(self.Damage_Recieved_Tracker.values()))
            Damage_Type = max(self.Damage_Recieved_Tracker, key=self.Damage_Recieved_Tracker.get)
        except:
            self.Highest_Single_Hit_Damage_Recieved = 0
            Damage_Type = ""
        
        return self.Highest_Single_Hit_Damage_Recieved, Damage_Type
    
    def Output_Total_Damage_Recieved(self):
        Total_Damage_List = []
        for list in self.Damage_Recieved_Tracker.values():
            Total_Damage_List = Total_Damage_List + list
        self.Total_Damage_Recieved = sum(Total_Damage_List)
        return self.Total_Damage_Recieved
    
    def Output_Average_Damage_Recieved(self):
        Total_Damage_List = []
        try:
            for list in self.Damage_Recieved_Tracker.values():
                Total_Damage_List = Total_Damage_List + list
            AverageDamageRecieved = sum(Total_Damage_List)/len(Total_Damage_List)
        except:
            AverageDamageRecieved = 0
        return AverageDamageRecieved
    
    def Output_Type_With_Highest_Damage_Recieved(self):
        Damage_Type_Sum = {"acid": 0, "bludgeoning": 0, "cold": 0, "fire": 0, "force": 0, "lightning": 0, "necrotic": 0, "piercing": 0, "poison": 0, "psychic": 0, "radiant": 0, "slashing": 0, "thunder": 0}
        for source in self.Damage_Recieved_Tracker:
            Damage_Type_Sum[source] = sum(self.Damage_Recieved_Tracker[source])
        Highest_Damage_Damage_Type = max(Damage_Type_Sum, key=Damage_Type_Sum.get)
        Damage_From_Highest_Damage_Damage_Type = Damage_Type_Sum[Highest_Damage_Damage_Type]
        return Highest_Damage_Damage_Type, Damage_From_Highest_Damage_Damage_Type

# Dealt
    def Output_Highest_Single_Hit_Damage_Dealt(self):
        try:
            self.Highest_Single_Hit_Damage_Dealt = max(max(self.Damage_Dealt_Tracker.values()))
            Damage_Type = max(self.Damage_Dealt_Tracker, key=self.Damage_Dealt_Tracker.get)
        except:
            self.Highest_Single_Hit_Damage_Dealt = 0
            Damage_Type = ""
        return self.Highest_Single_Hit_Damage_Dealt, Damage_Type
    
    def Output_Total_Damage_Dealt(self):
        Total_Damage_List = []
        for list in self.Damage_Dealt_Tracker.values():
            Total_Damage_List = Total_Damage_List + list
        self.Total_Damage_Dealt = sum(Total_Damage_List)
        return self.Total_Damage_Dealt
    
    def Output_Average_Damage_Dealt(self):
        Total_Damage_List = []
        try:
            for list in self.Damage_Dealt_Tracker.values():
                Total_Damage_List = Total_Damage_List + list
            AverageDamageDealt = sum(Total_Damage_List)/len(Total_Damage_List)
        except:
            AverageDamageDealt = 0
        return AverageDamageDealt
    
    def Output_Type_With_Highest_Damage_Dealt(self):
        Damage_Type_Sum = {"acid": 0, "bludgeoning": 0, "cold": 0, "fire": 0, "force": 0, "lightning": 0, "necrotic": 0, "piercing": 0, "poison": 0, "psychic": 0, "radiant": 0, "slashing": 0, "thunder": 0}
        for source in self.Damage_Dealt_Tracker:
            Damage_Type_Sum[source] = sum(self.Damage_Dealt_Tracker[source])
        Highest_Damage_Damage_Type = max(Damage_Type_Sum, key=Damage_Type_Sum.get)
        Damage_From_Highest_Damage_Damage_Type = Damage_Type_Sum[Highest_Damage_Damage_Type]
        return Highest_Damage_Damage_Type, Damage_From_Highest_Damage_Damage_Type
    
# Outputs for Healing
    
    def Output_Total_Healing_Dealt(self):
        self.Total_Healing_Dealt = sum(self.Healing_Dealt)
        return self.Total_Healing_Dealt
    
    def Output_Total_Healing_Recieved(self):
        self.Total_Healing_Recieved = sum(self.Healing_Recieved)
        return self.Total_Healing_Recieved
    
    def Output_Highest_Single_Hit_Heal(self):
        try:
            self.Highest_Single_Hit_Healing = max(self.Healing_Dealt)
        except:
            self.Highest_Single_Hit_Healing = 0
        return self.Highest_Single_Hit_Healing
     
# Outputs for d20 Averages (and total rolls)

    def Output_Average_Attack(self):
        try:
            Attack_Average = sum(self.Attacks)/len(self.Attacks)
        except:
            Attack_Average = 0
        return Attack_Average
    
    def Output_Average_Skill(self):
        try:
            Skill_Average = sum(self.Skills)/len(self.Skills)
        except:
            Skill_Average = 0
        return Skill_Average
    
    def Output_Average_Save(self):
        try:
            Save_Average = sum(self.Saves)/len(self.Saves)
        except:
            Save_Average = 0
        return Save_Average
    
    def Output_Average_Misc(self):
        try:
            Misc_Average = sum(self.Misc)/len(self.Misc)
        except:
            Misc_Average = 0
        return Misc_Average
    
    def Output_Average_Total(self):
        Total_d20_Rolls = []
        Total_d20_Rolls = self.Attacks + self.Skills + self.Saves + self.Misc
        try:
            self.Total_Average = sum(Total_d20_Rolls)/len(Total_d20_Rolls)
        except:
            self.Total_Average = 0
        return self.Total_Average
       
    def Output_Total_Rolls(self):
        return self.Total_Rolls
       
# Initializing character and their associated stats. This will need to be done automatically for a party later on. 
Kalina = Character_Intake("Kalina Latour")
Loric = Character_Intake("Neralin Loric Sarliah")
Evangeline = Character_Intake("Evangeline Mikelle Devereaux")

# Dice rolling for testing purposes

for i in range(3000):
    Attribute = r.randint(1,32)
    
    CharacterRolling = r.randint(1,len(Character_Intake.Characters))
    match CharacterRolling:
        case 1:
            Character = Kalina
        case 2:
            Character = Loric
        case 3:
            Character = Evangeline
    
    if Attribute == 1:
        DieType = 20
    elif Attribute == 2:
        DieType = 20
    elif Attribute == 3:
        DieType = 20
    elif Attribute == 4:
        DieType = 20
    elif Attribute == 31:
        DieType = "NA"
    else:
        DieType = r.randint(3,7)
        match DieType:
            case 1:
                DieType = 100
            case 2:
                DieType = 20
            case 3:
                DieType = 12
            case 4:
                DieType = 10
            case 5:
                DieType = 8
            case 6:
                DieType = 6
            case 7:
                DieType = 4
    
    match Attribute:
        case 1:
            Character.Intake(DieType, r.randint(1,DieType), "attack")
        case 2:
            Character.Intake(DieType, r.randint(1,DieType), "skill")
        case 3:
            Character.Intake(DieType, r.randint(1,DieType), "save")
        case 4:
            Character.Intake(DieType, r.randint(1,DieType), "misc")
        case 5:
            Character.Intake(DieType, r.randint(1,DieType), "acid R")
        case 6:
            Character.Intake(DieType, r.randint(1,DieType), "bludgeoning R")
        case 7:
            Character.Intake(DieType, r.randint(1,DieType), "cold R")
        case 8:
            Character.Intake(DieType, r.randint(1,DieType), "fire R")
        case 9:
            Character.Intake(DieType, r.randint(1,DieType), "force R")
        case 10:
            Character.Intake(DieType, r.randint(1,DieType), "lightning R")
        case 11:
            Character.Intake(DieType, r.randint(1,DieType), "necrotic R")
        case 12:
            Character.Intake(DieType, r.randint(1,DieType), "piercing R")
        case 13:
            Character.Intake(DieType, r.randint(1,DieType), "poison R")
        case 14:
            Character.Intake(DieType, r.randint(1,DieType), "psychic R")
        case 15:
            Character.Intake(DieType, r.randint(1,DieType), "radiant R")
        case 16:
            Character.Intake(DieType, r.randint(1,DieType), "slashing R")
        case 17:
            Character.Intake(DieType, r.randint(1,DieType), "thunder R")
        case 18:
            Character.Intake(DieType, r.randint(1,DieType), "acid D")
        case 19:
            Character.Intake(DieType, r.randint(1,DieType), "bludgeoning D")
        case 20:
            Character.Intake(DieType, r.randint(1,DieType), "cold D")
        case 21:
            Character.Intake(DieType, r.randint(1,DieType), "fire D")
        case 22:
            Character.Intake(DieType, r.randint(1,DieType), "force D")
        case 23:
            Character.Intake(DieType, r.randint(1,DieType), "lightning D")
        case 24:
            Character.Intake(DieType, r.randint(1,DieType), "necrotic D")
        case 25:
            Character.Intake(DieType, r.randint(1,DieType), "piercing D")
        case 26:
            Character.Intake(DieType, r.randint(1,DieType), "poison D")
        case 27:
            Character.Intake(DieType, r.randint(1,DieType), "psychic D")
        case 28:
            Character.Intake(DieType, r.randint(1,DieType), "radiant D")
        case 29:
            Character.Intake(DieType, r.randint(1,DieType), "slashing D")
        case 30:
            Character.Intake(DieType, r.randint(1,DieType), "thunder D")
        case 31:
            Character.Intake(DieType, r.randint(1,100), "healing D")
        case 32:
            Character.Intake(DieType, r.randint(1,100), "healing R")
            
# Prints, later will be exported to CSVs or something

def Output_Character_Stats(Character):
    print("\n-------------------")
    print(Character.Character_Name)
    print("-------------------\n")
    print(f"Total Number of Rolls: {Character.Output_Total_Rolls()}")
    print(f"Total Number of Nat 20s: {Character.Output_Criticals()[0]}")
    print(f"Total Number of Nat 1s: {Character.Output_Criticals()[1]}")
    print(f"")
    print(f"--Averages")
    print(f"Average Dice Roll: {Character.Output_Average_Total()}")
    print(f"Average Attack Roll: {Character.Output_Average_Attack()}")
    print(f"Average Skill Check Roll: {Character.Output_Average_Skill()}")
    print(f"Average Saving Throw Roll: {Character.Output_Average_Save()}")
    print(f"Average Misc Roll: {Character.Output_Average_Misc()}")
    print(f"")
    print(f"--Damage Recieved")
    print(f"Most Damage Recieved in a Single Hit: {Character.Output_Highest_Single_Hit_Damage_Recieved()[0]} {Character.Output_Highest_Single_Hit_Damage_Recieved()[1]} damage.")
    print(f"Total Damage Recieved: {Character.Output_Total_Damage_Recieved()}")
    print(f"Damage Type That You Recieved The Most Damage From: {Character.Output_Type_With_Highest_Damage_Recieved()[0]}, you recieved {Character.Output_Type_With_Highest_Damage_Recieved()[1]} damage of this type.")
    print(f"Average Damage Recieved: {Character.Output_Average_Damage_Recieved()}")
    print(f"")
    print(f"--Damage Dealt")
    print(f"Most Damage Dealt in a Single Hit: {Character.Output_Highest_Single_Hit_Damage_Dealt()[0]} {Character.Output_Highest_Single_Hit_Damage_Dealt()[1]} damage.")
    print(f"Total Damage Dealt: {Character.Output_Total_Damage_Dealt()}")
    print(f"Damage Type You Dealt The Most Damage With: {Character.Output_Type_With_Highest_Damage_Dealt()[0]}, you dealt {Character.Output_Type_With_Highest_Damage_Dealt()[1]} damage of this type.")
    print(f"Average Damage Dealt: {Character.Output_Average_Damage_Dealt()}")
    print(f"")
    print(f"--Healing")
    print(f"Total Healing Dealt: {Character.Output_Total_Healing_Dealt()}")
    print(f"Total Healing Recieved: {Character.Output_Total_Healing_Recieved()}")
    print(f"Most HP Healed in a Single Hit: {Character.Output_Highest_Single_Hit_Heal()}\n")
    
Output_Character_Stats(Kalina)
Output_Character_Stats(Loric)
Output_Character_Stats(Evangeline)

if Allow_Player_Comparison:
    Characters = Character_Intake.Characters
    Nat20s = {}
    Nat1s = {}
    DamageRecieved = {}
    DamageDealt = {}
    HealingDealt = {}
    HealingRecieved = {}
    HighestAverage = {}
    LowestAverage = {}
    
    for Character in Characters:
        Nat20s[Character.Character_Name] = Character.Nat20_Counter
        Nat1s[Character.Character_Name] = Character.Nat1_Counter
        DamageRecieved[Character.Character_Name] = Character.Total_Damage_Recieved
        DamageDealt[Character.Character_Name] = Character.Total_Damage_Dealt
        HealingDealt[Character.Character_Name] = Character.Total_Healing_Dealt
        HealingRecieved[Character.Character_Name] = Character.Total_Healing_Recieved
        HighestAverage[Character.Character_Name] = Character.Total_Average
        LowestAverage[Character.Character_Name] = Character.Total_Average
        
    Most_Nat_20s = max(Nat20s, key=Nat20s.get)
    Most_Nat_20s_Number = Nat20s.get(Most_Nat_20s)
    
    Most_Nat_1s = max(Nat1s, key=Nat1s.get)
    Most_Nat_1s_Number = Nat1s.get(Most_Nat_1s)
    
    Most_Damage_Recieved = max(DamageRecieved, key=DamageRecieved.get)
    Most_Damage_Recieved_Number = DamageRecieved.get(Most_Damage_Recieved)
    
    Most_Damage_Dealt = max(DamageDealt, key=DamageDealt.get)
    Most_Damage_Dealt_Number = DamageDealt.get(Most_Damage_Dealt)
    
    Most_Healing_Dealt = max(HealingDealt, key=HealingDealt.get)
    Most_Healing_Dealt_Number = HealingDealt.get(Most_Healing_Dealt)
    
    Most_Healing_Recieved = max(HealingRecieved, key=HealingRecieved.get)
    Most_Healing_Recieved_Number = HealingRecieved.get(Most_Healing_Recieved)
    
    HighestAverageName = max(HighestAverage, key=HighestAverage.get)
    HighestAverageNumber = HighestAverage.get(HighestAverageName)
    
    LowestAverageName = min(LowestAverage, key=LowestAverage.get)
    LowestAverageNumber = LowestAverage.get(LowestAverageName)
    
    print(f"The player with the most Natural 20s is {Most_Nat_20s}! They rolled {Most_Nat_20s_Number} Natural 20s!")
    print(f"The player with the most Natural 1s is {Most_Nat_1s}! They rolled {Most_Nat_1s_Number} Natural 1s!")
    print(f"The player with the most Damage Recieved is {Most_Damage_Recieved}! They recieved {Most_Damage_Recieved_Number} Damage!")
    print(f"The player with the most Damage Dealt is {Most_Damage_Dealt}! They dealt {Most_Damage_Dealt_Number} Damage!")
    print(f"The player with the most Healing Dealt is {Most_Healing_Dealt}! They dealt {Most_Healing_Dealt_Number} Healing!")
    print(f"The player with the highest average d20 roll is {HighestAverageName}! Their average was {HighestAverageNumber}!")
    print(f"The player with the lowest average d20 roll is {LowestAverageName}! Their average was {LowestAverageNumber}!")