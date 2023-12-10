# Git Basics

Create empty Git repo in specified directory. Run with no arguments to initialize the current directory as a git repository.

```bash
git init
```

Stage all changes in for the next commit. Replace with a to change a specific file.

```bash
git add
```

Clone repo located at onto local machine. Original repo can be located on the local filesystem or on a remote machine via HTTP or SSH .

```bash
git clone <repo link>
```

Define author name to be used for all commits in current repo. Devs commonly use --global flag to set config options for current user.

```bash
git config user.name <name>
```

Commit the staged snapshot, but instead of launching a text editor, use as the commit message.

```bash
git commit -m "<message>"
```

List which files are staged, unstaged, and untracked.

```bash
git status
```

Display the entire commit history using the default format. For customization see additional options.

```bash
git log
```

Show unstaged changes between your index and working directory.

```bash
git diff
```

# Undo Changes

Create new commit that undoes all of the changes made in , then apply it to the current branch.

```bash
git revert <commit>
```

Remove from the staging area, but leave the working directory unchanged. This unstages a file without overwriting any changes.

```bash
git reset <file>
```

Shows which files would be removed from working directory. Use the -f flag in place of the -n flag to execute the clean.

```bash
git clean -n
```

# Rewriting Git History

Replace the last commit with the staged changes and last commit combined. Use with nothing staged to edit the last commit’s message.

```bash
git commit --amend
```

Rebase the current branch onto . can be a commit ID, branch name, a tag, or a relative reference to HEAD.

```bash
git rebase <commit>
```

Show a log of changes to the local repository’s HEAD . Add --relative-date flag to show date info or --all to show all refs.

```bash
git reflog
```

# Git Branches

List all of the branches in your repo. Add a argument to create a new branch with the name .

```bash
git branch
```

Create and check out a new branch named . Drop the -b flag to checkout an existing branch.

```bash
git checkout -b <branch>
```

Merge into the current branch.

```bash
git merge <branch>
```

# Remote Repositories

Create a new connection to a remote repo. After adding a remote, you can use as a shortcut for in other commands.

```bash
git remote add <remote> <url>
```

Fetches a specific , from the repo. Leave off to fetch all remote refs.

```bash
git fetch <remote> <branch>
```

Fetch the specified remote’s copy of current branch and immediately merge it into the local copy.

```bash
git pull <remote>
```

Push the branch to , along with necessary commits and objects. Creates named branch in the remote repo if it doesn’t exist.

```bash
git push <remote> <branch>
```

Git Config Define the author name to be used for all commits by the current user.

```bash
git config --global user.name "<name>"
```

Define the author email to be used for all commits by the current user.

```bash
git config --global user.email "<email>"
```

# Git Diff

Show difference between working directory and last commit.

```bash
git diff HEAD
```

Show difference between staged changes and last commit

```bash
git diff --staged
```


# Git Rebase

Interactively rebase current branch onto . Launches editor to enter commands for how each commit will be transferred to the new base.

```bash
git rebase -i <base>
```

# Git Pull

Fetch the remote’s copy of current branch and rebases it into the local copy. Uses git rebase instead of merge to integrate the branches.

```bash
git pull --rebase <remote>
```

# Git Push

Forces the git push even if it results in a non-fast-forward merge. Do not use the --force flag unless you’re absolutely sure you know what you’re doing.

```bash
git push --force <remote>
```

Push all of your local branches to the specified remote.

```bash
git push --all <remote>
```

Tags aren’t automatically pushed when you push a branch or use the --all flag. The --tags flag sends all of your local tags to the remote repo.

```bash
git push --tags <remote>
```

# Git Log

Limit number of commits by . E.g. ”git log -5” will limit to 5 commits.

```bash
git log -<number>
```

Condense each commit to a single line.

```bash
git log --online
```

Display the full diff of each commit.

```bash
git log -p
```

Include which files were altered and the relative number of lines that were added or deleted from each of them.

```bash
git log --stat
```

Search for commits by a particular author.

```bash
git log --author=<name>
```

Search for commits with a commit message that matches.

```bash
git log --grep=<string>
```

Only display commits that have the specified file.

```bash
git log -- <file>
```

--graph flag draws a text based graph of commits on left side of commit msgs. --decorate adds names of branches or tags of commits shown.

```bash
git log --graph --decorate
```



