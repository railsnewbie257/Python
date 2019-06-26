Installed here: C:\Users\pihpj\AppData\Local\Continuum\anaconda3
<br>
<br>
Download: https://www.anaconda.com/distribution/
          https://docs.anaconda.com/anaconda/install/windows/#
<br>
<br>
<br>
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/

To <b>SETUP</b> an environment

<pre>
conda search "^python$"  <em>#check available versions of Python</em>

conda update conda

conda create -n <em>deeplearning</em> python=<em>3.7</em> anaconda
</pre>

To <b>INSTALL</b> a package

<pre>
conda install -n <em>deeplearning</em> <em>packageName</em>
</pre>

To <b>DELETE</b> an environment

<pre>
conda remove -n <em>deeplearning</em> -all
</pre>

<br>
<br>
[anaconda.org dashboard](https://anaconda.org/railsnewbie257/dashboard)
