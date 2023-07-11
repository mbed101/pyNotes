import cv2

# Load the main image and the template image
main_image = cv2.imread('main_image.jpg')
template_image = cv2.imread('template_image.jpg')

# Convert both images to grayscale
main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

# Apply template matching
result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)

# Set a threshold for the similarity score
threshold = 0.8

# Find the locations where the template matches the main image above the threshold
locations = np.where(result >= threshold)
for pt in zip(*locations[::-1]):
    # Draw a rectangle around the matched region
    cv2.rectangle(main_image, pt, (pt[0] + template_image.shape[1], pt[1] + template_image.shape[0]), (0, 255, 0), 2)

# Display the result
cv2.imshow('Result', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
