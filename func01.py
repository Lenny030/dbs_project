"""
 ______ _    _ _   _ _  _________ _____ ____  _   _  _____ 
 |  ____| |  | | \ | | |/ /__   __|_   _/ __ \| \ | |/ ____|
 | |__  | |  | |  \| | ' /   | |    | || |  | |  \| | (___  
 |  __| | |  | | . ` |  <    | |    | || |  | | . ` |\___ \ 
 | |    | |__| | |\  | . \   | |   _| || |__| | |\  |____) |
 |_|     \____/|_| \_|_|\_\  |_|  |_____\____/|_| \_|_____/ 

"""
import json

def print_all (dic):
    for key, val in dic.items():

        print(key, " : ", val)

    return;

def dump_data (dic):
    with open("data_file.json" , "w") as write_file:
            json.dump(dic, write_file)

def del_key (dic, arr):
    for e in arr:

        for k in list(dic.keys()):

            if(e == k):

                del dic[e]

def dic_creator (dic):

    snd_dic = {}
    for k, v in dic.items():
        
        if(k == "countriesAndTerritories" or k == "countryterritoryCode" or k == "popData2018" or k == "continentExp"):

            snd_dic[k] = v

    snd_dic["data_log"] = []

    return snd_dic;

def dic_creator_small(dic):

    third_dic = {}
    for k, v in dic.items():

        if(k == "dateRep" or k == "cases" or k == "deaths"):

            third_dic[k] = v

    return third_dic;

