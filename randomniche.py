# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 08:22:11 2016

@author: adam
"""

import random

#Dictionary of possible node connections, running the program creates a random node path, or niche
#Dictionary will need updating to account for new possible nodes
T = {
         "mineandmill" : ["conversion", "enrichment", "HWR"],
         "conversion" : ["enrichment", "UO2 fabrication", "UO2 fabrication", "UO2 fabrication", "TRISO fabrication", "HWR"],
         "enrichment" : ["UO2 fabrication", "TRISO fabrication", "HWR"],
         "UO2 fabrication" : ["LWR", "AGR", "RBMK"],
         "TRISO fabrication" : ["pebble bed"],
         "LWR" : ["spent fuel pool", "dry cask", "dry reprocessing","PUREX","near surface disposal", "deep geological disposal"],
         "HWR" : ["spent fuel pool", "dry cask", "near surface disposal", "deep geological disposal"],
         "AGR" : ["spent fuel pool", "dry cask", "dry reprocessing","PUREX","near surface disposal", "deep geological disposal"],         
         "RBMK" : ["spent fuel pool", "dry cask", "dry reprocessing","PUREX","near surface disposal", "deep geological disposal"],         
         "pebble bed" : ["near surface disposal", "deep geological disposal"],         
         "spent fuel pool" : ["dry reprocessing","PUREX","near surface disposal", "deep geological disposal"],         
         "dry cask" : ["dry reprocessing","PUREX","near surface disposal", "deep geological disposal"],
         "dry reprocessing" : ["conversion","enrichment","HWR"],
         "PUREX" : ["conversion", "enrichment", "HWR"],
         "deep geological disposal" : [None],          
         "near surface disposal" : [None] #need to add a null
}

#may need to add disposal as a null option for every case

n = int(input("Input number of niches ")) #User inputs the number of niches desired

c0 = "mineandmill" #initial key, fuel cycle starts with mining
numniche = [c0] #defines the list in which each node will be stored

i = 0 #for iteration through the while

while i < n:                                 #Iterates through the desired number of niches
    if numniche[i] == None:
        print("Marks the end of the cycle")
        break
    print(numniche[i])
    ci = random.choice(T[numniche[i]])       #randomly selects new key from list to act as a node and a new key
    numniche.append(ci)                      #adds new node to the path
    i = i + 1
        



