import json
import connect2
import connect2_0
import mysql.connector

with open ("FINAL.json") as f:
    data = json.load(f)

arr = []

for geo_id, v in data.items():

    for countriesAndTerritories, v1 in v.items():

        if countriesAndTerritories == "countriesAndTerritories":

            for continentExp, v2 in v.items():

                if continentExp == "continentExp":

                    for median_age, v3 in v.items():

                        if median_age == "median_age":

                            for gdp_per_capita, v4 in v.items():

                                if gdp_per_capita == "gdp_per_capita":

                                    for bed_per_1k, v5 in v.items():

                                        if bed_per_1k == "bed_per_1k":

                                            for popData2018, v6 in v.items():

                                                if popData2018 == "popData2018":

                                                    for first_rec, v7 in v.items():

                                                        if first_rec == "first_rec":

                                                            if v6 == "":

                                                                arr.append((v2, v1, geo_id, 0, v4, v3, v5, v7))
                                                            if v6 != "":

                                                                arr.append((v2, v1, geo_id, int(v6), v4, v3, v5, v7))

arr0 = []

for k, v in data.items():
    
    for k0, v0 in v.items():

        if k0 == "data_log":

            for dic in v0:

                for dateRep, v1 in dic.items():

                    if dateRep == "dateRep":

                        for cases, v2 in dic.items():

                            if cases == "cases":

                                for deaths, v3 in dic.items():

                                    if deaths == "deaths":

                                        arr0.append((k, v1, v2, v3))


print(arr0[0])
#connect2.insert_stuff(arr)
connect2_0.insert_stuff(arr0)

#print(len(data))            
#print(arr[0])
