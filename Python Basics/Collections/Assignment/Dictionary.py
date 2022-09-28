import json

# input
airlines = ["US", "Australia", "Pakistan", "UAE", "Canada", "Australia", "US", "Australia", "Canada",
            "UAE", "Canada", "Pakistan", "US"]

# output
'''
airline_count = {
    "US" : 3,
    "Australia" : 3,
    "Pakistan" : 2,
    "UAE" : 2,
    "Canada" : 3
}
'''

unique_countries = []
airline_count = {}

for country in airlines:
    if country not in unique_countries:
        unique_countries.append(country)

print(unique_countries)

for country in unique_countries:
    airline_count[country] = 0

print(airline_count)

for country in airlines:
    airline_count[country] += 1


print(json.dumps(airline_count, indent=4))



