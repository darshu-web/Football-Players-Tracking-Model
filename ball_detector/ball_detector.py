import cv2
import numpy as np

class BallDetector:
    def __init__(self, color_range=((29, 86, 6), (64, 255, 255))):
        self.color_lower = np.array(color_range[0], dtype="uint8")
        self.color_upper = np.array(color_range[1], dtype="uint8")

    def detect_ball(self, frame):
        # Convert the image to the HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Create a mask for the ball color
        mask = cv2.inRange(hsv_frame, self.color_lower, self.color_upper)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # If no contours are found, return None
        if not contours:
            return None
        
        # Find the largest contour and its bounding box
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Return the bounding box of the detected ball
        return (x, y, w, h)
