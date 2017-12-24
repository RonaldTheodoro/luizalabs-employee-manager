# Luizalabs Employee Manager

Desafio tecnico do Luizalabs para a vaga de desenvolvedor python

## Como desenvolver:

1. Clone o repositorio
2. Crie um virtualenv com python 3.6
3. Ative o virtualenv
4. Instale as dependencias
5. Configure a instancia com o .env
6. Execute os testes

```console
git clone https://ronaldtheodoro@bitbucket.org/ronaldtheodoro/luizalabs-employee-manager.git
cd luizalabs-employee-manager
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Instale o [Heroku Toolbelt](https://devcenter.heroku.com/articles/heroku-cli)
2. Instale o plugin [heroku-config](https://github.com/xavdid/heroku-config)
3. Crie um instancia no heroku
4. Envie as configurações para o heroku
5. Defina uma SECRET_KEY para a instancia
6. Defina DEBUG=False
7. Envie o codigo para o heroku

```console
heroku create minhainstancia
heroku plugins:install heroku-config
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
git push heroku master --force
```