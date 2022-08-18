# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install thrift
#
# You can edit this file again by typing:
#
#     spack edit thrift
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
from spack.pkg.builtin.thrift import Thrift as BuiltinThrift


class Thrift(BuiltinThrift):
    """A lightweight, language-independent software stack for point-to-point RPC implementation"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/apache/thrift"
    url      = "https://github.com/apache/thrift/archive/refs/tags/v0.14.1.tar.gz"
    git = "https://github.com/apache/thrift"

    # maintainers = ['github_user1', 'github_user2']

    version('master', branch='master')
