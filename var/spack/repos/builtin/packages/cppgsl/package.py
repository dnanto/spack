# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Cppgsl(CMakePackage):
    """C++ Guideline Support Library"""

    homepage = "https://github.com/Microsoft/GSL"
    url      = "https://github.com/Microsoft/GSL/archive/v2.0.0.tar.gz"
    git      = "https://github.com/Microsoft/GSL.git"

    version('develop', branch='master')
    version('2.0.0', sha256='6cce6fb16b651e62711a4f58e484931013c33979b795d1b1f7646f640cfa9c8e')
    version('1.0.0', sha256='9694b04cd78e5b1a769868f19fdd9eea2002de3d4c3a81a1b769209364543c36')

    variant('cxxstd',
            default='14',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('cmake@3.1.3:', type='build')

    def cmake_args(self):
        args = [
            '-DGSL_CXX_STANDARD={0}'.format(self.spec.variants['cxxstd'].value)
        ]
        return args
