from __future__ import print_function

import numpy as np
import random

#damage for this card = [servantAtk * npDamageMultiplier * (firstCardBonus + (cardDamageValue * (1 + cardMod)))
#* classAtkBonus * triangleModifier * attributeModifier * randomModifier * 0.23 *
#(1 + atkMod - defMod) * criticalModifier * extraCardModifier * (1 - specialDefMod)
#* {1 + powerMod + selfDamageMod + (critDamageMod * isCrit) + (npDamageMod * isNP)} * {1 + ((superEffectiveModifier - 1)
#* isSuperEffective)}] + dmgPlusAdd + selfDmgCutAdd + (servantAtk * busterChainMod)

def npDamge(serAtk, npBase, cardtype, order, cardModBonus, servantClass, oppClass, serAttr, oppAttr):
    basedamage = serAtk * npBase * (firstCardBonus(cardtype)+(cardDamageValue(cardtype, order,"np")*(1+cardModBonus)))
    classdamage = baseDamageClass(servantClass)*triangleBonus(servantClass, oppClass)*attributeModifier(serAttr,oppAttr)
    addDamage = random.uniform(0.9, 1.1)



#First    Second    Third
#Arts    100%    120%    140%
#Buster    150%    180%    210%
#Quick    80%    96%    112%

def cardDamageValue(cardtype, order, np):
    quickbonus = [0.8, 0.96, 1.12]
    artbonus = [1, 1.2, 1.4]
    busterbonus = [1.5, 1.8, 2.1]
    if np =  "np":
        order = 1
    if cardtype == "quick":
        damage = quickbonus[order -1]
    elif cardtype == "art":
        damage = artbonus[order-1]
    else:
        damage = busterbonus[order -1]

    return damage


#Saber	1.0x	1.0x	0.5x	2.0x	1.0x	1.0x	1.0x	2.0x	1.0x	0.5x	2.0x	1.0x	1.0x
#Archer	0.95x	2.0x	1.0x	0.5x	1.0x	1.0x	1.0x	2.0x	1.0x	0.5x	2.0x	1.0x	1.0x
#Lancer	1.05x	0.5x	2.0x	1.0x	1.0x	1.0x	1.0x	2.0x	1.0x	0.5x	2.0x	1.0x	1.0x
#Rider	1.0x	1.0x	1.0x	1.0x	1.0x	2.0x	0.5x	2.0x	1.0x	0.5x	1.0x	1.0x	2.0x
#Caster	0.9x	1.0x	1.0x	1.0x	0.5x	1.0x	2.0x	2.0x	1.0x	0.5x	1.0x	1.0x	2.0x
#Assassin	0.9x	1.0x	1.0x	1.0x	2.0x	0.5x	1.0x	2.0x	1.0x	0.5x	1.0x	1.0x	2.0x
#Berserker	1.1x	1.5x	1.5x	1.5x	1.5x	1.5x	1.5x	1.5x	1.0x	1.5x	1.5x	1.5x	1.5x
#Shielder	1.0x	1.0x	1.0x	1.0x	1.0x	1.0x	1.0x	1.0x	1.0x	1.0x	1.0x	1.0x	1.0x
#Ruler	1.1x	1.0x	1.0x	1.0x	1.0x	1.0x	1.0x	2.0x	1.0x	1.0x	1.0x	0.5x	1.0x
#Alter-Ego	1.0x	1.0x	1.0x	1.0x	2.0x	2.0x	2.0x	2.0x	1.0x	1.0x	1.0x	1.0x	1.0x
#Avenger	1.1x	1.0x	1.0x	1.0x	1.0x	1.0x	1.0x	2.0x	1.0x	2.0x	1.0x	1.0x	1.0x
#Beast	1.0x	2.0x	2.0x	2.0x	1.0x	1.0x	1.0x	2.0x	1.0x	1.0x	1.0x	0.5x	1.0x


#Attacker / Defender	Man	    Sky	    Earth	Star	Beast
#Man	                1.0x	1.1x	0.9x	1.0x	1.0x
#Sky	                0.9x	1.0x	1.1x	1.0x	1.0x
#Earth	                1.1x	0.9x	1.0x	1.0x	1.0x
#Star	                1.0x	1.0x	1.0x	1.0x	1.1x
#Beast	                1.0x	1.0x	1.0x	1.1x	0.0x

def attributeModifier(serAtrribute, oppAttribute):
    attributes = ["man", "sky", "earth", "star", "beast"]
    if checkStringExists(serAtrribute, attributes):
        if checkStringExists(oppAttribute, attributes):
            serIndex = checkIndex(serAtrribute, attributes)
            oppIndex = checkIndex(oppAttribute, attributes)
            diff = serIndex - oppIndex
            if diff == 3 or diff == 0 or diff == -3:
                modifier = 1
            elif diff == 2:
                if serAtrribute == "earth":
                    modifier = 1.1
                else:
                    modifier = 1
            elif diff == 1:
                if serAtrribute =="earth":
                    modifier = 1
                else:
                    modifier = 0.9
            elif diff == -2:
                if serAtrribute == "man":
                    modifier = 0.9
                else:
                    modifier = 1
            else:
                if serAtrribute == "earth":
                    modifier = 1
                else:
                    modifier = 1.1
        else:
            print("bad attribute, choose another opponent attribute")
            modifier = 0
    else:
        print("bad attribute, choose another servant attribute")
        modifier = 0
    return modifier

def baseDamageClass(servantClass):
    if servantClass == "saber" or servantClass == "rider" or servantclass == "shielder" or servantClass == "alterego":
        basedamage = 1
    elif servantClass == "archer":
        basedamage = 0.95
    elif servantClass == "lancer":
        basedamage = 1.05
    elif servantClass == "berserker" or servantClass == "ruler" or servantClass == "avenger":
        basedamage = 1.1
    elif servantClass == "caster" or servantClass == "assasin"
        basedamage = 0.9
    else:
        print("not a servant")
        basedamage = 0

    return basedamage

def firstCardBonus(cardtype):
    if cardtype == "buster":
        bonus = 0.5
    else:
        bonus = 0
    return bonus

def triangleBonus(servantClass, oponent):
    # define the classes in knights or cavs
    knights = ["saber", "lancer", "archer"]
    cavs = ["caster", "assasin", "rider"]
    if checkStringExists(servantClass, knights):
        if checkStringExists(oponent, knights):
            serIndex = checkIndex(servantClass, knights)
            oppIndex = checkIndex(oponent, knights)
            diff = serIndex - oppIndex
        else:
            print("Your oponent class does not exists")
            diff = 42
    elif checkStringExists(servantClass, cavs):
        if checkStringExists(oponent, cavs):
                serIndex = checkIndex(servantClass, cavs)
                oppIndex = checkIndex(oponent, cavs)
                diff = serIndex - oppIndex
        else:
            print("Your opponent class does not exists")
            diff = 42
    else:
        print("Your class does not exists")
        diff = 42
    if diff == 1:
        triBonus = 0.5
    elif diff == 0:
        triBonus = 1
    elif diff == 2:
        triBonus = 2
    elif diff == -1:
        triBonus = 2
    elif diff == -2:
        triBonus = 0.5
    else:
        triBonus = 0
    return triBonus

def checkStringExists(word, wordlist):
    lenlist = len(wordlist)
    i = 0
    status = False
    while i < lenlist and status == False:
        if word == wordlist[i]:
            status = True
        i = i+1
    return status

def checkIndex(word, wordlist):
    wordlen = len(wordlist)
    status = False
    i = 0
    while i < wordlen and status == False:
        if word == wordlist[i]:
            status = True
            break
        else:
            i = i+1
    return i








