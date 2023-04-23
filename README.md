Hashicorp Consul
=========
> This repository is only a mirror. Development and testing is done on a private gitlab server.

This role install and configure consul on **debian-based** distributions.

Requirements
------------

None.

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
hashi_consul_data_dir: "/opt/consul" # by default, set to /opt/consul
```
This value defines the path where consul data will be stored on the node. Defaults to `/opt/consul`.

```yaml
hashi_consul_configuration: {} # by default, set to a simple configuration
```
This variable sets all of the configuration parameters for consul. For more information on all of them, please check the [documentation](https://developer.hashicorp.com/consul/docs/agent/config/config-files). This variable is parsed and converted to json format to create the config file, so each key and value should be set according to the documentation. This method of passing configuration allows for compatibility with every configuration parameters that consul has to offer. The defaults are simply here to deploy a simple, single-node consul server without much configuration, and should NOT be used in production. You will want to edit this to deploy production-ready clusters.

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