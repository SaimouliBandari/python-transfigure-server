# python-transfigure-server

### Commands

1. pip3 install -t dependencies -r requirements.txt
2. (cd dependencies; zip ../{name of ur application}.zip -r .)
3. zip {name of ur application}.zip -u main.py
4. zip {name of ur application}.zip -u src/**/**

### Generating requirements.txt file from existing packages.
1. pip freeze > requirements.txt

### Removal of exiting dependencies
1. pip freeze | xargs pip uninstall -y // to remove existing packages.
