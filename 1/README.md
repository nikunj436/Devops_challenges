requirement: 
        - "Linux Bash or"
        - "windows if wsl installed"

To run: 
    - in terminal ". file_name.sh"

--> There is sh file:- 1_oneliner_for_1_file.sh  - which handle only 1 file 
                       2_oneliner_all_file.sh    - which handle all files in folder
                                                 - used for loop in script


-->
's|([[:alnum:]]+)\s+\1|\1|g'    #delimiter as "|"

- alnum is extend regex, it's searching the pattern with space(s+) and same pattern match(\1)

- Delete files in output folder if there any before running though it's overwrite everytime runs for same input file.