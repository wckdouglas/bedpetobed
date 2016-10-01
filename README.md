This package install a script to convert bedpe file to bed file

To install:
```
pip install git+https://github.com/wckdouglas/pileup2bed.git
```

```
usage: bedpe_to_bed.py [-h] -i I [-o O] [--min MIN] [--max MAX]

To convert bedpe file to bed file

optional arguments:
  -h, --help  show this help message and exit
  -i I        Input bedpe file, must have no unmapped bedpe record (use:
              /dev/stdin as stdin)
  -o O        Output bed file (default: stdout)
  --min MIN   Minimum length of fragment (default = 10)
  --max MAX   Maximum length of fragment (default = 10000)
```
