import os
import ast
from graphviz import Digraph
from subprocess import check_call

def generate_calltree(
    filename,
    output = "calltree.png"):
    
    g = Digraph('G', filename='calltree.gv', engine='sfdp')
    
    lines = [line for line in open(filename)]
    
    with open(filename) as f:
        code = f.read()

    a = ast.parse(code)
    definitions = [n for n in ast.walk(a) if type(n) == ast.FunctionDef]


    defs = [lines[(i.lineno-1)] for i in definitions]
    defs = [i.replace("def ","") for i in defs]
    defs = [i.split("(")[0] for i in defs]
    defs = [{"name":i,"calls":[]} for i in defs]

    for i in range(0,len(definitions)):
        if(i == (len(definitions)-1)):
            max_lines = len(lines)-1
        else:
            max_lines = (definitions[i+1].lineno)-1
        code_lines = [lines[i] for i in range(definitions[i].lineno,max_lines)]
        for code_line in code_lines:
            for definition in [i["name"] for i in defs]:
                if definition+"(" in code_line:
                    if(definition not in defs[i]["calls"]):
                        defs[i]["calls"].append(definition)
                        #g.edge(defs[i]["name"],definition)
    for defi in defs:
        for call in defi["calls"]:
            g.edge(defi["name"], call)
    g.view()
    check_call(['dot','-Tpng','calltree.gv','-o',output])
    os.remove('calltree.gv')
    os.remove('calltree.gv.pdf')
