'''
Name: _core_constants.py

Description:
    This class stores the common-core constants that will be used in-game across various classes

    For instance, the creature in-game class "BARBARIAN" is used for things such as weapon requirements,
    custom dialogs, level progression system, etc. Instead of the name "BARBARIAN" applying only to
    core__creature files (which, the creatures would be "barbarians" in-game), the constants for them
    can be used universally.
'''

class index_reader:
    '''
    Used for reading common data in the constant classes
    ''' 

    def __init__(self):
        None

    def __is_real(self,val=None):
        if val == None:
            return False,False
        else:
            try:
                is_int = bool(int(val) or 1) # This always sets true so long as val is a string integer
            except ValueError:
                is_int = False

                   
            if is_int and 0 <= int(val) < len(self.INDEX):
                return True, dict(zip(range(0,len(self.INDEX)),self.INDEX))[int(val)]
            elif type(val) == str:
                if val.lower() in self.INDEX:
                    return True, val.lower()
            
                elif val.replace(" ","").lower() in [i.replace(" ","").lower() for i in self.INDEX_LONG]:
                    return True, dict(zip([i.replace(" ","").lower() for i in self.INDEX_LONG],self.INDEX))[val.replace(" ","").lower()]

        return False,False
    
    def verify(self,val=None):
        '''
        This takes either the constant or an ID number and returns the shorthand constant.

        This is used to make a check on custom scripts that may get used or verifying a range
        of constants via ID numbers.
        
        Also intended for use with default settings of in-game classes. If something is supposed to
        be altered, but can't be "verified", a default can be set in place upon this returning False.
        '''
        real,value = self.__is_real(val)
        if real:
            return value
        else:
            return False

    def filter_list(self, unfiltered_list=None):
        '''
        Takes a list of values (int, str, core_constant) and returns a list 
        with only verified values that are built-in to the game. This is useful 
        for filtering data imported from spreadsheets
        '''
        if type(unfiltered_list) == list:
            filtered_list = []
            for i,j in enumerate(unfiltered_list):
                verified = self.verify(j)
                if verified:
                    filtered_list.append(verified)
            return filtered_list
        return self.filter_list([unfiltered_list])

    
    def get_index(self):
        '''
        Returns the index of the inheriting class which includes all of the constants that can normally be called upon
        '''
        return self.INDEX

    def get_index_length(self):
        '''
        Returns the length of the index. This gives the total amount of of items per constant
        class

        Ex. self.ABILITY() has six different constants: str, dex, con, wis, int, and chr
        This function outputs an integer with the count
        '''

        return len(self.INDEX) 
    
    def get_long_name(self,val=None):
        '''
        Returns the long name for the given constant. 

        Ex. ABILITY.STRENGTH = 'str' = 'strength'
        This would return 'strength'
        '''
        constant = self.verify(val)
        return dict(zip(self.INDEX,self.INDEX_LONG))[constant]

    def get_index_id(self, val=None):
        constant = self.verify(val)
        return dict(zip(self.INDEX, range(len(self.INDEX))))[constant]




class _core_const_ability(index_reader):
    '''
    Used as a class to hold constants for creature abilities
    '''
    def __init__(self):
        index_reader.__init__(self)
        self.STR=self.STRENGTH='str'
        self.INT=self.INTELLIGENCE='int'
        self.CON=self.CONSTITUTION='con'
        self.WIS=self.WISDOM='wis'
        self.DEX=self.DEXTERITY='dex'
        self.CHR=self.CHARISMA='chr'

        self.INDEX=[self.STR,self.INT,self.CON,self.WIS,self.DEX,self.CHR]
        self.INDEX_LONG=['strength','intelligence','constitution','wisdom','dexterity','charisma']

class _core_const_alignment(index_reader):
    '''
    Used as a class to hold possible alignment constants for a creature
    '''
    def __init__(self):
        index_reader.__init__(self)
        self.LAW = self.LAWFUL = 'law'
        self.NTL = self.NEUTRALLvC = 'ntl'
        self.CHA = self.CHAOTIC = 'cha'
        self.GOD = self.GOOD = 'good'
        self.NTG = self.NEUTRALGvE = 'ntg'
        self.EVL = self.EVIL = 'evl'
        self.LAG = self.LAWFULGOOD = 'lag'
        self.LAN = self.LAWFULNEUTRAL = 'lan'
        self.LAE = self.LAWFULEVIL = 'lae'
        self.NEG = self.NEUTRALGOOD = 'neg'
        self.NEN = self.TRN = self.NEUTRALNEUTRAL = self.TRUENEUTRAL = 'nen'
        self.NEE = self.NEUTRALEVIL = 'nee'
        self.CHG = self.CHAOTICGOOD = 'chg'
        self.CHN = self.CHAOTICNEUTRAL = 'chn'
        self.CHE = self.CHAOTICEVIL = 'che'

        self.INDEX = [self.LAW, self.NTL, self.CHA, self.GOD, self.NTG, 
                      self.EVL, self.LAG, self.LAN, self.LAE, self.NEG,
                      self.NEN, self.NEE, self.CHG, self.CHN, self.CHE]

        self.INDEX_LONG = ['lawful', 'neutral', 'chaotic', 'good', 'neutral',
                           'evil', 'lawful good', 'lawful neutral', 'lawful evil', 'neutral good',
                           'true neutral', 'neutral evil', 'chaotic good', 'chaotic neutral', 'chaotic evil']


class _core_const_baseAttackBonus(index_reader):
    '''
    Used as a class to hold constants for base attack bonuses
    '''
    def __init__(self):
        index_reader.__init__(self)
        self.GOOD = 'good' # Returns the constant for 'good' attack bonuses
        self.AVERAGE = self.AVRG = 'avrg' # Returns the constant for 'average' attack bonuses
        self.POOR = 'poor' # Returns the constant for 'poor' attack bonuses
        self.MONK = 'monk' # Returns the constant for 'monk' attack bonuses

        self.INDEX = [self.POOR,self.AVERAGE,self.GOOD,self.MONK]
        self.INDEX_LONG=['poor','average','good','monk']

class _core_const_baseSaveBonus(index_reader):
    '''
    Used as a class to hold constants for base save bonuses
    '''
    def __init__(self):
        index_reader.__init__(self)
        self.GOOD = 'good' # Returns the constant for 'good' save bonuses
        self.POOR = 'poor' # Returns the constant for 'poor' save bonuses

        self.INDEX = [self.POOR,self.GOOD]
        self.INDEX_LONG = ['poor','good']

class _core_const_creatureClass(index_reader):
    '''
    Used to provide constants for valid creature classes
    '''
    def __init__(self):
        index_reader.__init__(self)
        self.UNIQUE = self.UNI = 'uni'
        self.BARBARIAN = self.BBN = 'bbn'
        self.BARD = self.BRD = 'brd'
        self.CLERIC = self.CLR = 'clr'
        self.DRUID = self.DRD = 'drd'
        self.FIGHTER = self.FTR = 'ftr'
        self.MONK = self.MNK = 'mnk'
        self.PALADIN = self.PLD = 'pld'
        self.RANGER = self.RGR = 'rgr'
        self.ROGUE = self.ROG = 'rog'
        self.SORCERER = self.SOR = 'sor'
        self.WIZARD = self.WIZ = 'wiz'

        self.INDEX = [self.UNI,self.BBN,self.BRD,self.CLR,self.DRD,
                      self.FTR,self.MNK,self.PLD,self.RGR,self.ROG,
                      self.SOR,self.WIZ]

        self.INDEX_LONG = ['unique','barbarian','bard','cleric','druid',
                           'fighter','monk','paladin','ranger','rogue',
                           'sorcerer','wizard']

class _core_const_creatureRace(index_reader):
    '''
    Used for holding the core races of the game
    '''
    def __init__(self):
        index_reader.__init__(self)
        self.UNI = self.UNIQUE = 'uni'
        self.ABR = self.ABERRATION = 'abr'
        self.ANI = self.ANIMAL = 'ani'
        self.BST = self.BEAST = 'bst'
        self.CON = self.CONSTRUCT = 'con'
        self.DRG = self.DRAGON = 'drg'
        self.DWF = self.DWARF = 'dwf'
        self.ELM = self.ELEMENTAL = 'elm'
        self.ELF = 'elf'
        self.FEY = 'fey'
        self.GNT = self.GIANT = 'gnt'
        self.GNO = self.GNOME = 'gno'
        self.GOB = self.GOBLINOID = 'gob'
        self.HFE = self.HALFELF = 'hfe'
        self.HFO = self.HALFORC = 'hfo'
        self.HFL = self.HALFLING = 'hfl'
        self.HUM = self.HUMAN = 'hum'
        self.MAG = self.MAGICAL_BEAST = 'mag'
        self.OOZ = self.OOZE = 'ooz'
        self.ORC = 'orc'
        self.OUT = self.OUTSIDER = 'out'
        self.REP = self.REPTILIAN = 'rep'
        self.SHP = self.SHAPECHANGER = 'shp'
        self.UND = self.UNDEAD = 'und'
        self.VRM = self.VERMIN = 'vrm'

        self.INDEX = [self.UNI,self.ABR,self.ANI,self.BST,self.CON,
                      self.DRG,self.DWF,self.ELM,self.ELF,self.FEY,
                      self.GNT,self.GNO,self.GOB,self.HFE,self.HFO,
                      self.HFL,self.HUM,self.MAG,self.OOZ,self.ORC,
                      self.OUT,self.REP,self.SHP,self.UND,self.VRM]

        self.INDEX_LONG = ['unique','aberration','animal','beast','construct',
                           'dragon','dwarf','elemental','elf','fey',
                           'giant','gnome','goblin','halfelf','halforc',
                           'halfling','human','magical beast','ooze','orc',
                           'outsider','reptilian','shapechanger','undead','vermin']

class _core_const_damageTypes(index_reader):
    '''
    Used as a class to hold constants for damage types
    '''
    def __init__(self):
        index_reader.__init__(self)

        self.ACI = self.ACID = 'dtacd'
        self.BLU = self.BLUDGEONING = 'dtblu'
        self.COL = self.COLD = 'dtcol'
        self.DIV = self.DIVINE = 'dtdiv'
        self.ELE = self.ELECTRIC = 'dtele'
        self.FIR = self.FIRE = 'dtfir'
        self.MAG = self.MAGICAL = 'dtmag'
        self.NEG = self.NEGATIVEENERGY = 'dtneg'
        self.PIE = self.PIERCING = 'dtpie'
        self.POS = self.POSITIVEENERGY = 'dtpos'
        self.SLA = self.SLASHING = 'dtsla'
        self.SON = self.SONIC = 'dtson'

        self.INDEX = [self.ACI, self.BLU, self.COL, self.DIV, self.ELE,
                      self.FIR, self.MAG, self.NEG, self.PIE, self.POS,
                      self.SLA, self.SON]

        self.INDEX_LONG = ['acid', 'bludgeoning', 'cold', 'divine', 'electric',
                           'fire', 'magical', 'negative energy', 'piercing', 'positive energy',
                           'slashing', 'sonic']

class _core_const_equipmentSlotTypes(index_reader):
    '''
    Used as a class to hold constants for the equipment slot types
    '''
    def __init__(self):
        index_reader.__init__(self)
        self.NAT = self.NATURAL = 'stnat'
        self.STA = self.STANDARD = 'ststa'

        self.INDEX = [self.NAT, self.STA]

        self.INDEX_LONG = ['natural','standard']


class _core_const_equipmentSlots(index_reader):
    '''
    Used as a class to hold constants for the possible equipment slots on the creature class
    '''
    def __init__(self):
        index_reader.__init__(self)
        self.MHD = self.MAINHAND = 'mhd'
        self.OHD = self.OFFHAND = 'ohd'
        self.ARM = self.ARMOR = 'arm'
        self.HLM = self.HELMET = 'hlm'
        self.GLV = self.GLOVES = 'glv'
        self.CLK = self.CLOAK = 'clk'
        self.BTS = self.BOOTS = 'bts'
        self.BLT = self.BELT = 'blt' # Mmm, bacon
        self.AMU = self.AMULET = 'amu'
        self.RG1 = self.RING1 = 'rg1'
        self.RG2 = self.RING2 = 'rg2'
        self.ARR = self.ARROWS = 'arr'
        self.BOL = self.BOLTS = 'bol'
        self.BUL = self.BULLETS = 'bul'

        self.INDEX = [self.MHD,self.OHD,self.ARM,self.HLM,
                      self.GLV,self.CLK,self.BTS,self.BLT,
                      self.AMU,self.RG1,self.RG2,self.ARR,
                      self.BOL,self.BUL]

        self.INDEX_LONG = ['mainhand','offhand','armor','helmet',
                           'gloves','cloak','boots','belt',
                           'amulet','first ring','second ring','arrows',
                           'bolts','bullets']

class _core_const_naturalEquipmentSlots(index_reader):
    '''
    Used as a class to hold constants for the natural equipment slots
    that are used by non-playable races
    '''
    def __init__(self):
        index_reader.__init__(self) 
        
        self.CLM = self.CLAWMAINHAND = 'neclm'
        self.CLO = self.CLAWOFFHAND = 'neclo'
        self.SPE = self.SPECIAL = 'nespe'
        self.SKI = self.SKIN = 'neski'

        self.INDEX = [self.CLM, self.CLO, self.SPE, self.SKI]

        self.INDEX_LONG = ['claw 1', 'claw 2', 'special', 'skin']
       
class _core_const_savingThrow(index_reader):
    '''
    Used as a class to hold constants for saving throws
    '''
    def __init__(self):
        index_reader.__init__(self)
        self.FOR=self.FORTITUDE='for' # Returns constant for fortitude saving throw
        self.REF=self.REFLEX='ref' # Returns constant for reflex saving throw
        self.WIL=self.WILL='wil' # Returns constant for will saving throw

        self.INDEX = [self.FOR,self.REF,self.WIL]
        self.INDEX_LONG = ['fortitude','reflex','will']

class _core_const_sizeClass(index_reader):
    '''
    Used as a class to hold constants for racial size classes
    '''
    def __init__(self):
        index_reader.__init__(self)
        self.UNI = self.UNIQUE = 'uni'
        self.FIN = self.FINE = 'fin'
        self.DIM = self.DIMINUTIVE = 'dim'
        self.TNY = self.TINY = 'tny'
        self.SML = self.SMALL = 'sml'
        self.MED = self.MEDIUM = 'med'
        self.LGT = self.LARGE_TALL = self.LARGE = 'lgt'
        self.LGL = self.LARGE_LONG = 'lgl'
        self.HGT = self.HUGE_TALL = self.HUGE = 'hgt'
        self.HGL = self.HUGE_LONG = 'hgl'
        self.GRT = self.GARGANTUAN_TALL = self.GARGANTUAN = 'grt'
        self.GRL = self.GARGANTUAN_LONG = 'grl'
        self.COT = self.COLOSSAL_TALL = self.COLOSSAL = 'cot'
        self.COL = self.COLOSSAL_LONG = 'col'
                                
        self.INDEX = [self.UNI,self.FIN,self.DIM,self.TNY,self.SML,
                      self.MED,self.LGT,self.LGL,self.HGT,self.HGL,
                      self.GRT,self.GRL,self.COT,self.COL]

        self.INDEX_LONG = ['unique','fine','diminutive','tiny','small',
                           'medium','large tall','large long','huge tall','huge long',
                           'gargantuan tall', 'gargantuan long', 'colossal tall', 'colossal long']

class _core_const_skill(index_reader):
    '''
    Used as a class to hold possible skills for a creature
    '''
    def __init__(self):
        index_reader.__init__(self)
        self.UNI = self.UNIQUE = 'uni'
        self.ANI = self.ANIMAL_EMPATHY = 'ani'
        self.APR = self.APPRAISE = 'apr'
        self.BLF = self.BLUFF = 'blf'
        self.CNC = self.CONCENTRATION = 'cnc'
        self.CAR = self.CRAFT_ARMOR = 'car'
        self.CTR = self.CRAFT_TRAP = 'ctr'
        self.CWE = self.CRAFT_WEAPON = 'cwe'
        self.DTR = self.DISABLE_TRAP = 'dtr'
        self.DIS = self.DISCIPLINE = 'dis'
        self.HEL = self.HEAL = 'hel'
        self.HID = self.HIDE = 'hid'
        self.ITM = self.INTIMIDATE = 'itm'
        self.LIS = self.LISTEN = 'lis'
        self.LOR = self.LORE = 'lor'
        self.MOV = self.MOVE_SILENTLY = 'mov'
        self.OPL = self.OPEN_LOCK = 'opl'
        self.PRY = self.PARRY = 'pry'
        self.PFM = self.PERFORM = 'pfm'
        self.PSD = self.PERSUADE = 'psd'
        self.PIC = self.PICK_POCKET = 'pic'
        self.RID = self.RIDE = 'rid'
        self.SRC = self.SEARCH = 'src'
        self.STR = self.SET_TRAP = 'str'
        self.SPL = self.SPELLCRAFT = 'spl'
        self.SPT = self.SPOT = 'spt'
        self.TNT = self.TAUNT = 'tnt'
        self.TBL = self.TUMBLE = 'tbl'
        self.UMD = self.USE_MAGIC_DEVICE = 'umd'

        self.INDEX = [self.UNI,self.ANI,self.APR,self.BLF,self.CNC,
                      self.CAR,self.CTR,self.CWE,self.DTR,self.DIS,
                      self.HEL,self.HID,self.ITM,self.LIS,self.LOR,
                      self.MOV,self.OPL,self.PRY,self.PFM,self.PSD,
                      self.PIC,self.RID,self.SRC,self.STR,self.SPL,
                      self.SPT,self.TNT,self.TBL,self.UMD]

        self.INDEX_LONG = ['unique', 'animal empathy', 'appraise', 'bluff', 'concentration',
                           'craft armor', 'craft trap', 'craft weapon', 'disable trap','discipline',
                           'heal', 'hide', 'intimidate', 'listen', 'lore',
                           'move silently', 'open lock', 'parry', 'perform', 'persuade',
                           'pick pocket', 'ride', 'search', 'set trap', 'spellcraft',
                           'spot', 'taunt', 'tumble', 'use magic device']


class _core_const_spellcasting_school(index_reader):
    '''
    Used to define the spellcasting school various classes use
    '''

    def __init__(self):
        index_reader.__init__(self)
        self.NON = self.NONMAGICAL = 'non'
        self.ARC = self.ARCANE = 'arc'
        self.DIV = self.DIVINE = 'div'

        self.INDEX = [self.NON, self.ARC, self.DIV]

        self.INDEX_LONG = ['nonmagical','arcane','divine']


class _core_const_item_classes(index_reader):

    def __init__(self):
        index_reader.__init__(self)

        self.ARM = self.ARMOR = 'icarm'
        self.CRA = self.CREATUREARMOR = 'iccra'
        self.CRW = self.CREATUREWEAPON = 'iccrw'
        self.MIS = self.MISCELLANEOUS = 'icmis'
        self.WEP = self.WEAPON = 'icwep'
        self.WER = self.WEARABLE = 'icwer'
        
        self.INDEX = [self.ARM, self.CRA, self.CRW,
                      self.MIS, self.WEP, self.WER]

        self.INDEX_LONG = ['armor', 'creature armor', 'creature weapon',
                           'miscellaneous', 'weapon', 'wearable']

class _core_const_weaponProficiencies(index_reader):

    def __init__(self):
        index_reader.__init__(self)

        self.SIM = self.SIMPLE = 'wpsim'
        self.MAR = self.MARTIAL = 'wpmar'
        self.EXO = self.EXOTIC = 'wpexo'
        self.CRE = self.CREATURE = 'wpcre'
        self.ELF = self.ELVEN = 'wpelf'
        self.ROG = self.ROGUE = 'wprog'
        self.DRU = self.DRUID = 'wpdru'
        self.MON = self.MONK = 'wpmon'
        self.WIZ = self.WIZARD = 'wpwiz'

        self.INDEX = [self.SIM, self.MAR, self.EXO, self.CRE, self.ELF,
                      self.ROG, self.DRU, self.MON, self.WIZ]

        self.INDEX_LONG = ['simple', 'martial', 'exotic', 'creature', 'elven',
                           'rogue', 'druid', 'monk', 'wizard']


ABILITY = _core_const_ability()
ALIGNMENT = _core_const_alignment()
BASEATTACKBONUS = _core_const_baseAttackBonus()
BASESAVEBONUS = _core_const_baseSaveBonus()
CREATURECLASS = _core_const_creatureClass()
CREATURERACE = _core_const_creatureRace()
DAMAGETYPE = _core_const_damageTypes()
EQUIPMENTSLOT = _core_const_equipmentSlots()
EQUIPMENTSLOTTYPE = _core_const_equipmentSlotTypes()
EQUIPMENTSLOTNATURAL = _core_const_naturalEquipmentSlots()
ITEMCLASS = _core_const_item_classes()
SAVINGTHROW = _core_const_savingThrow()
SIZECLASS = _core_const_sizeClass()
SKILL = _core_const_skill()
SPELLCASTING_SCHOOL = _core_const_spellcasting_school()
WEAPONPROFICIENCY = _core_const_weaponProficiencies()
