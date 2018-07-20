## siRNA knockdown
[![DOI](https://zenodo.org/badge/141714508.svg)](https://zenodo.org/badge/latestdoi/141714508)

This project contains Python code for analyzing the siRNA knockdown data in the `data` directory.

### Installation
This installation guide assumes a functioning Python3.6 setup with `pip` installed. To set up the project on your computer, follow these steps:

1. Clone/download the project.
1. Create a new virtual environment inside the project base folder (denoted as `<TARGET>`):
    ```
    python -m venv <TARGET>
    ```
1. Enter the `<TARGET>` directory, if not done yet:
    ```
    cd <TARGET>
    ```
1. Activate the virtual environment:
    ```
    source bin/activate
    ```
1. Install the required Python modules:
    ```
    pip install -r requirements.txt
    ```
1. Activate `ipywidgets`:
    ```
    jupyter nbextension enable --py widgetsnbextension --sys-prefix
    ```

### Usage
To view (and change) the jupyter notebooks in this project, first activate the virtual environment:
```
source bin/activate
```
Then, you can start the notebook server:
```
jupyter notebook
```
Open the URL displayed on your console in your web browser to access the notebooks.

When you have finished working on the notebooks, you can deactivate the virtual environment:
```
deactivate
```

### Content
There are three notebooks of interest:

* `siRNA_knockdown_calibrated.ipynb` is the notebook for fitting the data with fixed protein maturation and degradation rates.
* `siRNA_knockdown_calibrated_nonfixed.ipynb` is the notebook for fitting the data without fixing protein maturation and degradation rates.
* `siRNA_knockdown_fixed.ipynb` is the notebook for obtaining the protein maturation and degradation rates from separate measurements.
