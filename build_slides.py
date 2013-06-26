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

html_file = prefix + '.html'
os.system('pandoc --highlight-style espresso -s --mathjax -i -t dzslides ' + tmp_md + ' -o ' + html_file)

os.remove(tmp_md)

f = open(html_file, 'r')
html_string = f.read()
f.close()

def backgroundimage(pagename, image, html_string):
    
    for s in ('', '-1', '-2', '-3', '-4', '-5', '-6', '-7'):
        pagenameid = "{0}{1}".format(pagename, s)
        before = 'id="{0}"'.format(pagenameid)
        after = '''id="%s" style="background-image:url('%s');"''' % (pagenameid, image)
        html_string = html_string.replace(before, after, 10)
    return html_string

html_string = backgroundimage('simulation-management', 'image2-50.png', html_string)
html_string = backgroundimage('sumatra', 'image2-50.png', html_string)
html_string = backgroundimage('version-control', 'stack-of-files60.png', html_string)
html_string = backgroundimage('andrew-davison', 'id_photo5-120.png', html_string)
html_string = backgroundimage('conclusion', 'image2-50.png', html_string)
#html_string = backgroundimage('context', 'manufact_goals40.png', html_string)

html_string = html_string.replace('transition: left', 'transition: right', 10)

html_string = html_string.replace('</section>', """
<footer style="border:0; padding:0px;background-color: #99D6EB;">
<p style="text-align: center; border:0; padding:0px; background-color: #99D6EB;"><img height="15%" border="0" padding="0" src="./NIST_logo_transparent.png"></p>
</footer>
</section>""", 1)

html_string = html_string.replace("font-family: Arial, serif", "font-family: Glode, Glode", 1)

html_string = html_string.replace("background-color: white", "background-color: #99D6EB", 1)

def span(slide, html_string):
    before = "<h1>{0}</h1>".format(slide)
    after = """<span style="display:block; background-color:#99D6EB;">{0}</span>""".format(before)
    return html_string.replace(before, after)

html_string = span("Simulation Management", html_string)
html_string = span("Sumatra", html_string)
html_string = span("Version Control", html_string)
html_string = span("Andrew Davison", html_string)
html_string = span("Conclusion", html_string)

# html_string = html_string.replace("<h1>Simulation Management</h1>", """<span style="display:block; background-color:#99D6EB;"><h1>Simulation Management</h1></span>""", 10)

# html_string = html_string.replace("<h1>Sumatra</h1>", """<span style="display:block; background-color:#99D6EB;"><h1>Sumatra</h1></span>""", 10)

# html_string = html_string.replace("<h1>Version Control</h1>", """<span style="display:block; background-color:#99D6EB;"><h1>Version Control</h1></span>""", 10)

f = open(html_file, 'w')
f.write(html_string)
f.close()
