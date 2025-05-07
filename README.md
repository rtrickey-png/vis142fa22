# Visual Systems – Generative Image & Animation Projects  
**Author:** Ryan Rickey  
**Course:** VIS 142 – Visual Arts & Computing (Fall 2022)  
**Platform:** Raspberry Pi, Python  

This repository documents two creative coding projects developed for a visual arts class focused on generative systems and creative computation. Both works explore nature-inspired forms through procedural algorithms, visual randomness, and performance-constrained rendering.

---

## Project 1: *Fractal Tree in the Wind*  
**Title:** *Taking a Picture of a Tree, but It’s Windy and Its Leaves Are Randomly Falling*  
**Tools:** Python, Turtle Graphics, Pillow, NumPy, pypng  
**Output:** Static PNG image

### Concept  
Inspired by the book *Artist and Computer* (1976), this project revisits early computer art through the lens of resource-limited generative visuals. I began by drawing a fractal tree using recursive turtle graphics, then transformed the resulting image with randomized pixel manipulation—simulating a windy day where the tree’s leaves scatter and blur.

### Process  
- Generated a recursive fractal tree (`rickey_in1.png`)
- Applied a blur using random pixel offsets across rows
- Overlaid random "chunks"—blocks of distorted pixel data—to suggest motion and decay
- Tested performance on a Raspberry Pi, adjusting for memory and render speed

### Reflection  
This project demonstrated how creative limits—both conceptual and technical—can shape compelling digital imagery. I treated randomness as a collaborator, letting the code misbehave beautifully within bounded rules. I delighted in the fact that every time the code is run, it will produce a different result. 

---

## Project 2: *Leaves Falling in the Breeze*  
**Medium:** Frame-by-frame Python animation rendered at 60 fps  
**Resolution:** 1920×1080 (working) → 4096×2160 (final)  
**Total Frames:** 1500 (25 seconds)  
**Exhibition:** *“20 Seconds for All”* group show, Dec 6, Dirty Birds La Jolla

### Concept  
Building directly on Project 1, this animation imagines a moment of gentle motion: leaves falling from a fractal tree, caught in an unpredictable breeze. Designed to loop indefinitely, the piece functions as an ambient screen-based installation.

### Process  
- Used `pygame` to layer a static background with animated falling leaves (`leaf.png`)
- Modeled each leaf as a `Chunk` object with randomized drift, acceleration, and pause
- Rendered 1500 high-res frames as a numbered PNG sequence
- Created title and credit frames as required for inclusion in the final class film

### Reflection  
Project 2 expanded my visual vocabulary into motion and time. The unpredictable paths of the leaves mirror the role of randomness in nature and computation alike. This piece taught me to think about visuals not as static endpoints, but as unfolding systems.

---

## Repository Structure
/a1/ (Project 1 parent folder)
* Chunk.py              - class definition for a block of pixels
* a1.py                 - main assignment script
* fractal_turtle.py     - script to generate the tree with Python Turtle
* rickey_in1.png        - input tree image for processing
* rickey_out1.png       - example output #1
* rickey_out2.png       - example output #2
* rickey_out3.png       - example output #3
* rickey_ryan_a1.ipynb  - Python notebook submitted for discussion
* tree_1.png            - initial fractal tree export

/project2/ (Project 2 parent folder)
* /frames/              - numbered frames for animation
* leaf.png              - leaf image to be spawned over tree and duplicated
* skel.py               - completed starter code that runs the animation
* tree_bg.png           - initial background image for animation
