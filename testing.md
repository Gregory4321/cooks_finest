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

## User Stories Testing

### Viewing and Navigation

1. As a site user, I want to be able to view a list of products so that I can select a product(s) to purchase.

- A user is presented a grid system of cards containing the products images, title, price, category and rating.

2. As a site user I want to be able to view a specific category of products so that I can quickly find products Im interested in without having to search through all products.

- A user is provided a clear navigation bar to direct them to categories of products or all products, as well as a call to action from the home page, all rendering a grid system of products clearly presented with images, their title, price, category and rating.

3. As a site user, I want to be able to view individual product details so that I can learn more about the product, seeing its image, price description and rating.

- Once a user has clicked the card of a product, a product detail page is rendered revealing all details of an individual product.

4. As a site user, I want to be able to easily pinpoint special offers so that I can save money on purchases.

- The navigation bar gives the user a direct link to take them to all special offers on the site.

### Registration and user accounts

5. As a site user, I want to be able to easily register for an account so that I can have a personal account and my own profile.

- A user is presented with a my account nav link, where the can select register from the dropdown, taking them to basic registration form.

6. As a site user, I want to be able to easily login and logout so that I can access my personal account information and securely logout.

- As like the registration link in the my account nav link, a user is presented with a link to take them to the login form. Upon logging in the are directed to their profile page. Once logged in from the same nav link, a user can click logout to then confirm on the next page and logout.

7. As a site user I want to be able to easily recover my password in the event I forget so that I can recover access to my account.

- From the login form page, a user can click a link to reset their password, giving them an input field to fill in with their email address to send a link to change their password.

8. As a site user I want to be able to receive a confirmation email after registration so that I can verify that my account registration was completed and successful.

- Upon registration to the site, a user will receive a confirmation email giving them a link to confirm their account registration.

9. As a site user I want to be able to have a personalised user profile so that I can review my previous orders, and save payment and delivery information.

- Each registered user gets their own profile page, accessible from the my account dropdown nav link. A users profile is presented in a nice collapsible accordion, separating the two sections, default delivery details and order history. Payment details are saved when a user places an order and selects save info, updating the delivery details accordingly.

10. As a site user I want to be able to subscribe to the sites newsletter so that I can stay up to date with upcoming offers.

- Unfortunately, I was not able to complete these section of the site, so there is no link to subscribe to a newsletter.

### Sorting and Searching

11. As a site user I want to be able to sort the list of available products so that I can easily establish the best priced and best rated products, and search products by category.

- Using the main navigation bar available across all pages, a user can sort products by each required field.

12. As a site user I want to be able to sort a specific category of products so that I can find the best priced and best rated product in a specific category, or sort the products in that category by name.

- On each product page, the user has access to a sort selector box that they can change the input using the dropdown to sort the selected categories products by price, rating and name.

13. As a site user I want to be able to sort multiple categories of products simultaneously so that I can find the best priced and best rated product across categories such as “cookware” or “tableware”.

- On each product page, the user has access to a sort selector box that they can change the input using the dropdown to sort the products by category.

14. As a site user I want to be able to search for a product by name or description so that I can find a specific product.

- Visible across all pages of the site, a search bar is visible for the user to enter a query, search all products names and descriptions for their queried word.

15. As a site user I want to be able to easily see what I’ve search for and the number of results so that I can quickly decide whether the product I want is available.

- After each search query, above the presented products to the left, a user can find the details of their search query and how many products match that query.

### Purchasing and Checkout

16. As a site user I want to be able to easily select the size and quantity of a product I want to purchase, if applicable so that I can ensure I select the correct size and quantity.

- A user is presented with clear input fields to select the quantity using increment and decrement buttons, and the size as a dropdown option.

17. As a site user I want to be able to view the items in my basket so that I can see what I am purchasing and the total cost.

- A user can direct to the basket page by clicking the basket icon from the navbar. Here they can clearly see each added item spread out as a table with the subtotal at the end, and then the order total at the bottom of the page.

18. As a site user I want to be able to adjust the quantity of individual items in my basket so that I can effortlessly make changes before checkout.

- From the basket page, a use can the same selector box as when adding the products quantity to change the amount of each product, clicking an update button to update the quantity.

19. As a site user I want to be able to easily enter my payment details so that I can complete my purchase with no worries.

- When a user is checking out they can enter their payment details by filling out a simple form, that will indicate any invalid inputs before submission.

20. As a site user I want to be able to view an order confirmation after checkout so that I can check I made no mistakes when checking out.

- When an order is completed, a user is directed to a checkout success page, render their order details. They can also access this page form their profile page and clicking the order number form their order history.

21. As a site user I want to be able to receive an order confirmation after secure checkout so that I can keep a record of my purchases.

- A user will receive an email confirmation containing all of their order details, as well as accessing the confirmation form their order history section of their profile.

### Admin and Store Management

22. As a store owner I want to be able to add a product so that I can add new products to my store.

- A store owner can add a product by signing in as their superuser account, clicking the my account nav link, and click product management. This will render a page with a form to add the products details and add a product to the site.

23. As a store owner I want to be able to edit a product so that I can change a products details.

- Signed in as a super user, the store owner will see an edit link in the product details from the products page and product details page. This will take them to an edit product form where they can change the details and update the product.

24. As a store owner I want to be able to delete a product so that I can delete a product that is no longer available for purchase.

- The same as the edit link, a delete link is presented to the superuser on both the products and products detail pages to delete a product. A modal popup will be initiated to conform the deletion of a product.

25. As a store owner I want to be able to add a blog post so that I can provide the site user’s with tips and trick.

- From the my account nav link, a blog management link is provided in the dropdown. This will render a page with a form to add a blog to the site.

26. As a store owner I want to be able to edit a blog post so that I can change and/or correct a blog post.

- Signed in as a super user, the store owner will see an edit link in the blog details section from the blog posts page and blog details page. This will take them to an edit blog form where they can change the details and update the blog.

27. As a store owner I want to be able to delete a blog post so that I can keep the most relevant blog posts circulating.

- The same as the edit link, a delete link is presented to the superuser on both the blog posts and blog detail pages to delete a blog. A modal popup will be initiated to conform the deletion of a blog.

---
