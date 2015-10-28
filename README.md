# github-scripts

Collection of scripts exploring and using the Github API for the development and management of dealii.

## Note

Github needs credentials to log in, but for obvious reasons, we do not want to put our passwords into this repository. Therefore, after cloning, a file `login.py` must be created in the root directory. An example for the contents of this file is
```
git = Github("user", "password")
```
Any ssh based alternative is highly appreciated.
