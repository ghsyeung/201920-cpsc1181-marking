# How to run auto-tester

## Prepare

1. Download assignment zip file from D2L
2. Place zip file in the same folder as the scripts folder
   - say `a1/a1-d2l.zip`
   
## Running

```bash
DEBUG_1181=1 python3 scripts/markall.py a1-d2l.zip . 
```

With `DEBUG` mode enabled, you'll see a lot of print-outs.


## Where to look

`marking` contains all the auto-testing relevant information
- `output` folder contains all the output of each test case
- `compile.out` contains any compilation error
- `validation.out` contains the information of all test results
  - look here to see how many test cases passed and failed
- `evaluation` is the file you should will create
  - includes the marking breakdown with the student's score
  - includes a section of your comments to the student
  - includes a section of your comments to me about the student
  
`scratch` contains all the extracted source code and compilation output
- you probably need to read the student's code here

Use the `lsCompileErrors` tool

```bash
python3 scripts/lsCompileErrors.py <root dir>/marking
```

to print out all students with compilation issues. 
Take a few minutes to fix anything trivial. 
Make a note in `marking/evaluation` to take marks off.
After you fix the code, you may want to turn `skitExtract` 
to `True` in `markall.py` to avoid overwriting your changes.

