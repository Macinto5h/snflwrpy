# snflwrpy

Visually demonstrates the function of sorting algorithms using Vogel's Fibonacci model of a Fermat spiral.

## Development

### Starting application
To start the application run
```bash
poetry run start [options]
```
To see available options add the argument `--help`.

### Testing
To perform tests run
```bash
poetry run pytest
```

To perform tests with coverage stats run
```bash
poetry run pytest --cov=snflwrpy
```

### Linting
To lint the source code along with the test suites run
```bash
poetry run pylint ./snflwrpy ./tests
```
