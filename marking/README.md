# How to run auto-tester

## Prepare

1. Download assignment zip file from D2L
2. Place zip file in the same folder as the root folder
   - say `a3-d2l.zip`
   
## Running

```bash
mkdir a3out
cp -R a3/java_files test_cases a3out
DEBUG_1181=1 python3 -m bin.a3 a3-d2l.zip a3out
```

### Extra command flags you can use

```bash
# Only extract the D2L zip file (skip compile and test)
DEBUG_1181=1 python3 -m bin.a3 -E a3-d2l.zip a3out 

# Skip compile and extract (useful if you modify a student's java file)
DEBUG_1181=1 python3 -m bin.a3 -c -e a3-d2l.zip a3out 

# Test a specific student (provide the student's folder name)
# - this can be use with -c -e
DEBUG_1181=1 python3 -m bin.a3 a3-d2l.zip a3out Lobsang_Dhargay
DEBUG_1181=1 python3 -m bin.a3 -c -e a3-d2l.zip a3out Lobsang_Dhargay
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
python3 -m common.lsCompileErrors <root dir>/marking
```

to print out all students with compilation issues. 
Take a few minutes to fix anything trivial. 
Make a note in `marking/evaluation` to take marks off.
After you fix the code, you may want to turn `skitExtract` 
to `True` in `markall.py` to avoid overwriting your changes.

