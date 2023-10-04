# distraction-flagger-api


Backend hosted at [distraction-flagger-api.vercel.app](https://distraction-flagger-api.vercel.app/) used for my [distraction-reducer](https://addons.mozilla.org/en-US/firefox/addon/distraction-reducer/) FireFox extension.


## What's happening here?

Limited by Vercel's free storage space (25mb) and inspired to write out a practical implementation of some from-scratch common ML modules, this API contains the training notebooks and hosted implementations of a logistic regression classifier I use to predict if a webpage's title is related to ML studying or not. 

## Why did I do this?

There's another FireFox extension, [OneTab](https://www.one-tab.com/) which I've been using for the past month or so which I've been using to close out of all my tabs. By saving this data down, I quickly noticed how many of these tabs were duplicates of each other (multiple Twitter, etc.) and wanted to find a way to better focus. 

The solution I came up with was the classify a page as "on-topic" or not, and if the page was off-topic, I could make it grayscale and therefore less likely for me to stay on it. 

I saved down tab data, labelled it by hand, and trained a classifier which is now hosted at the link above. Specifics of this model can be found in the notebook also at this level, which is admitedly a little empty beyond the basic training.


## What comes next?

This is a toy project and more of a way to build out tools rather than seek the best accuracy, but open to any suggestions which also fit within the free tier of a Vercel app.

Most next steps I think of revolve around adding more endpoints to the API. 
Some examples I have are: 
- One endpoint which tells you the model's accuracy
- One endpoint that you can use to retrain

Or alternatively, we can update the extension to collect feedback from users, and investigate some form of active learning. 





