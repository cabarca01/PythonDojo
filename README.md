# PythonDojo
Small projects to practice python skills

## Environment preparation
For this tutorial the following tools must be available in your system (this guide is written for a Unix-Based system)

* Homebrew
* Pyenv
* Python 3.5 or above (this guide will describe the process to install Python 3.9.0)
* Mongo DB
* An IDE of your choice (I will use Visual Studio Code - just because!)

### Homebrew
From [Wikipedia](https://en.wikipedia.org/wiki/Homebrew_(package_manager)): Homebrew is a free and open-source software package management system that simplifies the installation of software on Apple's macOS operating system and Linux.

We will use Homebrew to install all the tools required for this tutorial. To install Homebrew on your system:

* Install the command line tools for XCode:

```bash
xcode-select --install
```
* Install Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
### Pyenv
From [Pyenv](https://github.com/pyenv/pyenv/wiki#suggested-build-environment): pyenv is a tool for simple Python version management. It allows us to install multiple versions of Python in our system without altering the one shipped with the operating system.

To install it:

* Install the dependencies required to build python in your system

```bash 
brew install openssl readline sqlite3 xz zlib bzip2
```

* export the required environment variables to be used by the build tools

```bash
export LDFLAGS="-L/usr/local/opt/bzip2/lib -L/usr/local/opt/zlib/lib" 
export CPPFLAGS="-I/usr/local/opt/bzip2/include -I/usr/local/opt/zlib/include"
```

* Install Pyenv 

```bash
brew update && brew install pyenv
```
* Add `pyenv init` to the shell:
  * On Bash:

  ```bash 
  echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
  ```

  * On Zsh:

  ```bash
  echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
  ```

* Verify your installation

```bash
pyenv --version
```

### Python
The core of this tutorial. Now that we have our Python version management tool installed we will use it to build our desired Python version and set it as the global version to use.

* Install Python 3.9.0

```bash
pyenv install 3.9.0
```

* Set Python 3.9.0 as your global version to use

```bash
pyenv global 3.9.0
```

* Start a new console session and verify your Python installation

```bash
python --version
```

### Visual Studio Code (or whatever....)
You can choose pretty much any IDE you want to use for this tutorial, it all depends on tastes. Moreover you can use a simple text editor like `vim` or [atom](https://atom.io/).  My taste is Visual Studio code and this is how to install it:

* install cask for Homebrew

```bash
brew install cask
```

* Cask install Visual Studio Code

```bash
brew install --cask visual-studio-code
```
