# Weight Calculation Application Documentation

## Overview

The Weight Calculation Application is a Tkinter-based graphical user interface (GUI) application designed to calculate and display the equivalent weight of a user on different celestial bodies (Sun, Moon, Mars) based on their weight on Earth.

## Table of Contents

1. [Setup and Installation](#setup-and-installation)
2. [Application Layout](#application-layout)
3. [Functionality](#functionality)
4. [Image Handling](#image-handling)
5. [Running the Application](#running-the-application)
6. [Conclusion](#conclusion)

## Setup and Installation

### Prerequisites

- Python 3.x installed on your system.
- Tkinter library (usually comes with Python installation).
- PIL (Pillow) library for image handling.

### Installation

1. **Install Pillow**:
   ```bash
   pip install pillow
   ```

2. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/your-repo/weight-calculation-app.git
   cd weight-calculation-app
   ```

3. **Prepare Images**:
   Place the images `earth.png`, `sun.png`, `moon.png`, and `mars.jpg` in the same directory as your script.

## Application Layout

The application window has a black background and a fixed size of 380x300 pixels. It includes an entry field for the user to input their weight on Earth and displays images and equivalent weights for the Sun, Moon, and Mars.

### Main Window

- **Title**: "Calculate weight"
- **Background Color**: Black (`#000000`)
- **Fixed Size**: 380x300 pixels

### Widgets

- **Earth Image**: Displayed at the top.
- **Input Label**: Prompting the user to input their weight on Earth.
- **Input Field**: Entry widget for user input.
- **Submit Button**: To trigger the weight calculation.
- **Images and Labels**: For the Sun, Moon, and Mars along with the calculated weights.

## Functionality

The application calculates the equivalent weight on different celestial bodies using predefined conversion factors:
- **Sun**: 27.01 times the Earth's weight.
- **Moon**: 0.16 times the Earth's weight.
- **Mars**: 0.38 times the Earth's weight.

### Weight Calculation Function
```python
def click():
    mas = float(Mass.get())
    mass_sun = mas * 27.01
    mass_moon = mas * 0.16
    mass_mars = mas * 0.38

    mass_sun1 = str(mass_sun)
    mass_moon1 = str(mass_moon)
    mass_mars1 = str(mass_mars)

    mass_sun_lbl = Label(root, text=mass_sun1 + "公斤", bg="black", fg="white")
    mass_sun_lbl.grid(row=3, column=0, pady=10, padx=10)

    mass_moon_lbl = Label(root, text=mass_moon1 + "公斤", bg="black", fg="white")
    mass_moon_lbl.grid(row=3, column=1, pady=10, padx=10)

    mass_mars_lbl = Label(root, text=mass_mars1 + "公斤", bg="black", fg="white")
    mass_mars_lbl.grid(row=3, column=2, pady=10, padx=10)
```

### Image Handling

The application uses the Pillow library to resize and display images for Earth, Sun, Moon, and Mars.

#### Resizing and Displaying Images
```python
earth = Image.open("earth.png")
resized_earth = earth.resize((100, 100), Image.ANTIALIAS)
new_earth = ImageTk.PhotoImage(resized_earth)
earth_lbl = Label(root, image=new_earth, border=0)
earth_lbl.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

# Similarly for Sun, Moon, and Mars
```

## Running the Application

To run the application, execute the Python script containing the code:
```bash
python weight_calculation_app.py
```

This will launch the main window of the Weight Calculation Application. From here, you can input your weight on Earth and view the equivalent weights on the Sun, Moon, and Mars.

## Conclusion

This documentation provides a comprehensive overview of the Weight Calculation Application, including setup, functionality, and usage. The application is designed to be user-friendly, allowing users to easily calculate their weight on different celestial bodies based on their Earth weight.
