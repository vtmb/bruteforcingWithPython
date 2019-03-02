echo "erstelle geheim.txt und erstelle passwortgeschütztes zip archiv mit dem passwort passwort"
touch geheim.txt
echo "mein geheimer text" > geheim.txt
zip -e passwortgeschuetzt.zip geheim.txt
rm geheim.txt
echo "fertig"
