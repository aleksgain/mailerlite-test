#!/usr/bin/env python3

import json, socket, requests, urllib.request, time, sqlite3

def main():
    while True:
        update()
        time.sleep(60)

def update():
    SQL = sqlite3.connect('/database/ip.db')
    database = SQL.cursor()
    database.execute("CREATE TABLE IF NOT EXISTS ip (timestamp integer PRIMARY KEY, city text, region text, country_name text, cont_name text, \
                        zip integer, lat integer, lon integer, language text, flag text, emoji text, phone_code integer)")
    ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    ip_url = 'http://api.ipstack.com/'+ip+'?access_key=9c4f70e64a64af13e587002fda3d020e&format=1'
    result = json.loads((requests.get(ip_url)).text)
    timestamp = int(time.time())
    city = result['city']
    region = result['region_name']
    country_name = result['country_name']
    cont_name = result['continent_name']
    zip = result['zip']
    lat = result['latitude']
    lon = result['longitude']
    language = result['location']['languages'][0]['name']
    flag = result['location']['country_flag']
    emoji = result['location']['country_flag_emoji']
    phone_code = result['location']['calling_code']
    database.execute("INSERT INTO ip (timestamp, city, region, country_name, cont_name, zip, lat, lon, language, flag, emoji, phone_code)" \
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (timestamp, city, region, country_name, cont_name, zip, lat, lon, language, flag, emoji, phone_code))
    SQL.commit()
    SQL.close()

if __name__ == "__main__":
    main()

