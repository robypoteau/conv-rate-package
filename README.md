The goal is to create a python package one step at a time. I will do it around a simple function I use for determining the convergence rate of a numerical algorithm.

### Commit 1
---
Create a simple program structure [[1]].

    conv-rate-package
    |----/convrate
    |       calc.py
    |----/tests
    |       test_calc.py
    └----README.md

I included empty files in each folder so they would show up in the initial commit. I chose the name test_calc.py for the test file because I plan to use pytest and I'm fairly sure that's the naming convention for test in that framework.

### Commit 2
---
Next we will add a gitignore file and we will create a virtual environment for our project.

    conv-rate-package
    |----/convrate
    |       calc.py
    |----/tests
    |       test_calc.py
    |----environment.yml
    └----README.md

I used these two article [[2]], [[3]] for guidance. After downloading and installing everything I ran:

    conda create --conv-rate-env python=3.7

Conda should automatically put you inside the newly created environment. From inside you will run:

    conda env export > environment.yml

To leave the virtual environment type:

    conda deactivate

and to reactivate it

    conda activate conv-rate-env

This way no matter what machine you pull this two you'll be able to run this package in the same environment. Though I'm sure there's a catch somewhere.

You can get a comprehensive premade .gitignore file from Github [4].

[1]: https://docs.python-guide.org/writing/structure/
[2]: https://towardsdatascience.com/getting-started-with-python-environments-using-conda-32e9f2779307
[3]: https://tdhopper.com/blog/my-python-environment-workflow-with-conda/
[4]: https://github.com/github/gitignore/blob/master/Python.gitignore
