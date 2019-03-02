# bruteforcingWithPython
example/test project that brute forces a zip password from a list

`setps.sh` tut folgendes:
* eine datei wird angelegt und ein text hinein geschrieben
* jene datei wird mit zip komprimiert und mit einem Passwort versehen
* die ursprüngliche Datei wird gelöscht

`main.py` tut folgendes:
* `passwortliste.txt` wird zeilenweise durchgegangen
* bei jedem Durchgang wird das komprimierte, passwortgeschützte Archiv geöffnet und die Zeile als Passwort eingegeben.

um das Projekt zu testen, checke es aus und führe folgendes aus:

```bash
./setup.sh
./main.py
```

