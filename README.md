Ansible Role: Zram Config
=========================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-zram-config.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-zram-config)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.zram--config-blue.svg)](https://galaxy.ansible.com/gantsign/zram-config)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-zram-config/master/LICENSE)

Role to install Zram Config for compressed RAM swap.

Requirements
------------

* Ubuntu

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.zram-config
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

To run the role (i.e. the `tests/test.yml` playbook), and test the results
(`tests/test_role.py`), execute the following command from the project root
(i.e. the directory with `molecule.yml` in it):

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
