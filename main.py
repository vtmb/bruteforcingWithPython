#! /usr/local/opt/python/bin/python3.7

from zipfile import ZipFile


def extractZipFile(zipfile, password):
    try:
        zf = ZipFile(zipfile)
        password_bytes = bytes(password, "utf-8")
        zf.extractall(pwd=password_bytes)
        return password
    except:
        return


passfile = open("passwortliste.txt", "r")

for line in passfile.readlines():
    password = line.strip("\n")
    guess = extractZipFile("passwortgeschuetzt.zip", password)
    if guess:
        print("password found: {0}".format(guess))
