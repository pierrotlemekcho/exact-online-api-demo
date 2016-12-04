# Exact online api demo
## Instalation steps

```bash

git clone https://github.com/alexBaizeau/exact-online-api-demo.git
cd exact-online-api-demo
virtualenv env
. ./env/bin/activate
pip install -r requirements.txt
cp config.ini.sample config.ini
```


## First time user
Make sure that you have an app here https://apps.exactonline.com/be/fr-BE/Manage if not create a test one
voir la nationalité
That's where the client id , secret and url are

```bash
python test_api.py setup --base-url=https://www.mycompany.com --client-id={XXXXXX-xxxx-xxxx-xxxx-XXXXXXXX} --client-secret=XXXXX
```

This step only need to be run once!!
Open `config.ini` to see the results


## Demo

```bash
python test_api.py demo
```
##Merci ALEX
