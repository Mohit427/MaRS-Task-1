# MaRS-Task-1

This repository contains the solutions for the **MaRS (Mobile Robotics Systems)** club recruitment, Task 1. 
---

## Light Dose Tasks

### Task 1: Ubuntu Commands
I started off by using the Ubuntu documentation to revise the basic commands of Linux and since I am on a Mac I directly used the terminal to put those to use. I didn't know how to do some of the tasks in the question. So I used Gemini and Google to learn the commands for the task and also its extensions just to satisfy my curiosity. 

I then created a GitHub repo and cloned it onto my laptop, created a folder structure and then a single bash script to automate directory creation and many such tasks, where I wrote all the commands in VS Code, but it didn't produce any output because I forgot to save the .sh file. So I saved it, gave some sample inputs and everything worked like a charm. I also had a bit of a learning curve with Git and GitHub but eventually came over it with the help of the given resources.

### Task 2: Bash Scripting
I learnt the basics of bash scripting from the cheat sheet and YouTube and the battery task was fairly straightforward from the sources. I was not worrying about the syntax but I learnt it in the hard way that even the spaces matter in bash scripting which led to an error. After solving that, I had slight trouble understanding the extensions of the ping command and how it worked by pinging google.com. But once I understood it, I was able to complete the Light Dose Task-2 as well.

---

## Medium Dose Tasks

### Task 1: Coordinate Transformation
Coordinate Transformation as a concept was not new to me, but its real life application was fascinating. I learnt from sources on the internet about how the translation of coordinates and rotation matrix was fascinating. The formulae used are attached in the screenshots. Once I learnt the math behind, the implementation using numpy arrays and python library math was very simple and straight forward.

### Task 2: Morse Code
This task was extremely straight forward especially with Python Dictionaries. But this changed my perspective about Morse code for I felt that it was just for sending encrypted information in high alert environments (Effect of movies). This was a new application perspective but other than that, no real hinderances for the solution.

### Task 3: Caesar Decode
This task involved creating a script to decrypt messages that were shifted using a pattern. I implemented the decryption logic in Python to handle character-by-character shifts based on the provided Caesar cipher rules. This was very straight forward, so I tried to do it with C++ for an extra challenge. It was fairly straight forward there as well.xs

### Task 4: Muchiko and Sanchiko Filters
I had a great time understanding how the Muchiko and Sanchiko filters play an important role in reducing the effect of noise in the data. Muchiko filter is used for datasets with small jitters (Gaussian noise) while Sanchiko filter is used to remove large spikes in the datasets. 

To prove the effectiveness of these filters, I used **variance** as a mathematical metric to show how the filtered data became more stable. I concluded that a **hybrid filter**, which removes the spikes first and then smooths the remaining white noise, gives the best result for reliable sensor readings.

### Task 5: Manipulator Wear Cost
For this task, I implemented a solution to minimize the wear cost of a three-segment telescopic arm. I used a **Dynamic Programming** approach to find the global minimum cost instead of just looking at the cheapest next move. This ensured that the rover satisfied the **stability constraint** where the absolute difference between the Inner and Outer segments remains less than or equal to 4 at every step ($|Inner - Outer| \le 4$). Plus The code actually found a more efficient path for the given inputs than the suggested example by tinkering the coordinates required to achieve target as 8

---

## Hard Dose Tasks

### Task 1: Arena Navigation
In this task, I navigated a rover through an $11 \times 11$ grid using a **Breadth-First Search (BFS)** algorithm. The program reads obstacle data from a file, where each line provides four distances representing boundaries. I processed these distances to define rectangular obstacle regions in the matrix. 

Since the rover moves like a King in chess but is restricted from diagonal movement, BFS was the ideal algorithm to guarantee the **shortest possible path** from the start point `[0,0]` to the destination `[10,10]`. The final output prints the entire arena matrix and the specific path the rover took to avoid the obstacles.

---

# Hard Dose: Task 2 - Arrow Distance Estimation

## 1. Problem Statement
The objective was to calculate the real-world distance of a detected arrow from the rover's camera[cite: 196].The system assumes a pinhole camera model using a webcam with a 1280x720 resolution and a 55° diagonal Field of View (FOV) 

## 2. Technical Approach
My implementation follows a three-step process to convert pixel data into physical distance:

### A. Focal Length Derivation
Since only the Diagonal FOV was provided, I first calculated the focal length ($f$) in pixels.
1. **Diagonal Resolution:** Calculated using the Pythagorean theorem: $\sqrt{1280^2 + 720^2} \approx 1468.6$ pixels.
2. **Focal Length Formula:** $$f = \frac{\text{Diagonal Resolution}}{2 \cdot \tan\left(\frac{\text{Diagonal FOV}}{2}\right)}$$

### B. Image Processing Pipeline
* **Preprocessing:** Converted the frame to grayscale and applied Gaussian Blur to filter out microgravity-induced sensor noise [cite: 210-211].
* **Edge Detection:** Used the Canny algorithm to identify sharp intensity changes .
* **Contour Approximation:** Utilized `cv2.approxPolyDP` with a 7-side vertex check to isolate the arrow shape .

### C. Distance Calculation
Using the Pinhole Camera Model[cite: 204], the distance is computed as:
$$Distance = \frac{\text{Real Width (17cm)} \times \text{Focal Length (pixels)}}{\text{Perceived Width (pixels)}}$$

## 3. Challenges & Debugging
* **OS Path Compatibility:** The initial script failed to load the image (`imread` error) because of Windows-style backslashes (`\`) being used on a macOS environment. I corrected this by implementing a relative path string[cite: 209].
* **Thresholding:** Fine-tuning the Canny thresholds (50, 150) was necessary to ensure the arrow's edges were closed loops for contour detection[cite: 213].



---
### Task 3: Behviour Tree
In this task, I learnt about the **Behaviour Tree** and its uses. It proved to be quite similar to a flowchart except for the two Types of nodes that it has and How both of them behave when put to test in a real life scenario. The two types of nodes being sequence node and fallback node. 

I also learnt the advantages of implementation of a Behaviour tree over tons and tons of if else statments. This was a very intuitive task at the surface level but still had lots of stuff to offer as learning.
---

## Folder Structure
* `medium_dose/`: Filter logic, manipulator optimization, and sensor logs.
* `hard_dose/`: BFS navigation script and obstacle coordinate files.
* `screenshots/`: Visual proof of successful test runs and mathematical logic.