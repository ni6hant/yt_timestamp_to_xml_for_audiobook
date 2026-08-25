# Convert YouTube Timestamps to XML format for Smart AudioBook Player for Android
This python application has a very specific use case where it's only job is to convert timestamps written in youtube videos comments into an XML format to be specifically used with [Smart Audiobook Player on Android Store](https://play.google.com/store/apps/details?id=ak.alizandro.smartaudiobookplayer).

# How to Use
1. Add the timestamps in this format in the file `timestamps.txt` :
```
0:00 - Teletubbies 
6:25 - Stream Anniversary Welcome: Eight Years of EFAP
...
```

 * As you can see, the timestamps needs to be first and the description is separted by `-`.
 * Make sure there are no extra `-` in the description.
 * I have replaced the special character `&` with `and` as it caused error in the Android Application to be used this with.
  * Note: Please create an issue if other characters also cause issues. The issue can be seen by no bookmarks being imported at all.
 
2. Make sure the file `bookmarks.sabp.xml` exists.
3. Run the python program: `python edit_time.py`.

# No LLM Used
No LLMs or even internet searches were used at all in writing this code. This code was manually written by me.