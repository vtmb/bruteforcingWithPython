#!/usr/bin/expect

spawn ./steps.sh

expect "Enter password:"
send "passwort\r"
expect "Verify password:"
send "passwort\r"
expect elf
