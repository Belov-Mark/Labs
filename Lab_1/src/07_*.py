s = input("in: ").strip()

for i in range(len(s)):
    if s[i].isupper():
        start = i
        break

n = len(s)

for k in range(1, n):
    text = ""
    pos = start
    while pos < n:
        text += s[pos]
        pos += k
    
    if len(text) > 1 and text[-1] == '.':
        second_pos = start + k
        if second_pos > 0 and s[second_pos - 1].isdigit():
            print(f"out: {text}")
            break