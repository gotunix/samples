#!/usr/bin/env python3

try:
    from subprocess import (
        run as subprocess_run,
        DEVNULL as subprocess_DEVNULL,
        CalledProcessError as subprocess_CalledProcessError
    )

except ImportError as error:
    print("Error importing module(s): {0}".format(error))
    exit(1)

class RunCommand(object):
    class Exception(object):
        class TypeError(Exception):
            pass

        class RunFailure(Exception):
            pass

    debug = True
    command = None

    def __init__(self, command=None, debug=True):
        if type(command) not in [list]:
            raise(
                RunCommand.Exception.TypeError(
                    "Expected list, got: {0}".format(
                        type(command).__name__
                        )
                    )
            )

        self.command = command
        self.debug = debug

    def run(self, **kwargs):
        log_cmd = ' '.join(self.command)
        print("Running command: {0}".format(log_cmd))

        try:
            if self.debug:
                run_cmd = subprocess_run(
                        self.command,
                        **kwargs,
                        check=True
                        )
            else:
                run_cmd = subprocess_run(
                        self.command,
                        **kwargs,
                        check=True,
                        stdout=subprocess_DEVNULL
                        )

        except subprocess_CalledProcessError as error:
            raise(
                    RunCommand.Exception.RunFailure(error)
                    )

        else:
            print("Command completed successfully")



run_command = RunCommand(["ls", "-la"]).run()
