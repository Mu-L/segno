# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 -- Lars Heuer - Semagia <http://www.semagia.com/>.
# All rights reserved.
#
# License: BSD License
#
"""\
Test against issue #18.
<https://github.com/heuer/segno/issues/18>

:author:       Lars Heuer (heuer[at]semagia.com)
:organization: Semagia - http://www.semagia.com/
:license:      BSD License
"""
from __future__ import unicode_literals, absolute_import
import segno


def test_issue_18():
    qr = segno.make_qr('')
    assert 1 == qr.version
    assert 'byte' == qr.mode
    assert 'H' == qr.error


def test_issue_18_micro():
    qr = segno.make_micro('')
    assert 'M3' == qr.version
    assert 'byte' == qr.mode
    assert 'M' == qr.error


def test_issue_18_automatic():
    qr = segno.make('')
    assert 'M3' == qr.version
    assert 'byte' == qr.mode
    assert 'M' == qr.error


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

