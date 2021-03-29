import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def postorder(root):
    if not root:
        return
    if root['left']:
        postorder(root['left'])
    if root['right']:
        postorder(root['right'])
    print(root['value'])

def _5639():
    tree={'value': int(input()), 'right': {}, 'left': {}}
    while True:
        try:
            value = int(input())
            root = tree
            while root:
                if root['value'] < value:
                    root = root['right']
                else:
                    root = root['left']
            root['value'] = value
            root['left'] = {}
            root['right'] = {}
        except Exception as e:
            break
    postorder(tree)

if __name__ == '__main__':
    _5639()