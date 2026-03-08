# Django Blog Project

## Features

- User registration, login, logout
- Profile management
- Create blog posts
- View blog posts
- Edit blog posts
- Delete blog posts

## Permissions

- Anyone can view posts
- Only logged-in users can create posts
- Only the author can edit or delete their posts

## URLs

/posts/ - List all posts  
/posts/new/ - Create a post  
/posts/<id>/ - View post  
/posts/<id>/edit/ - Edit post  
/posts/<id>/delete/ - Delete post



## Comment System

Users can interact with blog posts through comments.

Features:

- View comments under each post
- Logged-in users can add comments
- Authors can edit their comments
- Authors can delete their comments

### URLs

/posts/<post_id>/comments/new/ – Add comment  
/comments/<comment_id>/edit/ – Edit comment  
/comments/<comment_id>/delete/ – Delete comment