import sys
import hashlib

SHA_PREFIX = b'\x20\x75\x4a\x41\xce'

SHAS = ['sha1', 'sha256', 'sha512']
#last = 700000000
#last_high = 9790630000

def test_hash(h):
    return h.digest()[:5] == SHA_PREFIX

def brute(lo, hi):
    print(f'[+] initializing search: {lo}:{hi}')
    for i in range(lo, hi):
        if i % 1_000_000 == 0:
            print(f'iteration: {i}')
        str_i = str(i).zfill(10).encode()
        for scheme in SHAS:
            h = hashlib.new(scheme)
            h.update(str_i)
            if test_hash(h):
                print('[+] FOUND')
                print(f'- {scheme}')
                print(f'- {str_i}')
                return
    print(f'[-] not in range: {lo}:{hi}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'USAGE: {sys.argv[0]} lo hi')
        sys.exit(-1)

    start = int(sys.argv[1])
    end = int(sys.argv[2])
    brute(start, end)
