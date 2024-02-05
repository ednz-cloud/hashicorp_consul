hashicorp_consul
=========
> This repository is only a mirror. Development and testing is done on a private gitea server.

This role install and configure consul on **debian-based** distributions.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/hashicorp_consul.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

This variable allows you to choose to automatically update consul if a newer version is available.
This variable is only relevant if using the `latest` version with the `host` deploy mode. In a `docker` deployment, the version is always kept up-to-date with the docker tag you chose (always the latest version of `latest` or `1.X` if you put this tag).
Updating consul is usually pretty safe if done on a regular basis, but for better control over the upgrade process, see `hashi_consul_version`.

```yaml
hashi_consul_start_service: true
```
This variable defines if the consul service should be started once it has been configured. This is usefull in case you're using this role to build golden images, in which case you might want to only enable the service, to have it start on the next boot (when the image is launched)

```yaml
hashi_consul_version: latest # by default, set to latest
```
This variable specifies the version of consul to install when `hashi_consul_install` is set to `true`. The version to specify is:
 - If `hashi_consul_deploy_method: host`, the version of the package on the hashicorp repository (`1.14.1-1` for example). This can be found by running `apt-cache madison consul` on a machine with the repository installed.
 - If `hashi_consul_deploy_method: docker`, the tag of the container on the [hashicorp registry](https://hub.docker.com/r/hashicorp/consul)

If the version is set to `latest`, the role will update the package/docker image on every run if a newer version is available. This will cause a restart cycle of your node/cluster, to update every agent to the latest version. Updating consul is usually pretty safe if done on a regular basis, but for better control over the upgrade process, please set the variable to a static release version.

```yaml
hashi_consul_deploy_method: host # by default, set to host
```
This variable defines the method of deployment of consul. The `host` method installs the binary directly on the host, and runs consul as a systemd service. The `docker` method install consul as a docker container, and maps volumes to it to persist configuration and data across restarts.

```yaml
hashi_consul_env_variables: # by default, set to {}
  ENV_VAR: value
```
This value is a list of key/value that will populate the `consul.env`(for host deployment method) or `/etc/default/consul`(for docker deploy method) file.

```yaml
hashi_consul_data_dir: "/opt/consul/data" # by default, set to /opt/consul
```
This value defines the path where consul data will be stored on the node. Defaults to `/opt/consul`.

```yaml
hashi_consul_extra_files: false # by default, set to false
```
This variable defines whether or not there is extra configuration files to copy to the target. If there are, these extra files are expected to be jinja2 templates located all in the same directory, and will be copied to the specified directory on the target machine.

```yaml
hashi_consul_extra_files_src: /tmp/extra_files # by default, set to /tmp/extra_files
```
This variable defines the source directory (without the trailing /) for the extra files to be copied in case there are some.

```yaml
hashi_consul_extra_files_dst: /etc/consul.d/extra_files # by default, set to /etc/consul.d/extra_files
```
This variable defines the destination directory (without the trailing /) for the extra files to be copied.

```yaml
hashi_consul_extra_container_volumes: [] # by default, set to []
```
This variable lets you defines more volumes to mount inside the container when using the `docker` deployment method. This is a list of string in the form: `"/path/on/host:/path/on/container"`. These volumes will not be created/checked before being mounted, so they need to exist prior to running this role.

```yaml
hashi_consul_envoy_install: false # by default, set to false
```
This variable allows you to install the envoy binary on the consul node, in case you need to deploy connect proxies. This feature is usefull when deploying consul agents that will handle services in the service mesh. It is NOT required on server nodes (since they most likely wont have services running in service mesh).
**IMPORTANT:** If `hashi_consul_deploy_method: docker`, and you need to install envoy, you need to make sure your `hashi_consul_version` is set to one of the `-ubi` tags. Consul docker images are built on alpine, and envoy is not compiled for alpine. The `-ubi` tags build off of the universal base image and envoy will work on it.

```yaml
hashi_consul_envoy_version: latest # by default, set to latest
```
This variable defines which version of envoy to install in case `hashi_consul_envoy_install` is set to true. **IMPORTANT:** The `latest` version set by default is not guaranteed to work, please refer to the [documentation](https://developer.hashicorp.com/consul/docs/connect/proxies/envoy#supported-versions) for informations about the support matrix for consul and envoy.

```yaml
hashi_consul_configuration: {} # by default, set to a simple configuration
```
This variable sets all of the configuration parameters for consul. For more information on all of them, please check the [documentation](https://developer.hashicorp.com/consul/docs/agent/config/config-files). This variable is parsed and converted to json format to create the config file, so each key and value should be set according to the documentation. This method of passing configuration allows for compatibility with every configuration parameters that consul has to offer. The defaults are simply here to deploy a simple, single-node consul server without much configuration, and should NOT be used in production. You will want to edit this to deploy production-ready clusters.

Dependencies
------------

`ednz_cloud.manage_repositories` to configure the hashicorp apt repository.
`ednz_cloud.docker_systemd_service` if installing consul in a container.

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
