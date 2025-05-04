<<<<<<< HEAD
<<<<<<< HEAD
# Neuro-manifold
=======
# neuronal_activity_estimation_with_manifolds
>>>>>>> a9cc782 (Initial commit)
=======
# Neuronal Activity Estimation with Manifolds

This repository contains the code and analysis pipeline for the research presented in the paper: "AI-powered mice behavior tracking and its application for neuronal manifold analysis based on hippocampal ensembles activity in Alzheimer’s disease mice model"

The study investigates the use of manifold learning techniques to analyze neural activity in the hippocampus of mice, with a focus on identifying features associated with Alzheimer's disease (AD).

## Repository Structure

* `manifold_with_tracking.ipynb`: This Jupyter Notebook contains the primary experimental workflow, including data loading, preprocessing, manifold construction, analysis, and visualization.
* `manifold_manager.py`: Provides a class using various teaching methods (PCA, ICA, the, MAP, DS) used in the study.
* `data_manager.py`: Provides a class for preprocessing raw neural activity data. This includes temporary aggregation and formatting of the data.
* `rating_manager.py`: Provides a class for calculating the main numeric parameters of the received manifolds.

##  Usage

1.  Clone the repository:

    ```bash
    git clone https://github.com/vainmoon/neuronal_activity_estimation_with_manifolds.git
    cd neuronal_activity_estimation_with_manifolds
    ```

2.  Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Run the main experiment notebook:

    ```bash
    jupyter notebook manifold_with_tracking.ipynb
    ```
>>>>>>> e9f1677 (add readme)
