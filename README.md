# vogel-sorter

Visually demonstrates the function of sorting algorithms using Vogel's Model.

## Development

### Starting application
To start the application run
```bash
poetry run python ./vogel_sorter/vogel_cli.py
```
with the arguments desired. To see available options add the argument `--help`.

### Testing
To perform tests run
```bash
poetry run pytest
```

To perform tests with coverage stats run
```bash
poetry run pytest --cov=vogel_sorter
```

### Linting
To lint the source code along with the test suites run
```bash
poetry run pylint ./vogel_sorter ./tests
```
