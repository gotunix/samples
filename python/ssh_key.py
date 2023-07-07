#!/usr/bin/env python3

from ansible.runner import Runner

# Path to VM host list
VM_HOSTS = '/home/ubuntu/workspace/ansible/hosts'


def generate_ssh_keys(remote_user, remote_ip):
    """Generate ssh keys on remote server by calling Ansible API
    and Ansible user module.
    Args:
    username: remote user
    remote_ip: remote IP address
    see: http://stackoverflow.com/a/27597987
    reference: http://docs.ansible.com/ansible/user_module.html
    """
    runner = Runner(
        host_list=VM_HOSTS,
        module_name='user',
        module_args="name=%s generate_ssh_key=yes ssh_key_comment='%s@%s'" %
        (remote_user, remote_user, remote_ip),
        pattern=remote_ip,
        sudo=True,
        remote_user='root',
        remote_pass='PASSWORD',
        sudo_pass='PASSWORD')
    ssh_keys_result = runner.run()
    return str(ssh_keys_result['contacted'][remote_ip]['ssh_public_key'])
