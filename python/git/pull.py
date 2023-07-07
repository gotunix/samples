#!/usr/bin/env python3

import subprocess
import os
import time


# put your GA directory here, e.g. '/home/fay/code/GA/DSI'
CWD = ''

# put the path to a .gitignore template here
# e.g. '/home/fay/code/GA/DSI/projects/West-Nile-Virus-Prediction/.gitignore'
GITIGNORE = ''

# put your GitHub repo upstream pattern here 
# e.g. 'git@git.generalassemb.ly:DSI-DC-5/'
UPSTREAM = ''

# put your GitHub origin pattern here
# e.g. 'git@git.generalassemb.ly:jingfeicai/'
ORIGIN = ''

# put a list of your other GitHub account patterns here (can be left empty)
# e.g. ['git@github.com:GA-DSI-DC-5-Team-1/', 'git@github.com:Ailuropoda1864/']
OTHER_GITHUB = []


def main():
    git_dir = find_git_dir(CWD)
    for dirpath, repo in git_dir.items():
        # print('current directory: {}'.format(dirpath))
        config_path = os.path.join(dirpath, '.git', 'config')
        config = read_file(config_path)

        if '[remote "upstream"]' in config:
            report = git_pull(dirpath, repo)
            if report:
                print(report)

        else:
            if ORIGIN in config:
                add_remote_upstream(dirpath)
                git_fetch(dirpath)

            elif UPSTREAM in config:
                report = git_pull(dirpath, repo, 'origin HEAD'.split())
                if report:
                    print(report)

            else:
                for github in OTHER_GITHUB:
                    if github in config:
                        break
                else:
                    print('{!r} does not have remote upstream.'.format(dirpath))

    print('Script finished at {}\n'.format((time.ctime())))


def find_git_dir(cwd):
    return {dirpath: {'dirnames': dirnames, 'filenames': filenames}
            for dirpath, dirnames, filenames in os.walk(cwd)
            if '.git' in dirnames}


def read_file(file):
    with open(file) as f:
        return f.read()


def git_pull(dirpath, repo, remote_branch=['upstream', 'master']):
    remote_ref_path = os.path.join(
        dirpath, '.git', 'refs', 'remotes', *remote_branch)
    try:
        remote_ref = read_file(remote_ref_path)
    except FileNotFoundError as e:
        print(str(e))
        remote_ref = None

    git_fetch(dirpath, remote_branch)

    # if .git/refs/remotes/upstream/master has changed since fetch
    if remote_ref and remote_ref != read_file(remote_ref_path):

        # add gitignore if not present
        if '.gitignore' not in repo['filenames']:
            add_gitignore(GITIGNORE, dirpath)

        # commit all local changes, then merge with upstream
        merge = git_merge(dirpath)
        return 'Remote branch of {!r} is updated:\n{}\n'.format(dirpath, merge)


def git_fetch(cwd, remote_branch=['upstream', 'master']):
    return subprocess.run(['git', 'fetch'] + remote_branch, cwd=cwd)


def git_merge(cwd):
    os.chdir(cwd)
    subprocess.run('git add .'.split())
    subprocess.run(
        'git commit -m'.split() + ["auto commit before merging with remote"])
    try:
        return subprocess.check_output(
            'git merge -m'.split() + ["auto merge by script", 'FETCH_HEAD'],
            stderr=subprocess.STDOUT,
            universal_newlines=True)
    except subprocess.CalledProcessError:
        return 'Error occurred during merge.'.format(cwd)


def add_gitignore(template, cwd):
    subprocess.run(['cp', template, os.path.join(cwd, '.gitignore')])


def add_remote_upstream(cwd):
    dir = cwd.split('/')[-1]
    subprocess.run(
        'git remote add upstream'.split() + [UPSTREAM + dir + '.git'], cwd=cwd)


if __name__ == '__main__':
    main()
