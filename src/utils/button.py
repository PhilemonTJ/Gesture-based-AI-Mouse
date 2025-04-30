import cv2
import time

class TextButton:
    """
    A simple button class for displaying text-based buttons on OpenCV windows
    with active/inactive states and timed activation features.
    """
    
    def __init__(self, text, x, y, width=175, height=30):
        """
        Initialize a new text button.
        
        Args:
            text (str): The text to display on the button
            x (int): X coordinate of the button's top-left corner
            y (int): Y coordinate of the button's top-left corner
            width (int): Width of the button (default: 175)
            height (int): Height of the button (default: 30)
        """
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_active = False
        self.active_until = 0

    def draw(self, img):
        """
        Draw the button on the given image.
        
        Args:
            img: OpenCV image to draw the button on
        """
        # Check if we should still show as active
        if self.active_until > 0:
            if time.time() > self.active_until:
                self.is_active = False
                self.active_until = 0

        # Set colors based on active state
        text_color = (255, 255, 255) if self.is_active else (0, 0, 0)
        bg_color = (0, 0, 0) if self.is_active else None
        border_color = (0, 0, 0)  # Always black border

        # Draw button background if active
        if self.is_active:
            cv2.rectangle(img, (self.x, self.y), 
                         (self.x + self.width, self.y + self.height), 
                         bg_color, -1)

        # Draw button border
        cv2.rectangle(img, (self.x, self.y), 
                     (self.x + self.width, self.y + self.height), 
                     border_color, 1)

        # Add text
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.7
        text_size = cv2.getTextSize(self.text, font, font_scale, 2)[0]
        text_x = self.x + (self.width - text_size[0]) // 2
        text_y = self.y + (self.height + text_size[1]) // 2
        cv2.putText(img, self.text, (text_x, text_y), 
                   font, font_scale, text_color, 2)

    def set_active(self, duration=0.5):
        """
        Set the button to active state for a specified duration.
        
        Args:
            duration (float): Duration in seconds to keep the button active
        """
        self.is_active = True
        self.active_until = time.time() + duration