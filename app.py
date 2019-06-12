#!/usr/bin/python
import digitalocean, time


# Enter your DO API Token Below. You can get it from https://cloud.digitalocean.com/account/api/tokens
token = ""

manager = digitalocean.Manager(token=token)

# This is Digital Ocean Droplet's hostname, usually your website's name. E.g. mysite.com
hostname = raw_input("Please Enter the hostname...\n")

with open("provision", "r") as provisioning:
        data = provisioning.read().replace('--hostname', '--hostname ' + hostname)


droplet = digitalocean.Droplet(token=token,
                               name=hostname,
                               region='nyc3', # New York 2
                               image='ubuntu-18-04-x64',
                               size_slug='512mb',  # 512MB
                               user_data=data,
                               #ssh_keys=[16588118], # You can add SSH key's ID here. You need to describe to get it.
                               backups=True)

try:
    droplet.create()
    print ("\nWaiting 10 seconds for " + hostname + " to come up...")
    time.sleep(10)
    load = droplet.load()
    print ("\nServer Launched...\n\nWeb Address: https://" + load.ip_address + ":8083\n Hostname: " + hostname)
    #droplet.destroy()

except Exception as e:
    droplet.destroy()
    print ("\nThere was an ERROR.\n Open a GitHub issue and provide below information :")
    print (e)
