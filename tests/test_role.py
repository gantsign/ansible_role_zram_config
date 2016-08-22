def test_zram_config_file(File):
    conf = File('/etc/init/zram-config.conf')

    assert conf.exists
    assert conf.is_file
    assert conf.user == 'root'
    assert conf.group == 'root'
    assert oct(conf.mode) == '0644'
