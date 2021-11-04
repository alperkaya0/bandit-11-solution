alp = []
_alp = []

for x in range(97,123):
    alp.append(chr(x))
for x in range(65,91):
    _alp.append(chr(x))


input_text = "Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh"
input_text = list(input_text)
rot = 13
rot = rot % len(alp)
print("Input given as:")
print("   ","".join(input_text))
print()
for idx,x in enumerate(input_text):
    if x.islower():
        i = alp.index(x)
        input_text[idx] = alp[i-rot]
    if x.isupper():
        i = _alp.index(x)
        input_text[idx] = _alp[i-rot]

print("Here is the output:")
print("   ","".join(input_text))
