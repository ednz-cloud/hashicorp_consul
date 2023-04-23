"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    etc_hosts = host.file("/etc/hosts")
    assert etc_hosts.exists
    assert etc_hosts.user == "root"
    assert etc_hosts.group == "root"

def test_consul_user_group(host):
    """Validate consul user and group."""
    consul_group = host.group("consul")
    consul_user = host.user("consul")
    assert consul_group.exists
    assert consul_user.exists
    assert consul_user.group == "consul"
    assert consul_user.shell == "/bin/false"

def test_consul_config(host):
    """Validate /etc/consul.d/ files."""
    etc_consul_d_consul_env = host.file("/etc/consul.d/consul.env")
    etc_consul_d_consul_json = host.file("/etc/consul.d/consul.json")
    for file in etc_consul_d_consul_env, etc_consul_d_consul_json:
        assert file.exists
        assert file.user == "consul"
        assert file.group == "consul"
        assert file.mode == 0o600
        if file == etc_consul_d_consul_json:
            assert file.content_string != ""

def test_consul_storage(host):
    """Validate /opt/consul directory."""
    opt_consul = host.file("/opt/consul")
    assert opt_consul.exists
    assert opt_consul.is_directory
    assert opt_consul.user == "consul"
    assert opt_consul.group =="consul"
    assert opt_consul.mode == 0o755

def test_consul_service_file(host):
    """Validate consul service file."""
    lib_systemd_system_consul_service = host.file("/lib/systemd/system/consul.service")
    assert lib_systemd_system_consul_service.exists
    assert lib_systemd_system_consul_service.user == "root"
    assert lib_systemd_system_consul_service.group == "root"
    assert lib_systemd_system_consul_service.mode == 0o644
    assert lib_systemd_system_consul_service.content_string != ""

def test_consul_service(host):
    """Validate consul service."""
    consul_service = host.service("consul.service")
    assert consul_service.is_enabled
    assert consul_service.is_running
    assert consul_service.systemd_properties["Restart"] == "on-failure"
    assert consul_service.systemd_properties["User"] == "consul"
    assert consul_service.systemd_properties["Group"] == "consul"
    assert consul_service.systemd_properties["EnvironmentFiles"] == "/etc/consul.d/consul.env (ignore_errors=yes)"
    assert consul_service.systemd_properties["FragmentPath"] == "/lib/systemd/system/consul.service"

def test_consul_interaction(host):
    """Validate interaction with consul with acl enabled."""
    acl_token = "1a1f2ce5-3730-47de-9a9c-89e037376bab"
    consul_kv_put = host.check_output("CONSUL_HTTP_TOKEN=" + acl_token + " consul kv put foo bar")
    consul_kv_get = host.check_output("CONSUL_HTTP_TOKEN=" + acl_token + " consul kv get foo")
    consul_kv_delete = host.check_output("CONSUL_HTTP_TOKEN=" + acl_token + " consul kv delete foo")
    assert host.check_output("CONSUL_HTTP_TOKEN=" + acl_token + " consul members")
    assert consul_kv_put == "Success! Data written to: foo"
    assert consul_kv_get == "bar"
    assert consul_kv_delete == "Success! Deleted key: foo"
