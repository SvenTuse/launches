Research plan:

## Mandatory output and scope rules

Follow the steps in this file without adding deliverables based on your own preferences, convenience, or a generic research workflow. The only research output files permitted in the project folder are:

- X-Flow.md
- x-mentions-flow.md
- website-analysis.md, when a website is provided; if it is unavailable, document that limitation in this file.
- other-info.md, only when additional information is found.
- project-overview.md, updating the existing file.
- whyitsent.md
- project-info.json, containing only the project metadata requested in step 9.

Do not create any additional files or folders unless the user explicitly requests them. In particular, do not save research-data.json, research-checklist.md, a research-evidence folder, separate datasets, calculation files, scripts, logs, screenshot crops, screenshots, dashboards, canvases, or extra summaries in the project folder. The metadata JSON required by step 9 is not permission to create a second JSON file containing research data.

Calculations, transcriptions, image enlargement/cropping, and completeness checks are working methods, not additional deliverables. Perform them in memory when possible. If a tool requires temporary files, use the system temporary directory outside the project folder and remove only the temporary files you created after they are no longer needed; never leave intermediate files in the project folder. Cropping long images as required in step 3 remains mandatory when needed for accurate reading, but the crops must not become saved project deliverables.

Put useful methodology, source references, calculation explanations, and evidence limitations inside the relevant required reports. Perform the review in step 6 internally; do not create a separate checklist or audit report. Preserve all supplied source files and folders and any unrelated existing files.

Before finishing, check that every file or folder you created for this research is on the permitted output list. Remove any extra artifacts you created and remove references to them from the reports, without deleting or changing supplied sources or unrelated existing files. The final response should describe the required results and material limitations, without adding another deliverable.

## Research steps

1. You analyze all the images in the x-posts folder showing the history of posts on X and create an md document called X-Flow.md in the folder of the project being researched. You put the entire sequence of posts you found in the x-posts folder into it. So, for the first post: the date, the post text. If there is an image, you describe in words what the image in this post is and what its message is. If the post contains a video, you write exactly that: “The post contains a video.” Based on the preview and the post text, you roughly work out what the video is likely to be about and what is in it.
Then you collect the metrics from the image: how many views this post has, how many likes, how many retweets, how many comments. And you do this for all the posts you find in the images, starting with the first and ending with the last.
This should give you roughly the following structure for each post:

Post date, time (if the time is shown in the image)
Attachment (if there is one: image or video) - a brief text description of the attachment.
Post text
Metrics (roughly like this, in table format):
Views     | likes | retweets | comments
12 000    |  1300 |  149     |     57

2. After you have fully written this MD document, described every post, and worked out how much engagement each post brought in, you summarize this information and write the Twitter account’s general information in the header, meaning at the very beginning of this X-Flow.md document:
- name
- unique handle
- what is in the avatar (text description)
- what is in the Twitter banner (text description)
- what the bio says
- following and follower counts, how many smart followers there are (shown below in the interface of an additional extension, rather than in X’s native interface)
- What verification does the project have? In other words, does it have a blue checkmark or a gold checkmark?
- total views
- total likes
- average engagement rate, meaning likes, retweets, and comments relative to views
- followers/views ratio


You also make a brief sequence of posts: the format is “Date, time, brief idea of the post, image or video, look at what was in it, how many views,” and do this briefly for all the posts, one after another. This is needed to understand the posting structure.

3. You analyze the images in the x-ca-mentions folder. The images can be very long, as I extract the whole X page with all the posts. You have to crop the long images to extract data properly, not losing any of the information. In case there are two many data there will be info.md or info.pdf file where will be text/photos info of metions, analyze it as photos.
This folder contains images from Twitter: all the posts returned when searching for this token’s contract. You create an md document called x-mentions-flow. You also list all the posts, from the first to the last. Just as in the X-Flow.md document, you record the statistics for each post. And in the header, you likewise write the overall statistics across all the posts, following the same approach as in the X-Flow.md document. In the header, you describe the sentiment around this token: what were people saying and writing? You count and list everyone who has a checkmark. In other words, you go through all the images and write down in the report all the usernames that have a checkmark.

4. You open the project-overview.md file and look at all the project information there. It will contain:
- Name
- Ticker
- Contract (meaning CA)
- X
- Website

If there is a website link, you start analyzing that website. Your task is to analyze this website and provide a website-analysis.md document describing what you found on the website. What should be in this document, paragraph by paragraph:
    1. The overall essence of the website: what it is, a landing page or an app, what this website does for users, what product they provide, what it is in general, what the narrative is, what story is built into it.
    2. Describe the technical functionality in detail: what is available on this website.
    3. Clearly describe the design: what you see; use the browser to navigate around the website. In other words, describe the design in detail: what colors are used, what animations, what images, how the buttons are positioned, what details there are. Basically, everything related to design. Overall, draw conclusions about the branding.

5. Next, search for additional information.
You start searching the internet, fetching, and running queries for:
- this project’s name
- this project’s ticker
- this project’s contract
- Twitter
- the website
You look for additional information you do not have yet. Whatever catches your eye, whatever you like — basically, collect all the info: what people said about this project online. Anything that could be useful for the analysis and for achieving our subsequent goal: creating a similar project and making money.
If there is any information: most of the projects are small, and there will most likely be no information about them on the regular internet. Most of their information is on their Twitter and website. If you find any additional information, create an additional document called other-info.md and include all of this information in it.

6. You go through all the files: x-mentions-flow.md, X-Flow.md, website-analysis.md (if a website was provided), other-info.md (if you created it), and analyze them. Have you followed all the instructions given in this how to research.md file, including the mandatory output and scope rules? Perform this check internally without creating a separate file. If all the instructions in this file have been followed, move on to the next step. If any instruction was skipped or not fully completed, finish it and move on to the next step.

7. Finally, make an overall overview based on all the files you created, meaning:
- the x-mentions-flow.md file
- the X-Flow.md file
- the website-analysis.md file
- the other-info.md file (if you created it)
You form an overall understanding of the project and compile the general information about it. Write all of this in existing file called project-overview.md.
Below the main information, write a structured report like this.
Report structure:
    1. Narrative. What is this project’s narrative? What is the meta? What is its tech? What do they offer users? What is the product? In other words, everything about the idea, everything about the product.
    2. How did they attract users’ attention? Through what? Maybe through the website design? Maybe through certain Twitter posts? In other words, analyze all the Twitter posts (X-Flow.md), all the Twitter statistics, all the Twitter mentions (x-mentions-flow.md), website-analysis.md, and also other-info.md if you created that file, and explain why this project worked out and became successful, how it attracted attention, and how it made money.
    3. What can we, as people launching projects, take away from this case? What hacks, what can we replicate, how can we apply this success? In other words, what is your advice to us based on this case?
    4. Think and give ten ideas similar to this project, and for each idea briefly explain how to implement it, how to promote it on Twitter, what creatives to use, and so on. In other words, an idea and literally three or four sentences of explanation for each idea.

8. Final step: explain why the project already sent.
After completing the research and project overview.md, create whyitsent.md in the folder of the project being researched. Review all the research files and distill the most significant findings into exactly three sentences, with an optional short title such as "Why [Ticker] Sent".

This is a retrospective explanation of why the project already became popular and reached its observed or reported capitalization, not a forecast of why it could send in the future. Formalize the idea and the thesis behind its existing success:
- Sentence 1: explain the core idea, narrative or meta, and what made the project immediately understandable and compelling.
- Sentence 2: explain the marketing factor behind its existing success: the evidenced distribution channels, paid ads or sponsored placements where verified, organic social posts, influencers, press or other media, and how the creatives and branding made the campaign recognizable and shareable; include a key metric only if it strengthens the explanation.
- Sentence 3: explain how that attention connected to speculative demand and valuation, including the token's economic thesis where supported by the research.

Synthesize the findings into three clear, connected sentences rather than listing all the information. Use retrospective language and concrete project-specific explanations. Distinguish observed evidence from inferred causes, label supplied or unverified capitalization figures as reported, and do not invent causality or equate token capitalization and trading volume with revenue or profit. The file should explain why it already sent, not offer recommendations, predict future growth or describe what would make it successful later.

Marketing analysis is mandatory alongside the idea and token thesis. Before writing whyitsent.md, identify how the project was marketed across ads and other media, the creative formats and messages used, and the role of colors, typography, recurring imagery, recognizable symbols and consistency between the website and social posts. Explain how those choices contributed to the attention it already received, using the strongest evidence rather than a generic claim that it had good marketing. Distinguish verified paid promotion, incentivized user content, organic distribution and media coverage; if paid advertising is not established, say so briefly rather than assuming that views came from ads. Compress the significant marketing findings into the same three-sentence summary, not a separate longer section.

In a final version of whyitsent.md, add more statistics and numeric data that you have acquired during the whole research of the whole project. Do not add all the numeric data and all the statistics you found. Add only that data that is relevant to the cause of why it was actually sent and why it was actually successful. 

9. At the end, add one JSON file named project-info.json with only this data about the project; do not add a separate research dataset JSON:
Name:
Ticker:
Contract (meaning CA):
X:
Website:
ATH:
Lifetime Volume:
gmgn link:https://gmgn.ai/robinhood/token/{CA} 
