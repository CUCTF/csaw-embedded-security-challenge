import hashlib

SHA_PREFIX = b'\xa7\x62\xd4\x90\x80'
SHAS = ['sha1', 'sha256', 'sha512']
last = 72386000

def test_hash(h):
    return h.digest()[:5] == SHA_PREFIX

def main():
    for i in range(last, 10_000_000_000):
        if i % 1000 == 0:
            print(f'iteration: {i}')
        str_i = str(i).zfill(10).encode()
        for scheme in SHAS:
            h = hashlib.new(scheme)
            h.update(str_i)
            if test_hash(h):
                print(scheme)
                print(str_i)
                return

if __name__ == '__main__':
    main()
