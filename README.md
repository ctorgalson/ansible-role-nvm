# Role Name

This role installs [nvm](https://github.com/creationix/nvm) on Ubuntu/macOS (and other \*nix environments).

Specifically, the role performs the following tasks:

1. Clones nvm to a specified location for one or more users, and
2. _Optionally_ writes nvm-specific code to one or more users' (configurable) `.*rc` files (this is optional in case some other role or script is responsible for the creation/management of users' `.*rc` files).

## Role Variables

| Variable name | Default value | Description |
|---------------|---------------|-------------|
| `nvm_repository`     | `https://github.com/creationix/nvm.git` | URL to be used by git clone. |
| `nvm_home_dir`       | `/home` | Path to home directory; set to `/Users` for macOS. |
| `nvm_user_data`      | `[]`    | An array of users to install/configure nvm for. each item must contain at least `user`; see `defaults/main.yml` and Example Playbook below for details. |
| `nvm_dir_name`       | `.nvm`  | Directory in user's home directory where nvm should be installed. |
| `nvm_git_update`     | `no`    | Whether or not to update git repository when role runs. |
| `nvm_git_version`    | `HEAD`  | Git-specific string for desired version. |
| `nvm_rc_file_block`  | `export NVM_DIR="$HOME/{{ nvm_dir_name }}" ; [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"` | Setup lines for nvm. |
| `nvm_rc_file_create` | `yes`   | Whether or not to create an `.*rc` file if not prsent. |
| `nvm_rc_file_backup` | `yes`   | Whether or not to backup the `*.rc` file the role modifies. |
| `nvm_rc_file_marker` | `# {MARK} Managed by Ansible role 'ctorgalson.nvm'` | File markers to insert before and after the lines the role adds to a `.*rc` file. |
| `nvm_rc_modify`      | `true`  | Whether or not to modify the `.*rc` file at all; set this to `false` if adding nvm-specific code by some other means. |

## Example Playbook

    - hosts: servers
      roles:
        - ctorgalson.nvm

      vars:
        - nvm_user_data:
          - user: "ctorgalson"
            rc_file: ".zshrc"

## License

MIT

## Author Information

Christopher Torgalson
