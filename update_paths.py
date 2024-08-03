import json
import os

# Load faces.json
with open('faces.json', 'r') as f:
    data = json.load(f)

# Function to update paths
def update_paths(face_list):
    for face in face_list:
        # Extract the image file name from the existing path
        image_file_name = os.path.basename(face['src'])
        # Update the path to be relative to the lfw2 folder
        face['src'] = os.path.join('lfw2', face['name'], image_file_name).replace('\\', '/')

# Update paths for both lists
update_paths(data.get('multiple_images_faces', []))
update_paths(data.get('single_image_faces', []))

# Save updated faces.json
with open('faces.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Paths updated successfully.")
