# Python-for-Data-Science-and-Machine-Learning
Udemy course

GitHub link
https://github.com/juinc/python_data_science_and_machine_learning_bootcamp

---------------
DJANGO commands
---------------

Verify your Django project works. Change into the outer mysite directory, if you haven’t already, and run the following commands:

--
    $ python manage.py runserver
--

    You’ll see the following output on the command line:

    Performing system checks...

    System check identified no issues (0 silenced).

    You have unapplied migrations; your app may not work properly until they are applied.
    Run 'python manage.py migrate' to apply them.

    April 19, 2018 - 15:50:53
    Django version 2.0, using settings 'mysite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Now that your environment – a “project” – is set up, you’re set to start doing work.

    Each application you write in Django consists of a Python package that follows a certain convention.
    Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus
    on writing code rather than creating directories.

        Projects vs. apps

        What’s the difference between a project and an app? An app is a Web application that does something – e.g., a
        Weblog system, a database of public records or a simple poll app. A project is a collection of configuration
        and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

    Your apps can live anywhere on your Python path. In this tutorial, we’ll create our poll app right next to your
    manage.py file so that it can be imported as its own top-level module.

    To create your app, make sure you’re in the same directory as manage.py and type this command:
--
    $ python manage.py startapp [app name]
--