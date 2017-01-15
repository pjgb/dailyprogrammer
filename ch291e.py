#!/usr/bin/env python3

challenge = """100 120
297 90
66 110
257 113
276 191
280 129
219 163
254 193
86 153
206 147
71 137
104 40
238 127
52 146
129 197
144 59
157 124
210 59
11 54
268 119
261 121
12 189
186 108
174 21
77 18
54 90
174 52
16 129
59 181
290 123
248 132"""

lines = challenge.split('\n')
weight, temperature = [int(i) for i in lines[0].split(' ')]
good_chairs = []

for i, line in enumerate(lines[1:]):
    chair, porridge = [int(i) for i in line.split(' ')]
    if (chair >= weight) and (porridge <= temperature):
        good_chairs.append(str(i+1))
print(' '.join(good_chairs))