# bruteforcingWithPython
example/test project that brute forces a zip password from a list

in `setps.sh` are the steps to create a file and zip it to a password protected archive. After that the file is deleted

in `setup.sh` the steps are run with predifined password (passwort)

to test run 

```bash
./setup.sh
./main.py
```

the main.py reads from passwortliste.txt and tries every line as a password.
