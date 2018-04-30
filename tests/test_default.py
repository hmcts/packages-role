import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_molecule_1_is_installed(Package):
    molecule = Package("molecule-test-1")
    assert molecule.is_installed


def test_molecule_2_is_not_installed(Package):
    molecule = Package("molecule-test-2")
    assert not molecule.is_installed


def test_molecule_1_rpm_is_removed(File):
    rpmExists = File("/tmp/test-1.rpm").exists
    assert not rpmExists


def test_molecule_1_sysconfig_is_present(File):
    sysconfig = File("/etc/sysconfig/molecule-test-1").exists
    assert sysconfig


def test_molecule_1_sysconfig_is_correct(File):
    sysconfig = File("/etc/sysconfig/molecule-test-1").content_string

    expected_sysconfig = open("tests/expected-sysconfig.txt", "r").read()

    assert sysconfig == expected_sysconfig
