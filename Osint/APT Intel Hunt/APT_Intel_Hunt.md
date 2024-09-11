## APT Intel Hunt
### Category: OSINT
### Points: 40
### Description
You’re up against one of the most notorious APT groups—Lazarus. These cyber troublemakers have been causing chaos, and it’s up to you to outsmart them before they can make their next move.

Word on the street is that they’ve dropped some hints about their latest scheme. A recent CyberMaterial report on their mischievous sub-group, Andariel, might just be the treasure map you need. But remember, Lazarus is like a sneaky cat—hard to catch and always up to something devious.

Can you unravel their devious plans and find the flag before they hit their next target? Put on your detective hat, crack the code, and save the day! The world’s fate might just hang in the balance. 🕵️‍♂️🔓

### Approach
First thing we can do is search for `cybermaterial Andariel` and we find this [post](https://www.linkedin.com/posts/cybermaterial_cyberthreats-threatactors-andariel-activity-7214387546854715392-w0Xt/) from where we visit this post on their [website](https://cybermaterial.com/andariel-lazarus-group-threat-actor/).
Scrolling this website we dont really find much except we can see a few hyperlinks.</br>
![alt text](image.png)</br>
this particular hyperlink redirects us to a [pastebin](https://pastebin.com/QUwg950y) where we can see a number of 2digit numbers, which are mostly hex codes for the characters of the flag. So writing the solve script for such.
#### Flag: CM{4pT_Gr0uP5_L4z4Ru5}




