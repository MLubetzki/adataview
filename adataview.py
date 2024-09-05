#!/usr/bin/env python
import warnings
import argparse
import mudata


def imports():
    global sc, np, sns, plt, IPython
    import scanpy as sc
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import IPython

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="adataview", description="Quickly inspect anndata objects. Also supports mudata")
    parser.add_argument("anndata", metavar="adata", nargs="+", help="Path to the anndata object to open")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show warnings")
    parser.add_argument("-s", "--shell", action="store_true", help="Open a shell with anndata object as \"adata\". If multiple adata objects are given, they are stored in a list called \"adatas\"")
    args = parser.parse_args()


    if args.shell:
        adatas = []
        for path in args.anndata:
            with warnings.catch_warnings():
                if not args.verbose:
                    warnings.simplefilter("ignore")
                adatas.append(mudata.read(path))
        if len(adatas) == 1:
            adata = adatas[0]
        imports()
        IPython.embed(colors="neutral")
    else:
        for path in args.anndata:
            with warnings.catch_warnings():
                if not args.verbose:
                    warnings.simplefilter("ignore")
                adata = mudata.read(path, backed=True)
            print(adata)
            del adata
