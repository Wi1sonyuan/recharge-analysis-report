with open('/tmp/fix3/magic_analysis_0821.html', 'r') as f:
    c = f.read()
c = c.replace('6.6% vs 上半年</div></div>\n\n<!-- PART 1', '6.6% vs 上半年</div></div>\n</div>\n\n<!-- PART 1')
with open('/tmp/fix3/magic_analysis_0821.html', 'w') as f:
    f.write(c)
print('Fixed')
