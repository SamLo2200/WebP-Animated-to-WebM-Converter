# WebP Animated to WebM Converter

## Description

The WebP Animated to WebM Converter is a program designed to facilitate the conversion of animated WebP images into WebM format. This tool aims to address common issues encountered with other converters available on the internet, such as desaturated colors, low quality, and improper frame playback.

The purpose of this converter is to ensure a seamless and accurate conversion process while maintaining the vibrancy and fidelity of the original animated WebP image.

## Features

1. **Preservation of Color Accuracy**: The converter is specifically designed to retain the original color saturation of animated WebP images during the conversion process. This ensures that the resulting WebM file accurately represents the original colors of the animation.

2. **High-Quality Output**: The converter employs advanced algorithms to ensure high-quality output in the resulting WebM file. It optimizes the conversion process to preserve as much detail as possible, resulting in a visually appealing and crisp final output.

3. **Frame-by-Frame Playback**: Unlike many other converters, the WebP Animated to WebM Converter ensures proper frame-by-frame playback of the animated WebP image. Each frame is correctly displayed in sequence, maintaining the intended animation flow without overlapping or stacking issues.

## Requirements

To run this program, you will need the following:

- **Operating System**: The converter is compatible with Windows. 
- **Python**: Ensure you have Python 3.x installed on your system.
- **Dependencies**: This script doesn't use typical python library, instead binary execuable is used. 

Please download the following execuable: 

1. https://developers.google.com/speed/webp/download
2. https://www.gyan.dev/ffmpeg/builds/ (Recommended to install the full version, because I haven't test whether the essential ffmpeg will work)

## Usage

Remember to change the following path variables in order for this script to work

1. file
2. pathToWebpmux (located in grep_file_info function)
3. extractedPath (located in extract_animated_webp function)
4. source (The folder path should be same as the extractedPath variable, located in the render function)
5. endOutput (located in the render function) 
6. pathToFFMPEG (located in the render function)

<br />
<br />

### Reminder for people who are not familiar with python 

In python, for any path, you need to use `\\` to represent a layer of folder

For example if the file path is: ```"C:\Users\sam\Downloads\WebP_Animated_Extractor"```.
Please change it to ```"C:\\Users\\sam\\Downloads\\WebP_Animated_Extractor"```

<br />

## Contributing

Feel free to contribute to this project to enhance the functionality and address any additional issues that users may encounter. If you would like to contribute to this project, please follow these steps:

1. Fork the repository to your GitHub account.
2. Create a new branch with a descriptive name for your contribution.
3. Make the necessary changes and improvements in your branch.
4. Test your changes to ensure they are functioning as expected.
5. Commit and push your changes to your forked repository.
6. Open a pull request in the original repository, explaining your changes and improvements.

## License

[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This project is licensed under the GNU General Public License version 3. Please see the `LICENSE` file for the full text of the license.

#### License Summary

The GPLv3 license grants users the freedom to modify, distribute, and use the project's source code, both in individual and commercial contexts. It requires that any modifications made to the code be released under the same license and mandates the availability of the source code.

For more details, please read the [full GPLv3 license](https://www.gnu.org/licenses/gpl-3.0).


## Disclaimer

While the WebP Animated to WebM Converter aims to provide accurate and high-quality conversions, it is essential to note that no software is perfect. The converter may not address all possible edge cases or scenarios. Please use the tool responsibly and consider testing the output thoroughly for your specific use cases. The developers and contributors are not liable for any issues or damages that may arise from the use of this program.

If you encounter any bugs or have suggestions for improvement, please create an issue on the repository, and we will do our best to address it in a timely manner.

Happy converting!
