The goal is to create a python package one step at a time. I will do it around a simple function I use for determining the convergence rate of a numerical algorithm. In addition I will try to follow the Git workflow as described in [[0]].

### Step 1
---
Create a simple program structure [[1]].

    conv-rate-package
    |----/convrate
    |       calc.py
    |----/tests
    |       test_calc.py
    └----README.md

I included empty files in each folder so they would show up in the initial commit. I chose the name test_calc.py for the test file because I plan to use pytest and I'm fairly sure that's the naming convention for test in that framework.

### Step 2
I used these two article [[2]], [[3]] for guidance. After downloading and installing everything I ran:

    conda create -n conv-rate-env python=3.7

Conda should automatically put you inside the newly created environment if it
does not you can start the virtual environment by running:

    conda activate conv-rate-env

and from inside we will create environment.yml by running

    conda env export > environment.yml

which will create a file from which you can recreate the current virtual
environment.

To leave the virtual environment type:

    conda deactivate

and use

    conda activate conv-rate-env

to reactivate it. The idea is that no matter what machine to which you clone
this repo you'll be able to run this package in the same environment. Though
I'm sure there's a catch somewhere.

You can get a comprehensive premade .gitignore file for python projects from
Github [[4]].

### Step 3
---
Here we are going to create the function and it's tests. For our funciton we
will need several packages. First make sure you activate the virtual
environment. Next from within the the environment run

    conda install numpy

and this will install the necessary packages. This packages will only be
install into the current virtual env. We will also add an empty __init__.py to
convrate folder.

    conv-rate-package
    |----/convrate
    |       __init__.py
    |       calc.py
    |----/tests
    |       test_calc.py
    |----environment.yml
    └----README.md

In order to run the test we add a setup.py file

    conv-rate-package
    |----/convrate
    |       __init__.py
    |       calc.py
    |----/tests
    |       test_calc.py
    |----README.md  
    |----environment.yml
    └----setup.py

Also install pytest, i.e. run `conda install pytest`. Once you've written the
function, the test and setup up the setup.py file, execute the command

    python setup.py pytest

to run the test.

## Step 3.a
We also added a requirements.txt because of issues I had with conda and
TravisCI [[2a]].

    conv-rate-package
    |----/convrate
    |       __init__.py
    |       calc.py
    |----/tests
    |       test_calc.py
    |----environment.yml
    |----README.md
    |----requirements.txt
    └----setup.py

To create this file I ran the command `pip freeze > requirements.txt` from
inside the virtual env.

## Step 3.b
Created a release branch and added some version info to setup.py and a license
file.

    conv-rate-package
    |----/convrate
    |       __init__.py
    |       calc.py
    |----/tests
    |       test_calc.py
    |----environment.yml
    |----LICENSE  
    |----README.md
    |----requirements.txt
    └----setup.py

### Step 4
    ---
    Add continuous integration using TravisCI [[5]].

        conv-rate-package
        |----/convrate
        |       calc.py
        |----/tests
        |       test_calc.py
        |----environment.yml
        └----README.md
        └----.travis.yml

    Add the `.travis.yml` file.


[0]: https://nvie.com/posts/a-successful-git-branching-model/
[1]: https://docs.python-guide.org/writing/structure/
[2]: https://towardsdatascience.com/getting-started-with-python-environments-using-conda-32e9f2779307
[2a]: https://stackoverflow.com/questions/50777849/from-conda-create-requirements-txt-for-pip3
[3]: https://tdhopper.com/blog/my-python-environment-workflow-with-conda/
[4]: https://github.com/github/gitignore/blob/master/Python.gitignore
[5]: https://docs.travis-ci.com/user/tutorial/
