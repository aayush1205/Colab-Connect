# Colab-Connect

[![Issues](https://img.shields.io/github/issues/aayush1205/Colab-Connect?style=plastic)]() [![PRs](https://img.shields.io/github/issues-pr/aayush1205/Colab-Connect)]() [![License](https://img.shields.io/github/license/aayush1205/Colab-Connect)]()

Links your **local machine** to Google Colab for hassle-free GPU enabled development.  

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Supported Distributions:
1. [Ubuntu](https://ubuntu.com/)

### Prerequisites
1. [Conda](https://docs.conda.io/en/latest/miniconda.html)
2. [Visual Studio Code](https://code.visualstudio.com/)

### Installing
The repository has the installer script. This is what you need to do to get muCLIar running on your system:

1. Clone the repository:

```
git clone https://github.com/aayush1205/Colab-Connect

```

2. Get into the muCLIar directory:

```
cd /path/to/repository

```

3. Run the installer: 

```
./env.sh
```

4. Run the tool: 

```
ctr -c

```

**NOTE**: Once the tunnel is openend up, it will prompt you for a password. The password is "colab". 


### Uninstalling

Use the uninstaller script. It will handle all the deletions and script removal.

```
./uninstall.sh
```

<br>


## Contributing
### How to Contribute?
* Make sure that your changes do not conflict with the core files (changing file directories will require a change in all called paths)
* Follow the original code structure
* Refactoring contributions are welcome, explicitly mention "[Refactor]" in your pull request
* Give a few days to review PRs, code reviews are welcome 

### Steps to sync fork with master (Open Source Contributors):
If you fork is behind from the master project you can do these to get the latest version in the master branch of your fork.
First go to your(cloned) project folders.
Open the terminal in this directory then enter the following commands in the terminal:
 - Configuring a remote for fork

       $ git remote -v 
       //Lists the current configured remote repository for your fork//
       $ git remote add upstream https://github.com/aayush1205/Colab-Connect
       //Specifies a new remote upstream repository that will be synced with the fork//
       $ git remote -v https://github.com/aayush1205/Colab-Connect
       //Should show the newly made remote *upstream* along with your previous remote//

 - Syncing the fork

       $ git fetch upstream
       //Fetch the branches and their respective commits from the upstream repository//
       $ git checkout master
       //Switches to local master branch//
       $ git merge upstream/master
       //Merges the upstearm remote (Main repo) into your local fork//
       
<br>

## Authors:

- [Aradhya Tripathi](https://github.com/Aradhya-Tripathi)



- [Astha Vijayvargiya](https://github.com/astha77-bot)


- [Aayush Upadhyay](https://github.com/aayush1205)






