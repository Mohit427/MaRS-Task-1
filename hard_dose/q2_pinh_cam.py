import cv2
import numpy as np
import math

# ── Camera specifications ──
RESOLUTION_WIDTH  = 1280   # pixels
RESOLUTION_HEIGHT = 720    # pixels
DIAGONAL_FOV      = 55     # degrees
REAL_ARROW_WIDTH  = 17.0   # cm

def calculate_focal_length():
    """
    Calculate focal length in pixels from camera specs.
    Uses diagonal FOV and resolution to derive horizontal FOV first,
    then computes focal length from horizontal FOV.
    """
    # Step 1 — diagonal resolution in pixels
    diagonal_pixels = math.sqrt(RESOLUTION_WIDTH**2 + RESOLUTION_HEIGHT**2)

    # Step 2 — convert diagonal FOV to horizontal FOV
    # Use half angles to avoid doubling errors
    half_diag_fov_rad = math.radians(DIAGONAL_FOV / 2)

    # Scale the tangent by the ratio of horizontal to diagonal pixels
    half_horiz_fov_rad = math.atan(
        math.tan(half_diag_fov_rad) * (RESOLUTION_WIDTH / diagonal_pixels)
    )

    horizontal_fov_deg = math.degrees(half_horiz_fov_rad) * 2
    print(f"Derived horizontal FOV: {horizontal_fov_deg:.2f} degrees")

    # Step 3 — focal length in pixels
    # focal_length = (image_width / 2) / tan(horizontal_fov / 2)
    focal_length = (RESOLUTION_WIDTH / 2) / math.tan(half_horiz_fov_rad)
    print(f"Calculated focal length: {focal_length:.2f} pixels")

    return focal_length


def find_distance(perceived_width):
    """
    Calculate real-world distance to the arrow using pinhole camera model.

    Formula:
        distance = (real_width × focal_length) / perceived_width

    perceived_width — width of arrow in pixels (from bounding box)
    Returns distance in cm
    """
    focal_length = calculate_focal_length()

    if perceived_width == 0:
        print("Error: perceived width is zero — cannot calculate distance")
        return -1

    distance = (REAL_ARROW_WIDTH * focal_length) / perceived_width
    return distance


def detect_arrow(image_path):
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(
        edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    arrow_found = False

    for cnt in contours:
        approx = cv2.approxPolyDP(
            cnt, 0.02 * cv2.arcLength(cnt, True), True
        )

        # Arrows typically have 7 sides
        if len(approx) == 7:
            cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)
            print("Arrow detected!")

            # Calculate bounding box
            x, y, w, h = cv2.boundingRect(approx)
            perceived_width = max(w, h)

            print(f"Perceived width (pixels): {perceived_width}")

            # Calculate distance
            distance = find_distance(perceived_width)
            print(f"Estimated Distance: {distance:.2f} cm")

            arrow_found = True

    if not arrow_found:
        print("No arrow detected in the image.")

    # Show the result
    cv2.imshow('Detected Arrow', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__=="__main__":
    image_path = "arrow1.png"
    detect_arrow(image_path)