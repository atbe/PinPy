# PinPy
A simple Python client for <a href="https://developers.pinterest.com/docs/api/overview/" target="_blank">Pinterest API</a>

[Click here for the documentation](https://atbe.github.io/pinpy/docs/_build/html/#)

>License: Apache License v2; see LICENSE file

## Installation

> Note: Supports Python 3.6+

Clone this package, Install it locally
```
git clone git@github.com:atbe/pinpy.git
cd pinpy
pip install -e .
```

## Basic Use

Instantiating a client is simple:

```pydocstring
>>> import pinpy

# place your actual access tokens in the fields
>>> client = pinpy.API(access_token='', v3_access_token='')
>>> client.get_me()
```

## Advanced Usage

The client can interface with both the public `v1` API and the mobile `v3` API (which contains a lot more endpoints)

### Checking a users followers

```pydocstring
>>> import pinpy

# place your actual access tokens in the fields
>>> client = pinpy.API(access_token='', v3_access_token='')
>>> followers = client.get_user_followers_v3('abeahmed2')
>>> for follower in followers: print(follower['username'])
nexusfool
```

**More to come**
