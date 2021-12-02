import argparse
import json

def mkparser():
    parser=argparse.ArgumentParser()
    parser.add_argument("--name", required=True, type=str)
    parser.add_argument("--country", required=True, type=str)
    parser.add_argument("--petal-color", required=True, type=str)
    parser.add_argument("--stem-length", required=True, type=int)
    parser.add_argument("--with-thorns", default=False, type=bool)
    parser.add_argument("--companion-plants", default=None, nargs='+')
    
    return parser

parser=mkparser()
key=parser.parse_args([])
with open('journal.txt','+') as file:
    flower={"name":key.name, "country": key.country, "stem-length": key.stem_length, "with-thorns": key.with_thorns, "companion-plants": key.companion_plants}
    flowers.append(flower)
    json.dump(flowers,file,ident=4)
