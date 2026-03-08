from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# model form for creating and updating blog posts
from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']


# form for handling comments


from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']


# form for handling tags

        from django import forms
from .models import Post, Tag


class PostForm(forms.ModelForm):

    tags = forms.CharField(required=False, help_text="Comma-separated tags")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

            tags = self.cleaned_data.get('tags')
            if tags:
                tag_list = tags.split(',')

                for tag in tag_list:
                    tag_obj, created = Tag.objects.get_or_create(name=tag.strip())
                    instance.tags.add(tag_obj)

        return instance
    


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']