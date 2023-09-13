import os

def update_config(path_to_config, desired_path):
    # Read the content of _config.yml
    with open(path_to_config, 'r') as file:
        content = file.read()
    
    # Check if the desired path is already in the content
    if desired_path not in content:
        # If not, append the path information to the file
        with open(path_to_config, 'a') as file:
            file.write(f'\nassets_path: {desired_path}\n')

    print(f"Path '{desired_path}' ensured in {path_to_config}")

if __name__ == "__main__":
    # Define path to _config.yml and desired asset path
    path_to_config = './_config.yml'
    desired_path = './assets/gallery/'

    # Call the update function
    update_config(path_to_config, desired_path)