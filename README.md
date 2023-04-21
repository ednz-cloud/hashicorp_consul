Hashicorp Consul
=========
> This repository is only a mirror. Development and testing is done on a private gitlab server.

This role install and configure consul on **debian-based** distributions.

Requirements
------------

**IMPORTANT**: This role uses a built-in [filter_plugin](https://docs.ansible.com/ansible/latest/plugins/filter.html), that helps converting YAML variables to HCL format. While the defaults on this role should provide you with enough configuration to get a production-grade consul up and running, you can also add more in case you need some specifics. Each additional value should be placed in the corresponding map (see variables details below). The key should match EXACTLY that of the configuration file (see consul [documentation](https://developer.hashicorp.com/consul/docs/agent/config/config-files)), and the value will be converted automatically to match hcl syntax.

For now, only the root variables(not inside of a block) and some specific blocks are supported (see variables below), but I will be adding more.

Example: to add the root [limits](https://developer.hashicorp.com/consul/docs/agent/config/config-files#limits) block (which is not present by default), you would need to add the following under `hashi_consul_general`:

```yaml
hashi_consul_general:
  limits:
    http_max_conns_per_client: 400
```
This will generate a new hcl block like:
```
limits = {
  http_max_conns_per_client = 400
}
```

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/hashicorp_consul.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
hashi_consul_install: true # by default, set to true
```
This variable defines if the consul package is to be installed or not before configuring. If you install consul using another task, you can set this to `false`.

```yaml
hashi_consul_start_service: true
```
This variable defines if the consul service should be started once it has been configured. This is usefull in case you're using this role to build golden images, in which case you might want to only enable the service, to have it start on the next boot (when the image is launched)

```yaml
hashi_consul_version: latest # by default, set to latest
```
This variable specifies the version of consul to install when `hashi_consul_install` is set to `true`. The version to specify is the version of the package on the hashicorp repository (`1.14.1-1` for example). This can be found by running `apt-cache madison consul` on a machine with the repository installed.

```yaml
hashi_consul_deploy_method: host # by default, set to host
```
This variable defines the method of deployment of consul. The `host` method installs the binary directly on the host, and runs consul as a systemd service. The `docker` method install consul as a docker container.
> Currently, only the `host` method is available, the `docker` method will be added later.

```yaml
hashi_consul_env_variables: # by default, set to {}
  env_var: value
```
This value is a list of key/value that will populate the `consul.env` file. You do not have to capitalize the KEYS, as it will be done automatically.

```yaml
hashi_consul_general:
```
This variable sets a bunch of configuration parameters for consul. For more information on all of them, please check the [documentation](https://developer.hashicorp.com/consul/docs/agent/config/config-files). I try to name them the same as in the configuration file, so that it is easier to search for it. Most of the defaults in the role are the default values of consul, however, some might differ.

```yaml
hashi_consul_tls:
```
This variable sets up all config to use TLS certificates with consul.

```yaml
hashi_consul_ports:
```
This variable sets up all of the ports used for consul communications. They default to the consul default values.

```yaml
hashi_consul_acl:
```
This variable sets a bunch of settings regarding the ACLs in consul. YOU NEED TO EDIT IT if you decide to enable ACLs on the cluster (you might want to look into `lookup plugins` to fetch tokens from a secret manager, like [vault](https://docs.ansible.com/ansible/latest/collections/community/hashi_vault/hashi_vault_lookup.html) or [bitwarden](https://docs.ansible.com/ansible/latest/collections/community/general/bitwarden_lookup.html)).

Dependencies
------------

This role has a task that installs its own dependencies located in `task/prerequisites.yml`, so that you don't need to manage them. This role requires both `ednxzu.manage_repositories` and `ednxzu.manage_apt_packages` to install consul.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.hashicorp_consul
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.