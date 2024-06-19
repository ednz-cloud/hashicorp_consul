## v0.2.0 (2024-06-19)

### Feat

- add ubuntu 24.04 to support list

### Fix

- remove deprecated code

## v0.1.1 (2024-06-17)

### Fix

- rename all variables to conform to ansible-lint var-naming rule, remove outdated documentation bits

## v0.1.0 (2024-06-17)

### Feat

- add simple test on binary presence
- change host install from package manager to direct binary download, fix restart and reload checks
- add pre-commits and commitizen file
- move to CICD workflow v2 for publishing
- **extra_files**: ensure destination directory exists before copying
- **tests**: adjust test variables
- **README**: remove mention of sample file after removal
- **extra_files**: allow copying multiple extra_files sources, either files or directories, recursvively, and allow jinja2 templating inside of them
- **docker**: adjust test for with_acl_enabled_vagrant
- **docker**: customize entrypoint and cmd to fit the deployment better
- **docker**: add cmd to container to avoid starting in dev mode
- **core**: change namespace
- **readme/vars**: remove install and auto_update vars, adjust default data_dir, adjust tests
- **task**: remove role dependency for installing consul from repo
- **task**: revamp the host install method to make sure it doesnt break quorum
- **task**: add extra volume mapping option for docker deployment
- **tests**: make sure vagrant tests write to correct data_dir
- **tasks**: copy service file after installing for host deploy method
- **tasks**: install-host needs to happen before configure
- **readme**: update documentation on docker install
- **test**: add acl_enabled tests with docker
- **tests**: added container specific tests to default_vagrant
- **tasks**: map extra volumes dinamically to container
- **tasks**: add docker deployment, some rework to accomodate it
- remove become from role
- fix #2
- add vagrant tests, add become:true to not rely on ansible.cfg
- variabilize test_os in vagrant scenarios
- gather_facts on verify.yml for molecule (skip-ci)
- some testing with vagrant

### Fix

- do not attempt to loop over undefined list when no extra_files or no extra_dirs
- linting
- revert tests for default scenario
