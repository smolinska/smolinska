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


### On windows
Get compiled **Pillow** from http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
download .whl file than do `pip install C:\path_to.whl`

```
pip install rjsmin rcssmin --install-option="--without-c-extensions"
```

##Development
```bash
git clone git@bitbucket.org:alpakara/django-sites.git
git submodule init
git submodule update
```

Fixtures:
- `python manage.py load`
- `python manage.py save`


[Get Yarn](https://yarnpkg.com/en/docs/install#linux-tab)
``` bash
sudo yarn global add bower gulp-cli coffee-script
yarn install
bower install

mkvirtualenv rybitwy --python=`which python3`
pip install -r requirements.txt

./manage.py migrate
./manage.py load
./manage.py make_gallery

gulp
```

To create example galeries run: `python manage.py make_gallery` (useful for working on UI)



