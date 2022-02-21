import click
import json
import os
import copy
from shared import *

@click.command()
@click.option('--tdir', type=str, default="template", prompt="template directory", help="directory with templates in it")
@click.option('--odir', type=str, default="packs", prompt="output directory", help="directory for database output")
@click.option('--cdir', type=str, default="import", prompt="import directory", help="directory for csv input files")
@click.option('--t', type=str, default="template.json", prompt="database template", help="Marked up template")
@click.option('--c', type=str, default="input.csv", prompt="csv file", help="csv formatted file")
@click.option('--o', type=str, default="output.db", prompt="output db", help="database of template merged with csv")

def run(tdir, odir, cdir, t, c, o):
    print(t, c, o)
    print(os.pardir)
    # reads a file into a string
    s = read_file(os.path.join(os.pardir, tdir, t))
    # read a csv into a list of dicts
    lofd = read_csv(os.path.join(os.pardir, cdir, c))
    # turn list of dicts into a list of json by substituting each key into s
    lofj = sub(s, lofd)
    # write the list of json the output file
    write_list_of_json_to_file(os.path.join(os.pardir, odir, o), lofj)

def sub(s, lofd):
    # step through the list of dicts, substituting each k, v into s
    # then create a json from it
    # output a list of json
    lofj = []
    for item in lofd:
        c = copy.copy(s)
        for k, v in item.items():
            c = c.replace('{{'+k+'}}', v)
        lofj.append(json.loads(c))
    return lofj

if __name__ == '__main__':
    run()