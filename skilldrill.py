#Skilldrill 1

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for key, value in counties_dict.items():
#     print(f"{key} county has {value:,} registered voters")

#Skilldrill 2

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353},
                 {"county":"Jefferson", "registered_voters": 432438}]

for i in voting_data:
    #print("My ith position is: ", i);
    print(f"{i['county']} county has {i['registered_voters']:,} registered voters")
    #print("-----------------")
        
    