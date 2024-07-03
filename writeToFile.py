import os

def get_unique_filename(base_name):
    if not os.path.exists(base_name):
        return base_name
    
    base, extension = os.path.splitext(base_name)
    counter = 1
    
    while True:
        new_name = f"{base}{counter}{extension}"
        if not os.path.exists(new_name):
            return new_name
        counter += 1

def save_to_file(data, filename):
    checkedFilename = get_unique_filename(filename)
    with open(checkedFilename, 'w') as file:
        if isinstance(data, dict):
            for key, value in data.items():
                print(f"{key}: {value}\n")
                file.write(f"{key}: {value}\n")
        else:
            for value in data:
                print(f"{value}\n")
                file.write(f"{value[0]}: {value[1]}\n")
