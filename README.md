# README

This repository holds bare django project on branch `master`. New sites should start from it.
Sites are written in Python's web framework - Django and works like simple CMS.

## Branches holding websites:

- groz -> www.groz.com.pl
- sliczna36 -> www.sliczna36.pl

### Other

- tool-colorpickers - For client who can't decide about colors. Cherry-pick it and customize.

## Scripts

- `install.sh` used to deploy website
- `apply_fixtures_on_prod.sh` creates fixture out of content edited via admin panel, uploads it and executes

Implemented stuff:

- Galleries
- Editable tabs and content
- Obfuscating emails after content is eddited
- Parsing `varieables.scss` so it's declarations are avaiable in JS

##Setting up ( use yarn it's much faster )
```bash
npm install -g yarn
yarn global add coffee-script bower
yarn
bower install
sudo apt-get install ruby-sass # TODO: Move to gulp

```

### On windows
Get compiled **Pillow** from http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
download .whl file than do `pip install C:\path_to.whl`

```
pip install rjsmin rcssmin --install-option="--without-c-extensions"
```

##Development
Fixtures:
- `python manage.py load`
- `python manage.py save`

To create example galeries run: `python manage.py make_gallery` (useful for working on UI)



