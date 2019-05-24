import os, sys, glob;

DEBUG_ON = os.environ.get("DEBUG_1181");


def debugPrint(*args):
    print(*args)


def noop(_):
    pass


debug = debugPrint if DEBUG_ON else noop
