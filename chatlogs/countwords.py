import collections
import sys

counts = collections.Counter()
remaining = ''
while True:
    chunk = remaining + sys.stdin.read(64*1024)
    if not chunk:
        break
    last_lf = chunk.rfind('\n')  # process to last LF character
    if last_lf == -1:
        remaining = ''
    else:
        remaining = chunk[last_lf+1:]
        chunk = chunk[:last_lf]
    counts.update(chunk.lower().split())

for word, count in counts.most_common(10):
    print(word, count)

# Get-Content fuslie.log | python countwords.py