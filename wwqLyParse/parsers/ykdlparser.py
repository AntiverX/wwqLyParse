#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# author wwqgtxx <wwqgtxx@gmail.com>


import urllib.request, io, os, sys, json, re, math, subprocess, traceback, logging

try:
    from ..common import *
except Exception as e:
    from common import *

__MODULE_CLASS_NAMES__ = ["YKDLParser"]
try:
    try:
        from . import yougetparser
    except Exception as e:
        import yougetparser


    class YKDLParser(yougetparser.YouGetParser):

        un_supports = yougetparser.YouGetParser.un_supports  # + ['www.iqiyi.com']
        bin = './ykdl/ykdl.py'
        name = "YouKuDownLoader解析"

        def _get_py_bin(self):
            py_bin = sys.executable
            if "wwqLyParse64.exe" in py_bin:
                py_bin = py_bin.replace("wwqLyParse64.exe", "wwqLyParse64-ykdl.exe")
            elif "wwqLyParse32.exe" in py_bin:
                py_bin = py_bin.replace("wwqLyParse32.exe", "wwqLyParse32-ykdl.exe")
            return py_bin

        # make arg
        def _make_arg(self, url, _format=None, use_info=False, *k, **kk):
            arg = self._make_proxy_arg()
            # NOTE ignore __default__ format
            if _format and (_format != '__default__'):
                arg += ['--format', _format]
            arg += ['-i']
            arg += ['--debug']
            arg += ['--json', url]
            return arg

        def _run(self, arg, need_stderr=False):
            return super(YKDLParser, self)._run(arg, need_stderr)

        def get_version(self):
            try:
                stdout, stderr = self._run(['-h'], True)
                if "Errno" in stderr:
                    return ""
                return stdout.split('(')[1].split(')')[0]
            except Exception as e:
                logging.exception("get version error")
                # print(e)
                # import traceback
                # traceback.print_exc()
            return ""

except:
    logging.exception("can't load yougetparser.py,it need to be super class")
    __MODULE_CLASS_NAMES__ = []
