import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture('robotDancing.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        canny = cv2.Canny(frame, 100, 350)
        cv2.imwrite("output.png", cv2.Canny(frame, 100, 350))
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv2.imshow('frame', canny)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()