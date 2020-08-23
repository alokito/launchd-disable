import plistlib
from pathlib import Path
import typer

def read_plist(filename):
    with open(filename, 'rb') as f:
        return plistlib.load(f)

def write_plist(fname, plist):
    with open(fname, "wb") as f:
        plistlib.dump(plist, f)

def main(filename: Path):
    typer.echo(f"modifying {filename}")
    plist = read_plist(filename)
    if 'RunAtLoad' in plist:
        plist['RunAtLoad'] = False
    plist['Disabled'] = True
    write_plist(filename, plist)

if __name__ == "__main__":
    typer.run(main)