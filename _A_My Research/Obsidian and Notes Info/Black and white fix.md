# [Blank / Black / White screen on startup / launch / open](https://forum.obsidian.md/t/blank-black-white-screen-on-startup-launch-open/75222)

[Help](https://forum.obsidian.md/c/get-help/19)

If obsidian doesn’t start properly and it shows a blank/black/white screen, It’s possible that some plugin is causing Obsidian to crash and the crash is unrecoverable.

To restore obsidian, use the following procedures on your vault. If you have multiple vaults and you don’t know which one has the problem, you need to try in all of them.

# [](https://forum.obsidian.md/t/blank-black-white-screen-on-startup-launch-open/75222#begin-1)Begin

1. Close Obsidian
2. Download and reinstall Obsidian from the website
3. Start Obsidian.

If it loads great, go to Final Steps. If it doesn’t work try Procedure A.

# [](https://forum.obsidian.md/t/blank-black-white-screen-on-startup-launch-open/75222#procedure-a-2)Procedure A

1. Close Obsidian
2. Using File Explorer/Finder, go to the folder that **contains** your vault’s folder.
3. Rename your vault folder
4. Start Obsidian

Obsidian should open and show you the vault selector, select your vault using the new name.  
If it doesn’t work try Procedure B.

# [](https://forum.obsidian.md/t/blank-black-white-screen-on-startup-launch-open/75222#procedure-b-3)Procedure B

1. Close Obsidian
2. In File Explorer/Finder go **inside** the folder corresponding to your vault.
3. Using your OS file manager, search for Markdown notes (`.md`) that are greater than 1 Megabyte
4. Move those notes out of the vault
5. Start Obsidian

If it loads great, go to Final Steps. If it doesn’t work try Procedure C.

# [](https://forum.obsidian.md/t/blank-black-white-screen-on-startup-launch-open/75222#procedure-c-4)Procedure C

1. Close Obsidian
2. In File Explorer/Finder go **inside** the folder corresponding to your vault.
3. Make sure you can see hidden files (On mac, press `cmd-shift-.`)
4. Move the `.obsidian` folder out of your vault to another location
5. Start Obsidian

At this point, Obsidian should start on your vault with default settings and no plugins. You can reconfigure your vault via the UI from scratch or you can attempt to copy your previous settings and plugins from your old `.obsidian` to your new `.obsidian` a little bit at the time and see if still works.

# [](https://forum.obsidian.md/t/blank-black-white-screen-on-startup-launch-open/75222#final-steps-5)Final Steps

Make sure your themes and plugins are up-to-date by checking for updates inside obsidian.