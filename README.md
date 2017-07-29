# blog_api

This is an assignment for CSIS 604. The objective is to provide a RESTful api for a blog. The blog api must include a way to add a new blog entry, delete an entry, edit an entry, and retrieve and entry.

## Retrieve Blog Posts
Use the example below to list all blog posts.
<pre>
curl -i http://secure-bonus-175013.appspot.com/blog/api/posts
</pre>

## Add Blog Post
To add a Blog post use the example below to create a title and description.
<pre>
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Example Title","description":"The brown fox jumps over a box."}' http://secure-bonus-175013.appspot.com/blog/api/posts
</pre>

## Delete Blog Post
To delete a Blog post first find the post id that you wish to delete. Then place the post id at the end of the url as shown below. (1 is the post id in used in the example below)
<pre>
curl -i -X DELETE http://secure-bonus-175013.appspot.com/blog/api/posts/1
</pre>

## Edit Blog Post
To make a change to a Blog post first find the post id number and then format your request like below where the post id number is at the end of the URL. (3 is the post id number in the example below)
<pre>
curl -i -H "Content-Type: application/json" -X PUT -d '{"title":"Edited Post","description":"This is text that is new"}' http://secure-bonus-175013.appspot.com/blog/api/posts/3
</pre>

## Sources and inspiration:
https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
https://cloud.google.com/python/getting-started/using-cloud-datastore