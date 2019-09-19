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


@pytest.mark.parametrize('username,filename', [
    ('lorem', '.zshrc')
])
def test_rc_file(host, username, filename):
    f = host.file('/home/{}/{}'.format(username, filename))

    assert f.exists
    assert 'export NVM_DIR=' in f.content_string
    assert f.user == username
    assert f.group == username
