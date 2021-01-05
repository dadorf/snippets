
# xargs


See also this: https://gist.github.com/porras/5b109bce228fb29784d5a0ab2c93c00c




xargs using placeholder "%" and starting a sub-shell
````
ls -A | xargs -n 1 -I % sh -c 'mv % ../..'
````


xargs using placeholder "%"
````
ls -A $HOME/test  | xargs -n 1 -I % echo "%"
````
