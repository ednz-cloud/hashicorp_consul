hashicorp_consul
=========
![Ansible Badge](https://img.shields.io/badge/Ansible-E00?logo=ansible&logoColor=fff&style=for-the-badge)
![HashiCorp Badge](https://img.shields.io/badge/HashiCorp-000?logo=hashicorp&logoColor=fff&style=for-the-badge)
![Consul Badge](https://img.shields.io/badge/Consul-F24C53?logo=consul&logoColor=fff&style=for-the-badge)

> This repository is only a mirror. Development and testing is done on a private gitea server.

This role install and configure consul on **debian-based** distributions.

Requirements
------------

The `unzip` package needs to be installed on the target host(s) to be able to decompress the consul release bundle.

Role Variables
--------------
Available variables are listed below, along with default values.

```yaml
hashicorp_consul_start_service: true
```
This variable defines if the consul service should be started once it has been configured. This is usefull in case you're using this role to build golden images, in which case you might want to only enable the service, to have it start on the next boot (when the image is launched)

```yaml
hashicorp_consul_version: latest # by default, set to latest
```
This variable specifies the version of consul to install. The version to specify is either `latest` (NOT RECOMMENDED), or any tag present on the [GitHub Repository](https://github.com/hashicorp/consul/releases) (without the leading `v`). Loose tags are **not supported** (1.7, 1, etc..).

```yaml
hashicorp_consul_env_variables: # by default, set to {}
  ENV_VAR: value
```
This value is a list of key/value that will populate the `consul.env` file.

```yaml
hashicorp_consul_data_dir: "/opt/consul" # by default, set to /opt/consul
```
This value defines the path where consul data will be stored on the node. Defaults to `/opt/consul`.

```yaml
hashicorp_consul_extra_files: false # by default, set to false
```
This variable defines whether or not there is extra configuration files to copy to the target.

```yaml
hashicorp_consul_extra_files_list: [] # by default, set to []
  # - src: /tmp/directory
  #   dest: /etc/consul.d/directory
  # - src: /tmp/file.conf
  #   dest: /etc/consul.d/file.conf
  # - src: /etc/consul.d/file.j2
  #   dest: /etc/consul.d/file
```
This variable lets you copy extra configuration files and directories over to the target host(s). It is a list of dicts. Each dict needs a `src` and a `dest` attribute. The source is expected to be located on the deployment machine. The source can be either a file or a directory. The destination must match the type of the source (file to file, dir to dir). If the source is a directory, every file inside of it will be recursively copied and templated over to the target directory.

For example, if you have the following source files to copy:

```bash
├── directory
│   ├── recursive
│   │   ├── test4.j2
│   │   └── test.j2024.conf
│   └── test3
├── file
├── file2.j2
```
You can set:

```yaml
hashicorp_consul_extra_files_list: [] # by default, set to []
  - src: /tmp/directory
    dest: /etc/consul.d/directory
  - src: /tmp/file
    dest: /etc/consul.d/file.conf
  - src: /etc/consul.d/file2.j2
    dest: /etc/consul.d/file2.conf
```
all the files shown above will be copied over, and the directory structure inside `directory` will be preserved.

```yaml
hashicorp_consul_envoy_install: false # by default, set to false
```
This variable allows you to install the envoy binary on the consul node, in case you need to deploy connect proxies. This feature is usefull when deploying consul agents that will handle services in the service mesh. It is NOT required on server nodes (since they most likely wont have services running in service mesh).

```yaml
hashicorp_consul_envoy_version: latest # by default, set to latest
```
This variable defines which version of envoy to install in case `hashicorp_consul_envoy_install` is set to true. **IMPORTANT:** The `latest` version set by default is not guaranteed to work, please refer to the [documentation](https://developer.hashicorp.com/consul/docs/connect/proxies/envoy#supported-versions) for informations about the support matrix for consul and envoy.

```yaml
hashicorp_consul_configuration: {} # by default, set to a simple configuration
```
This variable sets all of the configuration parameters for consul. For more information on all of them, please check the [documentation](https://developer.hashicorp.com/consul/docs/agent/config/config-files). This variable is parsed and converted to json format to create the config file, so each key and value should be set according to the documentation. This method of passing configuration allows for compatibility with every configuration parameters that consul has to offer. The defaults are simply here to deploy a simple, single-node consul server without much configuration, and should NOT be used in production. You will want to edit this to deploy production-ready clusters.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednz_cloud.hashicorp_consul
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
