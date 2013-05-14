% Using Sumatra to Manage Numerical Simulations
% Daniel Wheeler
% May 14, 2013

## 

<!-- pandoc -t dzslides -s presentation.md -o presentation.html -->

<!-- pandoc --highlight-style pygments -s --mathml -i -t dzslides presentation.md -o presentation.html -->
<!-- pandoc --highlight-style espresso -s --mathml -i -t dzslides presntation.md -o presentation.html -->

<p style="text-align: center;"> <i>"Automate away ability to make dumb
mistakes. Don't use human based process."</i>,<br>
Tim Clem, Github bigwig, SciPy 2012 </p>

 <!-- - This is a short clip from a talk I saw at scipy last year. -->
 <!-- - The speaker is a git hub gut and his talk was about ideas and philosophy used at github. -->

<p style="text-align: center;"><iframe width="560" height="410" src="http://www.youtube.com/embed/R75krhS51d0?rel=0" frameborder="0"> </iframe></p>

<!-- ffmpeg -acodec copy -vcodec copy -ss START -t LENGTH -i ORIGINALFILE.mp4 OUTFILE.mp4 -->
<!-- START 00:27:43 -->
<!-- LENGTH 00:01:00 -->

## Example

~~~~{.python .numberLines}
## script.py
import time
import sys
wait = float(sys.argv[1])
print 'waiting for ' + str(wait) + '(s)'
time.sleep(wait)
~~~~

## A Workflow

~~~~{.console}
$ python script.py 6
waiting for 6(s)
$ edit script.py ## Add another argument ...
$ python script.py 4 1
waiting for 5(s)
~~~~

<p style="text-align: center;">No history.</p>
<br>

~~~~{.console}
$ cp script.py script-old.py
$ edit script.py ## Make some changes ...
$ cp script-old.py script-older.py
$ cp script.py script-old.py
~~~~

<p style="text-align: center;">Invent scheme for version control.</p>
<br>

##  Version Control

<p style="text-align: center;">Initialize repository.</p>

~~~~{.console}
$ git init
Initialized empty Git repository in ...
~~~~

<br>
<p style="text-align: center;">Store a version of the code.</p>

~~~~{.console}
$ git add script.py
$ git commit script.py -m "First commit."
[master (root-commit) 2f12eae] First commit
 1 files changed, 20 insertions(+), 0 deletions(-)
 create mode 100644 script.py
~~~~

## Version Control

<p style="text-align: center;">Edit and run as before.</p>

~~~~{.console}
$ edit script.py ## Add another argument ...
$ python script.py 4 4
waiting for 8(s)
~~~~

<br>
<p style="text-align: center;">Store the new version.</p>

~~~~{.console}
$ git add script.py
$ git ci script.py -m "Add another argument ..."
[master 250e0a9] Add another argument ...
 1 files changed, 4 insertions(+), 2 deletions(-)
~~~~

## Version Control

<p style="text-align: center;">History.</p>

~~~~{.console}
$ git log
250e0a989a19 Add another argument ...
2f12eaef785b First commit.
~~~~

<br>
<p style="text-align: center;">Query history.</p>

~~~~{.console}
$ git diff 2f12ea..250e0a
-wait = float(sys.argv[1]) 
+wait = float(sys.argv[1]) + \
+    float(sys.argv[2])
~~~~

## Simulation Management

<p style="text-align: center;">Version control is good, but no record of simulations.</p>

~~~~{.console}
$ python script.py 4 4 ## no record
waiting for 8(s)
~~~~

<br>
<br>
<p style="text-align: center;">Invent scheme for recording simulations.</p>

~~~~{.console}
$ ## record event
$ python script.py 4 4 > output0 
$ git add output0
$ git ci output0 -m "Adding output file."
~~~~

<br>
<p style="text-align: center;">Version control does not record events.</p>

## Sumatra

<p style="text-align: center;">Create Sumatra repository.</p>

~~~~{.console}
$ smt init sumatrademo
Sumatra project successfully set up
$ smt configure --executable=python \
    --main=script.py
~~~~

<br>
<p style="text-align: center;">Run simulation using Sumatra.</p>

~~~~{.console}
$ smt run 2 1 ## python script.py 2 1
waiting for 3.0(s)
No data produced.
Created record store
~~~~

## Sumatra

<p style="text-align: center;">View record.</p>

~~~~{.console}
$ smt list --long
----------------------------------------------
Label            : 622fbd437c4a
Timestamp        : 2013-05-08 12:07:15.8991...
Duration         : 3.02781295776
Repository       : GitRepository at /users/...
Main_File        : script.py
Version          : 250e0a989a19
Script_Arguments : 2 1
Executable       : Python (version: 2.6.6) ...
Launch_Mode      : serial
User             : Daniel Wheeler <daniel.w...
~~~~

## 

<!-- on ruth do "smtweb --allips --no-browser -p 8001" -->
<p style="text-align: center;"><iframe width="100%" height="80%"  allowfullscreen seamless src="http://129.6.153.60:8001/sumatrademo/622fbd437c4a/" frameborder="0" border="0"> </iframe></p>

## Modify Code

<p style="text-align: center;">```import fipy``` to view dependencies.</p>

~~~~{.python .numberLines}
## script.py
import time
import sys

import fipy

wait = float(sys.argv[1]) + \
    float(sys.argv[2])
print 'waiting for ' + str(wait) + '(s)'
time.sleep(wait)
~~~~

## 

<p style="text-align: center;"><iframe width="100%" height="80%"  allowfullscreen seamless src="http://129.6.153.60:8001/sumatrademo/6b53762ca24e/" frameborder="0" border="0"> </iframe></p>

## Sumatra Web Interface

<p style="text-align: center;"> <http://129.6.153.60:8001/sumatrademo/> </p>

## 

<p style="text-align: center;"><iframe width="100%" height="80%" allowfullscreen seamless src="https://www.ohloh.net/p/Sumatra" frameborder="0" border="0"> </iframe></p>

## Andrew Davison

<p style="text-align: center;">Eats his own dog food.</p>
 
![](id_photo5.jpg)

<!-- ## Andrew Davison -->

<!-- He eats his own dog food -->
<!-- Based at CNRS <br> -->
<!-- Models neuronal networks <br> -->
<!-- Promotes reproducible research in neuroscience <br> -->
<!-- PyNN, NineML and NeuroML, Sumatra, Neo and Helmholtz project. -->

## Why do I like Sumatra?

<p style="text-align: center; "> <font color="red"> Doesn't require a
wholesale change to the way I work.  </font> </p>

<br> <p style="text-align: center; "> This </p>

~~~~{.console}
$ python script.py 3 2
~~~~

<p style="text-align: center; "> versus this </p>

~~~~{.console}
$ smt run 3 2
~~~~

## Issues

<br>

 - Concurrency (fixed with Postgres instead of SQLite) <br><br>
 - Live inspection (kill, suspend and restart) <br><br>
 - Parallel, distributed, SGE 

## Active Research Example

<p style="text-align: center;"> <http://129.6.153.60:8000/extremefill/> </p>
<!-- <p style="text-align: center;"><iframe width="100%" height="80%"  allowfullscreen seamless src="http://129.6.153.60:8000/extremefill/" frameborder="0" border="0"> </iframe></p> -->

## IPython Notebook and Sumatra

<p style="text-align: center;"> <http://129.6.153.60:7000> </p>
<!-- <p style="text-align: center;"><iframe width="100%" height="80%"  allowfullscreen seamless src="http://129.6.153.60:7000" frameborder="0" border="0"> </iframe></p> -->

## Why is IPython Notebook a Big Deal?

<br>
<p style="text-align: center; "> <font color="red"> Embed live code with documentation on the web!!! </font> </p>

<br> <br>
<p style="text-align: center; "> Dynamic, not static </p>

<br> <br>
<p style="text-align: center; "> but sometimes we need static </p>

## Blogging

<p style="text-align: center;"> <http://wd15.github.io/2013/05/07/extremefill2d/> </p>
<!-- <p style="text-align: center;"><iframe width="100%" height="80%" allowfullscreen seamless src="http://wd15.github.io/2013/05/07/extremefill2d/" frameborder="0" border="0"> </iframe></p> -->

## API

~~~~{.python .numberLines}
import sumatra as smt

project = smt.load_project()
record = project.new_record(parameters,
                            main_file, 
                            reason)
record.tags.add('tag')
runMySimulation(parameters)
project.add_record(record)
project.save()
~~~~

## Future Work

 - Postgres patch and database configuration. <br><br>
 - Live inspection (kill, suspend and restart). <br><br>
 - Web interface improvements (URL filtering instead of AJAX) <br><br>
 - Testing (close integration with Buildbot). <br><br>
 - Distributed?

 
 
