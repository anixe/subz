Sublime-Z
=========

Sublime-Z is a plugin for Sublime Text 3 to edit and test ARIZ files.

# Features:

- Add any section using command or menu item
- Use aclr8 either from a binary or source code
- Run aclr8 tests
- Run single query
- Check aclr8 version
- Make use of ANSI escape codes when [ANSIescape](https://github.com/aziz/SublimeANSI) plugin in installed

![demo](https://github.com/synek317/subz/raw/master/img/demo.gif "Demo")

# Installation:

The simplest way is to install this plugin using [Package Control](https://packagecontrol.io):

1. Install [Package Control](https://packagecontrol.io)
2. Add this repository to Package Control repositories:
  - open command input (`[shift] + [ctrl] + [p]`)
  - type "add repository" and press `Enter`
  - paste this repository url: `https://github.com/synek317/subz.git` and press `Enter`
3. Install Sublime-Z package:
  - open command input (`[shift] + [ctrl] + [p]`)
  - type "install package" and press `Enter`
  - type "subz" and press `Enter`

![installation guide](https://github.com/synek317/subz/raw/master/img/install.gif "Installation guide")

Alternatively you can clone this repository, rename it to `subz` and move it to your packages directory. Depending on your system it is:

- Windows: `%APPDATA%\Sublime Text 3`
- OS X: `~/Library/Application Support/Sublime Text 3`
- Linux: `~/.config/sublime-text-3`

# Setup

ARIZ file editting is definitely easier with following packages installed:

- [MarkdownTableFormatter](https://github.com/bitwiser73/MarkdownTableFormatter) for formatting sections
- [ANSIescape](https://github.com/aziz/SublimeANSI) for coloring tests output

In order to run aclr8-related commands, Sublime-Z must be able to find aclr8. Its path is stored in Sublime-Z settings in `aclr8_path` key.
You may provide there

- just the executable name if it is included in your `PATH` env variable
- absolute path to the executable (with or without `.exe` extension)
- absolute path to the root of aclr8 source

It may be good idea to first run `check aclr8 version` command and see if it works. If aclr8 is not found, Sublime-Z will ask you to enter the path. Check recipes for more details.

# Tips and tricks

- There are two versions of `[CONTRACT]` section. The `minimal` one inserts only minimum number of required properties while `full` inserts all possible properties.
- You don't have to type whole command. Typically, section name is enough to narrow down search results to single item.
- Output panel (at the bottom of the window) can be quickly closed by pressing `[Esc]`
- When some of the tests are failing, new tab will be opened. It ignores any changes and can be quickly closed by pressing `[ctrl] + w`
- You *don't* have to save the `.ion` file in order to run tests or query

# Recipes:

## Check aclr8 version:

1. Run the command
  a. with mouse: choose `Tools -> Sublime-Z -> Aclr8 -> Check aclr8 version`
  b. with keyboard: press `[shift] + [ctrl] + p` to open command input and then type `Check aclr8 version`
2. If aclr8 is not found, you have to provide it in the input box that pops up at the bottom of the window and confirm with `[Enter]`
3. When everything is configured correctly, the command and aclr8 version should be shown in the output panel at the bottom of the window

![check aclr8 version](https://github.com/synek317/subz/raw/master/img/check_version.gif "Check aclr8 version")

## Create ARIZ:

1. Create new file (`File -> New File` or `[ctrl] + n`)
2. Insert sections using either menu or command
  a. with mouse: choose `Tools -> Sublime-Z -> Insert Section` and then choose selected section
  b. with keyboard: press `[shift] + [ctrl] + p` to open command input and then type `Insert [TEST] section`. Replace `TEST` with any section name.

![create ariz](https://github.com/synek317/subz/raw/master/img/create_ariz.gif "Create ARIZ")

## Run single query

1. Create ARIZ as described previously
2. Open query input
  a. with mouse: choose `Tools -> Sublime-Z -> Aclr8 -> Run aclr8 query`
  b. with keyboard: press `[shift] + [ctrl] + p` to open command input and then type `Run aclr8 query`
3. Fill the query in the input box (by default it shows up at the bottom of the window) and press `[Enter]` when ready
4. The results should appear in the output panel.

![run query](https://github.com/synek317/subz/raw/master/img/run_query.gif "Run query")

## Run tests

1. Create ARIZ as described previously
2. Open query input
  a. with mouse: choose `Tools -> Sublime-Z -> Aclr8 -> Run aclr8 tests`
  b. with keyboard: press `[shift] + [ctrl] + p` to open command input and then type `Run aclr8 tests`
3. If all tests pass, short message will appear in the output panel
4. Otherwise, the output will appear in the `Sublime-Z Results` tab

![run tests](https://github.com/synek317/subz/raw/master/img/run tests.gif "Run tests")