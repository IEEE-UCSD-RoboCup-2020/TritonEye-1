import cv2
import numpy as np
import sys

def main():
    #cap = cv2.VideoCapture('ballRolling.mp4')
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, default_file = cap.read()
        # if frame is read correctly ret is True
        filename = default_file
    # Loads an image
        #src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_COLOR)
        src = default_file
    # Check if image is loaded fine
        if src is None:
            print ('Error opening image!')
            print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
            return -1
        #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    
        gray = cv2.medianBlur(gray, 15)
    
        rows = gray.shape[0]
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=20, maxRadius=400)
    
    
        if circles is not None:
            #print('circles found')
            circles = np.uint16(np.around(circles))
            a = 0
            srcnew = src
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle center
                cv2.circle(srcnew, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = i[2]
                cv2.circle(srcnew, center, radius, (255, 0, 255), 3)
                print('center ',a,': ',center,)
                print('radius  ',a,':',radius,)
                print('BGR: ' ,src[i[1]][i[0]])
                a = a + 1
                #print(radius)
            cv2.imwrite('outputvid.png', src)
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            cv2.imshow('frame', srcnew)
            if cv2.waitKey(1) == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()