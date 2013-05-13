#!/usr/bin/env python

import sys
import re
import os


def pygmetize(s):
    tmp_console = 'tmp.console'
    tmp_html = 'tmp.html'
    f = open(tmp_console, 'w')
    f.write(s)
    f.close()
    os.system('pygmentize -f html -O style=colorful -l console -o ' + tmp_html + " " + tmp_console)
    # os.system('pygmentize -f html -O full,style=colorful,linenos=1 -l console -o ' + tmp_html + " " + tmp_console)
    os.remove(tmp_console)
    html = open(tmp_html, 'r').read()
    os.remove(tmp_html)
    html = html.replace('<span class="gp">', '<span class="gp" style="color: #008000; font-weight: bold ">')
    html = html.replace('<span class="go">', '<span class="go" style="color: #808080;">')
    html = html.replace('<span class="c">', '<span class="c" style="color: #808080;">')
    #    html = html.replace('<table class="highlighttable">', '<table class="sourceCode numberLines">')
    html = html.replace('<table class="highlighttable">', '<table class="sourceCode">')
    html = html.replace('<td class="linenos">', '<td class="lineNumbers">')
    return html

md_file = sys.argv[1]
prefix = os.path.splitext(md_file)[0]
f = open(md_file, 'r')
md_string = f.read()
f.close()


console_pattern = r"~~~~~*[{]\s*[.]console\s*[}]((.|\n)*?)~~~~~*"
match = re.search(console_pattern, md_string)

while match:
    md_string = md_string.replace(match.group(0), pygmetize(match.group(1)))
    match = re.search(console_pattern, md_string)

tmp_md = "tmp.md"
f = open(tmp_md, 'w')
f.write(md_string)
f.close()

os.system('pandoc --highlight-style espresso -s --mathml -i -t dzslides ' + tmp_md + ' -o ' + prefix + '.html')

os.remove(tmp_md)
