import argparse

def hello_demo():
    parser = argparse.ArgumentParser()
    parser.add_argument("Hisaan")
    args = parser.parse_args(["Ahmad"])
    print(f"Hello, {args.Hisaan}!")

def ab_demo():
    parsers = argparse.ArgumentParser()
    parsers.add_argument("a")
    parsers.add_argument("b")
    args = parsers.parse_args(["10", "20"])
    print(f"A = {args.a}, B = {args.b}")

hello_demo()
ab_demo()



parser = argparse.ArgumentParser()
parser.add_argument("--age")
args = parser.parse_args()

print(f"Age is {args.age}")