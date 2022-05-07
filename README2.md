# system-design

# Step 1: Constraints and use cases
Just like algorithm design, system design questions will also most likely be weakly defined. Consider the question about the URL-shortening service ("Design a URL shortening service like bit.ly"). There are so many things that are unclear about it! Without knowing more, it will be impossible to design an appropriate solution. Actually, many candidates forget about this and start designing a solution immediately.

Don’t make this mistake!

The very first thing you should do with any system design question is to clarify the system's constraints and to identify what use cases the system needs to satisfy. Spend a few minutes questioning your interviewer and agreeing on the scope of the system. Many of the same rules we discussed while talking about algorithm design apply here as well.

Usually, part of what the interviewer wants to see is if you can gather the requirements about the problem at hand, and design a solution that covers them well. Never assume things that were not explicitly stated.

For example, the URL-shortening service could be meant to serve just a few thousand users, but each could be sharing millions of URLs. It could be meant to handle millions of clicks on the shortened URLs, or dozens. The service may have to provide extensive statistics about each shortened URL (which will increase your data size), or statistics may not be a requirement at all.

You will also have to think about the use cases that are expected to occur. Your system will be designed based on what it's expected to do. Don't forget to make sure you know all the requirements the interviewer didn't tell you about in the beginning.

# Step 2: Abstract design (High Level Design)
Once you've scoped the system you're about to design, you should continue by outlining a high-level abstract design. The goal of this is to outline all the important components that your architecture will need.

You can tell the interviewer that you would like to do that and draw a simple diagram of your ideas. Sketch your main components and the connections between them. If you do this, very quickly you will be able to get feedback if you are moving in the right direction. Of course, you must be able to justify the high-level design that you just drew.

Don’t get lured to dive deep into some particular aspect of the abstract design. Not yet. Rather, make sure you sketch the important components and the connections between them. Justify your ideas in front of the interviewer and try to address every constraint and use case.

Usually, this sort of high-level design is a combination of well-known techniques, which people have developed. You have to make sure you are familiar with what's out there and feel comfortable using this knowledge. In this chapter we will assume that you have enough experience to design such a high-level system. Our goal is to focus more on the next steps, where we will talk mainly about scalability and about removing bottlenecks.

If you feel like a complete beginner in system design, perhaps it will be very useful for you to first look at a book on the topic or take advantage of some of the resources we've shared in the sections of this course.


# Step 3: Understanding bottlenecks
Most likely your high-level design will have one or more bottlenecks given the constraints of the problem. This is perfectly ok. You are not expected to design a system from the ground up, which immediately handles all the load in the world. It just needs to be scalable, in order for you to be able to improve it using some standard tools and techniques.

Now that you have your high-level design, start thinking about what bottlenecks it has. Perhaps your system needs a load balancer and many machines behind it to handle the user requests. Or maybe the data is so huge that you need to distribute your database on multiple machines. What are some of the downsides that occur from doing that? Is the database too slow and does it need some in-memory caching?

These are just examples of questions that you may have to answer in order to make your solution complete. It may be the case that the interviewer wants to direct the discussion in one particular direction. Then, maybe you won’t need to address all the bottlenecks but rather talk in more depth about one particular area. In any case, you need to be able to identify the weak spots in a system and be able to resolve them.

Remember, usually each solution is a trade-off of some kind. Changing something will worsen something else. However, the important thing is to be able to talk about these trade-offs, and to measure their impact on the system given the constraints and use cases defined.

Once you've outlined the core bottlenecks you see, you can start addressing them in the next step.

# Step 4: Scaling your abstract design (Low Level Design)
Once you're ready with your high-level design and have made sure that the interviewer is ok with it, you can dive into making it more detailed. Usually, this means making your system scale.

I've devoted the next section of this course to the topic of scalability. We will first cover some theoretical fundamentals, and then look at many real-life examples of scalable architectures.