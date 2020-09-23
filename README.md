# universetech-lotterydraw

## Installation

OS X & Linux:

```
# cd to your repos dir
git clone https://github.com/j3ygithub/universetech-lotterydraw
cd universetech-lotterydraw
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows:

```
# cd to your repos dir
git clone https://github.com/j3ygithub/universetech-lotterydraw
cd universetech-lotterydraw
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Initialization
```
# cd to the repo root
python onefake/manage.py makemigrations
python onefake/manage.py migrate
python onefake/manage.py createlottery
python onefake/manage.py runserver

python twofake/manage.py makemigrations
python twofake/manage.py migrate
python twofake/manage.py createlottery
python twofake/manage.py runserver

python lotterydraw/manage.py makemigrations
python lotterydraw/manage.py migrate
python lotterydraw/manage.py createlottery
python lotterydraw/manage.py runserver
```

Update Data
```
# cd to the repo root
python onefake/manage.py updatelottery
python twofake/manage.py updatelottery
python lotterydraw/manage.py updatelottery
```

## Meta

Jimmy Lin <b00502013@gmail.com>

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/j3ygithub/](https://github.com/j3ygithub/)

## Contributing

1. Fork it (<https://github.com/j3ygithub/universetech-lotterydraw/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
