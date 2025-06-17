# F1-Race-Line-Analyzer


El Plan:

A computer vision tool that analyzes an F1 driver’s racing line using onboard footage and a circuit layout. It reconstructs the car's path, maps it onto a real track layout, and evaluates its efficiency compared to an ideal racing line.

- Extract frames from onboard F1 video
- Track car movement using optical flow or feature matching
- Map trajectory to a circuit layout using homography
- Load and overlay ideal racing line
- Analyze driver efficiency: apex deviation, curvature, smoothness
- Visualize real vs. ideal lines on the track map
- Generate heatmaps for inefficient zones
