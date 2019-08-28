# Semantive reqruitment task documentation
## Author: Jakub Pawłowski

###  Shortcuts:

1. [ How to run ](#r)
1. [ Commit order ](#o)
1. [ Check order status ](#c)
1. [ Export ](#e)
1. [ Donwload ](#d)

<a name="r"></a>
# How to run

Make sure you are in Semanvite project directory and run in a console:
<pre><code class="sh">
sudo docker-compose build
sudo docker-compose up
</code></pre>

If container build succed, you can try Hello Semantive! homepage:
http://0.0.0.0:5000/

<a name="o"></a>
# Commit order

To let service scrap resources from website, just make an order:

http://0.0.0.0:5000/order/ _WEBSITE_

where _WEBSITE_ means web address with http://

##### Try this examples:

- http://0.0.0.0:5000/order/https://www.github.com/
- http://0.0.0.0:5000/order/https://en.wikipedia.org/wiki/Website
- http://0.0.0.0:5000/order/https://www.semantive.pl/

<a name="c"></a>
# Check order status

Service answers:

- starting : service just started to process your order
- in progress : service is still working at it
- finished : resources from website are already in database

http://0.0.0.0:5000/order/ _WEBSITE_

- where _WEBSITE_ means web address with http://

##### Try this examples:

- http://0.0.0.0:5000/order/https://www.github.com/
- http://0.0.0.0:5000/order/https://en.wikipedia.org/wiki/Website
- http://0.0.0.0:5000/order/https://www.semantive.pl/

<a name="e"></a>
# Export

Funcion display resources in a two formats:

- json
- csv

http://0.0.0.0:5000/export/ _FORMAT_ / _WEBSITE_

- where _WEBSITE_ means web address with http://
**if value missed**, service returns **all data**
- where _FORMAT_ json or csv

##### Try this examples:

- http://0.0.0.0:5000/export/json
- http://0.0.0.0:5000/export/csv

- http://0.0.0.0:5000/export/json/https://www.github.com/

- http://0.0.0.0:5000/export/json/https://en.wikipedia.org/wiki/Website

- http://0.0.0.0:5000/export/json/https://www.semantive.pl/
- http://0.0.0.0:5000/export/csv/https://www.github.com/
- http://0.0.0.0:5000/export/csv/https://en.wikipedia.org/wiki/Website
- http://0.0.0.0:5000/export/csv/https://www.semantive.pl/


<a name="e"></a>
# Download

Funcion is very simillar to *export*. *Downlaod* funcion allows to **download** resources in a two formats:

- json
- csv

http://0.0.0.0:5000/download/ _FORMAT_ / _WEBSITE_

- where _WEBSITE_ means web address with http://
**if value missed**, service returns **all data**
- where _FORMAT_ json or csv


##### Try this examples:

- http://0.0.0.0:5000/download/json
- http://0.0.0.0:5000/download/csv

- http://0.0.0.0:5000/download/json/https://www.github.com/
- http://0.0.0.0:5000/download/json/https://en.wikipedia.org/wiki/Website
- http://0.0.0.0:5000/download/json/https://www.semantive.pl/

- http://0.0.0.0:5000/download/csv/https://www.github.com/
- http://0.0.0.0:5000/download/csv/https://en.wikipedia.org/wiki/Website
- http://0.0.0.0:5000/download/csv/https://www.semantive.pl/