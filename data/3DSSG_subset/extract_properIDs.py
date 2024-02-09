import json

# # Function to read JSON file and extract 'scans' list
# def extract_scans_from_json(json_file):
#     with open(json_file, 'r') as file:
#         data = json.load(file)
#         scans = data['scans']
#     return scans

# # Function to combine 'scans' lists from two JSON files
# def combine_scans(json_file1, json_file2):
#     scans1 = extract_scans_from_json(json_file1)
#     scans2 = extract_scans_from_json(json_file2)
#     combined_scans = scans1 + scans2
#     return combined_scans

# # Paths to JSON files
# json_file1 = 'relationships_train_old.json'
# json_file2 = 'relationships_validation_old.json'

# # Combine scans from both files
# combined_scans = combine_scans(json_file1, json_file2)
# final_scans_data = {"scans": combined_scans}
# # Print combined scans
# output_file = "combined_scans.json"
# with open(output_file, 'w') as file:
#     json.dump(final_scans_data, file, indent=4)
# print(json.dumps(final_scans_data, indent=4))



# Open and read train_scans.txt to get file ids
with open('train_scans.txt', 'r') as f:
    file_ids = [line.strip() for line in f]

print(file_ids)

ids_to_be_saved = []

# Open and read relationshop.json to find matches with file ids
with open('combined_scans.json', 'r') as f:
    data = json.load(f)
    print(data)
    for scan_i in data["scans"]:
        print(scan_i)
        if scan_i['scan'] not in file_ids:
            continue
        print('\n')

        ids_to_be_saved.append(scan_i)


# Save matching scans to relationship_validation.json
ids_combined = {"scans": ids_to_be_saved}
with open('relationships_train.json', 'w') as f:
    json.dump(ids_combined, f, indent=4)





# Open and read validation_scans.txt to get file ids
with open('validation_scans.txt', 'r') as f:
    file_ids = [line.strip() for line in f]

print(file_ids)

ids_to_be_saved = []

# Open and read relationshop.json to find matches with file ids
with open('combined_scans.json', 'r') as f:
    data = json.load(f)
    print(data)
    for scan_i in data["scans"]:
        print(scan_i)
        if scan_i['scan'] not in file_ids:
            continue
        print('\n')

        ids_to_be_saved.append(scan_i)


# Save matching scans to relationship_train.json
ids_combined = {"scans": ids_to_be_saved}
with open('relationships_validation.json', 'w') as f:
    json.dump(ids_combined, f, indent=4)