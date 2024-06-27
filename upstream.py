#!/usr/bin/env python
import os
import re
import pathlib
import argparse
import subprocess
if os.environ.get("SPACK_ROOT", "") == "":
    print("spack must be loaded to upstream")
    exit(1)
SPACK_ROOT = pathlib.Path(os.environ["SPACK_ROOT"])
SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()


#default match all pattern
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", action="append", default=["new", "changes"])
parser.add_argument("-n", "--dryrun", action="store_true")
parser.add_argument("pattern", default=re.compile(".*"), type=re.compile, nargs='?')
args = parser.parse_args()

if args.dryrun:
    action = print
else:
    action = subprocess.run

for downstream_pkg in SCRIPT_DIR.glob("packages/*/package.py"):
    pkg=str(downstream_pkg.parent.name)
    #check if the pattern matches
    if not args.pattern.match(pkg):
        continue
    upstream_pkg= SPACK_ROOT /"var/spack/repos/builtin/packages/" / pkg / "package.py"
    if upstream_pkg.exists() and "changes" in args.mode: 
        #nvim -d $downstream_pkg $upstream_pkg
        action(["nvim", "-d", str(downstream_pkg), str(upstream_pkg)])
    #check if we need to upstream
    elif "new"  in args.mode:
        if not args.dryrun:
            upstream_pkg.mkdir(exist_ok=True)
        action(["nvim", "-d", str(downstream_pkg), str(upstream_pkg)])
