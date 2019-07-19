# Junior DevOps Engineer challenge

Hi! Please see my solution to the challenge below :)


# Vagrant

VM is based on **Ubuntu 18.04** and includes a Docker container running the script within with exported database available on host machine

# Ansible

A very simple rulebook takes care of the open file limit by adjusting the PAM  nofile limit to an arbitrary number of **39693561**

# Python Script

Python script is querying [Ident.Me](https://ident.me) for external IP (so works in case of NAT) and parsing the [FreeGeoIP](https://freegeoip.net/) **API** for the location information that is then dumped from the JSON to an SQLite3 database. Script is on perpetual schedule with 1 minute pause between parses.

# Docker

Script is packed into a Docker container based on official **Python3-slim** image and has the database share exported to the host. 


*CHEERS!*