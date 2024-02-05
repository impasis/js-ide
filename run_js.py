import subprocess


def run_js(filename):
    subprocess.call(['start', 'cmd', '/k', f'node {filename} Pause'], shell=True)


"""
Test:

run_js("test.js")
"""