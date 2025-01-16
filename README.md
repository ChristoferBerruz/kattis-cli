# Kattis CLI

Kattis online judge command line tool written in Python. Requires Python 3.

# Download the repo

Run `git clone https://github.com/Kattis/kattis-cli` to clone the repository.

# Using the client from the cloned repo
To run the client directly, `cd` into the `kattis-cli` directory and run `python submit.py`.

See the section for your operating system below for instructions on how to install the submission client as a command runnable from anywhere on your file system.

If the `python` command is not installed, try using `python3` instead.

# Building a wheel and installing the client in a virtualenv

You need to have `wheel` as a dependency. You can install it using
```code
pip install wheel
```

In order to build the package, you can simply run
```code
python setup.py bdist_wheel
```

This will generate a wheel object. Once you have a wheel object, you can create a virtualenv using your method of choice and simply install
the wheel **inside the virtualenv** by doing.

```code
pip install <wheel_path>
```

Inside your virtual environment, you can use the kattis-cli package
using the name

```code
kattis-cli
```

Double check the installation was successful by doing
```code
kattis-cli --help
```

## Windows

To run the client as a command, you can create a file `kattis.bat` in `kattis-cli`:
```bat
@echo off
python %~dp0\submit.py %*
```

To install it, you can add the `kattis-cli` directory to your `%PATH%` variable.
To do that, run `setx PATH "%PATH%;C:\Users\user\Desktop\kattis-cli"` where `C:\Users\user\Desktop\kattis-cli` is the path to your cloned repository.
You can now run the command `kattis` from anywhere!

## MacOS/Linux

To run the client as a command, you can create an executable file `kattis` in `kattis-cli`:
```sh
#!/bin/sh
python "${BASH_SOURCE%/*}/submit.py" "$@"
```

To install it, you can add the `kattis-cli` directory to your `$PATH` variable.
To do that, open the file `~/.bash_profile` in a text editor and add the line `export PATH="$PATH:/Users/user/Desktop/kattis-cli"`, where `/Users/user/Desktop/kattis-cli` is the path to the `kattis-cli` directory, at the end of the file.
You can now run the command `kattis` from anywhere!
**Note:** You might need admin privileges to change the file.

# Configuration file

Before running the submission client, you need to [download a configuration file](https://open.kattis.com/download/kattisrc). This file includes a secret personal token that allows you to log in. It should be placed in your home directory, or in the same directory as `submit.py`, and be called `.kattisrc`.

# Running the client

The easiest way to use the client is if you have named your source code to *problemid*.suffix, where suffix is something suitable for the language (e.g., `.java` for Java, `.c` for C, `.cc` or `.cpp` for C++, `.py` for Python, `.cs` for C#, `.go` for Go, and so on...).

Let's assume you're solving the problem [Hello World!](https://open.kattis.com/problems/hello) (with problem id `hello`) and that your java solution is in the file `Hello.java`. Then you can simply run `kattis Hello.java`, and the client will make the correct guesses. You will always be prompted before a submission is sent.

**Note:** If you get an error message like this: `ModuleNotFoundError: No module named 'requests'` when you run `kattis` it's because the module 'requests' isn't installed. To install the module, check out [this](https://stackoverflow.com/a/17309309/4132739) StackOverflow answer.

# More advanced options

The submit client can handle multiple files in a submission. For such submissions, the filename and suffix of the first file listed on the command line is the basis of the guesses. It is ok to list a file multiple times, e.g., `kattis Hello.java *.java` will work as intended.

In case the client guesses wrong, you can correct it by specifying a command line option. Running `kattis -h` will list all options. The options are:

* `-p <problem_id>`: overrides problem guess
* `-m <mainclass>`: overrides mainclass guess
* `-l <language>`: overrides language guess
* `-f`: forces submission (i.e., no prompt)
