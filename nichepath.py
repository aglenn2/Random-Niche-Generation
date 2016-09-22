# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:18:30 2016

@author: adam
"""

import random

T = {
    "mine" : {"conversion", "enrichment", "hwr"},
    "conversion" : {"enrichment", "uo2 fabrication", "uo2 fabrication", "uo2 fabrication", "triso fabrication", "hwr"}, 
    "enrichment" : {"uo2 fabrication", "triso fabrication", "hwr"},
    "uo2 fabrication" : {"lwr", "htgr", "rbmk"},
    "triso fabrication" : {"pebble bed"},
    "lwr" : {"storage", "dry reprocessing","purex","near surface repository", "deep geological repository"},
    "hwr" : {"storage", "near surface repository", "deep geological repository"},
    "htgr" : {"storage", "dry reprocessing","purex","near surface repository", "deep geological repository"},         
    "rbmk" : {"storage", "dry reprocessing","purex","near surface repository", "deep geological repository"},         
    "pebble bed" : {"near surface repository", "deep geological repository"},         
    "storage" : {"dry reprocessing","purex","near surface repository", "deep geological repository"},         
    "dry reprocessing" : {"conversion","enrichment","hwr"},
    "purex" : {"conversion", "enrichment", "hwr"},
    "deep geological repository" : {None},          
    "near surface repository" : {None} #need to add a null
}

def test(niches, nichelist = {"mine"}, choice = "mine"):
     if niches == 1 or None in nichelist:
         return nichelist
     else:
         choice = random.sample(T[choice],1)[0]
         nichelist.add(choice)
         return test(niches-1, nichelist, choice)








def randomniche(niches, startkey = "mine"):    
    
    nichelist = set(startkey)
    i = 0
    while i < niches:
        if None in nichelist:
            break
        ci = random.choice(T[nichelist(i)])
        nichelist.update(ci)
        i = i + 1
    return nichelist
    