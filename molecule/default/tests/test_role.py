import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_zram_config_file(host):
    conf = host.file('/etc/init/zram-config.conf')

    assert conf.exists
    assert conf.is_file
    assert conf.user == 'root'
    assert conf.group == 'root'
    assert oct(conf.mode) == '0644'


def test_zram_sysctl_file(host):
    conf = host.file('/etc/sysctl.d/20-ansible-zram.conf')

    assert conf.exists
    assert conf.is_file
    assert conf.user == 'root'
    assert conf.group == 'root'
    assert oct(conf.mode) == '0644'
    conf.contains('^vm\\.min_free_kbytes=65536$')
    conf.contains('^vm\\.swappiness=10$')
