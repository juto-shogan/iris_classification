# 🌸 Iris Flower Species Classifier

## Project Overview

This project presents a basic yet effective machine learning model designed to classify Iris flower species based on their distinct botanical measurements. Utilizing a classic dataset, this classifier serves as an excellent introduction to supervised learning techniques and data science workflows.

The primary objective is to accurately predict the species of an Iris flower (Setosa, Versicolor, or Virginica) given its sepal length, sepal width, petal length, and petal width.

## Features

* **Accurate Classification:** Predicts Iris species with a trained machine learning model.
* **Data Exploration:** Includes basic data visualization and analysis of the Iris dataset.
* **Simple Setup:** Easy to install and run, perfect for beginners in machine learning.
* **Leverages Popular Libraries:** Built using widely-used Python data science libraries.

## Technologies Used

This project is built using the following Python libraries:

* **`numpy`**: For numerical operations and array manipulation.
* **`pandas`**: For data manipulation and analysis.
* **`matplotlib`**: For creating static, interactive, and animated visualizations.
* **`seaborn`**: For statistical data visualization based on Matplotlib.
* **`scikit-learn` (sklearn)**: For machine learning algorithms, model training, and evaluation.

## Installation

To get this project up and running on your local machine, follow the instructions below.

### Prerequisites

Ensure you have Python 3.x installed on your system.

### Via pip (Recommended for all environments)

The most straightforward way to install all necessary dependencies is using `pip`. It is highly recommended to use a virtual environment to avoid conflicts with your system's Python packages.

1.  **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    ```
2.  **Activate the virtual environment:**
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
3.  **Install the required libraries:**
    ```bash
    pip install numpy pandas matplotlib seaborn scikit-learn
    ```

### Alternative Installation for Global Linux Environment (Less Recommended)

While `pip` within a virtual environment is preferred, you can install some packages globally on Linux using `apt` if you understand the implications for your system. **Note:** `scikit-learn` is generally best installed via `pip`.

```bash
sudo apt update
sudo apt install python3-numpy
sudo apt install python3-pandas
sudo apt install python3-matplotlib
# For scikit-learn, it's strongly recommended to use pip:
# pip install scikit-learn
