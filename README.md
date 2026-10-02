# server-load-check

A small Python automation script I wrote while learning Python for a
DevOps Trainee role.

## What it does

Takes a server name and a load figure, validates that the number is real,
decides a status, then loops over a whole fleet of servers and reports
each one.

## Example

    $ python3 server-load-check.py
    Enter your name: diwakar
    Enter your server name: web
    WEB
    Enter server total number of people: 400
    400.0
    WEB: Balanced
    WEB is in the list

    --- fleet report ---
    WEB > Low
    FORM > High
    WEB -01 > High

## Run it

    python3 server-load-check.py

Non-interactive, the way a pipeline would call it:

    printf 'ci\nWEB\n300\n' | python3 server-load-check.py

## How it works

    ask input
      -> clean it            .upper()
      -> validate it         try / except ValueError
      -> decide              if / elif / else
      -> report              f-string
      -> repeat              for loop over (name, load) pairs

## What I practised here

| Skill | Where it shows up |
|---|---|
| `input()` and `float()` conversion | reading the load figure |
| String cleaning | `.upper()` so `web` and `WEB` match |
| Error handling | `try / except ValueError` + `exit()` |
| Decisions | `if / elif / else` in `check_server()` |
| Functions and `return` | one function, many servers |
| Lists of tuples | `("WEB", 100)` pairs |
| List comprehension | pulling names out of the pairs |
| Loop unpacking | `for server_name, server_load in servers` |
| f-strings | the report lines |

## Status rules

    load <= 200   ->  Low
    load >= 1000  ->  High
    otherwise     ->  Balanced
