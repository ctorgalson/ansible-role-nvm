# Ansible Role NVM

[![Build Status](https://travis-ci.com/ctorgalson/ansible-role-nvm.svg?branch=master)](https://travis-ci.com/ctorgalson/ansible-role-nvm)

This role installs [nvm](https://github.com/nvm-sh/nvm) on Linux/macOS (and other \*nix environments).

Specifically, the role performs the following tasks:

1. Clones nvm to a specified location for one or more users, and
2. _Optionally_ writes nvm-specific code to one or more users' (configurable) `.*rc` files (this is optional in case some other role or script is responsible for the creation/management of users' `.*rc` files).

## Role Variables

All of the following variables can be set, but _only_ `nvm_users` is
mandatory.

| Variable name | Default value | Description |
|---------------|---------------|-------------|
| `nvm_repository`     | `https://github.com/nvm-sh/nvm.git` | URL to be used by git clone. |
| `nvm_user`           | `null` | A dict containing info about the user to install/configure nvm for. Must contain at least `name`; see `defaults/main.yml`, `molecule/default/playbook`, and Example Playbook below for details. |
| `nvm_dir_name`       | `.nvm` | Directory in user's home directory where nvm should be installed. |
| `nvm_git_update`     | `false`| Whether or not to update git repository when role runs. |
| `nvm_git_version`    | `HEAD` | Git-specific string for desired version. |
| `nvm_rc_file_create` | `true` | Whether or not to create an `.*rc` file if not present. |
| `nvm_rc_file_backup` | `true` | Whether or not to backup the `.*rc` file the role modifies. |

## Example Playbook

    - hosts: servers
      roles:
        - ctorgalson.nvm

      vars:
        nvm_user:
          name: "ctorgalson"
          rc_file: ".zshrc"

## License

GPLv3

## Author Information

Christopher Torgalson
