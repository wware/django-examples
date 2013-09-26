HTML5 offline app
=================

The first thing is to set up the app cache to save a bunch of HTML/CSS/JS
files.

The second thing is to detect in JS whether or not we are online, and based on
that, choose between local storage and a back end. How to do that? I think you
do it for each Ajax call, and if the call fails you do a backup plan with local
storage.

http://stackoverflow.com/questions/5811365/using-ajax-with-offline-cache

When I try to do a fetch, I'm getting a readyState of 4 and a status of 0 where
I expected 200. This is apparently something to be expected when you're
operating out of the appcache. A status of 0 means that you're trying to fetch
from a different host (like a cross-site scripting attack) and the Django
server will give you bogus response text in that case. So if you can detect
that you're offline, you should treat the 0 status as a 200.

You want to think of offline as the normal operating mode for your app. Think of
it in layers. Ordinarily you're interacting with local storage, and then when
possible, local storage syncs with the server, but that syncing is largely
invisible to the user.

One way to go about that would be to have dirty flags for the stuff in local
storage, saying that this needs to be sent to the server. But you also have to
think about the whole 3-way merge problem. Save a copy of the last value I got
from the server, and when I send to the server, first fetch what's on the server
now and compare it to my original. If it's mergeable with my change, do the
merge and then try to do the write. Actually the whole approach to this problem
we are using at work (which I am proud to have done most of the figuring out
myself) is really the way to go. You still need to save copies of the things
you downloaded from the server plus hash values, but it's worth it to have
bullet-proof use of database transactions. So the whole 409/412 thing is
worth it.
