#!/bin/bash

# setup global git config
git config --global user.email "jimthompson5802@gmail.com"
git config --global user.name "Jim Thompson"

# setup credential helper for 2 hour time limit
git config credential.helper 'cache --timeout=7200'


# setup bashrc
cat dot_bashrc >> ~/.bashrc
chmod 755 ~/.bashrc
