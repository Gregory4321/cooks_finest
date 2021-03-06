# Milestone Project 4 - Cook's Finest

View live project [here](https://cooks-finest.herokuapp.com/)

![Cook's Finest Am I Responsive image](media/readme_content/responsive.png)

Cook's Finest is an online e-commerce store, offering a collection of kitchenware for the savy home cook. User's can create their own account, saving their details for faster checkout for future purchases, but are not limited, and can make a purchase as a guest if wanted. The registered user can edit their personal details and access their shopping history. Blogs are presented for good reads, and a newsletter sign up is offered.

---

## Table of Contents

- [What does it do and what does it need to fulfill?](#what-does-it-do-and-what-does-it-need-to-fulfill)
  - [Project Goals](#project-goals)
- [User Experience](#user-experience)
  - [User Goals](#user-goals)
  - [User Stories](#user-stories)
  - [Site Owner Goals](#site-owner-goals)
- [Design](#design)
  - [Research](#research)
  - [The Five Planes of UX](#the-five-planes-of-ux)
    - [Wireframes](#wireframes)
    - [The Colour Scheme](#the-colour-scheme)
    - [Font](#font)
    - [The Logo](#the-logo)
    - [Conclusion](#conclusion)
- [Technologies Used](#technologies-used)
- [Database Structure](#database-structure)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
  - [Deployment to Heroku](#deployment-to-heroku)
- [Credits](#credits)
  - [Content](#content)
  - [Code](#code)
  - [Media](#media)
- [Acknowledgements](#acknowledgements)
- [Special Thanks](#special-thanks)
- [Disclaimer](#disclaimer)

---

## **What does it do and what does it need to fulfill?**

This is my fourth and final milestone project of Code Institute's Full-Stack Web Developer Course. The projects main requirements were to build a Django web application with the use of HTML, CSS, JavaScript and Python, and utilising a relational database, allowing users to store and manipulate data records of a particular domain. This was achieved with the user profile model, where user's can add and edit their personal details, as well as the site owner having the ability to add, edit and delete products from the site.
The use of Stripe was also a requirement, which I fulfilled with the use of a checkout system for user's to purchase their selected product(s).
IMPORTANT: The Stripe API used for handling payments is currently only for educational purposes and is not for taking real card payments. To test the payment functionality successfully, use the test card number Stripe provides, of "4242 4242 4242 4242", and then the other details chosen at random.
This project is a Django-Python web application, plugged into a PostgreSQL database, with SQLite3 used in the development, and was deployed using Heroku. The Bootstrap framework and grid system was used for effective styling across the pages of the site.

### **Project Goals**

My goal was to supply the home cook with a website where they can browse and purchase products they want for their home kitchen, and provide helpful tips and ideas on how to improve the kitchen space.

---

## **User Experience**

### User Stories

Due to the the quantity of user stories for this project, and for best practice, I compiled my user stories on a spreadsheet to make it more clear which story is related to what and who.

Please view the user stories spreadsheet [here](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/user-stories.png)

[Back to Top](#table-of-contents)

---

## **Design**

### Research

Reasearching for this project, I came across only a handful of sites that catered only for kitchen products. The design and layouts of the sites kept a clear and to-the-point attitude about them. Colours were kept very neutral as the images of the products on display were to be kept at the fore front of the site.

Sites I used for inspiration were:

- [Robert Dyas](https://www.robertdyas.co.uk/)
- [Lakeland](https://www.lakeland.co.uk/)
- [Wayfair](https://www.wayfair.co.uk/)
- [ProCook](https://www.procook.co.uk/)
- [Sous Chef](https://www.souschef.co.uk/)
- [Amazon](https://www.amazon.co.uk/)
- [Dunelm](https://www.dunelm.com/)

### The Five Planes of UX

#### The Strategy Plane

Afer researching other kitchen products and accessories websites, I noticed that the competition was spread. There were only a few sites that focused solely on kitchen equipment, where a lot of other sites were more braod, offering products not just relevant to kitchens. I wanted to create a site where the home cook could come to find the product(s) they wanted for their kitchens. I wanted an environment that purely focused on this area, and enhanced their cooking knowledge through informative blogs of ideas and tips. I wanted each user to have the ability to create theor own account, provide and securelystore their personal information, with the option to edit and remove that information, and make purchases.

#### The Scope Plane

With deciding on my app idea, and what type of user would use it, I really considered what features would be beneficail to the user, and what would make this a successful and easily useable site. I knew the main feature would be the ability to purchase a product through a secure checkout. I wanted the user to be able to easily sort and search through the products, adding product to the basket, and then having the ability to securely checkout. I also wanted the user to utilise the blog posts, learning cooking tips provided, as well as subcribing to a newsletter through entering their email address. I wanted users to be notified of their actions along the way, such as bag updates, success and error messages.

#### The Structure Plane

Once I had decided what features I wanted to include, I began the think about the structure of the site. I wanted to keep the presentation clean, and make use of margins to keep content well organised. I wanted all site users to easily search for a product, using keywords but also a sorting system to sort by category, and then each or multiple categories by sorted to meet the user's needs. I used bootstraps grid system to help clearly present the content of the pages. I wanted a nav bar that would change accordingly to whether the user was an external user or logged in user. From this, to better the user experience, I decided that upon clicking 'My Account' on the nav bar, an external user would see login and register, but a logged in user would see profile and logout. For the store owner, signed in as a superuser, would see the profile and logout options, but also product management option too. With this, the store owner would also see the option to edit and/or delete products from the individual product details page, and also from the products pages.

#### The Skeleton Plane

At this level, I really thought about how a user would navigate around the site. I wanted a clear structure throughout the site. Each page would have a fixed navbar and footer that was consistent and the ease of navigation across the site was enhanced further with breadcrumb navigation and call to action buttons. A user always needed an easy way to return home, so the use of a breadcrumb navigation would appear once the user navigated away from the home page. This also give's the user the ease of returning to the previous page(s) with ease. The call to action buttons would be used to direct the users to shop now, taking them to the all products page, or to the corresponding blog page. Here the user will find images as links to open specific blogs. There is also a call to action to open a specific special offer.

Upon opneing the website, The user would immediately see the my account text (or just the icon if on mobile) and have access to the register or login pages. These pages would present a form depending on what page the user clicked, and a link to direct them to the other if they clicked the wrong link to begin with. Regardless of which form was completed, the user is directed to the home page to encourage immediate shopping. From the homepage, the user can also clearly see the menu bar, or hamburger on smaller screens, and have access to navigate between specific product category pages of the site. The search bar provided in the navbar would further aid the user, using the keyword used and navigating to a specific area or category.
I wanted content hinting on the home page to encourage the user to scroll down the page, accessing best selling products. A back to top button would also appear across all pages that scrolled past a certain point, aiding ease of use for the user, to return to the top with a click instead of having to scroll all the way back to the top.
The user's profile page would consist of accordions to present the users details and order history in a cleaner way. This would avoid any overwhelming of content and information, and keep the area's broken up.

#### The Surface Plane

From the beginning of my research, I had discovered that e-commerce sites would be very colourful, no matter what, due to the colurful content of product images. Because of this I wanted to keep the design simple, and not have overpowering colours that would clutter the site. The volume of content of an e-commerce site could easily make a site feel too busy, so I wanted to design this site so that a user could effortlessly navigate the site. Having researched and thought over the design process thoroughly, I created a workspace on Figma. I had initially sketched ideas onto paper, so now I could start to bring them to life. I created all the pages I had planned for desktop and mobile screen sizes, clearly showing how the structure of the content would mould together on the different sizes, creating more enhanced wireframes.

Find the links to these wireframes below.

<details>

<summary>Wireframes</summary>

- Base Template
  - [Desktop View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/base-wire.png)
  - [Mobile View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/mob-base-wire.png)
- Home Page
  - [Desktop View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/home-wire.png)
  - [Mobile View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/mob-home-wire.png)
- Products Page
  - [Desktop View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/products-wire.png)
  - [Mobile View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/mob-products-wire.png)
- Individual Product Page
  - [Desktop View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/product-wire.png)
  - [Mobile View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/mob-product-wire.png)
- My Account Page
  - [Desktop View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/profile-wire.png)
  - [Mobile View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/mob-profile-wire.png)
- Login Page
  - [Desktop View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/login-wire.png)
  - [Mobile View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/mob-login-wire.png)
- Register Page
  - [Desktop View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/register-wire.png)
  - [Mobile View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/mob-register-wire.png)
- My Basket Page
  - [Desktop View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/basket-wire.png)
  - [Mobile View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/mob-basket-wire.png)
- Checkout Page
  - [Desktop View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/checkout-wire.png)
  - [Mobile View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/mob-checkout-wire.png)
- Contact Page
  - [Desktop View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/contact-wire.png)
  - [Mobile View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/mob-contact-wire.png)
- Blog Home Page
  - [Desktop View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/blog-wire.png)
  - [Mobile View](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/mob-blog-wire.png)

</details>

[Back to Top](#table-of-contents)

##### The Colour Scheme

I wanted to use monochromatic styling for this site effectively, as the strong tonal variation provides a good contrast between the areas of the page. I wanted a brighter colour to pop out from the black and white, to enhance areas of activity like call to actions buttons, the delivery banner and the back to top button. This colour scheme would prove useful as the content of the site was to potentially be bright and busy, so this monochromatic style helped to break up these areas. I found the final colours in my scheme blend well and don???t fight each other and the screen doesn???t seem too chaotic

The colours I used are:

![Colour scheme](media/readme_content/colours.png)

The primary colour, Goldenrod(yellow), was used for areas I wanted to pop out to the user, such as the delivery banner, back to top button, and text colour on hover of particular elements, as well as buttons background colour when hovered over, across pages. Using the colour tool that appears when hovering over a colour set in the style.css page, I toned down this colour to obtain the colour used for the basket icon when it is already coloured Goldenrod when there are items in the basket, giving a clear contrast for the user that their cursor is over the basket icon.

The secondary colour I chose was Black. This was to provide clear contrast when used alongside the backgound of the pages(White), and the primary colour(Goldenrod). The main nav was coloured black, with the top nav above being white, and the promotional banner below, yellow. Therefore, the text of the main nav is white, and changes to yellow when the user hoveres over it. The main buttons across the site were also coloured black, again with white text, and the yellow on hover. Text colour across the entire rest of the site is black so that it stands out against the white background. Exceptions to this include the placeholder text of the forms(#aab7c4), small sub headings, and the category and rating text of the products description (all coloured in Bootstraps text-muted class, #6c757d).

I also used Bootstraps success, danger, warning and info colours as toast colour indicators, as well as the primary class for the edit link presented to the superuser, with the delete link colour as danger.

##### Font

I decided to use one font for my site. I found a font I liked using [Google Fonts](https://fonts.google.com/), and refining the search criteria to only sans serif fonts. I found the Montserrat font, which I thought would work well as it was simple and easy to read. I found that this font stood out and was clear no matter where it was used. I included this fonts by inserting a link taken from google fonts into the head of my base.html.

##### The Logo

For this project, I decided to keep the logo as a basic h2 heading, in black font to keep a theme across the site. I wanted to use a basic design and structure for this as I felt a fancy designed logo for this site wasn't neccassarily needed, and the h2 would help with the transitioning of different screen sizes.

#### Conclusion

I kept the development of this site very close to the design from the wireframes I made during the planning stages. The end result is nearly a carbon copy of these wireframes with a few exceptons. I slightly changed the layout of the pages haveing the headings to the left rather than centered, and on the product detail page I moved the Add to Basket button to below the description. There changes were for the benefit of the user's experience and kept a nicer flow across the pages. I also was not abe to incorporate the breadcrumb navigation with the time this projcct demanded.

[Back to Top](#table-of-contents)

---

## **Technologies Used**

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5) - Language used to create the structure of the pages.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Language used to add styling across all pages.

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Language used to create interactivity across the pages.

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>) - Language used to create the back-end functionality of the app.

### Libraries, Frameworks and Editors

- [Django](https://www.djangoproject.com/) - a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

- [Bootstrap](https://getbootstrap.com/) - used as the base structure and layout of the site, using its grid system to aid responsiveness across screen sizes. Many components such as the navbar, cards and modals were used. Bootstraps inbuilt Javascript and jQuery was used for initialization of many components such as the dropdown elements, modal pop up and the navbar expand and collapse on small screens.

- [jQuery](https://jquery.com/) - utilising it's extensive library to simplify and help writing Javascript code.

- [Google Fonts](https://fonts.google.com/) - used to embed the 'Montserrat' and 'Quiksand' fonts used across the site.

- [Font Awesome](https://fontawesome.com/) - used for their free range of icons.

- [Favicon.io](https://favicon.io/) - was used to generate the favicon image.

- [Gitpod](https://www.gitpod.io/) - used as preferred choice of IDE for writing my code. Halfway through this project gitpod upgraded their IDE to [Visual Studio Code](https://code.visualstudio.com/) which I then continued using as the main IDE to write my code.

- [Git](https://git-scm.com/) - used for version control by making use of the Gitpod terminal to add, commit and push to Github.

- [Github](https://github.com) - used to host the project's repository and store the code, and linked to Heroku to push latest changes to the deployed build version.

- [Heroku](https://www.heroku.com/) - used as a hosting platform for deploying my live version of this CRUD application.

- [Unsplash](https://unsplash.com/) - used to find images for use across the site.

- [Google Images](https://google.com) - used to find images for use across the site.

### Extensions and Packages

- [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) - used as an authentification system, utilising it's templates and logics.

- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - used to format forms, automatically using Bootstrap styling.

- [Pillow](https://pillow.readthedocs.io/en/stable/) - Python Imaging Library to help store imagery into a database.

- [psycopg2](https://www.psycopg.org/docs/) - PostgreSQL database adapter for the Python.

### Databases

- [Sqlite 3](https://www.sqlite.org/index.html) - used as the database during development.

- [PostgresSQL](https://www.postgresql.org/) - used as the database for deployment, enabling it as an add on through [Heroku](https://www.heroku.com/postgres).

### Tools

- [Stripe](https://stripe.com/gb) - used as the payment infrastructure to take payments on the site.

- [Google](https://www.google.co.uk/) - used for researching various techniques, styles and information.

- [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - used for testing and debugging.

- [Figma](https://www.figma.com/) - used for creating the wireframes in the design stage.

- [Coolors](https://coolors.co/) - used to find and compare colours that complimented one another, retrieve names of colours, and showcase
  the colours on the README.md file as an image.

- [Canva](https://www.canva.com/) - used to design and create the favicon logo, and resize the product images too be all the same size.

- [Picresize](https://picresize.com/) - used to resize and crop images for better implementation, such as 25% or 50% smaller.

- [Am I Responsive](http://ami.responsivedesign.is/) - used for showing the responsiveness of the site across different screen sizes and providing the image at the top of this document.

- [Free Online HTML Formatter](https://www.freeformatter.com/html-formatter.html#ad-output) - used to format the HTML code in a neater and more organised fashion.

- [Free Online CSS Formatter](https://www.freeformatter.com/css-beautifier.html) - used to format the CSS code in a neater and more organised fashion.

- [Free Online JS Formatter](https://www.freeformatter.com/javascript-beautifier.html) - used to format the JavaScript code in a neater and more organised fashion.

[Back to Top](#table-of-contents)

---

## **Database Structure**

During the development of this Django project, I worked with the SQLite3 database, which is the default database used by Django. For deployment of this project, I changed to a PostgreSQL database, that is provided by Heroku as an add-on.

Using Django Allauth and it's default `django.contrib.auth.models`, provided me with the the **User model** used in the profile app.

The structure of the Product and Checkout apps are guided by the Code Institute's walkthrough project, **Boutique Ado**.

### Data Models

#### Profile app

##### UserProfile model

| Name             | Database Key         | Field Type           | Validation                                          |
| ---------------- | -------------------- | -------------------- | --------------------------------------------------- |
| User             | user                 | OneToOneField 'User' | on_delete=models.CASCADE                            |
| Full Name        | default_full_name    | models.CharField     | max_length=50, default='', blank=True               |
| Phone Number     | default_phone_number | models.CharField     | max_length=20, default='', blank=True               |
| Street Address 1 | street_address1      | models.CharField     | max_length=80, default='', blank=True               |
| Street Address 2 | street_address2      | models.CharField     | max_length=80, default='', blank=True               |
| Town or City     | default_town_or_city | models.CharField     | max_length=40, default='', blank=True               |
| County           | default_county       | models.CharField     | max_length=80, default='', blank=True               |
| Postcode         | default_postcode     | models.CharField     | max_length=20, default='', blank=True               |
| Country          | default_country      | models.CharField     | blank_label='Select Country', null=True, blank=True |

#### Products app

##### Category model

| Name          | Database Key  | Field Type | Validation                             |
| ------------- | ------------- | ---------- | -------------------------------------- |
| Name          | name          | CharField  | max_length=254                         |
| Friendly Name | friendly_name | CharField  | max_length=254, default='', blank=True |

##### Product model

| Name        | Database Key | Field Type          | Validation                                                    |
| ----------- | ------------ | ------------------- | ------------------------------------------------------------- |
| Category    | category     | models.ForeignKey   | 'Category', default='', blank=True, on_delete=models.SET_NULL |
| Sku         | sku          | models.CharField    | max_length=254, default='', blank=True                        |
| Name        | name         | models.CharField    | max_length=254                                                |
| Price       | price        | models.DecimalField | max_digits=6, decimal_places=2                                |
| Sizes       | has_sizes    | models.BooleanField | default=False, null=True, blank=True                          |
| Description | description  | models.TextField    |                                                               |
| Rating      | rating       | models.DecimalField | max_digits=6, decimal_places=2, null=True, blank=True         |
| Image       | image        | models.ImageField   | default='', blank=True                                        |
| Image URL   | image_url    | models.URLField     | max_length=1024, default='', blank=True                       |

#### Checkout app

##### Order model

| Name                     | Database Key    | Field Type           | Validation                                                                          |
| ------------------------ | --------------- | -------------------- | ----------------------------------------------------------------------------------- |
| Order Number             | order_number    | models.CharField     | max_length=32, null=False, editable=False                                           |
| User Profile             | user_profile    | models.ForeignKey    | UserProfile, on_delete=models.SET_NULL, null=True, blank=True,related_name='orders' |
| Full Name                | full_name       | models.CharField     | max_length=50, null=False, blank=False                                              |
| Email                    | email           | models.EmailField    | max_length=254, null=False, blank=False                                             |
| Phone Number             | phone_number    | models.CharField     | max_length=20, null=False, blank=False                                              |
| Country                  | country         | CountryField         | blank_label='Select Country \*', null=False, blank=False                            |
| Postcode                 | postcode        | models.CharField     | max_length=20, default='', blank=True                                               |
| Town or City             | town_or_city    | models.CharField     | max_length=40, null=False, blank=False                                              |
| Street Address 1         | street_address1 | models.CharField     | max_length=80, null=False, blank=False                                              |
| Street Address 2         | street_address2 | models.CharField     | max_length=80, null=False, blank=False                                              |
| County                   | county          | models.CharField     | max_length=80, default='', blank=True                                               |
| Date                     | date            | models.DateTimeField | auto_now_add=True                                                                   |
| Promotion Cost           | promotion_cost  | models.DecimalField  | max_digits=6, decimal_places=2, null=False, default=0                               |
| Order Total              | order_total     | models.DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                              |
| Grand Total              | grand_total     | models.DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                              |
| Original Basket          | original_basket | models.TextField     | null=False, blank=False, default=''                                                 |
| Stripe Payment Intent ID | stripe_pid      | models.CharField     | max_length=254, null=False, blank=False, default=''                                 |

##### Order Line Item model

| Name            | Database Key   | Field Type          | Validation                                                                         |
| --------------- | -------------- | ------------------- | ---------------------------------------------------------------------------------- |
| Order           | order          | models.ForeignKey   | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| Product         | product        | models.ForeignKey   | Product, null=False, blank=False, on_delete=models.CASCADE                         |
| Product Size    | product_size   | models.CharField    | max_length=2, default='', blank=True                                               |
| Quantity        | quantity       | models.IntegerField | null=False, blank=False, default=0                                                 |
| Line Item Total | lineitem_total | models.DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False            |

#### Blog app

##### BlogPost model

| Name         | Database Key | Field Type           | Validation                                                 |
| ------------ | ------------ | -------------------- | ---------------------------------------------------------- |
| Title        | title        | models.CharField     | max_length=254, unique=True                                |
| Date Created | created_on   | models.DateTimeField | auto_now_add=True                                          |
| Date Updated | updated_on   | models.DateTimeField | auto_now= True                                             |
| Slug         | slug         | models.SlugField     | max_length=254, unique=True                                |
| Author       | author       | models.ForeignKey    | User, on_delete= models.CASCADE, related_name='blog_posts' |
| Body         | body         | models.TextField     |                                                            |
| Image        | image        | models.ImageField    | default='', blank=True                                     |
| Image URL    | image_url    | models.URLField      | max_length=1024, default='', blank=True                    |
| Status       | status       | models.IntegerField  | choices=STATUS, default=0                                  |

#### Reiviews app

##### Product Review

| Name         | Database Key   | Field Type           | Validation                                                                                |
| ------------ | -------------- | -------------------- | ----------------------------------------------------------------------------------------- |
| Product Name | product        | models.ForeignKey    | 'products.Product', null=True, blank=True, on_delete=models.SET_NULL                      |
| User Profile | user_profile   | models.ForeignKey    | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_review' |
| Date Created | created_on     | models.DateTimeField | auto_now_add=True                                                                         |
| Rating       | review_rating  | models.CharField     | default="3"                                                                               |
| Title        | review_title   | models.CharField     | max_length=254                                                                            |
| Content      | review_content | models.TextField     | max_length=1000, null=False, blank=False, default=''                                      |

[Back to Top](#table-of-contents)

---

## **Features**

### Existing Features

Navigation Bar:

All pages consist of a fixed nav bar visible at all times. It features a search box on the left to search keywords of a products name and description, and the sites logo in the middle. To the right two icons, one to represent a dropdown menu for 'my account', and a basket total which is a clickable link to the basket page. The 'my account' dropdown reveals different options depending who the user is. If a user is not signed in, 'login' and 'register' links are offered. Once a user is signed in, a link to 'my profile' and 'logout' is offered, as well as a box telling the user who is signed in. If the user is a superuser, they will also see a 'product management' link to take them to the corresponding page. Below this 'top nav', is the main navigation of the site. Here the user can click on links opening a dropdown menu, reealing more links to specific areas and categories of the site. The entire nav is fully responsive, with the logo being removed on tablet screen sizes and below, and the main nav moving to a collapsible hamburger menu on the left. The search bar is still present, but is revealed upon clicking a search icon, to keep the site on smaller screens feeling too busy.

Footer:

As with the navigation bar, all pages consist of a page footer. Here the user can click social media icons foind in the center of the footer, taking them to the corresponding social media pages. To the left of these icons a disclaimer is displayed that the site is copyright to me, the site owner, and to the right a clickable link taking the user to the contact page.

Back to Top Button:

A back to top button is displayed to the user at the bottom right of the screen across all pages when the user scrolls down past 200px.

Landing Page:

A hero image showcases the type of products a user will find on the site. A jumbotron houses a call to action button to encourage the user to shop now, directing them to the all products page. Upon scrolling below the hero image, two cards with image backgrounds and overlaying text offer call to action buttons to the blog and special offers pages. Below this, 6 cards offer an insight of new arrivals to the site, presented as clickable card links to the products.

Products Pages:

Products can be viewed in various different ways, either as all products of the entire site, all products of a chosen category, or products of a specific sub category. Each of these pages follow the same layout and design to maintain consistency. Products are presented fully responsive cards, using Bootstraps grid system, containing the products image, as a link to the product, the products title and price, the category and rating. The category is presented as a clickable badge, taking the user to said category page. A dropdown menu is offered at the top right of the page above the products, to sort the products in different ways. : 'Price (low to high)/(high to low)', 'Name (A-Z)/(Z-A)' and 'Rating (low to high)/(high to low)' and 'Category (A-Z)/(Z-A)'. If the user is a superuser, then edit/delete buttons are offered in each product card for ease of management.

Product Details Page:

Individual products are viewed on this page, with the image to the left, and details to the right. The details are presented the saem as the products card on the products pages, along with the products description. A quantity selector box is given on this page for the user to input manually or use selector buttons (+/-) to increase/decrease the quantity of the respective product. There are two buttons below this for the user to go back to the all products page to 'Continue Shopping', or 'Add to Basket' to add the product to the user's basket.The edit/delete buttons are presented here also to only a superuser. If any products on the enitre site contain a size, then a dropdown above the quantity selector box is presented for the user to select as size. 'M' for medium is selected by default.

Review Views:
The user has the ability to add a review to a product. From the product detail page, they can click a button to reveal a dropdown of reviews for that product, being displayed with stacked cards of reviews, or an individual card saying that there are currently no reviews for this product. About this buttin, is some small text as a link for the user to add a review. Clicking this link will take the user to a 'Add Review' page where they will find a form presenting the required fields needed to submit a review.

Profile Page:

This page is accessed through the dropdown of the 'My Account' link from the navbar. HEre a user is presented with a simple accordion. The first dropdown of the accordion will be open by default, and holds a form of the users default delivery information, which will be empty for the first time, and then updated whenever an order is placed and details are entered into the checkout form. The user can also update their details here by filling in the ofrm and clicking the 'Update Information' button belwo the form. The second dropdown holds the users order history. This is presented as a simple table, showing the order number, date, items and order total. The order number is given as the forst 5 digits of the unoquie number, and can be hovered over to reveal the entire number, and clicked to take the user to that orders confirmation page.

Basket Page:

This page lists to the user everything they have added to their basket. Basic product information is shown, along with a quantity selector box for the user to ammend their order. There is an update button to update the given quantity, and a remove button to completely remove the product fromt their basket. The basket total is given at the bottom right of the page, followed by the total discount if applicable, and then the grand total. If the user has not hit the discount threshold, text is shown informing how much more the user needs to spend to get the discount. If that threshold is hit, then the logic is executed to deduct the discount from the basket total, ammending the grand total to match. There are two buttons below this, one to 'Continue Shopping' taking the user back to all products, and the other the procedd to the checkout page.

Checkout Page:

The checkout page is split into two columns.To the right is a brief order summary, giving the user a final opportunity to check thier basket. On the left, a form to enter personal and delivery information. If the user is a new user, then the form will be empty. If the user has palced an order previously, or entered their information on the profile page, then the form will be pre filled with what was entered last time. Below the form, a checkbox offers the user to save the (if any) input information to their profile, and if not logged in then links to create an account or login are presented. An input box is then found to input the users payment method. Finally, there are again two buttons, one to go back to adjust user's basket, and one to complete their order. Upon clicking 'Complete Order', a yellow overlay takes the screen with a spinning gif indicating the order is being placed.

Checkout Success Page:

This page is accessed once a user completes an order. but can also be accessed through the profile page by clicking on the order umber from their 'Order History'. Here, the user will have a summary of their order, a confiramtion message of the successfully placement of the order, and a button to check out the lastest deals, to encourage further shopping. If accessing this page through their order history, a user will be notifued that they are viewing a past confirmation.

Blog Page:

The user can access this page by clicking on the card from the home page. All users have access to view thedse blogs, enhancing user interactivity with the site. The page kept a simple view to keep interaction for the user easy. Individual blogs will be presented as cards, with the image to the left, and then the title, a glimpse of the blogs body content limitied to 150 characters, and created by and on details. Below this a button to open the respective blog. The cards on this page are fully responive to the diferent screen sizes, moving the image to above the text on tablet screen sizes and less. If the user is a super user, then an add blog button will be present above the cards to the right.

Blog Details Page:

The individual blog pages have been kept simple, and fully responsive on different screen sizes. When opened from the blog page, they are opened in a seperate window to keep a good flow to the site, in case a user wanted to open multiple blogs. This page presents the blogs image, if any, then the title, created by and on details, and the blogs content. If the user is the supersuser, then links to edit/delete will be visible below the created by and on details.

Back to top button:

A back to top button becomes visble across all pages when a user scrolls past 200 pixels. The colour changes to the yellow from the colour scheme when hovered over, and when click, scrolls at a set speed back to the top of the page.

Product Management Page:

This page is only visible to a superuser. It can be accessed by logging in, and finding the link in the dropdown of the 'my account' link of the navbar. The purpose of this page is for the store owner(superuser) to add a product to the site. The page loads a form with all fields of a product, having the required fields marked by a \*. There is a 'Select Image' button to upload an image from the superusers computer, where upon choosing an image, the image chosen name displayed below the button. Below the form, is a canel btton to cancel the process, and a button for added the product to the site. if the form is not valid, the the from will not be submitted and the user will be notified of which fields to fill in.

Contact Page:

This page is accessed by clicking on 'Contact Us' on the right side of the footer. It renders a simple form with the purpose of a user sending a message to the store, for enquiries or simple questions, all relevant nonetheless. When the form is submitted, the user is present with a success message as a toast, or else an error message if the form is not valid.

Toasts:

All pages have the ability to display toast messages to the user, which are displayed below the navbar on the right hand side. There are four different types of toast messages: success, error, warning and info. The toast colours will change to reflect each type of message. When a user adds a product to their basket, the success toast is rendered, displaying the contents of their basket, and the total excluding the discount. At the bottom of the toast a button is given for the user to go to secure checkout and open their basket page to review their order.

Delete Modal:

If the user is a superuser, they willl have the ability to edit and delete products and blogs. Upon clicking the delete but, a modal will pop up at the top of the screen, asking them to confirm they want to delete the chosen product or blog. They can simply hit the cancel button which will just close the modal and keep them on the page they are on.

### Future Features

Time was against me with this project, and unfortuantly I wasn't able to implement all the features that I want for this site. The possibilities for an e-commerce site like this could be endless, but some features I wanted to include are:

- A Newsletter

  - A section found as part of the footer for a user to enter their email address and subscribe to a newsletter, receiving monthly subscriptions once a fully running site.

- Account login via social media

  - I would have liked to incorporate the user having the ability to sign in to the site using their social media accounts. In the world we live in now nearly everyone has a social media account. Being able to log in to this site using their social media accounts would be very desirable as it would save them having to manually enter their details into the register form, and with that their email addrerss would be automatically confirmed as they would have had to allow access from their chosen social media sign up choice.

- Custom error pages

  - Having custom error pages built in to keep everything on site erradicating the need to use defualt error pages that may be less informative.

- Edit and Delete functions of reviews

  - It would be nice for a user that after submitting a review to a product they can edit that review post in case of a typo or spelling error. It would also be very useful for the store owner to have the ability to dlete a review, in case their is any bad laguage or discrimination posted with the reviews.

- Breadcrumb navigation

  - Using a breadcrumb navigation would allow for an even easier navigation of the site, enabling a user to easily see what page they are on, how it is they got there, and moving back to the desired page.

Unfortunately the time scale of this project is quite short for the quantity of work to be done here and is a massive learning curve, so there are just the surface of what I would like to incorporate to this site to make the user experience that much better and the general use of the site that more clean, tidy and desirable.

[Back to Top](#table-of-contents)

---

## **Testing**

Testing of this site can be found [here](https://github.com/Gregory4321/cooks_finest/blob/master/testing.md) in a seperate file

---

## **Deployment**

This multi-page fully functioning e-commerce website was developed in Gitpod and pushed to a remote repository on Github, using Git as version control. This project was deployed to Heroku, and made use of AWS (Amazon Web Services and its S3 Bucket) to store static and media files.

---

### Local Deployment

To run your own version of this project, it can be cloned or downloaded from Github. Once you have decided on which IDE you want to use, make sure that you have the following installed:

- Git - for version control
- PIP - to install packages
- Python - the programming language used for the backend logic

Github offers a few ways to clone a repository. You can simply download the entire repo as a zip file, and then upload that zip into a new workspace. Otherwise, on the repositories page in Github, follow these steps:

1. Click the 'Code' button.

2. In its dropdown menu, click the clipboard icon to copy the URL.

3. In the terminal window back in your IDE, make sure the current working directory is the location where you wan to clone the repository.

4. In the command line, paste in the URL retrieved from the repo using the command:

```bash
git clone <copied-repository-url-from-Step-2-^^>
```

5. Create your environment variables. You can either go to the Gitpod dashboard, go to Settings => Variables => and then add them there, or create a env.py file, and add the env.py file to your .gitignore file in your projects rot directory. Either way works the great and the same way, just make sure these variables are included:

```bash
DEVELOPMENT = True
SECRET_KEY = YOUR_SECRET_KEY
STRIPE_PUBLIC_KEY = YOUR_STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY = YOUR_STRIPE_SECRET_KEY
STRIPE_WH_SECRET = YOUR_STRIPE_WH_SECRET
```

You will need to sign up to stripe. Upon doing so, you can get the PUBLIC and SECRET keys from the left column of the page, clicking "Developers", and API Keys. Once you have set up the webhook endpoints, you will be given a unique STRIPE_WH_SECRET key.

More information on this can be found [here](https://stripe.com/docs).

6. Install the required dependencies needed to run the app by typing in the command line:

```bash
pip3 install -r requirements.txt
```

7. This project will now be set up and ready to run. In the command line, type:

```bash
python3 manage.py runserver
```

You can create a super user to access the admin backend.

```bash
python3 manage.py creatsuperuser
```

To access the admin backend add to the end of the sites url:

```bash
https://<cooks-finest-url>/admin
```

This will allow to do add, edit and delete products, categories, users, orders, as well as verify any email addresses.

8. Your models will need to be migrated in order to create them in the database. In the command line, type:

```bash
python3 manage.py makemigrations

***FOLLOWED BY***

python3 manage.py migrate
```

Whenever a model is edited they will need to be migrated. To make sure you are migrating the correct models, you can run a dry run flag on makemigrations to make sure you know which models are to be migrated, and a plan flag on migrate before actually using 'makemigrations' and 'migrate',

```bash
python3 manage.py makemigrations --dry-run

python3 manage.py migrate --plan
```

[Back to Top](#table-of-contents)

---

### Deployment to Heroku

Deploying this site to Heroku.

1. If you haven't got one already, create an account for Heroku. From signing in on their website, click 'New', found at the top right of the dashboard, and then 'Create new app'.

2. Give the app a unique name, and set the region to whatever region is closet to your own location, then click 'Create app'.

3. Once created, click on the 'Resources' tab, and in the add ons search bar, type postgres, and click 'Heroku Postgres', and then use the free plan, and confirm. This will provision a new Postgres database.

4. There are some extra dependencies and files needed. You will also need to install:

- psycopg2-binary - a PostgreSQL database adapter for the Python programming language.
- dj_database_url - a Django utility which allows you to utilise the 12factor inspired DATABASE_URL environment variable to configure your Django application.

You will also need to install - gunicorn - a Python Web Server Gateway Interface(WSGI) HTTP server., which will act as our web server.

5. After installing these dependencies, run the command:

```bash
pip3 freeze > requirements.txt
```

This will ensure that Heroku installs all our apps requirements when we deploy.

6. To save having to manually re-create your database (Postgres is the database used for deployment, and files aren't automatically transferred), you can easily transfer from the development database.

- Make sure you are connected to your mysql database.

- Backup your current database and load it into a db.json file by typing in the command line:

```bash
python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
```

7. Now to set up the new database. Head to your projects 'settings.py', and import dj_database_url at the top.

8. Scroll down to database's setting, and comment out the default configuration, replacing it with a call to dj_database_url.parse and give it the database URL from Heroku:

```bash
DATABASES = {
        'default': dj_database_url.parse("<YOUR_Postrgres_database_URL>")
    }
```

This can be found from the settings tab on Heroku, clicking 'Reveal config vars' and copying the value there from the DATABASE_URL key. It will start with 'postgres://'.
You can also get this from typing in the command line:

```bash
heroku config
```

Note: This is a temporary set up, and you should NOT add, commit and push to Github with this URL in your settings file. You DO NOT want this Heroku database config URL in version control for security reasons.

This is now connecting your manage.py file to your new Postgres database. As this is now a new database, you will need to run migrations again to get the database all set up.

9. After this, you can load your product data from the db.json file into Postgres using:

```bash
python3 manage.py loaddata db.json
```

10. Next you want to create a superuser to use on the Postgres database:

```bash
python3 manage.py createsuperuser
```

Follow the prompts it suggests, and your super user will be created.

11. In 'settings.py', you want to create an if statement so when the Heroku app is running, you connect to the Postgres database, otherwise, you connect to the development database. Replace the database setting with this code:

```bash
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

12. Create a Procfile, to tell Heroku how to run this project. Inside this file, add:

```bash
web: gunicorn cooks_finest.wsgi:application
```

13. Login to Heroku on the command line, using:

```bash
heroku login -i
```

14. Disable collect static so Heroku won't try to collect static files when we deploy. Type in the command line:

```bash
heroku config:set DISABLE_COLLECTSTATIC=1
```

15. Add the hostname of your Heroku app to allowed hosts in 'settings.py'.

Heroku can be connected to Github to automatically deploy each time you issue a git push in the command line. The easiest way to enable this is:

1. Open Heroku and navigate to the 'Deploy' tab.

2. Under 'Deployment Method' select 'Connect to Github'.

3. Search for your repositories name and click connect.

4. Then scroll down and click 'Enable Automatic Deploys'.

Your code will now be automatically deployed with every git push from you IDE command line. Upon a git push, you will see the build in progress in the 'Activity' tab on Heroku. You are now deployed to Heroku.

### Hosting Images on Amazon Web Service S3

For this site, the static and media files are hosted in an AWS S3 bucket. You will need to create an account with AWS, and create an S3 bucket, giving it public access. Once this is complete, upload your static and media files into the correct folders. The CORS configuration I used was what Code Institute provided, which is:

```bash
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

This is the basic setup of the S3 bucket with AWS, more details can be found [here](https://docs.aws.amazon.com/s3/index.html).

You will the need to set the static and media files in your workspace. For this, you will need to do the following:

1. First, do a pip install of 'boto3' and 'django-storages', and then freeze them into the requirements.txt file so they get installed upon the next push to Heroku.

2. In 'settings.py', add 'storages' under INSTALLED APPS. Then add these following settings to tell Django which bucket it should be communicating with:

```bash
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'cooks-finest'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and Media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

When you set up your S3 bucket, you would have downloaded a csv file. In this file you will find your AWS access key and secret access key.

NOTE: It is very important to keep these keys private. If they end up in version control then someone can use them to move and store data through your S3 bucket, where Amazon would bill YOUR registered credit card if it exceeded the limit.

3. Add these keys to your Heroku config variables.

4. Add a variable here with the key of 'USE_AWS' with a value of 'True'. This ensures your settings file knows to use the AWS configuration when deploying to Heroku.

5. Delete the DISABLE_COLLECTIC static variable from Heroku so Django can collect static files automatically uploading them to the S3 bucket.

6. Create a file called 'custom_storages.py'. This will contain the following:

```bash
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

This file will link with the settings from above ^^ and tells Django that during production, use the S3 bucket to store the static files whenever collectstatic is run, and any uploaded product images.

7. Add and commit all of these changes, then issue a git push command. This will trigger an automatic deployment to Heroku, and then all of this logic will be implemented, and your static and media files will be applied to your deployed site.

[Back to Top](#table-of-contents)

---

## **Credits**

### Content

Content on the website was written by me, the developer, with inspiration taken from other food and recipe sites and e-commerce stores.

Product details were obtained from the linked site of the image I sourced on google images, and the description and used some details either directly or edited.

### Code

- The code throughout this project used [Bootstrap](https://getbootstrap.com/) to help keep the site responsive to the different screen sizes, allowing for layout changes and font sizes to take place with ease.

- I used inspiration from all of my previous milestone projects in implementing certain areas of code.

- [Stackoverflow](https://stackoverflow.com/) was a useful place to find hints and solutions to fix problems to code and it's implementation.

- Tutor support provided me with support and code logic tips to help get my reviews app enabled.

- There are some areas of the code that were taken from other sites, and have been credited as a comment above the code, such as the back to top button and the icon display format.

A healthy portion of this projects code was inspired by and coded alongside the Boutique Ado walkthrough videos from Code Institute, helping set up the site and making use of the django allauth template logic. The code was used as a template and then edited, adapted and customised to suit the design and purpose of the project. My own two models of the blog app and reviews app were inspired by many google searches and research of different current sites and stackoverflow questions along with the django docs to create the two functioning models.

### Media

The images used on the website were mostly taken from [Google Images](https://www.google.com/) for use as the products images. [Unsplash](https://unsplash.com/) was also used to find other suitable images for use across the site.

These images were then resized to my required sizes for use on the site to keep any stretching or shrinking of images to the bare minimum. To do this I used two site:

- [Canva](https://www.canva.com/)

- [Picresize](https://picresize.com/)

The favicon image was created and exported to my computer using the site Canva, and then uploaded to the site [Favicon.io](https://favicon.io/) to be generated as an ico image, to then be exported back to my computer and then added to my root directory on gitpod.

---

## **Acknowledgements**

### Pages used for inspiration

- [Lakeland](https://www.lakeland.co.uk/)
- [ProCook](https://www.procook.co.uk/)
- [Sous Chef](https://www.souschef.co.uk/)
- [Wayfair](https://www.wayfair.co.uk/)

### Pages used for information

- [Code Institute](https://codeinstitute.net/)
- [Django Documentation](https://docs.djangoproject.com/en/3.2/)
- [Bootstrap](https://getbootstrap.com/)
- [Stack overflow](https://stackoverflow.com/)
- [W3schools](https://www.w3schools.com/)
- [CSS-Tricks](https://css-tricks.com/)
- [Slack](https://slack.com/intl/en-gb/)
- [YouTube](https://www.youtube.com/)
- [Code Pen](https://codepen.io/)
- [Python Documentation](https://docs.python.org/3/)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

### Special thanks

- My extended thanks goes out to my mentor [Oluwaseun Owonikoko](https://github.com/seunkoko) for her help, support and guidance along this journey of the Code Institue's Full Stack Web Developer Course.

- Code Institute's Tutor Support for being there to curve ball me to the solution I was needed, and their understanding and patience.

- The Slack community for the useful questions and information already present, but my fellow students, alumni, tutors and mentors that are present daiy to help aid problem solving.

- A special thanks to [Chris Zielinski](https://github.com/ckz8780) for his extremely helpful training videos and for his guidance throughout this project.

- My family and friends for their feedback during the build and testing stages.

- My nearest and dearest for supporting me along my journey to complete this Ful Stack Web Developer Course, and having such patient with me over this last year.

## **Disclaimer**

This project was created for educational use only. It has been part of studying at the Code Institute as part of their Full Stack Web Developer Course.
