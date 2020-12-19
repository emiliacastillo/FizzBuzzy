
def fizzbuzz(i):
    return 'fizz'*(not i % 3)+'buzz'*(not i % 5) or i


def main(a, b):
    res = 'Sequence\n'
    for i in range(a, b+1):
        res += str((fizzbuzz(i)))+','*(not i == b)+'\n'*(not i % 10)
    return res
