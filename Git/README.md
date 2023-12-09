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



