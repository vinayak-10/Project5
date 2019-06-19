import sys
import Inst
import pathlib as pl


pat = pl.WindowsPath
pa = pat.cwd()
sys.path.append(str(pa))


def main():
    choice = input("Enter 'n' for NEW entries \n And 'o' for Old entries:")

    if choice == 'n':
        Inst.inp()
        Inst.alloc()

    elif choice == 'o':
        print('No old data present')


if __name__ == '__main__':
    main()
