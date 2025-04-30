# AI Gesture Mouse Control

Control your mouse cursor using hand gestures captured through your webcam. This project uses computer vision and hand tracking to convert hand movements and gestures into mouse actions.

## Features

- Mouse cursor control using index finger
- Left click, right click, and double click gestures
- Scroll up/down functionality
- Mouse movement lock
- Visual feedback with on-screen buttons
- Smooth cursor movement

## Requirements

- Python 3.7 or higher
- Webcam
- Required packages (listed in requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-gesture-mouse.git
cd ai-gesture-mouse
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script:
```bash
python src/main.py
```

### Gesture Controls

- **Move Mouse**: Raise your index finger and thumb
- **Lock Movement**: Raise index, middle finger and thumb
- **Left Click**: Join index and middle fingers
- **Right Click**: Join index and middle fingers + raise ring finger
- **Double Click**: Join index and middle fingers + raise pinky
- **Scroll Up**: Join index and middle fingers + raise pinky (thumb down)
- **Scroll Down**: Join index and middle fingers (thumb down)

## Project Structure

```
ai-gesture-mouse/
├── src/
│   ├── main.py              # Main application script
│   └── utils/
│       ├── hand_detector.py # Hand detection and tracking
│       └── button.py        # UI button implementation
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```

## License

This project is part of AICTE Internship.

## Contributing

Feel free to open issues and pull requests for any improvements.