import pandas as pd 
npa = pd.read_csv("votebuilder_npa_precinct_11.6.csv", index_col=0)
total = pd.read_csv("votebuilder_total_precinct_11.6.csv", index_col=0)
precinct_list = []
for x in total.precinct.unique():
    precinct_list.append(x)
del precinct_list [-1]
npa_dict = {}
#print(len(precinct_list))
for x in precinct_list: 
    df = total[total["precinct"] == x]
    num_people = df["Total People"]
    num = 0 
    for y in num_people:
        num += int(y)
    #num = total number of people in each precinct
    df2 = npa[npa["precinct"] == x]
    num_npas = df2["Total People"]
    numy = 0 
    for z in num_npas:
        numy += int(z)
    #numy total number of npas in each precinct
    percent_npa = numy/num
    npa_dict[x] = percent_npa
sorted_npa_dict = sorted(npa_dict.items(), key = lambda x: x[1], reverse = True)
print(npa_dict["R009"], npa_dict["R015"], npa_dict["R035"])











