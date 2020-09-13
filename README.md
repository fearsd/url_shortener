# url_shortener

This project is backend of the url shortener service. The frontend is located [there](https://github.com/fearsd/url_shortener_front)

## Steps to run

`$ git clone https://github.com/fearsd/url_shortener.git`<br />
`$ cd url_shortener`<br />
`$ python3 -m virtualenv venv`<br />
`$ source venv/bin/activate`<br />
`$ pip install -r requirements.txt`<br />
`$ python manage.py migrate`<br />
`$ python manage.py runserver`<br />