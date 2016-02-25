# http://www.codewars.com/kata/55c933c115a8c426ac000082/


def eval_object(v):
    return {"+": v['a'] + v['b'],
        "-": v['a'] - v['b'],
        "/": v['a'] / v['b'],
        "*": v['a'] * v['b'],
        "%": v['a'] % v['b'],
        "**": v['a'] ** v['b']}.get(v.get('operation', 1))
