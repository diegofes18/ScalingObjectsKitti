# Image and Annotation Resizer
This Python script resizes images and annotations in the KITTI format to a specified size. The resized images and annotations are saved to a new directory structure, which can be used for training computer vision models. This script uses the OpenCV library to resize images and the os library to create directory structures and read files.

## Usage
To use this script, you will need to have Python 3 and OpenCV installed on your machine. You can run the script with the following command:

```
python image_annotation_resizer.py img_path notes_path output_path
```

The script takes three arguments:

- img_path: The path to the directory containing the images in the KITTI format.
- notes_path: The path to the directory containing the annotations in the KITTI format.
- output_path: The path to the directory where the resized images and annotations will be saved.

The script will create a new directory structure in the output_path directory with two subdirectories: images and annotations. The resized images and annotations will be saved in these subdirectories.

## Example
Here is an example of how to use the script:

```
python image_annotation_resizer.py ./data/images ./data/annotations ./output
```

This command will resize the images and annotations in the ./data/images and ./data/annotations directories to 284x284 pixels and save the resized images and annotations in the ./output directory.

## License
This script is licensed under the MIT License. See the LICENSE file for more information.

## Contributing
If you have any suggestions or find any issues with this script, please feel free to submit an issue or pull request. Your contributions are greatly appreciated!
