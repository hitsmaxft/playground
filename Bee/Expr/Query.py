# coding=utf-8

import Expr.Wrapper as w

class Query(object):
    """
    针对节点查寻的一个工具类. 用于解析和定位节点类型/值等
    """
    t_node = r"([a-z]+.)?[a-z]+"

    def is_node(path):
        """

        >>>Query.is_node("data.nav")
        True
        """
        return True
        pass

    def is_node_get_len(path):
        pass

    def is_node_get_keys(path):
        pass

    def is_node_get_int(path):
        pass

    def __init__(self, url, data):
        self._url = url
        self._d = data
        pass

    #查寻节点
    def query(self, ind=""):
        """
        :param ind: string
        """
        node_path = ind.split(".")
        node_ind = self._d
        if node_path:
            while 1:
                cur = node_path.pop()
                if not cur or cur not in node_ind:
                    return w(None)
                else:
                    pass

    def check_path(self, path):
        pass

    def _data(self):
        return {
            'data': {
                'nav': {
                'type': 3,
                'cat': ['13', '1512'],
                'prop': None
                },
                'headCrumb': {
                    'cat': '15'
                }
            },
            'log':None,
            'config':None
        }