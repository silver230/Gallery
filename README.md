# GALLERY
## Description
This is a gallery application that allows me to post diffrent photos and allows users to come and view the diffrent photos based on the location they were taken ,the user  also has an option of copying and sharing the link provided
## Setup/Installation Requirements
# installations required
- python version should be 3.6
-Django version 1.11 `pip install django==1.11`
- Additionally, you’ll need to make sure you have pip available. You can check this by running:
- `pip --Version`
- Install Pipenv `pip install --user pipenv`
- install virtualenv and then test it
- `python3.6 pip install --user --upgrade pip`
- `python3.6 -m virtualenv env`
- `source env/bin/activate`

Inorder to clone , follow the procedure below;
- On GitHub, navigate to the main page of the repository.
- Under the repository name, click Clone or downlonload.
- click the paste button.
- Open Terminal.
- Change the current working directory to the location where  -  you want the cloned directory to be made.
- Type git clone, and then paste the URL you copied in Step 2.
#creating a database
- `psql`
- `CREATE DATABASE gallery`
- connect to the database `\c gallery`
- check if tables have been created `\dt`

#Run migrations
- `python3.6 manage.py migrate`
- `python3.6 manage.py makemigrations gallerys`

#Running the app
- `python3.6 manage.py runserver`

#testing
- `python3.6 manage.py test gallerys`


## Technologies Used
- HTML
- CSS
- Python
- Django
- Postgres
- javascript

# Known Bugs
- the website does not function well on explorer

### License
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
Copyright (c) {2018}