import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("--torch", action="store_true")
args = parser.parse_args()

print(f"{args.name} betritt das Verlies.")
if args.torch:
    print("🕯️")
