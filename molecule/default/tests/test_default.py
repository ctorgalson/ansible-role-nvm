import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize('username', [
    'lorem',
    'ipsum',
])
def test_nvm_dir(host, username):
    d = host.file('/home/{}'.format(username))

    assert d.exists
    assert d.user == username
    assert d.group == username
