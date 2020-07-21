import json
import time
import connect2 
import func01
##############reading the json file######################
with open ("covid19_more01.json") as f:
    data0 = json.load(f)

with open ("covid19_valid.json") as f:
    data1 = json.load(f)
    
start = time.time()

arr_dic = data1["records"]
final_dict = {}

########################DataCleaning######################
#deleting usless data
for x in arr_dic:
    func01.del_key(x, ["day", "month", "year"])

########################CopyPasta#########################
#each country gets one record copied for semi-redundant data
for obj in arr_dic:

    for k, v in obj.items():
        
        if (k == "geoId"):

            final_dict[v] = func01.dic_creator(obj)

########################DataMerging#######################
#adding dicts to the value of data_log
for obj in arr_dic: 

    for fk0, fv0 in obj.items():

        for k0, v0 in final_dict.items():

            if(fk0 == "geoId"):

                if(fv0 == k0):

                    for k1, v1 in v0.items():

                        if(k1 == "data_log"):

                            v1.append(func01.dic_creator_small(obj))


end = time.time()

########################data_dump#########################
#func01.dump_data(final_dict)

########################print#############################
print(end -start)
connect2.connect()
#print(json.dumps(final_dict, indent = 4, sort_keys = True, separators = ("; ", " : ")))
