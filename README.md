# cookiecutter-go
* This is a "cookiecutter" repository designed to be used as a framework to create repository structure.

## How to use a "cookiecutter" repository

1. First install the python library called [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/)

```text
pip install cookiecutter
```

2. Create a **TOTALLY** empty repository in a GIT based system.  In my example I am creating a repo called
   throw-me-away.

3. Use the cookiecutter repository to create your structure.

* To use latest

### HTTPS

```text
cookiecutter https://github.com/btr1975/cookiecutter-go
```

### SSH

```text
cookiecutter git@github.com:btr1975/cookiecutter-go
```

* To use a specific release

### HTTPS

```text
cookiecutter https://github.com/btr1975/cookiecutter-go -c 1.0.0
```

### SSH

```text
cookiecutter git@github.com:btr1975/cookiecutter-go -c 1.0.0
```

4. Now you will be asked a series of questions. This is an example
   **THE QUESTIONS MAY NOT BE THE EXACT FOR THIS COOKIECUTTER**, also if you have downloaded it before
   you will be asked if you want to download it again, always say yes to get the latest version.

```text
full_name [Your Full Name]: Ben T
email [Your E-Mail Address]: somename@example.com
git_username [Your GitHub Username]: btr1975
git_repo_name [The Repository Name]: throw-me-away
git_url [The GIT URL]: https://github.com/btr1975/throw-me-away
app_description [A short description]: This is great
app_version [0.1.0]: 
```

5. Now initialize it and push it up to the GIT based system.

```text
git init -b main
git add --all
git commit -m "First"
git remote add origin https://github.com/btr1975/throw-me-away.git
git push -u origin main
```
