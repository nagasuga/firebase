# Firebase

Python library to use Firebase


# Install

```
pip install https://github.com/nagasuga/firebase.git
```


# Usage

## Instantiate

    ```
    from firebase import Firebase
    firebase = Firebase('https://<project_name>.firebaseio.com')
    ```

## PUT new data

    ```
    resp = self.firebase.put('user/john', data={'John': {'last': 'Doe', 'first': 'John'}, 'Jeff': {'last': 'Nagasuga', 'first': 'Jeff'}})

    print(resp.status_code)
    >>> 200
    print(resp.text)
    >>> {"Jeff":{"first":"Jeff","last":"Nagasuga"},"John":{"first":"John","last":"Doe"}}
    ```


## GET data

    ```
    resp = self.firebase.get('user/john', params={'print': 'pretty'})
    print(resp.status_code)
    >>> 200

    print(resp.text)
    >>>
    {
      "Jeff" : {
        "first" : "Jeff",
        "last" : "Nagasuga"
      },
      "John" : {
        "first" : "John",
        "last" : "Doe"
      }
    }
    ```
