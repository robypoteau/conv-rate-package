

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

[1]: https://docs.python-guide.org/writing/structure/
[2]: https://towardsdatascience.com/getting-started-with-python-environments-using-conda-32e9f2779307
[3]: https://tdhopper.com/blog/my-python-environment-workflow-with-conda/
[4]: https://github.com/github/gitignore/blob/master/Python.gitignore
[5]: https://docs.travis-ci.com/user/tutorial/
