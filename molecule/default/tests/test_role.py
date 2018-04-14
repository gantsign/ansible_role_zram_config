import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_zram_config_file(File):
    conf = File('/etc/init/zram-config.conf')

    assert conf.exists
    assert conf.is_file
    assert conf.user == 'root'
    assert conf.group == 'root'
    assert oct(conf.mode) == '0644'
