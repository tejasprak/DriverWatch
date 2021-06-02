# DriverWatch
This is a (WIP) real-time drowsy driving detector that will alert the driver if their eyes are closing and they are at risk of falling asleep. It has been implemented using 1) HAAR feature-based cascade classifier 2) dlib's fast and efficient HOG (Histogram of Oriented Gradients) + Linear SVM (support vector machine) 3) MMOD CNN


Completed: HAAR-based detector. Utilizing HAAR cascade classifier to detect eyes, and alerts if eyes are not detected.
![HAAR In Action GIF](gif/HAAR_based_detector.gif)

The problem with HAAR is that the lighting becomes an issue. A possible solution is to use the more robust HOG+LinearSVM and the MMOD CNN options.

TODO: Explore preprocessing options on frame to improve HAAR efficiency. Complete implementation of HOG+Linear SVM as well as MMOD CNN. Explore more efficient ways to determine whether eyes are drooping, rather than using a binary-style detection.
