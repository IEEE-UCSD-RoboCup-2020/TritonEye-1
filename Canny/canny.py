import cv2
import numpy as np

def main():
    img = cv2.imread("./images/theBall.png", 0)
    cv2.imwrite("canny.png", cv2.Canny(img, 100, 350))
    cv2.imshow("canny", cv2.imread("canny.png"))
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()