import sys

def uret(s2, s3):
    b = s2.split("=")[1]
    d = s3.split("=")[1]
    return b,d


if len(sys.argv) > 2:
    s2 = sys.argv[2]
    s3 = sys.argv[3]

    b, d = uret(s2, s3)

    print(b)
    print(d)