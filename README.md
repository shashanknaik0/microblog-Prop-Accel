# microblog - Instructions for setting up and running the application
<hr>
<h2>Clone the repo</h2>

step 1: use below cammand to clone the repo

<pre>
git clone https://github.com/shashanknaik0/microblog-Prop-Accel.git
</pre>


step 2: get into the directory
<pre>
cd microblog-Prop-Accel
</pre>

<hr>
<h2>Setup the virtual environment</h2>
use <a href="https://www.w3schools.com/django/django_create_virtual_environment.php">this</a> link to get Instructions to create and activate virtual environment.

<hr>
<h2>Install dependecies</h2>

step 1: use below cammand install python dependecies from <code>requirement.txt</code>
<pre>
pip install -r requirements.txt
</pre>

step 2: install <a href="https://www.postgresql.org/download/">postgres</a> database and create database with name <code>'your_database_name'</code>

<hr>
<h2>Setup environment variable</h2>

step 1: create <code>.env</code> file inside <code>microblog</code> directory.

step 2: add secret key and database settings in <code>.env</code> file like below
<pre>
SECRET_KEY='your_secret_key'
DATABASE_NAME='your_database_name'
DATABASE_USER='your_username'
DATABASE_PASS='your_password'
DATABASE_HOST='localhost'
DATABASE_PORT='5432'
</pre>

<hr>
<h2>Run the project</h2>

step 1: rum below cammand to migrate the django models.
<pre>
python manage.py makemigrations
</pre>
<pre>
python manage.py migrate
</pre>

step 2: if you want to create superuser run below cammand. (<a href="https://docs.djangoproject.com/en/4.2/intro/tutorial02/#creating-an-admin-user">click me</a> for more info)
<pre>
python manage.py createsuperuser
</pre>

step 3: run the server
<pre>
python manage.py runserver
</pre>

step 4: visit the development server at http://127.0.0.1:8000 and use below api endpoints 
<pre>
/api/users/ - (POST) Add a new user to the platform. The user details will include fields like username, email, and password. 
/api/users/	&lt;int:user_id&gt;/ - (GET) Retrieve details of a specific user.
/api/users/	&lt;int:user_id&gt;/ - (PUT/PATCH) Update the details of a specific user.
/api/posts/ - (POST) A user creates a new post. The post details will include fields like user_id, content, and post_date.
/api/posts/	&lt;int:post_id&gt;/ - (GET, PUT/PATCH, DELETE) - CRUD operations for a specific post.
/api/posts/ - (GET) List all posts available on the platform.
</pre>

