# Tables
 - working tree (id, commit message, branch name)
 - commitfolder(workingtree_id, folder_id, files_id)
 - folders (id, folder_id, folder_name, sub_folder/file_id)
 - mediam b/w folder and files
 - files (id, file_id, file_name, content)

 ## imporved idea 
 - working tree (commit_id unique primary key, message, Branch_name, time Text)
 - commitfolders(commit_id, folder_id, file_id)
 - folder (folder_id, folder_name, subfolder_id, file_id)
 - files (id, file_name, content)

## imporved idea 
 - working tree (commit_id unique primary key, message, Branch_name, time Text)
 - commitfolders(commit_id, folder_file_id)
 - folder_file(id, path, subfolder_file_id, content)

# Functions

## git add .
- sab file/folder add karne hai + content database me store karna hai
- .gitignore maybe

## git commit
- update working tree
- just take the folder_id and 

## git log
- git graph

# GitHub
- lets say pi me ek flask server host to wo localhost access kar sakte kya
- 


```
# TODO

- [x] Table Layout
- [x] Add function algorithm
- [] Add function k liye helper function
- [] implementation Add function
- [] Commit function algorithm
- [] Implementation
- [] Commit function algorithm
- [] Git log implementaion
- [] isFileChange function
- [] gitstatus function
- [] flask app
- [] pi setup
- [] git push
- [] git pull

```