# VestaCP-WP-DO
This project launches a VestaCP with Wordpress installed on Digital Ocean's $5/mo Droplet.<br>
_Cheaper and Faster than WPEngine. Way faster than ancient shared hosting providers like GoDaddy or Hostgator etc._

VestaCP is a very efficient, free Web Server Control Panel, a free/lighter alternative to cPanel.<br>
Comes with side by side Nginx/Apache and lots of preconfigured packages out of the box.<br>
It surprisingly runs vert well on $5/mo standard DO droplet.
http://vestacp.com/

After Vesta is installed, script changes default admin password and turns of unnecessary access to ports like MySQL and ICMP from outside.

Then downloads WordPress and shows you the login URL. There is a commented out section where you can further customize WordPress options.<br>

"app.py" contains Digital Ocean's Droplet sections.<br> 
_You can get it from https://cloud.digitalocean.com/account/api/tokens_<br>
"provision" file contains Bash scripts that gets issues within the OS after its launched.

This script could get hundreds of customization/improvement. If you'd like to contribute please send a pull request.
