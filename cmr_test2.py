import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print(ret)

while ret:

# Our operations on the frame come here
  # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  ret, frame = cap.read()

# Display the resulting frame
  cv2.imshow('frame',frame)
 
  if cv2.waitKey(0) & 0xFF == ord('q'):
    break


# When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()