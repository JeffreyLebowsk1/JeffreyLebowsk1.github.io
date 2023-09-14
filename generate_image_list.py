import os

def generate_image_list(directory):
    html_string = "<div class='image-gallery'>\n"

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Filter only image files by their extensions
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                relative_path = os.path.join(root, file).replace("\\", "/")  # Adjust path format
                image_tag = f"<img src='{relative_path}' width='200px' alt='{file}'>\n"
                html_string += image_tag

    html_string += "</div>"

    # Write the generated HTML to a file
    with open('image_list.html', 'w') as f:
        f.write(html_string)

    print("Image list generated successfully in 'image_list.html'.")

if __name__ == "__main__":
    directory_to_scan = "./assets"  # Replace with the path to your image directory
    generate_image_list(directory_to_scan)

