# Basic Usage

First, list the non-disabled plist items with

    python list.py

Second, I recommend initializing a git repo in the folder of whichever plists you are going to modify, 

    cd ~/Library/LaunchAgents
    git init
    git add .
    git commit -m "Initial import of plist files"

Third, go through and disable whichever plist files by copying and pasting the complete path form the list output:

    python disable.py /Users/username/Library/LaunchAgents/com.valvesoftware.steamclean.plist

This command will only modify the plist file that is listed. 

Finally, I commit the changes to plist in git. This will help detect when new programs modify the launchd configuration.