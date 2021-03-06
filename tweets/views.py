from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet
# Create your views here.

def home_view(request, *arg, **kwargs):
    return render(request, "../twitter_clone_project/templates/pages/home.html", context={}, status=200)

def tweet_detail_view(request, tweet_id, *arg, **kwargs):
    """
    REST API VIEW
    Consume by Javascript
    return json data
    """
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except: 
        data['message'] = "Not found"
        status = 404
    
    # data = {
    #     "id": tweet_id,
    #     "content": obj.content,
    #     # "image_path": obj.image.url,
    # }
    return JsonResponse(data, status=status)

