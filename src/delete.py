import re

thisdict =	{
    "rule": {'LHS': 'S',
	'RHS': ['_epsilon_', 'V', 'aSb']},
    "model": "Mustang",
	"year": 1964
}

r = thisdict["rule"]

v = r["LHS"]

p = r["RHS"]
print("productions: ")
print(p)

pro = p[0]
print("pre pro: " + p[0])

if "_epsilon_" in p[0]:
	p[0] = re.sub("_epsilon_", "", p[0])

print("post pro: " + p[0])

if p[0] == "":
    p.pop(0)
