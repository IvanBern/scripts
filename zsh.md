# How to Customize the zsh Prompt in the macOS Terminal

### zsh

The Z shell (also known as zsh) is a Unix shell that is built on top of bash (the default shell for macOS) with additional features. It's recommended to use zsh over bash. It's also highly recommended to install a framework with zsh as it makes dealing with configuration, plugins and themes a lot nicer.

Install zsh using Homebrew:

``` 
brew install zsh
```

The configuration file for zsh is called .zshrc and lives in your home folder (~/.zshrc).

### Create a Z Shell Profile to Store All Settings
Creating a new .zshrc profile is recommended to store all the settings like the zsh prompt looks and behaves.

Here's how to create the zsh profile (dotfile):

1. Open Terminal app.

2. Type the following command and hit the Return key.

```touch ~/.zshrc```

That'll create a `.zshrc` profile in your user account's home directory. You can see it under /User/<username>/ path in the Finder if you have enabled viewing hidden system files.

After that, the zsh profile will be available for the login and interactive shells every time you launch Terminal. However, it won't be active in the SSH sessions.

All the changes you want to make to the zsh prompt can be included in this profile.


### Customize the zsh Prompt in Terminal

Typically, the default zsh prompt carries information like the username, machine name, and location starting in the user's home directory. These details are stored in the zsh shell's system file at the /etc/zshrc location.

```
PS1="%n@%m %1~ %#"
```

In this string of variables:

 - %n is the username of your account.
 - %m is the MacBook's model name.
 - %1~ symbol means the current working directory path where the ~ strips the $HOME directory location.
 - %# means that the prompt will show # if the shell is running with root (administrator) privileges, or else offers % if it doesn't.
 - 
To make any change to the default zsh prompt, you'll have to add relevant values for the prompt to appear differently than the default.

Here's how to go about that. Open Terminal, type the following command, and hit enter.

``` 
nano ~/.zshrc
```

It'll be blank if you're accessing it for the first time. You can add a new line with the text PROMPT='...' and include relevant values in the ellipses.

For a simple modification to the zsh prompt, you can type these values in the .zshrc profile.

```
PROMPT='%F{cyan}%~%f:$ '
```

### Enable colorized output fo `ls` command
Add the line to `~/.zshrc`

```
export CLICOLOR=1
```

### File search functions

```
function f() { find . -iname "*$1*" ${@:2} }
```
