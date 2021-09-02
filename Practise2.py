counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county,votes in counties_dict.items():
    print(county + ' ' + "has" + ' ' + str(votes) + ' ' + "registered voters")

#List of dictoniaries

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(voting_data)):
    print(voting_data[i])

#New code

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for i in voting_data:
    for j in i.values():
        print(j)    

#Next code
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for i in voting_data:

    print(i['county'])



