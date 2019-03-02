# bruteforcingWithPython
example/test project that brute forces a zip password from a list

`setps.sh` tut folgendes:
* eine Datei wird angelegt und ein text hinein geschrieben
* jene Datei wird mit zip komprimiert und mit einem Passwort versehen
* die ursprüngliche Datei wird gelöscht

`main.py` tut folgendes:
* `passwortliste.txt` wird zeilenweise durchgegangen
* bei jedem Durchgang wird versucht, das komprimierte, passwortgeschützte Archiv zu öffnen und dabei der Zeileninhalt als Passwort verwendet.

um das Projekt zu testen, checke es aus und führe folgendes aus:

```bash
./setup.sh
./main.py
```
