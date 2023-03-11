Manage repositories
=========
> This repository is only a mirror. Development and testing is done on a private gitlab server.

This role enables you to manage repositories on **debian-based** distributions. It can be used on its own , or be called by other roles the configure repositories on demand.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/manage_repositories.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
manage_repositories_enable_default_repo: true # by default, set to true
```
This variable enable or disable the configuration of the main distribution repositories (useful when calling this role to configure repo for another role like installing docker).

Dependencies
------------

This role requires both `ednxzu.manage_repositories` and `ednxzu.manage_apt_packages` to install consul. If you already installed consul, you can set `hashi_consul_install` to `false`, and that'll remove the dependencies.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:
```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - manage_repositories
```

```yaml
# calling the role inside a playbook and injecting variables (in another role for example)
- hosts: servers
  tasks:
    - name: "Configure hashicorp repository"
      ansible.builtin.include_role: 
        name: manage_repositories
      vars:
        manage_repositories_enable_default_repo: false
        manage_repositories_enable_custom_repo: true
        manage_repositories_custom_repo:
          - uri: "https://apt.releases.hashicorp.com"
            gpg_key: "https://apt.releases.hashicorp.com/gpg"
            comments: "hashicorp repository"
            type: "deb"
            suites: "{{ ansible_distribution_release }}"
            components: "main"
            filename: "hashicorp"
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.