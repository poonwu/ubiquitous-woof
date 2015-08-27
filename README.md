# ubiquitous-woof

## Day 1

Tested OpenCV, ran into [https://github.com/Itseez/opencv/issues/4603]() bug with constants.
Issue diverted by using `detectMultiScale` for `CascadeClassifier`.

Defect detection on Bill Gates' face. Experimenting looks okay with some noise. Expect more noise when testing with real images from camera iface. How do we eliminate that? Maybe by putting higher thres.?
