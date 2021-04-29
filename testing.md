# Testing

[back to README.md file](https://github.com/Gregory4321/cooks_finest/blob/master/README.md)

## Table of Contents:

- [Validators](#validators)
  - [W3C Validators](#w3c-validators)
  - [JSHint Validator](#jshint-validator)
  - [pylint-django](#pylint-django)
  - [Markdown](#markdown)
- [User Story Testing](#user-story-testing)
- [Manual Testing](#manual-testing)
  - [Dev Tools](#dev-tools)
- [User Testing](#user-testing)

---

## Validators

This project was put through vigorous testing. Throughout development, I manually tested along the way as I built the website to identify any bugs, and then once deployed, I enhanced the testing process using automatic testing in the form of validators.

### W3C Validators

The W3C Markup Validator and W3C CSS Validator Services were used to validate the code on all of the pages across all apps, and to make sure that there were no syntax errors in the project.

- [W3C Markup Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

#### CSS

All css files passed through the validator with no errors.

[CSS Validation Passed](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/testing_images/css-pass.png)

#### HTML

When running the html code through the validator there appeared to be a pattern of reoccurring errors. These errors were flagged from the use of Django templating logic in the html code, so these errors could be overlooked as they were not a true error.

[HTML Extending base error](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/testing_images/base-temp-error.png)

[HTML Django template error 1](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/testing_images/temp-error1.png)

[HTML Django template error 2](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/testing_images/temp-error2.png)

[HTML Django template error 3](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/testing_images/temp-error3.png)

#### JavaScript

All js files were tested automatically using JSHint. No errors were given from this, just advice on missing semicolons and warnings of let being available in ES6. Other than this minor issues, all js files and scripts passed.

[JS Hint Warning 1](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/testing_images/jshint-warning1.png)

[JS Hint Warning 2](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/testing_images/jshint-warning2.png)

#### Python

The pylint-django extension was installed to the workspace through the command line. This was a great tool to check that all python code had no errors, and over come any code that was tripping up due to Django syntax. I had to create a settings.json file to load the plugs of pyint-django, enabling it to work properly. This straight away resolved some of the issues I had appearing in Django syntax. The special character must be escaped error was removed, and the Class ‘’ has no ‘objects’ member was resolved for all of these occurences.

[Special Escape Warning](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/testing_images/special-escape.png)

[No Object Warning](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/testing_images/no-object.png)

It also indicated simple errors that were highlighted due to pylint-django requirements. These were easily rectified by executing what it suggested.

[Missing DOC string Warning](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/testing_images/missing-docstg.png)

#### Markdown

To conform with markdown requirements I installed the markdown-lint extension. This was another great tool for ensuring all markdown content conformed and its syntax was correct. It indicated some errors that were not there before. I know these errors were void as I used them in my previous project and were taken from the markdown GitHub, so creating a markdownlint.json file, I was able to disable these errors.

[Markdownlint File](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/testing_images/markdown.png)

---
