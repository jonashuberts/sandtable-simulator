# SandTable Simulator

SandTable Simulator is a Python-based application using pygame to simulate a sand table with customizable paths and ball animations.

![SandTable Simulator](web.png)

## Features

- Display paths read from .thr files in a graphical interface.
- Smooth animation of a ball following the displayed paths.
- Option to display paths using RGB colors based on polar coordinates.

## Requirements

- Python 3.x
- pygame library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/sandtable-simulator.git
   ```

2. **Install pygame:**

   If you haven't installed pygame yet, you can install it using pip:

   ```bash
   pip install pygame
   ```

3. **Run the application:**

   Navigate to the project directory and run `main.py`:

   ```bash
   cd sandtable-simulator
   python main.py
   ```

## Usage

- Upon running the application, it will display a pygame window showing paths and a ball animation.
- Paths are read from .thr files located in the specified `input_folder`.
- The ball follows the paths with smooth animation, adjusting speed and appearance based on configuration variables in `constants.py`.

## Configuration

- Adjust configuration variables in `constants.py` to customize screen dimensions, colors, ball speed, and more.
- Set `use_rgb_path` to `True` to display paths using RGB colors derived from polar coordinates.

## File Structure

```
sandtable-simulator/
│
├── main.py           # Main entry point of the application
├── constants.py      # Configuration variables
├── utils.py          # Utility functions (polar/cartesian conversions, file operations)
└── drawing.py        # Drawing functions (path rendering)
```
