# Milestone Project 4 - Cook's Finest
View live project <a href=“#”>here</a>

![Cook's Finest Am I Responsive image]()

Cook's Finest is an online e-commerce store, offering a collection of kitchenware for the savy home cook. User's can create their own account, saving their details for faster checkout for future purchases, but are not limited, and can make a purchase as a guest if wanted. The registered user can edit their personal details and access their shopping history. Blogs are presented for good reads, and a newsletter sign up is offered.

***
## Table of Contents:
* [What does it do and what does it need to fulfill?](#what-does-it-do-and-what-does-it-need-to-fulfill)
   * [Project Goals](#project-goals)
* [User Experience](#user-experience)
   * [User Goals](#user-goals)
   * [User Stories](#user-stories)
   * [Site Owner Goals](#site-owner-goals)
* [Design](#design)
    * [Research](#research)
    * [The Five Planes of UX](#the-five-planes-of-ux)
        * [Wireframes](#wireframes)
        * [The Colour Scheme](#the-colour-scheme)
        * [Font](#font)
        * [The Logo](#the-logo)
    * [Conclusion](#conclusion)
* [Technologies Used](#technologies-used)
* [Database Structure](#database-structure)
* [Features](#features)
   * [ Existing Features](#existing-features)
   * [Future Features](#future-features)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Local Deployment](#local-deployment)
    * [Deployment to Heroku](#deployment-to-heroku)
* [Credits](#credits)
    * [Content](#content)
    * [Code](#code)
    * [Media](#media)
* [Acknowledgements](#acknowledgements)
* [Special Thanks](#special-thanks)
* [Disclaimer](#disclaimer)

***

## **What does it do and what does it need to fulfill?**

This is my fourth and final milestone project of Code Institute's Full-Stack Web Developer Course. The projects main requirements were to build a Django web application with the use of HTML, CSS, JavaScript and Python, and utilising a relational database, allowing users to store and manipulate data records of a particular domain. This was achieved with the user profile model, where user's can add and edit their personal details, as well as the site owner having the ability to add, edit and delete products from the site.
The use of Stripe was also a requirement, which I fulfilled with the use of a checkout system for user's to purchase their selected product(s).
IMPORTANT: The Stripe API used for handling payments is currently only for educational purposes and is not for taking real card payments. To test the payment functionality successfully, use the test card number Stripe provides, of "4242 4242 4242 4242", and then the other details chosen at random. 
This project is a Django-Python web application, plugged into a PostgreSQL database, with SQLite3 used in the development, and was deployed using Heroku. The Bootstrap framework and grid system was used for effective styling across the pages of the site.

### **Project Goals**

My goal was to supply the home cook with a website where they can browse and purchase products they want for their home kitchen, and provide helpful tips and ideas on how to improve the kitchen space.

***

## **User Experience**

### User Stories:

Due to the the quantity of user stories for this project, and for best practice, I compiled my user stories on a spreadsheet to make it more clear which story is related to what and who.

Please view the user stories spreadsheet [here](https://github.com/Gregory4321/cooks_finest/blob/master/media/readme_content/user-stories.png)

[Back to Top](#table-of-contents)

***

## **Design**

### Research

Reasearching for this project, I came across only a handful of sites that catered only for kitchen products. The design and layouts of the sites kept a clear and to-the-point attitude about them. Colours were kept very neutral as the images of the products on display were to be kept at the fore front of the site.

Sites I used for inspiration were:

* [Lakeland](https://www.lakeland.co.uk/)
* [ProCook](https://www.procook.co.uk/)
* [Sous Chef](https://www.souschef.co.uk/)

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

* Base Template
    * [Desktop View]()
    * [Mobile View]()
* Home Page
    * [Desktop View]()
    * [Mobile View]()
* Products Page
    * [Desktop View]()
    * [Mobile View]()
* Individual Products Page
    * [Desktop View]()
    * [Mobile View]()
* My Account Page
    * [Desktop View]()
    * [Mobile View]()
* Login Page
    * [Desktop View]()
    * [Mobile View]()
* My Basket Page
    * [Desktop View]()
    * [Mobile View]()
* Checkout Page
    * [Desktop View]()
    * [Mobile View]()
* Contact Page
    * [Desktop View]()
    * [Mobile View]()
* Blog Home Page
    * [Desktop View]()
    * [Mobile View]()
* Individual Blog Page
    * [Desktop View]()
    * [Mobile View]()
</details>

[Back to Top](#table-of-contents)

##### The Colour Scheme

##### Font

##### The Logo

#### Conclusion

[Back to Top](#table-of-contents)

***

## **Technologies Used**

### Languages

### Libraries, Frameworks and Editors

### Tools

[Back to Top](#table-of-contents)

***

## **Database Structure**

***

## **Features**

### Existing Features

### Future Features

***

## Testing

***

## **Deployment**

***

### Local Deployment

To run your own version of this project, it can be cloned or downloaded from Github

***

### Deployment to Heroku

To deploy this project to Heroku:

***

## **Credits**

#### Content

#### Code

#### Media

***

## **Acknowledgements**

#### Pages used for inspiration

#### Pages used for information

#### Special thanks

## **Disclaimer**

This project was created for educational use only. It has been part of studying at the Code Institute as part of their Full Stack Web Developer Course.