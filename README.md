# hierarchical_data
A simple Django server that uses MPTT models from django-mptt to create a Dropbox-esque web interface where you can create "folders" and "files" in an arbitrary structure and then display that structure.

Sometimes when categorizing data, there are potentially infinite ways that the data can be organized. For example, a file path for an operating system includes all the parent folders and the the location of the item itself, like this:

/Users/jkaufeld/demo/test.py
If we're looking at an object called test.py and we want to find all of the "parent nodes", or the folders that contain this object, then we have to do a recursive call upwards. In a 'traditional' Django ORM setup, a naive example might look something like this:

def get_complete_path(item):
  complete_path = list()

  while True:
   item = item.parent
   complete_path.prepend(item.path)
   if item.path == '/':
     break

  return os.path.join(complete_path)
This results in a database call for every single layer, which works out to three calls to get the complete path of our mythical object. We can do a lot better though... what if we could get that info in one call?

Using something called Modified Preorder Tree Traversal (MPTT), we can treat all our data like a gigantic tree, with a single starting point (the "root" object) and parents, siblings, and children galore. We can get the same data as above with a single call:

item.get_ancestors()
Your Task
The goal of this assignment is to learn about this type of database and different ways of working with it. Build a simple Django server that uses MPTT models from django-mptt to create a Dropbox-esque web interface where you can create "folders" and "files" in an arbitrary structure and then display that structure. We won't actually be uploading anything, just making model instances and using them to represent real data. See the rubric for more detailed information. Submit as link to your repo on Github.

Resources:

https://django-mptt.readthedocs.io/en/latest/overview.html (Links to an external site.)Links to an external site.
Extra Credit:

3 BONUS POINTS: Add forms to create folders / "files" without using the admin panel.
5 BONUS POINTS: Add a basic authentication system where each user has their own tree. Login / logout pages / endpoints included.
Submission
Submit a link to your GitHub repo.

https://github.com/<github_username>/hierarchical_data
Rubric
A rubric short of a full load
A rubric short of a full load
Criteria	Ratings	Pts
This criterion is linked to a Learning OutcomeDB is committed with repo
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
This criterion is linked to a Learning OutcomeREADME included in repo that explains the project and anything needed to run it.
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
This criterion is linked to a Learning Outcomeuses django-mptt to create one model: a file object that can be a folder or a "file"
4.0 pts
Full Marks
0.0 pts
No Marks
4.0 pts
This criterion is linked to a Learning OutcomeUses django-mptt draggable admin to make modifications easy in the admin panel
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
This criterion is linked to a Learning OutcomeDisplays the built tree on the homepage
3.0 pts
Full Marks
0.0 pts
No Marks
3.0 pts
This criterion is linked to a Learning Outcome3 BONUS POINTS: Add forms to create folders / "files" without using the admin panel.
0.0 pts
Full Marks
0.0 pts
No Marks
0.0 pts
This criterion is linked to a Learning Outcome5 BONUS POINTS: Add a basic authentication system where each user has their own tree. Login / logout pages / endpoints included.
0.0 pts
Full Marks
0.0 pts
No Marks
0.0 pts
This criterion is linked to a Learning OutcomeRepo contains pyproject.toml that includes all necessary dependencies to run application
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
Total Points: 15.0

superuser (username: reggy / password: asdf)