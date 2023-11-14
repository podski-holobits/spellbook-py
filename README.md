# spellbook-py

Personal set of python tools used for varying purposes, like arranging my own Twitter bookmarks, developing AI tools for myself etc. It is a very dirty repo. This README.md is just list of helpful notes that can help anyone to run the tools, including me in a few weeks/months or years if I won't forget about it.

## Installation instruction

### Initial setup

1. Start from the repo

    ```bash
    git clone git@github.com:podski-holobits/spellbook-py.git
    ```

2. Make sure that you have Python newer than 3.9.0 and newest version of pip. If not - best to upgrade both before proceeding further

3. From main project path folder path create a new virutal environment ( name should start with venv_, so it will work well with the .gitignore):

    ```bash
    On windows:
    ---------------
    python -m venv venv_xxxx

    On Linux:
    ---------------
    python3 -m venv venv_xxxx
    ```

4. Activate your virtual environment. To do that on Windows, run (still beeing in project e.g. spellbook-py folder):

    ```bash
    On windows:
    ---------------
    .\venv_xxxx\Scripts\activate

    On Linux or MacOS run:
    ---------------
    source venv_xxxx/bin/activate
    ```

    If the command does not work, you need to fix execution permission on the file  .\venv_xxxx\Scripts\activate or source venv_xxxx/bin/activate. The method is specific for OS - should be easy to google.
    You should see now in the terminal indication, that you are indeed now in the virtual environment (depending on your terminal app). Your virtual environment is almost empty now - you can run _pip list --local_ on windows or _pip3 list --local_ on  linux/macos to see that only a few packages will be now donwloaded.

5. Install spellbook-py package in development mode using following command.

    ```bash
    On windows:
    ---------------
    pip install --editable .

    On Linux or MacOS run:
    ---------------
    pip3 install --editable .

6. This collection of scripts uses dotenv module to set up all the api keys etc. Create a .env file in your project folder, and set up all the relevant keys and env variables there (use .env-default file as a template). 

7. Good reading resources about python tools, packages, etc. Most of the tools here are based on these wonderful pieces of code/tips from fantastic developers:

   - Wonderful [Norah Sakal](https://norahsakal.com/blog/automatically-organize-twitter-bookmarks-in-notion) and her set of interesting tutorials (2023)
   - [https://packaging.python.org/en/latest/](https://packaging.python.org/en/latest/)
   - [I wanna to try it out once or twice](https://www.ethicalads.io/)

8. Pylance fix to work with new path  of project

   - for PyCharm, mark folder src/qrem as a Source Root  (right-click the folder and choose Mark Directory as | Sources Root).
   - for vscode - add to workspace setting extra path for pylance "src/spellbook-py" - open ctrl-shift-p write Workspace Preferences, open them and search for ExtraPaths and under Python > Analysis Extra Path add src/qrem. You can also add it in .vscode/settings.json folder if you already have it, like that:
  
    ```json
    "python.analysis.extraPaths": [
        "src\\qrem"
    ]
    ```

9. To update qrem package at any time in development mode from local folders using following command.

    ```bash
    On windows:
    ---------------
    pip install --editable .

    On Linux or MacOS run:
    ---------------
    pip3 install --editable .

10. To use Jupyter notebook inside virutal environment, you need to set its python interpreter to the one from your virtual environment. For example, if you named your virtual environment venv_test, after opening any jupyter notebook you should see somewhere an option to choose kernel, and on the list of kernels - one that is marked with venv_test name.

    - if you use vscode, you can find instruction where to find it : [here](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
    - if you use pycharm, you can [find location where to set kernel in notebook toolbar](https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html#cell-toolbar)