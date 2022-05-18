# Command Line Interface for Twingate

A simple command line interface for Twingate

## How to use it

1. Clone this repository
2. Authenticate (you can pass a Session Name or let it generate one at random):

```
python ./tgcli.py auth login -r "https://xxxx.twingate.com/api/graphql/" -a "my twingate API token"
```

3. Check CLI Help to look at available Commands:

```
python ./tgcli.py -h
```

4. Check CLI Help to look at available subcommands for a given command:

```
python ./tgcli.py auth -h
```

5. Check CLI Help to look at available parameters for a given subcommand:
```
python ./tgcli.py auth login -h
```

## Things to know:

Before you can run any of the commands, you need to **authenticate** using *python ./tgcli.py auth login*:

```
python ./tgcli.py auth login -r "https://xxxx.twingate.com/api/graphql/" -a "my twingate API token"
```

The **authentication token** along with the **URL** in the authentication call are **stored locally** and **do not need to be passed as parameters beyond the first authentication call**.

The **Session Name** needs to be passed in all calls (it serves to retrieve the URL and Authentication Token dynamically)

Apart from the initial authentication call, each call should contain **at least 1 option**: **-s** (**-s** is used to specify the **Session Name**.)

The output format can be set to CSV, DF (DataFrame) or JSON (Default) by using the -f option in addition to the -s option


## Commands & Subcommands Currently Available:

* Twingate CLI:

  * auth
    * login: create a session
    * logout: revoke a session
    * list: list existing sessions

  * device
    * list

  * connector
    * list
    
## Examples
```
# Authenticate
python ./tgcli.py auth login -r "https://xxxx.twingate.com/api/graphql/" -a "my twingate API token"
```

```
# List all devices (and display as Json (Default))
python ./tgcli.py -s RedPeacock device list
```

```
# List all devices (and display as DataFrame)
python ./tgcli.py -s RedPeacock -f DF device list
```

```
# List all devices (and display as CSV)
python ./tgcli.py -s RedPeacock -f CSV device list
```


## TO DO