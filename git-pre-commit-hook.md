
# Git Pre-Commit Hook

Preferred: Option 2 because it will apply to all git repos
without individual configuration.

Use case:

* you want to sent a notification to a bug tracking tool
* you want to run a code formatting tool before committing
* if you have files in your repo that you want to encrypt before committing and pushing them

## Option 1

Rename `.git/hooks/pre-commit.sample` to `pre-commit`.
Then add some code as shoen below to call a script
in your project dir so that the pre-commit code can be 
versioned as-well.

````
#!/bin/bash
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

ROOT_DIR=$(git rev-parse --show-toplevel)
echo "ROOT_DIR: $ROOT_DIR"

$ROOT_DIR/pre-commit.sh

````

## Option 2

create a bash function, e.g. in ~/.bash_aliases:

````
git()
{
  if [ $# -gt 0 ] && [ "$1" == "commit" ] ; then
     shift
     if [[ -f ./pre-commit.sh ]]
     then
        ./pre-commit.sh
     elif [[ -f ~/bin/pre-commit.sh ]]
     then
        ~/bin/pre-commit.sh
     fi
     git status
     command git commit "$@"
  else
     command git "$@"
  fi
}
````

Place a _pre-commit.sh_ script in your local _~/bin_ folder.
`chmod u+x ~/bin/pre-commit.sh`

Disable pre-commit hook in git repo (e.g. by renaming .git/hooks/pre-commit).
