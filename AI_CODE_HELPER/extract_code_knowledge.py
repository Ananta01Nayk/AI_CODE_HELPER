import os, ast, json

BASE = os.path.dirname(__file__)
TARGET = r"D:\ananta\AI_engineer_Intership\Day3\AI_CODE_HELPER\SAMPLES"
OUT = os.path.join(BASE, "DATA", "code_knowledge.json")

data = {
    "functions": {},
    "classes": {},
    "calls": {}
}

class Analyzer(ast.NodeVisitor):
    def __init__(self, file, code):
        self.file = file
        self.lines = code.splitlines()
        self.current = None

    def visit_FunctionDef(self, node):
        code = "\n".join(self.lines[node.lineno-1:node.end_lineno])

        data["functions"][node.name] = {
            "name": node.name,
            "file": self.file,
            "start": node.lineno,
            "end": node.end_lineno,
            "code": code,
            "called_by": []
        }

        self.current = node.name
        self.generic_visit(node)
        self.current = None

    def visit_ClassDef(self, node):
        code = "\n".join(self.lines[node.lineno-1:node.end_lineno])

        data["classes"][node.name] = {
            "name": node.name,
            "file": self.file,
            "start": node.lineno,
            "end": node.end_lineno,
            "code": code
        }
        self.generic_visit(node)

    def visit_Call(self, node):
        if self.current and isinstance(node.func, ast.Name):
            data["calls"].setdefault(self.current, []).append(node.func.id)
        self.generic_visit(node)

# scan files
files=[]
for r,_,f in os.walk(TARGET):
    for file in f:
        if file.endswith(".py"):
            files.append(os.path.join(r,file))

for f in files:
    try:
        code=open(f,encoding="utf8").read()
        Analyzer(f,code).visit(ast.parse(code))
    except: pass

# build reverse dependencies
for caller, callees in data["calls"].items():
    for callee in callees:
        if callee in data["functions"]:
            data["functions"][callee]["called_by"].append(caller)

os.makedirs("DATA",exist_ok=True)
json.dump(data, open(OUT,"w",encoding="utf8"), indent=2)

print("code knowledge extracted")
