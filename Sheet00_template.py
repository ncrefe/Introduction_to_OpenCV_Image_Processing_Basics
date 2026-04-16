"""
Exercise 0 for MA-INF 2201 Computer Vision WS25/26
Introduction to OpenCV - Template
Python 3.12, OpenCV 4.11, NumPy 2.3.3
Image: bonn.jpeg
"""

import cv2
import numpy as np
import random
import time


# ============================================================================
# Exercise 1: Read and Display Image (0.5 Points)
# ============================================================================
def exercise1():
    """
    Read and display the image bonn.jpeg.
    Print the image dimensions and data type.
    """
    print("Exercise 1: Read and Display Image")

    # TODO: Read the image 'bonn.jpeg' using cv2.imread()
    img = cv2.imread("bonn.jpeg")

    # TODO: Check if image was loaded successfully
    assert img is not None, "Error: Image not found or unable to load."

    # TODO: Display the image using cv2.imshow()
    cv2.imshow("Image", img)

    # TODO: Wait for a key press using cv2.waitKey(0)
    cv2.waitKey(0)

    # TODO: Close all windows using cv2.destroyAllWindows()
    cv2.destroyAllWindows()

    # TODO: Print image dimensions (height, width, channels)
    print("Image shape (Height, Width, Channels):", img.shape)

    # TODO: Print image data type
    print("Image data type:", img.dtype)

    print("Exercise 1 completed!\n")
    return img


# ============================================================================
# Exercise 2: HSV Color Space (0.5 Points)
# ============================================================================
def exercise2(img):
    """
    Convert image to HSV color space and display all three channels separately.
    """
    print("Exercise 2: HSV Color Space")

    # TODO: Convert to HSV using cv2.cvtColor() with cv2.COLOR_BGR2HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # TODO: Split HSV into H, S, V channels using cv2.split()
    h, s, v = cv2.split(hsv)

    # TODO: Display all three channels
    # Hint: You can concatenate them horizontally using cv2.hconcat()
    hsv_concat = cv2.hconcat([h, s, v])

    cv2.imshow("H | S | V Channels", hsv_concat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Exercise 2 completed!\n")
    return hsv


# ============================================================================
# Exercise 3: Brightness Adjustment with Loops (1 Point)
# ============================================================================
def exercise3(img):
    """
    Add 50 to all pixel values and clip to [0, 255] using nested for-loops.
    Display original and brightened images side by side.
    """
    print("Exercise 3: Brightness Adjustment with Loops")

    # TODO: Create a copy of the image
    result = img.copy()

    # TODO: Get image dimensions
    height, width, channels = result.shape

    # TODO: Use nested for-loops to iterate through each pixel, add 50 to pixel value, and clip pixel value to [0, 255]
    # Iterate over each pixel in the image
    for i in range(height):
        for j in range(width):
            for c in range(channels):
                # Add 50 to the current pixel value and clip it to [0, 255]
                # np.clip is required to ensure that pixel values remain within the valid range [0, 255]
                result[i, j, c] = np.clip(int(result[i, j, c]) + 50, 0, 255)

    # TODO: Display original and result side by side
    concatenated = cv2.hconcat([img, result])

    cv2.imshow("Original Img and Brighter Result Img", concatenated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Exercise 3 completed!\n")
    return result


# ============================================================================
# Exercise 4: Vectorized Brightness Adjustment (1 Points)
# ============================================================================
def exercise4(img):
    """
    Perform the same brightness adjustment using NumPy in one line.
    Compare execution time with loop-based approach.
    """
    print("Exercise 4: Vectorized Brightness Adjustment")

    # TODO: Time the loop-based approach (from exercise 3)
    copy_image = img.copy()

    height, width, channels = copy_image.shape

    start_time_loop = time.time()

    for i in range(height):
        for j in range(width):
            for c in range(channels):
                # Add 50 to the current pixel value and clip it to [0, 255]
                # np.clip is required to ensure that pixel values remain within the valid range [0, 255]
                copy_image[i, j, c] = np.clip(int(copy_image[i, j, c]) + 50, 0, 255)

    end_time_loop = time.time()

    # TODO: Time the vectorized approach
    start_time_vec = time.time()

    # TODO: Add 50 and clip in one line using np.clip()
    result = np.clip(img.astype(np.int16) + 50, 0, 255).astype(np.uint8)

    end_time_vec = time.time()

    # TODO: Print execution times
    print(f"Loop-based approach: {end_time_loop - start_time_loop:.4f} seconds")
    print(f"Vectorized approach: {end_time_vec - start_time_vec:.4f} seconds")

    # TODO: Display the result
    concatenated = cv2.hconcat([copy_image, result])

    cv2.imshow("Nested-Loop Approach vs Vectorized Approach", concatenated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Exercise 4 completed!\n")
    return result


# ============================================================================
# Exercise 5: Extract and Paste Patch (0.5 Points)
# ============================================================================
def exercise5(img):
    """
    Extract a 32×32 patch from top-left corner and paste at 3 random locations.
    """
    print("Exercise 5: Extract and Paste Patch")

    # TODO: Extract 32x32 patch from top-left corner (starting at 0,0)
    patch_size = 32
    patch = img[0:patch_size, 0:patch_size]  # slicing to get a 32x32 area

    # TODO: Create a copy of the image
    img_copy = img.copy()

    # TODO: Get image dimensions
    h, w, c = img.shape

    # TODO: Generate 3 random locations and paste the patch
    # Use random.randint() and ensure patch fits within boundaries
    for i in range(3):
        # TODO: Generate random coordinates and paste
        random_height = random.randint(0, h - patch_size)
        random_width = random.randint(0, w - patch_size)

        img_copy[random_height:random_height + patch_size, random_width:random_width + patch_size] = patch.copy()

    # TODO: Display the result
    cv2.imshow("Extract and Paste Patch", img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Exercise 5 completed!\n")


# ============================================================================
# Exercise 6: Binary Masking (0.5 Points)
# ============================================================================
def exercise6(img):
    """
    Create masked version showing only bright regions.
    Convert to grayscale, threshold at 128, use as mask.
    """
    print("Exercise 6: Binary Masking")

    # TODO: Convert to grayscale using cv2.cvtColor() with cv2.COLOR_BGR2GRAY
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # TODO: Apply binary threshold at value 128
    # Use cv2.threshold() with cv2.THRESH_BINARY
    # All pixels brighter than 128 become 255 (white), others become 0 (black)
    _, mask = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    # TODO: Apply mask to original color image
    # Hint: Use cv2.bitwise_and() with the mask
    # cv2.bitwise_and keeps pixel values only where mask == 255
    masked = cv2.bitwise_and(img, img, mask=mask)

    # TODO: Display original, mask, and masked result
    combined = cv2.hconcat([
        img,  # Original
        cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR),  # Binary mask (converted to 3 channels for display)
        masked  # Masked result
    ])

    cv2.imshow("Original | Mask | Masked Result", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Exercise 6 completed!\n")


# ============================================================================
# Exercise 7: Border and Annotations (1 Points)
# ============================================================================
def exercise7(img):
    """
    Add 20-pixel border and draw 5 circles and 5 text labels at random positions.
    """
    print("Exercise 7: Border and Annotations")

    # TODO: Add 20-pixel border using cv2.copyMakeBorder()
    # Use cv2.BORDER_CONSTANT with a color of your choice
    bordered = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT)

    # TODO: Get dimensions of bordered image
    h, w, c = bordered.shape

    # TODO: Draw 5 random circles
    # Use random.randint() and cv2.circle(img, center, radius, color, thickness)
    for i in range(5):
        # TODO: Implement circle drawing
        x = random.randint(20, w - 20)   # x → width
        y = random.randint(20, h - 20)   # y → height
        bordered = cv2.circle(bordered, (x, y), 20, (255, 255, 255), -1)

    # TODO: Add 5 random text labels
    # Use random.randint() and cv2.putText(img, text, org, font, fontScale, color, thickness)
    for i in range(5):
        # TODO: Implement text drawing
        x = random.randint(20, w - 100)
        y = random.randint(40, h - 20)
        bordered = cv2.putText(bordered, '100', (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                               1, (255, 0, 0), 2, cv2.LINE_AA)

    # TODO: Display the result
    cv2.imshow("Border", bordered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Exercise 7 completed!\n")


# ============================================================================
# Main function
# ============================================================================
def main():
    """
    Run all exercises.
    """
    print("=" * 60)
    print("Exercise 0: Introduction to OpenCV")
    print("=" * 60 + "\n")

    # Uncomment the exercises you want to run:
    img = exercise1()
    if img is None:
        return
    exercise2(img)
    exercise3(img)
    exercise4(img)
    exercise5(img)
    exercise6(img)
    exercise7(img)

    print("=" * 60)
    print("All exercises completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
