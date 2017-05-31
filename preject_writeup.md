# **Finding Lane Lines on the Road** 

Lane detection is one of the most important aspects of autonomous navigation. It is the first step in enabling the vehicle to visualize and then make sense or its environment.

The goals for this project was to create a pipeline that finds lane lines on the road.

[//]: # (Image References)

### 1. The Approach

1. The original image is first converted to grayscale.

[image1]: ./screenshots/gray.png "Grayscale image"  
![alt text][image1]

2. The grayed out image is then soomthed out using the opencv library's gaussianBlur function.

[image2]: ./screenshots/gray_smooth.png "Smoothed out grayscale image"
![alt text][image2]

This helps remove any noise from the image. It's an important pre-processing step for canny edge detection.

3. Then the edges in the image are detected by passing the smoothed out gray image onto the opencv's canny function. 

[image3]: ./screenshots/canny.png "Canny Edge Detection"
![alt text][image3]

4. After the edges have been detected, only that portion of the image needs to be considered for further processing that has road lane lines in view.

[image4]: ./screenshots/polygon.png "Polygon shape to take the portion from the image having lane lines"
![alt text][image4] 

5. Now that the image only has the canny edges for the lane lines portion and the rest of it blacked out, lines are drawn from those detected edges.

[image5]: ./screenshots/filtered-canny.png "Applying the polygon shape over the canny edge image"
![alt text][image5]

[image6]: ./screenshots/hough.png "Hough lines drawn for the lane lines"
![alt text][image6]

Drawing lines from the detected edges is one of the most important aspects for this project. For two single lines to be drawn over the edges, one for each line of the lane (left and right), the draw_line() is function is modified in the following way:

  ### DRAW-LINE ALGORITHM
  
 a. To extrapolate the lines returned from the hough lines and create two single lines, two endpoints (x_min, y_min, x_max. y_max) for the two lane lines and their corresponding  slope values (positive_slope, negative_slope) and intercepts (positive_intercept, negative_intercept) are needed. This forms the problem statement for the algorithm.
  
  b. The array of lines returned from the hough_lines() function is iterated upon and for each line, the slope is calculated and stored in spearate arrays for positive and negative slopes.
  
  c. From whether the slope is positive or negative, it can be inferred if the line belongs to the left line of the lane or the right line.
  
  d. To remove noisy lines pertaining to edges not belonging to any lane, but still within the lane area, a threshold is defined for the value of the slope acceptable for the algorithm.
  
  e. For each line, the intercept is also calculated and stored.
  
  f. The y_max for both lane lines is the point at the bottom of the image, from where the lines start.
  
  g. The slope values for both lines can be calculated by taking the averages of the corresponding positive and negative slope values. This also helps in removing some noise pertaining to the slope values.
  
  h. Similarly, the intercept for both lane lines can be calculated by taking the mean of the stored intercepts.
  
  i. The y_min can be found out by taking the comparing all the y values in all the lines and taking the minimum value.
  
  j. Now x_min and x_max can be found out by just fitting all the peviously found parameters in an equation of the line.
  
  k. The lines can now be drawn over the lane lines.


6. This image is now combined with the original image and the returned image would be the original one, with the algorithm generated lane lines drawn over it.

[image7]: ./screenshots/result.png "Final image with the generated lane lines"
![alt text][image7]


### 2. Potential shortcomings

1. The method used to detect the lane lines is not quite robust. A change of scene, or even a change in the resolution of the image could throw it off, thus rendering the entire pipeline useless.

2. As noticed in the challenge.mp4 video, the canny edge detection of the algorithm is thrown off by light. The noise increases substantially, which makes it hard for the algorithm to detect lane lines.

[image8]: ./screenshots/light.gif "Left lane line thrown off by the noise generated due to light"
![alt text][image8]

[image9]: ./screenshots/light-canny.png "Noise in the canny detected image increases upon entering the light region"
![alt text][image9]


### 3. Possible improvements

1. For the current pipeline, the lane line area is being detected using quite ad-hoc solution which might not work for all the cases. This could be improved by using some sort of regresison analysis over the coordinates of lane lines and subsequent position and shape of the area covering the entire lane.

1. Another improvement for the pipeline could be for slope detection and handling. Right now, the pipeline cant not handle much noise, especially thrown by light. Use of pattern recognition could be used to apply better thresholds over accepted values of slope for lane lines.  
