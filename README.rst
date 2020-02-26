aioworkers-vault
=====================

.. image:: https://img.shields.io/pypi/pyversions/aioworkers-vault.svg
  :target: https://pypi.python.org/pypi/aioworkers-vault
  :alt: Python versions

.. image:: https://img.shields.io/pypi/v/aioworkers-vault.svg
  :target: https://pypi.python.org/pypi/aioworkers-vault


Use
---

.. code-block:: yaml

    a:
      secret: TARGET

    vault:
      servers:
        a:
          address: http://localhost:8200
          namespace: myproject/prod
          token: my_super_secret_token
        b:
          address: https://localhost:8200
          namespace: myproject/prod
          token_file: /path/to/my_super_secret_token
      secrets:
        - server: a
          type: kv
          name: my_secret
          values:
            field: a.secret
        - server: a
          type: kv-v2
          name: my_secret2
          values:
            field: a.secret


Development
-----------

Install dev requirements:


.. code-block:: shell

    pipenv install --dev --skip-lock


Run tests:

.. code-block:: shell

    pipenv run pytest
