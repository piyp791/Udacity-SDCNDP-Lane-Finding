# **Finding Lane Lines on the Road** 

Lane detection is one of the most important aspects of autonomous navigation. It is the first step in enabling the vehicle to visualize and then make sense or its environment.

The goals for this project was to create a pipeline that finds lane lines on the road.

[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

![alt text][image1]

### 1. The Approach

1. The image is first converted to grayscale.

[image2]: ./test_images_1/solidWhiteCurve.jpg "Original"
![alt text][image2]

2. The grayed image is then soomthed out using the opencv library's gaussianBlur function.
3. Then the edges in the image are detected by passing the smoothed out gray image onto the opencv's canny function. 
Canny function works using the intensity gradients of the image, with detecting edges (nothing but collection of points in really close quarter having intensity gradient over a certain a threshold given as an input to the algorithm.)
4. After the edges have been found out, only that portion of the image needs to be taken for further processing having road lane lines. 
This part is achieved by masking the 
5. Now that the image only has the canny edges for the lane lines portion and the rest of it blacked out, lines are drawn from those detected edges.
Drawing lines from the detected edges is one of the most important aspects for this project. For two single lines to be drawn over the edges, one for each line of the lane (left and right), the draw_line() is function is modified in the following way:
  5. a. The array of lines returned from the hough_lines() function is iterated upon and for each line, the slope is calculated and stored in spearate arrays for positive and negative slopes.
  5. b. Whether the slope is positive or negative, it can be inferred if the line belongs to the left line of the lane or the right line.   
  5. c. To remove noisy lines pertaining to edges (and thus lines) not belonging to any lane, but still within the lane area, a threshold is defined for the value of te slope acceptable for the algorithm.
  5. d. For each line, the intercept is also calculated and stored.
  5. e. To extrapolate the lines returned from the hough lines, we need the two endpoints for the two lane lines and their corresponding  slope values.
  5. f. The y_max for both lane lines is the point at the bottom of the image, from where the lines start.
  5. g. The slope for both lines can be calculated by taking the average of all the positive and negative slope values. This also helps in removing some noise pertaining to the slope values.
  5. h. Similarly, the intercept for both lane lines can be calculated by taking the mean of the stored intercepts.
  5. i. The y_min can be found out by taking the comparing all the y values in all the lines and taking the minimum value.
  5. j. Now x_min and x_max can be found out by just fitting all the peviously found parameters in an equation of the line.
  5. k. The line can now be drawn over the lane lines.
6. This image is now combined with the original image and the returned image would be the original one, with the algorithm generated lane lines drawn over it.


### 2. Identify potential shortcomings with your current pipeline

1. The method used to detect the lane lines is not quite robust. A change of scene could thrwo it off thus rendering the entire pipeline useless.
2. As noticed in the challenge.mp4 video, the canny edge detection of the algorithm is thrown off by light. The noise increases substantially, which makes it hard for the algorithm to detect lane lines.


### 3. Suggest possible improvements to your pipeline

For the current pipeline, the lane line area is being detected using quite ad-hoc solution which might not work for all the cases. This could be improved by using some sort of regresison analysis over the coordinates of lane lines and subsequent position and shape of the area covering the entire lane.

Another improvement for the pipeline could be for slope detection and handling. Right now, the pipeline cant not handle much noise, especially thrown by light. Use of pattern recognition could be used to apply better thresholds over accepted values of slope for lane lines.  