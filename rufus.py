#!/usr/bin/env python3

import sys, os
from git import Repo
import time

description = "./rufus.py <git_dir>"

def get_current_active_branch(repo):
  return repo.active_branch.name

def check_local_changes(repo):
  return repo.is_dirty()

def get_last_commit_time(repo):
  return repo.head.commit.committed_date

def check_last_commit_in_last_24_hours(repo):
  week_ago = time.time() - 7 * 24 * 60 * 60
  last_commit_epoch = get_last_commit_time(repo)
  return last_commit_epoch > week_ago

def get_last_commit_author(repo):
  return repo.head.commit.author.name

def check_last_commit_author(repo):
  return get_last_commit_author(repo).lower() == "rufus"

def run_git_commands(git_working_dir):
  # Check if the directory exists
  if not os.path.exists(git_working_dir):
    print("Directory does not exist")
    return
  # Check if the directory is a git repository
  elif not os.path.exists(git_working_dir + "/.git"):
    print("Not a git repository")
    return
  repo = Repo(git_working_dir)
  print("active branch: " + get_current_active_branch(repo))
  print("local changes: " + str(check_local_changes(repo)))
  print("recent commit: " + str(check_last_commit_in_last_24_hours(repo)))
  # print("last commit author: " + get_last_commit_author(repo))
  print("blame Rufus: " + str(check_last_commit_author(repo)))


def main():
  arg_length = len(sys.argv)
  if arg_length == 1:
    print("No arguments provided")
    print(description)
  elif arg_length > 2:
    print("Too many arguments provided")
    print(description)
  else:
    # Get the directory from the first argument
    dir = os.path.abspath(sys.argv[1])
    run_git_commands(dir)


if __name__ == '__main__':
  main()