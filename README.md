Contains a single Python script that was used on 2012-04-23 to put telegraph.co.uk metadata onto various objects in Fluidinfo.

What it does
------------

The `dataset` variable in `telegraph.py` holds a list of dicts. Each dict contains `about` and `data`:

  `about`: a list of about values for Fluidinfo objects.
  `data`: a string (a JSON dump of a dict) to be put onto each of the about values

Once the data is on all the about values, anyone using the latest version
of the Fluidinfo Chrome extension will see the `data` pop up (formatted
into a list of Telegraph.co.uk links) if they visit any of the `about`
values or select text containing one of the about value. So the about lists
each contain a phrase (e.g., `abu qatada`) and a set of URLs. This gives
the two ways to trigger the display of the relevant Telegraph links. To see
the information pop up, you'll need to be following telegraph.co.uk on
Fluidinfo.com (i.e., have a username/follows tag on the Fluidinfo object
whose about value is telegraph.co.uk).

Running
-------

In a virtualenv:

    $ pip install -r requirements.txt
    $ export FLUIDINFO_TELEGRAPH_PASSWORD=<password>  # ask Terry for this.
    $ python telegraph.py
