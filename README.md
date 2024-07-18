# hashicorp_consul

![Ansible Badge](https://img.shields.io/badge/Ansible-E00?logo=ansible&logoColor=fff&style=for-the-badge)
![HashiCorp Badge](https://img.shields.io/badge/HashiCorp-000?logo=hashicorp&logoColor=fff&style=for-the-badge)
![Consul Badge](https://img.shields.io/badge/Consul-F24C53?logo=consul&logoColor=fff&style=for-the-badge)

> This repository is only a mirror. Development and testing is done on a private gitea server.
<!-- DOCSIBLE START -->

# 📃 Role overview

## hashicorp_consul



Description: Install and configure hashicorp consul for debian-based distros.


| Field         | Value      |
|---------------|------------|
| Readme update | 17/07/2024 |

### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var                                                                     | Type | Value                                                                                                                                                                                                                                                                                    | Required | Title |
|-------------------------------------------------------------------------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|
| [hashicorp_consul_version](defaults/main.yml#L4)                        | str  | `latest`                                                                                                                                                                                                                                                                                 | n/a      | n/a   |
| [hashicorp_consul_start_service](defaults/main.yml#L5)                  | bool | `True`                                                                                                                                                                                                                                                                                   | n/a      | n/a   |
| [hashicorp_consul_config_dir](defaults/main.yml#L6)                     | str  | `/etc/consul.d`                                                                                                                                                                                                                                                                          | n/a      | n/a   |
| [hashicorp_consul_data_dir](defaults/main.yml#L7)                       | str  | `/opt/consul`                                                                                                                                                                                                                                                                            | n/a      | n/a   |
| [hashicorp_consul_certs_dir](defaults/main.yml#L8)                      | str  | `{{ hashicorp_consul_config_dir }}/tls`                                                                                                                                                                                                                                                  | n/a      | n/a   |
| [hashicorp_consul_logs_dir](defaults/main.yml#L9)                       | str  | `/var/log/consul`                                                                                                                                                                                                                                                                        | n/a      | n/a   |
| [hashicorp_consul_envoy_install](defaults/main.yml#L11)                 | bool | `False`                                                                                                                                                                                                                                                                                  | n/a      | n/a   |
| [hashicorp_consul_envoy_version](defaults/main.yml#L12)                 | str  | `latest`                                                                                                                                                                                                                                                                                 | n/a      | n/a   |
| [hashicorp_consul_extra_files](defaults/main.yml#L14)                   | bool | `False`                                                                                                                                                                                                                                                                                  | n/a      | n/a   |
| [hashicorp_consul_extra_files_list](defaults/main.yml#L15)              | list | `[]`                                                                                                                                                                                                                                                                                     | n/a      | n/a   |
| [hashicorp_consul_env_variables](defaults/main.yml#L17)                 | dict | `{}`                                                                                                                                                                                                                                                                                     | n/a      | n/a   |
| [hashicorp_consul_extra_configuration](defaults/main.yml#L28)           | dict | `{}`                                                                                                                                                                                                                                                                                     | n/a      | n/a   |
| [hashicorp_consul_domain](defaults/main.yml#L34)                        | str  | `consul`                                                                                                                                                                                                                                                                                 | n/a      | n/a   |
| [hashicorp_consul_datacenter](defaults/main.yml#L35)                    | str  | `dc1`                                                                                                                                                                                                                                                                                    | n/a      | n/a   |
| [hashicorp_consul_primary_datacenter](defaults/main.yml#L36)            | str  | `{{ hashicorp_consul_datacenter }}`                                                                                                                                                                                                                                                      | n/a      | n/a   |
| [hashicorp_consul_gossip_encryption_key](defaults/main.yml#L37)         | str  | `{{ 'mysupersecretgossipencryptionkey'\|b64encode }}`                                                                                                                                                                                                                                    | n/a      | n/a   |
| [hashicorp_consul_enable_script_checks](defaults/main.yml#L38)          | bool | `False`                                                                                                                                                                                                                                                                                  | n/a      | n/a   |
| [hashicorp_consul_leave_on_terminate](defaults/main.yml#L44)            | bool | `True`                                                                                                                                                                                                                                                                                   | n/a      | n/a   |
| [hashicorp_consul_rejoin_after_leave](defaults/main.yml#L45)            | bool | `True`                                                                                                                                                                                                                                                                                   | n/a      | n/a   |
| [hashicorp_consul_join_configuration](defaults/main.yml#L51)            | dict | `{'retry_join': ['{{ ansible_default_ipv4.address }}'], 'retry_interval': '30s', 'retry_max': 0}`                                                                                                                                                                                        | n/a      | n/a   |
| [hashicorp_consul_enable_server](defaults/main.yml#L61)                 | bool | `True`                                                                                                                                                                                                                                                                                   | n/a      | n/a   |
| [hashicorp_consul_bootstrap_expect](defaults/main.yml#L62)              | int  | `1`                                                                                                                                                                                                                                                                                      | n/a      | n/a   |
| [hashicorp_consul_ui_configuration](defaults/main.yml#L68)              | dict | `{'enabled': '{{ hashicorp_consul_enable_server }}'}`                                                                                                                                                                                                                                    | n/a      | n/a   |
| [hashicorp_consul_bind_addr](defaults/main.yml#L75)                     | str  | `0.0.0.0`                                                                                                                                                                                                                                                                                | n/a      | n/a   |
| [hashicorp_consul_advertise_addr](defaults/main.yml#L76)                | str  | `{{ ansible_default_ipv4.address }}`                                                                                                                                                                                                                                                     | n/a      | n/a   |
| [hashicorp_consul_address_configuration](defaults/main.yml#L77)         | dict | `{'client_addr': '{{ hashicorp_consul_bind_addr }}', 'bind_addr': '{{ hashicorp_consul_advertise_addr }}', 'advertise_addr': '{{ hashicorp_consul_advertise_addr }}'}`                                                                                                                   | n/a      | n/a   |
| [hashicorp_consul_acl_configuration](defaults/main.yml#L86)             | dict | `{'enabled': False, 'default_policy': 'deny', 'enable_token_persistence': True}`                                                                                                                                                                                                         | n/a      | n/a   |
| [hashicorp_consul_mesh_configuration](defaults/main.yml#L97)            | dict | `{'enabled': False}`                                                                                                                                                                                                                                                                     | n/a      | n/a   |
| [hashicorp_consul_dns_configuration](defaults/main.yml#L104)            | dict | `{'allow_stale': True, 'enable_truncate': True, 'only_passing': True}`                                                                                                                                                                                                                   | n/a      | n/a   |
| [hashicorp_consul_enable_tls](defaults/main.yml#L113)                   | bool | `False`                                                                                                                                                                                                                                                                                  | n/a      | n/a   |
| [hashicorp_consul_tls_configuration](defaults/main.yml#L114)            | dict | `{'defaults': {'ca_file': '/etc/ssl/certs/ca-certificates.crt', 'cert_file': '{{ hashicorp_consul_certs_dir }}/cert.pem', 'key_file': '{{ hashicorp_consul_certs_dir }}/key.pem', 'verify_incoming': False, 'verify_outgoing': True}, 'internal_rpc': {'verify_server_hostname': True}}` | n/a      | n/a   |
| [hashicorp_consul_certificates_extra_files_dir](defaults/main.yml#L124) | list | `[]`                                                                                                                                                                                                                                                                                     | n/a      | n/a   |
| [hashicorp_consul_enable_prometheus_metrics](defaults/main.yml#L133)    | bool | `False`                                                                                                                                                                                                                                                                                  | n/a      | n/a   |
| [hashicorp_consul_prometheus_retention_time](defaults/main.yml#L134)    | str  | `60s`                                                                                                                                                                                                                                                                                    | n/a      | n/a   |
| [hashicorp_consul_telemetry_configuration](defaults/main.yml#L135)      | dict | `{}`                                                                                                                                                                                                                                                                                     | n/a      | n/a   |
| [hashicorp_consul_log_level](defaults/main.yml#L141)                    | str  | `info`                                                                                                                                                                                                                                                                                   | n/a      | n/a   |
| [hashicorp_consul_enable_log_to_file](defaults/main.yml#L142)           | bool | `False`                                                                                                                                                                                                                                                                                  | n/a      | n/a   |
| [hashicorp_consul_log_to_file_configuration](defaults/main.yml#L143)    | dict | `{'log_file': '{{ hashicorp_consul_logs_dir }}/consul.log', 'log_rotate_duration': '24h', 'log_rotate_max_files': 30}`                                                                                                                                                                   | n/a      | n/a   |


### Vars

**These are variables with higher priority**
#### File: vars/main.yml

| Var                                                          | Type | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Required | Title |
|--------------------------------------------------------------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|
| [hashicorp_consul_user](vars/main.yml#L3)                    | str  | `consul`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | n/a      | n/a   |
| [hashicorp_consul_group](vars/main.yml#L4)                   | str  | `consul`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | n/a      | n/a   |
| [hashicorp_consul_binary_path](vars/main.yml#L5)             | str  | `/usr/local/bin/consul`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | n/a      | n/a   |
| [hashicorp_consul_envoy_binary_path](vars/main.yml#L6)       | str  | `/usr/local/bin/envoy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | n/a      | n/a   |
| [hashicorp_consul_deb_architecture_map](vars/main.yml#L7)    | dict | `{'x86_64': 'amd64', 'aarch64': 'arm64', 'armv7l': 'arm', 'armv6l': 'arm'}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | n/a      | n/a   |
| [hashicorp_consul_envoy_architecture_map](vars/main.yml#L12) | dict | `{'x86_64': 'x86_64', 'aarch64': 'aarch64'}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | n/a      | n/a   |
| [hashicorp_consul_architecture](vars/main.yml#L15)           | str  | `{{ hashicorp_consul_deb_architecture_map[ansible_architecture] \| default(ansible_architecture) }}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | n/a      | n/a   |
| [hashicorp_consul_envoy_architecture](vars/main.yml#L16)     | str  | `{{ hashicorp_consul_envoy_architecture_map[ansible_architecture] \| default(ansible_architecture) }}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | n/a      | n/a   |
| [hashicorp_consul_service_name](vars/main.yml#L17)           | str  | `consul`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | n/a      | n/a   |
| [hashicorp_consul_github_api](vars/main.yml#L18)             | str  | `https://api.github.com/repos`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | n/a      | n/a   |
| [hashicorp_consul_envoy_github_project](vars/main.yml#L19)   | str  | `envoyproxy/envoy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | n/a      | n/a   |
| [hashicorp_consul_github_project](vars/main.yml#L20)         | str  | `hashicorp/consul`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | n/a      | n/a   |
| [hashicorp_consul_github_url](vars/main.yml#L21)             | str  | `https://github.com`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | n/a      | n/a   |
| [hashicorp_consul_repository_url](vars/main.yml#L22)         | str  | `https://releases.hashicorp.com/consul`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | n/a      | n/a   |
| [hashicorp_consul_configuration](vars/main.yml#L24)          | dict | `{'domain': '{{ hashicorp_consul_domain }}', 'datacenter': '{{ hashicorp_consul_datacenter }}', 'primary_datacenter': '{{ hashicorp_consul_primary_datacenter }}', 'data_dir': '{{ hashicorp_consul_data_dir }}', 'encrypt': '{{ hashicorp_consul_gossip_encryption_key }}', 'server': '{{ hashicorp_consul_enable_server }}', 'ui_config': '{{ hashicorp_consul_ui_configuration }}', 'connect': '{{ hashicorp_consul_mesh_configuration }}', 'leave_on_terminate': '{{ hashicorp_consul_leave_on_terminate }}', 'rejoin_after_leave': '{{ hashicorp_consul_rejoin_after_leave }}', 'enable_script_checks': '{{ hashicorp_consul_enable_script_checks }}', 'enable_syslog': True, 'acl': '{{ hashicorp_consul_acl_configuration }}', 'dns_config': '{{ hashicorp_consul_dns_configuration }}', 'log_level': '{{ hashicorp_consul_log_level }}', 'ports': {'dns': 8600, 'server': 8300, 'serf_lan': 8301, 'serf_wan': 8302, 'sidecar_min_port': 21000, 'sidecar_max_port': 21255, 'expose_min_port': 21500, 'expose_max_port': 21755}}` | n/a      | n/a   |
| [hashicorp_consul_configuration_string](vars/main.yml#L50)    | str   | `ports:
  http: {{ ('8500'\|int) if not hashicorp_consul_enable_tls else ('-1' \| int) }}
  https: {{ ('8501'\|int) if hashicorp_consul_enable_tls else ('-1' \| int) }}
  grpc: {{ ('8502'\|int) if not hashicorp_consul_enable_tls else ('-1' \| int) }}
  grpc_tls: {{ ('8503'\|int) if hashicorp_consul_enable_tls else ('-1' \| int) }}
`  | n/a | n/a |
| [hashicorp_consul_server_configuration_string](vars/main.yml#L57)    | str   | `bootstrap_expect: {{ hashicorp_consul_bootstrap_expect }}
`  | n/a | n/a |


### Tasks


#### File: tasks/recursive_copy_extra_dirs.yml

| Name                                          | Module                   | Has Conditions | Comments |
|-----------------------------------------------|--------------------------|----------------|----------|
| Consul \| Ensure destination directory exists | ansible.builtin.file     | False          |          |
| Consul \| Create extra directory sources      | ansible.builtin.file     | True           |          |
| Consul \| Template extra directory sources    | ansible.builtin.template | True           |          |

#### File: tasks/merge_variables.yml

| Name                                                      | Module                   | Has Conditions | Comments |
|-----------------------------------------------------------|--------------------------|----------------|----------|
| Consul \| Merge stringified configuration                 | vars                     | False          |          |
| Consul \| Merge server specific stringified configuration | vars                     | True           |          |
| Consul \| Merge addresses configuration                   | vars                     | False          |          |
| Consul \| Merge TLS configuration                         | block                    | True           |          |
| Consul \| Merge TLS configuration                         | vars                     | False          |          |
| Consul \| Add certificates directory to extra_files_dir   | ansible.builtin.set_fact | False          |          |
| Consul \| Merge extra configuration settings              | vars                     | False          |          |
| Consul \| Merge log to file configuration                 | vars                     | True           |          |
| Consul \| Merge telemetry configuration                   | block                    | False          |          |
| Consul \| Merge prometheus metrics configuration          | vars                     | True           |          |
| Consul \| Merge telemtry configuration                    | vars                     | False          |          |

#### File: tasks/main.yml

| Name                                                          | Module                        | Has Conditions | Comments |
|---------------------------------------------------------------|-------------------------------|----------------|----------|
| Consul \| Set reload-check & restart-check variable           | ansible.builtin.set_fact      | False          |          |
| Consul \| Import merge_variables.yml                          | ansible.builtin.include_tasks | False          |          |
| Consul \| Import prerequisites.yml                            | ansible.builtin.include_tasks | False          |          |
| Consul \| Import install_envoy.yml                            | ansible.builtin.include_tasks | True           |          |
| Consul \| Import install.yml                                  | ansible.builtin.include_tasks | False          |          |
| Consul \| Import configure.yml                                | ansible.builtin.include_tasks | False          |          |
| Consul \| Populate service facts                              | ansible.builtin.service_facts | False          |          |
| Consul \| Set restart-check variable                          | ansible.builtin.set_fact      | True           |          |
| Consul \| Enable service: {{ hashicorp_consul_service_name }} | ansible.builtin.service       | False          |          |
| Consul \| Reload systemd daemon                               | ansible.builtin.systemd       | True           |          |
| Consul \| Start service: {{ hashicorp_consul_service_name }}  | ansible.builtin.service       | True           |          |

#### File: tasks/install.yml

| Name                                                                  | Module                    | Has Conditions | Comments |
|-----------------------------------------------------------------------|---------------------------|----------------|----------|
| Consul \| Get latest release of consul                                | block                     | True           |          |
| Consul \| Get latest consul release from github api                   | ansible.builtin.uri       | False          |          |
| Consul \| Set wanted consul version to latest tag                     | ansible.builtin.set_fact  | False          |          |
| Consul \| Set wanted consul version to {{ hashicorp_consul_version }} | ansible.builtin.set_fact  | True           |          |
| Consul \| Get current consul version                                  | block                     | False          |          |
| Consul \| Stat consul version file                                    | ansible.builtin.stat      | False          |          |
| Consul \| Get current consul version                                  | ansible.builtin.slurp     | True           |          |
| Consul \| Download and install consul binary                          | block                     | True           |          |
| Consul \| Set consul package name to download                         | ansible.builtin.set_fact  | False          |          |
| Consul \| Download checksum file for consul archive                   | ansible.builtin.get_url   | False          |          |
| Consul \| Extract correct checksum from checksum file                 | ansible.builtin.command   | False          |          |
| Consul \| Parse the expected checksum                                 | ansible.builtin.set_fact  | False          |          |
| Consul \| Download consul binary archive                              | ansible.builtin.get_url   | False          |          |
| Consul \| Create temporary directory for archive decompression        | ansible.builtin.file      | False          |          |
| Consul \| Unpack consul archive                                       | ansible.builtin.unarchive | False          |          |
| Consul \| Copy consul binary to {{ hashicorp_consul_binary_path }}    | ansible.builtin.copy      | False          |          |
| Consul \| Update consul version file                                  | ansible.builtin.copy      | False          |          |
| Consul \| Set restart-check variable                                  | ansible.builtin.set_fact  | False          |          |
| Consul \| Cleanup temporary directory                                 | ansible.builtin.file      | False          |          |
| Consul \| Copy systemd service file for consul                        | ansible.builtin.template  | False          |          |
| Consul \| Set reload-check & restart-check variable                   | ansible.builtin.set_fact  | True           |          |

#### File: tasks/install_envoy.yml

| Name                                                                              | Module                   | Has Conditions | Comments |
|-----------------------------------------------------------------------------------|--------------------------|----------------|----------|
| Consul \| Get release for envoy:{{ hashicorp_consul_envoy_version }}              | vars                     | False          |          |
| Consul \| Check if envoy is already installed                                     | ansible.builtin.stat     | False          |          |
| Consul \| Check current envoy version                                             | ansible.builtin.command  | True           |          |
| Consul \| Set facts for wanted envoy release                                      | ansible.builtin.set_fact | True           |          |
| Consul \| Set facts for current envoy release                                     | ansible.builtin.set_fact | True           |          |
| Consul \| Create envoy directory                                                  | ansible.builtin.file     | False          |          |
| Consul \| Install envoy                                                           | block                    | True           |          |
| Consul \| Remove old compose binary if different                                  | ansible.builtin.file     | False          |          |
| Consul \| Download and install envoy version:{{ hashicorp_consul_envoy_version }} | ansible.builtin.get_url  | False          |          |
| Consul \| Update version file                                                     | ansible.builtin.copy     | False          |          |

#### File: tasks/prerequisites.yml

| Name                                                         | Module                | Has Conditions | Comments |
|--------------------------------------------------------------|-----------------------|----------------|----------|
| Consul \| Create group {{ hashicorp_consul_group }}          | ansible.builtin.group | False          |          |
| Consul \| Create user {{ hashicorp_consul_user }}            | ansible.builtin.user  | False          |          |
| Consul \| Create directory {{ hashicorp_consul_config_dir }} | ansible.builtin.file  | False          |          |
| Consul \| Create directory {{ hashicorp_consul_data_dir}}    | ansible.builtin.file  | False          |          |
| Consul \| Create directory {{ hashicorp_consul_certs_dir }}  | ansible.builtin.file  | False          |          |
| Consul \| Create directory {{ hashicorp_consul_logs_dir }}   | ansible.builtin.file  | True           |          |

#### File: tasks/configure.yml

| Name                                       | Module                        | Has Conditions | Comments |
|--------------------------------------------|-------------------------------|----------------|----------|
| Consul \| Create consul.env                | ansible.builtin.template      | False          |          |
| Consul \| Copy consul.json template        | ansible.builtin.template      | False          |          |
| Consul \| Set restart-check variable       | ansible.builtin.set_fact      | True           |          |
| Consul \| Copy extra configuration files   | block                         | True           |          |
| Consul \| Get extra file types             | ansible.builtin.stat          | False          |          |
| Consul \| Set list for file sources        | vars                          | True           |          |
| Consul \| Set list for directory sources   | vars                          | True           |          |
| Consul \| Template extra file sources      | ansible.builtin.template      | True           |          |
| Consul \| Template extra directory sources | ansible.builtin.include_tasks | True           |          |







## Author Information
Bertrand Lanson

#### License

license (BSD, MIT)

#### Minimum Ansible Version

2.10

#### Platforms

- **Ubuntu**: ['focal', 'jammy', 'noble']
- **Debian**: ['bullseye', 'bookworm']

<!-- DOCSIBLE END -->
