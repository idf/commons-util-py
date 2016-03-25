import subprocess

__author__ = 'Daniel'


def basic_child_process():
    """
    .Popen to start a child process
    .Popen is non-blocking
    .Popen is a class, class constructor
    .communicate to wait for termination and read the output
    """
    proc1 = subprocess.Popen(
        ['echo', 'Hello from the child!'],
        stdout = subprocess.PIPE
    )
    proc2 = subprocess.Popen(
        ['sleep', '2'],
        stdout=subprocess.PIPE
    )
    print ".Popen is non-blocking"
    out, err = proc1.communicate()
    print out

    print "Wait for sleep termination"
    proc2.communicate()
    return out.decode('utf-8')


def poll_status():
    """
    .poll() to get the status of the child process
    """
    proc = subprocess.Popen(['sleep', '0.03'])
    cnt = 0
    while proc.poll() is None:  # while not terminated
        cnt += 1

    print cnt
    return 'Exit status %s' % proc.poll()
