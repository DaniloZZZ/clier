Use this package to create an interactive cli app for some funcions 


## Usage

Use `clier.command` decorator to add a funcion(command) to cli. Use `cli.start` to start listening input commands.

## Command interface 

`help` to display info about commands generated from docstdings.

Use funcion name to call from cli and pass params separated by spaces

## Arguments conversion

Arguments annotated with types are converted to this type from str.

Use the following syntax for this.
```python
def factorial(x: int):
    ...

```
