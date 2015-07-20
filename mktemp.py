#!/usr/bin/env python

import json
import os
import requests
import tempfile

from ansible.callbacks import vv
from ansible.errors import AnsibleError as ae
from ansible.runner.return_data import ReturnData
from ansible.utils import parse_kv

class ActionModule(object):
    ''' Create a new temporary file or directory'''

    def __init__(self, runner):
        self.runner = runner
        self.path = None
        self.type = None


    def run(self, conn, tmp, module_name, module_args, inject, complex_args=None, **kwargs):

        args = {}
        if complex_args:
            args.update(complex_args)
        args.update(parse_kv(module_args))

        self.type = 'file'
        result = {}

        suffix = ''
        prefix = 'tmp'
        dir = None

        if (self.type == 'file')
            path = self.mktempFile(suffix=suffix, prefix=prefix, dir=dir)
            print path
        return ReturnData(result=result)

    def mktempFile(suffix, prefix, dir)
      f = tempfile.TemporaryFile(suffix=suffix, prefix=prefix, dir=dir, delete=False)
      return f.name
