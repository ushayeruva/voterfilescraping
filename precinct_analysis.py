import pandas as pd 
total = pd.read_csv("votebuilder_total_precinct_11.6.csv", index_col=0)
precinct_list = []
for x in total.precinct.unique():
    precinct_list.append(x)
del precinct_list [-1]
all_precincts = []
for x in precinct_list: 
    precinct = {}
    precinct["Name"] = x 
    df = total[total["precinct"] == x]
    num_people = df["Total People"]
    num = 0 
    for y in num_people:
        num += int(y)
    #num = total number of people in each precinct
    df2 = df[df["Ethnicity"] == "White"]
    num_whites = df2["Total People"]
    numwhite = 0 
    for x in num_whites:
        numwhite += int (x)
    precinct["white"] = (numwhite / num)
    df3 = df[df["Ethnicity"] == "African American"]
    num_africanamericans = df3["Total People"]
    numafricanamericans = 0 
    for x in num_africanamericans:
        numafricanamericans += int (x)
    precinct["african_americans"] = (numafricanamericans / num)
    df4 = df[df["Ethnicity"] == "Hispanic"]
    num_hispanics = df4["Total People"]
    numhispanics = 0 
    for x in num_hispanics:
        numhispanics += int (x)
    precinct["hispanics"] = (numhispanics / num)

    df5 = df[df["Ethnicity"] == "Other"]
    num_other = df5["Total People"]
    numother = 0 
    for x in num_other:
        numother += int (x)
    precinct["other"] = (numother / num)

    df6 = df[df["Gender"] == "Male"]
    num_male = df6["Total People"]
    nummale = 0 
    for x in num_male:
        nummale += int (x)
    precinct["male"] = (nummale / num)
    df7 = df[df["Gender"] == "Female"]
    num_women = df7["Total People"]
    numwomen = 0 
    for x in num_women:
        numwomen += int (x)
    precinct["female"] = (numwomen / num)
    df8 = df[df["Age"] == "18 to 24"]
    num_18 = df8["Total People"]
    num18 = 0 
    for x in num_18:
        num18 += int (x)
    precinct["18 - 24"] = (num18 / num)
    df9 = df[df["Age"] == "25 to 34"]
    num_25 = df9["Total People"]
    num25 = 0 
    for x in num_25:
        num25 += int (x)
    precinct["25 - 34"] = (num25 / num)
    df10 = df[df["Age"] == "35 to 49"]
    num_35 = df10["Total People"]
    num35 = 0 
    for x in num_35:
        num35 += int (x)
    precinct["35 - 49"] = (num35 / num)
    df11 = df[df["Age"] == "50 to 64"]
    num_50 = df8["Total People"]
    num50 = 0 
    for x in num_50:
        num50 += int (x)
    precinct["50 - 64"] = (num50 / num)
    df12 = df[df["Age"] == "65+"]
    num_65 = df12["Total People"]
    num65 = 0 
    for x in num_65:
        num65 += int (x)
    precinct["65+"] = (num65 / num)
    all_precincts.append(precinct)

for x in all_precincts:
    if x["Name"] == "R035":
        print(x)

    

    


