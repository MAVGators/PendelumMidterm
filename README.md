
# PendelumMidterm

## Overview
PendelumMidterm is an alternative to Pasco Capstone for video analysis by Caiman, David and Brandon. This project provides tools and scripts to analyze video data for double and single pendelums effectively using Python, because
Pasco was being annoying to work with.

## Features
- Capture mouse clicks to select points on video frames.
- Calculate angles between selected points.
- Save angle data and timestamps to CSV files.

## How to Use
1. **Clone the Repository**
   ```bash
   git clone https://github.com/MAVGators/PendelumMidterm.git
   cd PendelumMidterm
   ```

2. **Install Dependencies**
   Ensure you have Python installed. Then, install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Analysis**
   Modify the `filename` variable in `cheap_pasco.py` to point to your video file:
   ```python
   filename = r"path/to/your/video/file.mp4"
   ```
   Then, run the script:
   ```bash
   python cheap_pasco.py
   ```

4. **Select Points**
   - Click on three points in the displayed video frame to draw lines and calculate angles.
   - The angles and timestamps will be saved to CSV files.

5. **View Results**
   The output CSV files will be saved in the current directory with the timestamp in their filenames.
