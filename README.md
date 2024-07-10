
# Visual Comparison

This Python script compares a baseline image with an actual image taken from a webpage. After any source code modifications, the visual changes can be easily compared through this script.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Selenium (`pip install selenium`)
- Visual-comparison (`pip install visual-comparison`) 

You will also need the appropriate WebDriver for your browser. This example uses ChromeDriver.

## How to Use

1. **Set Up WebDriver**: Ensure that the WebDriver executable (e.g., `chromedriver`) is in your system's PATH or specify its location in the script.
2. **Update URLs and Credentials**: Modify the script to target your specific webpage and use the appropriate login credentials.

### Steps

1. **Open the Target Webpage**: The script navigates to the target webpage.
2. **Login**: Logs into the website using provided credentials.
3. **Take Screenshots**: Takes a screenshot after login to visualize the changes.
4. **Compare Images**: Compares the baseline image (expected) with the actual image taken after login.
5. **Save Result**: Saves the comparison result and prints the similarity index.

## Usage

### Running the Script

1. For creating baseline image, run '**baseline_image.py**'
2. Then image comparison can be performed through executing '**image_comparison.py**'

