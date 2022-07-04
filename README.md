# vogel-sorter

Visually demonstrates the function of sorting algorithms using Vogel's Model.

This project is currently hosted on GitHub.  This is not ideal; GitHub is a
proprietary, trade-secret system that is not Free and Open Souce Software
(FOSS).  We are deeply concerned about using a proprietary system like GitHub
to develop our FOSS project. We urge you to read about the
[Give up GitHub](https://GiveUpGitHub.org) campaign from
[the Software Freedom Conservancy](https://sfconservancy.org) to understand
some of the reasons why GitHub is not a good place to host FOSS projects.

Any use of this project's code by GitHub Copilot, past or present, is done
without our permission.  We do not consent to GitHub's use of this project's
code in Copilot.

![Logo of the GiveUpGitHub campaign](https://sfconservancy.org/img/GiveUpGitHub.png)

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
