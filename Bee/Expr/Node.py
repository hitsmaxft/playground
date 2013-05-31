#!/bin/bash/python
# -*- coding: utf-8 -*-

import Wrapper

class Node(Wrapper):
    _path=None


    def __init__(self, path):
        Wrapper.__init__(path)
        self._path = path
        #self._v = query(path)

    def parse(expr):
        """


        :return:
        """
        return expr

    def __len__(self):
        """
        检测节点值的长度 如果节点类型不是数组, 则返回错误

        :return: int|None
        """

        if (isinstance(self._getV(), dict) or
                isinstance(self._getV(), list)):
            return len(self._getV())
        return None
