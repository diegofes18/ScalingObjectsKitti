#Import libraries
import sys
import os
import cv2

#Variables with the arguments
img_path = sys.argv[1]
notes_path = sys.argv[2]
output_path = sys.argv[3]

#Create directory structure
os.makedirs(os.path.join(output_path, 'images'), exist_ok=True)
os.makedirs(os.path.join(output_path, 'annotations'), exist_ok=True)

#Read files on a loop (it's the same if its the image path or annotations)
for file in os.listdir(img_path):
    
    #Rename the file with just the number and .jpg extension
    file_number = file.split("_")[0]
    new_imgfile_name = f"{file_number}.jpg"

    #Read the image with OpenCV 
    image_path = os.path.join(img_path, file)
    image = cv2.imread(image_path)

    # Resize image
    resized_image = cv2.resize(image, (284,284))

    #Write the image on the new output images path
    image_output_path = os.path.join(output_path, 'images', new_imgfile_name)
    cv2.imwrite(image_output_path, resized_image)

    #Rename the annotations path
    new_notefile_name = f"{file_number}.txt"

    #Start reading the lines in the KITTI format file
    annotation_file_path = os.path.join(notes_path, os.path.splitext(file)[0] + '.txt')
    with open(annotation_file_path, 'r') as f:

        annotations = f.readlines()


    output_annotations = []
    for annotation in annotations:
        # Loop and scale for each line
        # Each line represents the values for the object 
        # I just need the colummns 4 5 6 7 that are the coordinates of the 
        # bounding box
        annotation_values = annotation.split()

        # name always  = helmet 
        label = annotation_values[0]

        x_min = int(float(annotation_values[4]))
        y_min = int(float(annotation_values[5]))
        x_max = int(float(annotation_values[6]))
        y_max = int(float(annotation_values[7]))

        # Scale bounding box coordinates
        scalefactor_x = 284 / image.shape[1]
        scalefactor_y = 284 / image.shape[0]

        scaled_x_min = int(x_min * scalefactor_x)
        scaled_y_min = int(y_min * scalefactor_y)
        scaled_x_max = int(x_max * scalefactor_x)
        scaled_y_max = int(y_max * scalefactor_y)

        # The new scaled information appended to the array
        # the other parameters are always zero
        output_annotations.append(f"{label} 0 0 0 {scaled_x_min} {scaled_y_min} {scaled_x_max} {scaled_y_max} 0 0 0 0 0 0 0\n")

    # Write the lines
    output_annotation_file_path = os.path.join(output_path, 'annotations', new_notefile_name)
    with open(output_annotation_file_path, 'w') as f:
        f.writelines(output_annotations)




