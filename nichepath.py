# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:18:30 2016

@author: adam
"""

import random

T = {
    "mine" : {"conversion", "enrichment", "hwr"},
    "conversion" : {"enrichment", "uo2 fabrication", "uo2 fabrication", "uo2 fabrication", "triso fabrication", "hwr"}, 
    "enrichment" : {"uo2 fabrication", "triso fabrication", "hwr", "fr"},
    "uo2 fabrication" : {"lwr", "htgr", "rbmk"},
    "triso fabrication" : {"pb"},
    "fr" : {"storage", "dry reprocessing", "purex", "deep geological repository", "near surface repository"},
    "lwr" : {"storage", "dry reprocessing","purex","near surface repository", "deep geological repository"},
    "hwr" : {"storage", "near surface repository", "deep geological repository"},
    "htgr" : {"storage", "dry reprocessing","purex","near surface repository", "deep geological repository"},         
    "rbmk" : {"storage", "dry reprocessing","purex","near surface repository", "deep geological repository"},         
    "pb" : {"near surface repository", "deep geological repository"},         
    "storage" : {"dry reprocessing","purex","near surface repository", "deep geological repository"},         
    "dry reprocessing" : {"conversion","enrichment","hwr", "mox"},
    "purex" : {"conversion", "enrichment", "hwr", "mox"},
    "mox fabrication" : {"fr", "lwr", "htgr", "rbmk"},
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

    
