# Course materials for the 2025/2026 edition of Basics of Machine Learning (Podstawy Uczenia Maszynowego) 
## Taught at the Faculty of Chemistry, Jagiellonian University in Kraków

```
                                                                     ,----,.
,-.----.                           ____                            ,'   ,' |
\    /  \                        ,'  , `.              ,----,    ,'   .'   |
|   :    \          ,--,      ,-+-,.' _ |            .'   .' \ ,----.'    .'
|   |  .\ :       ,'_ /|   ,-+-. ;   , ||    ,---,.,----,'    ||    |   .'  
.   :  |: |  .--. |  | :  ,--.'|'   |  ;|  ,'  .' ||    :  .  ;:    :  |--, 
|   |   \ :,'_ /| :  . | |   |  ,', |  ':,---.'   ,;    |.'  / :    |  ;.' \
|   : .   /|  ' | |  . . |   | /  | |  |||   |    |`----'/  ;  |    |      |
;   | |`-' |  | ' |  | | '   | :  | :  |,:   :  .'   /  ;  /   `----'.'\   ;
|   | ;    :  | | :  ' ; ;   . |  ; |--' :   |.'    ;  /  /-,    __  \  .  |
:   ' |    |  ; ' |  | ' |   : |  | ,    `---'     /  /  /.`|  /   /\/  /  :
:   : :    :  | : ;  ; | |   : '  |/             ./__;      : / ,,/  ',-   .
|   | :    '  :  `--'   \;   | |`-'              |   :    .'  \ ''\       ; 
`---'.|    :  ,      .-./|   ;/                  ;   | .'      \   \    .'  
  `---`     `--`----'    '---'                   `---'          `--`-,-'    
```

## Table of contents
* Lab 1 - Python basics. Classes and objects.
* Lab 2 - Linear algebra in NumPy. Linear regression.
* Lab 3 - Binary classification. Building a classifier model with `scikit-learn`.
* Lab 4 - Data preprocessing. Building a regression model. Coding a simple app in Streamlit.
* Lab 5 - Implementing a simple perceptron. Introduction to neural networks with PyTorch.
* ... (COMING SOON)

## Course info
During the semester you will have to complete a series of six laboratory sessions. 
The course material is divided into notebooks, each dedicated to a specific topic.

A notebook is divided into exercises, each of which is worth a certain number of points. The maximum number of points you
can earn at each laboratory session is 10, making it a total of 60 points from the whole course.
At the end of the semester, the points from all notebooks will be summed up and converted into the final grade according 
to the following scale:

* 30 - 36 points: 3.0
* 37 - 42 points: 3.5
* 43 - 48 points: 4.0
* 49 - 54 points: 4.5
* 55 - 60 points: 5.0

The exercises preceded by a star (*) are not graded, but they introduce some fun concepts or more advanced topics. 
Solving them can sometimes earn you additional points. The information about the extra points will be included 
in the exercise description or announced during the laboratory session.

You need to get at least 30 points to pass the course. During each laboratory session, you can earn additional points
by solving extracurricular problems, actively participating in the class, and contributing to the course in other ways.

The course is taught in Polish, but the course materials are in English so that you can get accustomed to the ML-related
terminology and use it in your future work.

<br>

## Setup

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) following the instructions for your operating
   system.
2. Clone the repository: `git clone https://github.com/hubertrybka/pum-25.git`
3. Navigate to the directory: `cd pum-25`
4. Download datasets from our dropbox (COMING SOON) and extract them to `data` directory.
5. Install environment from the YAML file: `conda env create -n pum-25 -f environment.yml`
6. Activate the environment: `conda activate pum-25`

Author: Hubert Rybka
