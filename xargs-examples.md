
# xargs


xargs using placeholder "%" and starting a sub-shell
````
ls -A | xargs -n 1 -I % sh -c 'mv % ../..'
````


xargs using placeholder "%"
````
ls -A $HOME/test  | xargs -n 1 -I % echo "%"
````
