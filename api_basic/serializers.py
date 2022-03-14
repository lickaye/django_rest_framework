from dataclasses import fields
from enum import auto
from pyexpat import model
from re import A
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = ['id','title','author','email']
        fields = '__all__'
        
   