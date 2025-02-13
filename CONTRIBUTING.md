# Contributing

Before contributing to the project, please read the general Cyberseals code of conduct [here](https://gitlab.com/hull-seals/welcome-to-the-hull-seals-devops-board/-/blob/master/CONTRIBUTING.md#our-standards)

## Helping with the project

1. Contact Rixxan or Rik079 on HSBC
2. Fork the project
3. Create a new branch from `master`
4. Write code!
5. Make sure your feature branch is up to date with the upstream master branch
6. Submit pull request

## Merge requests

- ALL merge requests MUST be peer reviewed by at least 1 Cyberseal team member
- Requests can only be submitted if the branch is in a FULLY working state

Make sure that the branch you're working on is up to date with master.

In the requests description, please mention the issue as `resolves #issueID` to automatically link the MR and the issue.

## Naming standards

### Commit messages
Prefix all commit messages with the issue number if applicable. If addressing multiple tickets, create a commit for each change and do not combine them. 

`[HALPY-7] Create awesome function`

If the commit isn't directly linkes to a ticket, please use the following tags:

`[Minor] For a really minor addition`
`[Fix] For a minor bugfix`
`[Cleanup] after you've used the code-broom`
`[Doc] for a minor documentation change`
`[Typo] Fix typos that don't affect functioning of the bot`

### Branches
Make a feature branch off of master using git checkout -b feature/IssueID. For other types of pull requests please use one of the following:

- doc - Documentation, or Documentation Update
- feature - New Features/Functionality
- fix - Bug fixes
- testing - New or updated tests.

An example of a correctly branch names is `feature/halpy-6`

Implementations of minor functions _may_ be included in the branch of a more major function, if creating a seperate branch for it would be too cumbersome. Keep the guidelines for commit messages in mind.

### Merge requests names

If working from a registered issue, Include the issue name enclosed in brackets in the title of your Pull Request, ie `[HALPY-123] Update to CONTRIBUTING.md`

Otherwise, use the type of request:

`[Doc] Make documentation even more awesome`

`[Fix] Solve issue that made bot eat rotten fish`

## Other

### Docstrings

#### Non-commands

This project uses [Google Style Python Docstrings](https://gist.github.com/redlotus/3bc387c2591e3e908c9b63b97b11d24e) for non-commands
(functions that do not directly interact with a command handler)

#### Commands

For commands, use this simple, custom style:

```python
"""
What this command does

Usage: !primary_name <subcommand> [required argument] (optional argument)
Aliases: secondary_name
"""
```

#### Files

Files that contain any meaningful code (use your own judgement here)
have to start with a docstring of the following format:

```python
"""
HalpyBOT v[VERSION]

file_name.py - One-sentence description of what this file does.

Copyright (c) 2021 The Hull Seals,
All rights reserved.

Licensed under the GNU General Public License
See license.md
"""
```

if the file makes use of licensed material, you must comply with all copyright
and license notice requirements listed in the license of said material. 