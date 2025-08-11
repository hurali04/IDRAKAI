country_information = {
    "Pakistan": 255_220_000,
    "China": 1_416_100_000,
    "Indonesia": 285_721_000,
    "United States": 347_276_000,
    "India": 1_463_870_000
}

country_information["Monaco"] = 40_000

highest = max(country_information, key=country_information.get)
lowest = min(country_information, key=country_information.get)

print("Countries Information:", country_information)
print("Country with highest population:", highest)
print("Country with lowest population:", lowest)
