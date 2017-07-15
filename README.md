Project Description:

This is an application that provides a list of travel destinations in Florida within a variety of categories as well as provide a user registration and authentication system. 

Registered users will have the ability to create, edit and delete their own favorite restaurants,hotels and things to do in a Florida city as recommendations to other people.

On the homepage, you will see a list of cities and click a city that you are interested in to find out some trip info that other users provided as real experience. 

You can add your own destinations after log in with your google or facebook account and edit trip info for that city or delete those you don't want to show anymore.

PreRequisites:

-Python

-Vagrant

-VirtualBox

Steps to run:

1.Install Python, Vagrant And VirtualBox

2.Download itemcatalog_app.zip and unzip it to vagrant folder

3.To launch the Vagrant VM, find the directory in your preferred terminal and type "vagrant up" and then type "vagrant ssh" 

4."cd /vagrant" to go into the directory where you save itemcatelog_app folder

5.Type "python db_setup.py" in your terminal to initialize your database

6.Type "python db_init.py" in your terminal to populate your database with some data that are already created for test purpose.

7.Now you will see your databse in folder named cityinfo.db in your folder now

8.Now you can type"python itemcatalogapp.py" in your terminal to run the application on localhost:5000

9.You can put"/JSON" after the urls with city trip info or city list to get JSON endpoints

10.If the CSS file is not loaded properly, try ctrl+f5 to reload the page

11.You can only view others' posts without editing but you can edit your own posts after sign in

12.Click on "show all destination" on top-left corner to return to homepage with a list of cities

