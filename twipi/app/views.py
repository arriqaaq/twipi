from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from app.models import UserProfile,Tweet,Replies
from django.db.models.signals import post_save
from datetime import datetime, timedelta

# Create your views here.
def test(request):
		user=User.objects.get(id=request.session['id'])
		b=None		
		try:		
			b=UserProfile.objects.get(user=user)
		except:
			b=None		
		if not b:		
			UserProfile.objects.create(user=user)		
		t=Tweet.objects.filter(user=user)
	       	return render(request, 'app/test.html',{'tweets':t})     


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
	
        if user:
	    request.session['id'] = user.id
            if user.is_active:
                login(request, user)
		
		request.session["fav_color"] = "blue"

                return HttpResponseRedirect('/app/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        return render(request, 'app/login.html', {})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    del request.session["id"]	
    logout(request)

    # Take the user back to the homepage.
    
    return HttpResponseRedirect('/app/login/')


def submit(request):
    luser=request.session['id']
    c={}
    print 'woahhhhhhhhhh', luser
    if request.method == 'POST':
	    tweettext=request.POST.get('tweettext')
	    user=User.objects.get(id=luser)
	    t=Tweet.objects.create(text=tweettext , user=user)          

    return HttpResponseRedirect('/app/')  
    

def retweet(request, tweet_id):
    luser=request.session['id']
    c={}
    print 'yeahhh', tweet_id
    if request.method == 'POST':
	    t=Tweet.objects.get(id=tweet_id)
	    user=User.objects.get(id=luser)
   	    try:
         	    p=Tweet.objects.get(text=t.text, user=user)
	    except:
		    p=None
	    if not p:        
	    	    Tweet.objects.create(text=t.text, user=user)
    return HttpResponseRedirect('/app/')  


def replies(request,tweet_id):
    print 'yeahhh', tweet_id
    if request.method == 'POST':
	    t=Tweet.objects.get(id=tweet_id)
	    retext=request.POST.get('reply')
	    re=Replies.objects.create(text=retext,tweet=t)
    return HttpResponseRedirect('/app/')  


def viewTweet(request,tweet_id):
    		t=Tweet.objects.filter(id=tweet_id)
    		r=Replies.objects.filter(tweet=t)
	        return render(request, 'app/tweet.html', {'tweet':t,'replies':r})
		
def viewUser(request,user_id):
		user_current=User.objects.get(id=request.session['id'])
		user=User.objects.get(id=user_id)
    		t=Tweet.objects.filter(user=user)
	       	return render(request, 'app/user.html',{'tweets':t,'userid':user_id})     


def follow(request,user_id):
		user_current=User.objects.get(id=request.session['id'])
		user=User.objects.get(id=user_id)
		user_follow=UserProfile.objects.get(user=user)
		user_current.userprofile.followers.add(user_follow)
		return HttpResponseRedirect('/app/') 


def filter(request, h):
		user=User.objects.get(id=request.session['id'])
		t=Tweet.objects.filter(user=user)
		time_threshold = datetime.now() - timedelta(hours=h)
		t=Tweet.objects.filter(time__gte=time_threshold)
	       	return render(request, 'app/test.html',{'tweets':t})     

