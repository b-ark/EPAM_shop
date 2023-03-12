# System Requirements Specifications #

# 1 Introduction #
## 1.1 Purpose ##
The purpose of the final project is to summarize the knowledge gained during the course. The main idea is to build a management system for categories and products 
## 1.2 Document Conventions ##
This document uses the following conventions:
<table>
<tr>
<th>Convention</th>
<th>Meaning</th>
</tr>
<tr>
<td>DB</td>
<td>Database</td>
</tr>
</table>

## 1.3 Glossary
## 1.4 Intended Audience and Reading Suggestions ##
This project is a shop management system, and it is restricted within the 
EPAM Systems learning program. This has been implemented under the guidance of 
EPAM Systems mentors. This project is useful for the shop owners.
## 1.5 Project Scope ##
The purpose of the online shop managment system is to ease product managment and to create 
a convenient and easy-to-use application for shop owners. The system is based on a relational 
database with realization of CRUD operations to manage categories and products
## 1.6 References ##

# 2 Overall Description #
## 2.1 Project Perspective ##
A distributed shop DB stores the following information:
### Category ###
<table>
<tr>
<th>dd</th>
<th>title</th>
<th>description</th>
<th>products</th>
<tr>
<td>int, primary_key</td>
<td>string</td>
<td>string</td>
<td>backref relationship</td>
</tr>
</table>

### Product ###
<table>
<tr>
<th>id</th>
<th>title</th>
<th>price</th>
<th>description</th>
<th>sales_start</th>
<th>amount</th>
<th>img_path</th>
<th>category_id</th>
<tr>
<td>int, primary_key</td>
<td>string</td>
<td>float</td>
<td>string</td>
<td>date</td>
<td>int</td>
<td>string</td>
<td>int, ForeignKey</td>
</tr>
</table>

Column "img_path" is used for getting access to images, uploaded by users and stored at 
/app/static/images/products folder. This approach allows to optimize the work of the database,
as it does not directly store any files.
## 2.2 Project Functions ##
Application is able to: 

<ul>
<li>execute CRUD operations with both entities (category and product)</li>
<li>search product entities (displays all available products by certain date)</li>
<li>display a list of items for each entity</li>
<li>display a sum of all products (by the filed "amount") in each category</li>
<li>display products in certain category</li>
</ul>

This functionality is available both for web application and web RESTful service.
<br>Endpoints for this web application are:

<table>
<tr>
<th>Endpoint</th>
<th>Functionality</th>
<tr>
<td>/</td>
<td>Main page</td>
</tr>
<tr>
<td>/categories</td>
<td>Page with the list of categories and products</td>
</tr>
<tr>
<td>/products</td>
<td>Page with the list of products</td>
</tr>
<tr>
<td>/categories/new</td>
<td>Page with the form to add new category</td>
</tr>
<tr>
<td>/products/new</td>
<td>Page with the form to add new product</td>
</tr>
<tr>
<td>/product/'<'int:_id'>'</td>
<td>Page to show product by id</td>
</tr>
<tr>
<td>/category/'<'int:_id'>'</td>
<td>Page to show category by id</td>
</tr>
<tr>
<td>/search</td>
<td>Page to search for products, available by certain date</td>
</tr>
<tr>
<td>/category/edit/'<'int:_id'>'</td>
<td>Page to edit category by id</td>
</tr>
<tr>
<td>/product/edit/'<'int:_id'>'</td>
<td>Page to edit product by id</td>
</tr>
<tr>
<td>/category/delete/'<'int:_id'>'</td>
<td>Page to delete category by id</td>
</tr>
</table>

Endpoints for the RESTful web service are:

<table>
<tr>
<th>Endpoint</th>
<th>Functionality</th>
<tr>
<td>/api/category</td>
<td>CRUD operations with single category object</td>
</tr>
<tr>
<td>/api/product</td>
<td>CRUD operations with single product object</td>
</tr>
<tr>
<td>/api/categories</td>
<td>Operations with all category objects</td>
</tr>
<tr>
<td>/api/products</td>
<td>Operations with all product objects</td>
</tr>
<tr>
<td>/api/category/sum</td>
<td>Calculates the sum of all products in the certain category</td>
</tr>
<tr>
<td>/api/search</td>
<td>Returns products, available by certain date</td>
</tr>
</table>

The major features of application functionality is shown below

[ER_model](ER_model.drawio.png)

## 2.3 User Classes and Characteristics ##
The application doesn't support user privileges.
## 2.4 Operating Environment ##
Operating environment for the application is as listed below.
<ul>
<li>client/server system</li>
<li>Operating system: Linux Ubuntu</li>
<li>Database: sqlalchemy using sqlite</li>
</ul>

## 2.5 Design and Implementation Constraints ##
The information of all categories and products is stored in the 
database that is accessible by the web application


# 3 External Interface Requirements #
## 3.1 User Interfaces ##
<ul>
<li>Back-end software: SQLite (SQLAlchemy), Python (Flask)</li>
<li>Front-end software: HTML, JS, Bootsrtap</li>
</ul>

## 3.2 Hardware Interfaces ##
<ul>
<li>Linux Ubuntu</li>
<li>A browser which supports HTML & Javascript.</li>
</ul>

## 3.3 Software Interfaces ##
Following are the software used for the online application:

<table>
<tr>
<th>Software used</th>
<th>Description</th>
<tr>
<td>DB</td>
<td>To save the items in the DB, we have chosen ORM approach (SQLAlchemy)</td>
</tr>
<tr>
<td>Operating system</td>
<td>We have chosen Ubuntu Linux as an operating system, because it's stable, reliable, well maintained</td>
</tr>
<tr>
<td>Flask</td>
<td>To implement the project we have chosen Flask python package due to its' flexibility and lightweight</td>
</tr>
<tr>
<td>/api/products</td>
<td>Operations with all product objects</td>
</tr>
<tr>
<td>/api/category/sum</td>
<td>Calculates the sum of all products in the certain category</td>
</tr>
<tr>
<td>/api/search</td>
<td>Returns products, available by certain date</td>
</tr>
</table>

## 3.4 Communication Interfaces ##
This project supports all types of web browsers. 

<!--appendix-->
