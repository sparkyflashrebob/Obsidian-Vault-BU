
## Using PowerShell to find and delete empty folders

Follow these steps to find empty folders and delete them using PowerShell:

1. Open **the Start menu**, type **Powershell,** right-click, and select **Run as administrator**.
2. Type **cd /d DriveName:\To\FolderPath** in the PowerShell window and press **Enter**.
3. To list empty directories, run this command: **Get-ChildItem -Directory -Recurse | Where-Object { $_.GetFiles().Count -eq 0 -and $_.GetDirectories().Count -eq 0 } | Select-Object FullName**
4. After reviewing the list, if you decide to delete the empty directories, run this command: **Get-ChildItem -Directory -Recurse | Where { $_.GetFiles().Count -eq 0 -and $_.GetDirectories().Count -eq 0 } | Remove-Item -Force**
    
    ![Windows power shell window with the codes to print and then remove empty folders](https://static1.anpoimages.com/wordpress/wp-content/uploads/2024/05/powershell-del.jpg)
    

This code scans the folders and subdirectories in **DriveName:\To\FolderPath** and finds empty directories (no files, no subfolders), and deletes them.

## Using Windows Explorer to find and delete empty folders

Here's a step-by-step guide for finding empty folders using Windows Explorer:

1. Press **Win + E** to open File Explorer.
2. Navigate to the drive or folder where you wish to search for empty directories.
3. Access the **View** tab and toggle **Hidden items** from the context menu to make all hidden files visible for the search.
    
    ![A screenshot of Windows file explorer showing the steps to show hidden files](https://static1.anpoimages.com/wordpress/wp-content/uploads/2024/05/explorer-show-hidden.jpg)
    
4. Activate the search ribbon by typing a word to activate the search, select **Search options**, and toggle **All subfolders** for a complete search.
    
    ![A screenshot of Windows file explorer showing the steps to toggle all subfolders in search options](https://static1.anpoimages.com/wordpress/wp-content/uploads/2024/05/all-subfolder-search.jpg)
    
5. Click the **Size** option, select **Empty (0 KB)**, and choose **Folder** under **Type**.
    
    ![Screenshot of Windows File Explorer displaying the search results for 'size:empty' with the size filter options open, showing 'Empty (0 KB)' selected.](https://static1.anpoimages.com/wordpress/wp-content/uploads/2024/05/win-search-sizez.jpg)
    
6. Alternatively, enter **type:folder size:empty** in the search box to locate empty directories.
    
    ![Screenshot of Windows File Explorer displaying the search results for 'type:folder' with the type filter options open, showing 'folder' selected.](https://static1.anpoimages.com/wordpress/wp-content/uploads/2024/05/windows-kind-search.jpg)
    
7. Delete the folders you want from the search results.
    
    ![Result of a search query in windows explorer's search function](https://static1.anpoimages.com/wordpress/wp-content/uploads/2024/05/search-results.jpg)
    

While this method is usually effective, it has limitations. For example, it can't remove folders containing empty or useless Windows files like **desktop.in** , which Windows uses to store custom settings for folder views. Additionally, it struggles with UNICODE characters. If your folders have non-Latin letters in their names, this command doesn't process them.


