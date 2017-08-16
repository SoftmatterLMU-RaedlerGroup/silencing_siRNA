## siRNA knockdown
This project contains Python code for analyzing the siRNA knockdown data by Rafał.

### Installation
This installation guide assumes a functioning Python3 setup with `pip` and `virtualenv` installed. To set up the project on your computer, follow these steps:

1. Clone/download the project.
1. Create a new virtual environment inside the project base folder (denoted as `<TARGET>`):

    ```
virtualenv <TARGET>
    ```
1. Enter the `<TARGET>` directory, if not done yet:

    ```bash
cd <TARGET>
    ```
1. Activate the virtual environment:

    ```bash
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

```bash
source bin/activate
```
Then, you can start the notebook server:

```bash
jupyter notebook
```
Open the URL displayed on your console in your web browser to access the notebooks.

When you have finished working on the notebooks, you can deactivate the virtual environment:

```bash
deactivate
```