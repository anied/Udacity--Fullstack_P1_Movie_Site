#Udacity Python Final Project-- Movie Site
##Alex Nied

###Introduction
My project is constructed so that, upon build, it will use the API at <a href="www.themoviedb.org" target="_blank">TheMovieDB.org</a> to get a list of the most popular movies and construct the page based on that list.  The data returned is cached as is the webpage-- once constructed, it will be served directly, without any build phase, until 24 hours has passed since data was pulled down from the remote API.  Once 24 hours has passed, fresh data will be pulled down when building the site.

The UI will show popovers containing relevant film information for any users who have a screen width above 990px.  Below that and the popover is not activated (we are _very_ roughly assuming that this is perhaps a tablet, so hover states will not apply.  Also, at this width the UI moves to a single column where the popover is difficult to be seen anyway).  Also, users below this size will be directed to the trailer video in a new window, instead of in a modal on the page.

###To Use
After expanding the zip, running the file `build_site.py` will do an initial build/deploy of the site-- this will take a moment due to the fetching of remote data.  After the first build/deploy, subsequent runs of `build_site.py` will utilize the cached page for 24 hours, so it will open in the browser much faster.

###Notes
This was built using Python 2.7.6 on Ubuntu 14.04.  The page was tested on Chrome and Firefox-- IE was not tested as this task seemed more about the Python aspect than the UI.

~~Github was not utilized to submit this assignment because the codebase contains an API key for TheMovieDB.  In the future I will ideally be using Github for submissions.~~  (I have figured out how to omit history containing the private API key-- thus I am now able to host this on Github)

Please contact me if there are any problems with the code or its execution so I can address them.

Thanks!