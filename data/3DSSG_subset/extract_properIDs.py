import json

# Open and read train_scans.txt to get file ids
with open('validation_scans.txt', 'r') as f:
    file_ids = [line.strip() for line in f]

# Initialize a list to store matching scans
matching_scans = []

# Open and read relationshop.json to find matches with file ids
with open('relationships.json', 'r') as f:
    data = json.load(f)
    for scan_i in data['scans']:
        if scan_i['scan'] in file_ids:
            matching_scans.append(scan_i)

# Save matching scans to relationship_train.json
with open('relationships_validation.json', 'w') as f:
    json.dump(matching_scans, f, indent=4)

print("Matching scans saved to relationships_validation.json.")
