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
