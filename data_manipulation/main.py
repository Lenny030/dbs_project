import json
import time
import func01

def final_dic_creator (dic0, dic1):

    snd_dic = {}

    for k0, v0 in dic0.items():

        for k1, v1 in dic1.items():

            if k0 != "data_log" and k0 != "countryterritoryCode":

                snd_dic[k0] = v0
                
            if k1 != "continetExp" and k1 != "countriesAndTerritories":

                snd_dic[k1] = v1

    return snd_dic

def small_dic_enricher(dic):
    """
    returns a small dict for each day
    """
    third_dic = {}

    for k, v in dic.items():

        if k == "total_cases" or k == "total_deaths": 
                
            third_dic[k] = v

        if k == "date":

            third_dic["dateRep"] = v

        if k == "new_cases":

            third_dic["cases"] = v

        if k == "new_deaths":

            third_dic["deaths"] = v


    return third_dic;
                
def dic_enricher(dic):
    """
    returns and dictonary with some key and value pairs
    one value is an array full of dicts with daily records
    """
    snd_dic = {}

    for k, v in dic.items():

        if k == "continent":
            snd_dic["continentExp"] = v

        if k == "location":
            snd_dic["countriesAndTerritories"] = v

        if k == "median_age":
            snd_dic[k] = v

        if k == "hospital_beds_per_thousand":
            snd_dic["bed_per_1k"] = v

        if k == "life_expectancy":
            snd_dic["life_expectancy"] = v

        if k == "data":

            data = []

            for x in v:

                data.append(small_dic_enricher(x))
            
            snd_dic[k] = data            
            
    return snd_dic;

##############reading the json file######################
with open ("covid19_more01.json") as f:
    data0 = json.load(f)

with open ("covid19_valid.json") as f:
    data1 = json.load(f)

start = time.time()

arr_dic = data1["records"]
semi_dict = {}

########################DataCleaning######################
#deleting usless data
for x in arr_dic:
    func01.del_key(x, ["day", "month", "year"])

#CopyPasta#########################
#each country gets one record copied for semi-redundant data
for obj in arr_dic:

    for k, v in obj.items():
        
        if (k == "geoId"):

            semi_dict[v] = func01.dic_creator(obj)

#DataMerging#######################
#adding dicts to the value of data_log
for obj in arr_dic: 

    for fk0, fv0 in obj.items():

        for k0, v0 in semi_dict.items():

            if(fk0 == "geoId"):

                if(fv0 == k0):

                    for k1, v1 in v0.items():

                        if(k1 == "data_log"):

                            v1.append(func01.dic_creator_small(obj))



########################data_enrich#########################
"""
some data gets extracted off a different dataset and but with the same herachie
as semi_dic in a dictonary
"""
more_dic = {}

for k0, v0 in data0.items():

    more_dic[k0] = dic_enricher(v0)
    
end = time.time()

########################final_merge#######################
#almost there

########################data_dump#########################
#with open('FINAL_DIC.json', 'w') as output:
#    json.dump(more_dic, output)

#########################print#############################
print(end -start)

#print(json.dumps(more_dic, indent = 4, sort_keys = True, separators = ("; ", " : ")))
