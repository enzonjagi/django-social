# Django-Social: a Django social media project

## Goals/Objectives
- Users will be able to either follow or not follow another user.
- If they follow someone, they’ll see that user’s content. If they don’t, they won’t.
- Users can follow a person without being followed back. Relationships in the social network can be asymmetrical, meaning that a user can follow someone and see their content without the reverse being true.
- Users need to be aware of who exists so that they know whom they can follow.
- Users should also be aware of who follows them.
- In the app’s most basic form, users won’t have many extra features available to them. We won’t implement a way to block people, and there won’t be a way to directly respond to content that someone else posted.

## Tools/Stack
- Python: Django
- HTML/CSS
- Bulma CSS

## Steps to Create
### Tutorial Series from: Real Python
- 📍 [Part 1: Models and Relationships](https://realpython.com/django-social-network-1/)
    * Step 1: Set Up the Base Project
    * Step 2: Extend the Django User Model
    * Step 3: Implement a Post-Save Hook
- ⏭ [Part 2: Templates and Front-End Styling](https://realpython.com/django-social-front-end-2/)
    * Step 4: Create a Base Template With Bulma
    * Step 5: List All User Profiles
    * Step 6: Access Individual Profile Pages
- ⏭ [Part 3: Follows and Dweets](https://realpython.com/django-social-post-3/)
    * Step 7: Follow and Unfollow Other Profiles
    * Step 8: Create the Back-End Logic For Dweets
    * Step 9: Display Dweets on the Front End
- ⏭ [Part 4: Forms and Submissions](https://realpython.com/django-social-forms-4/)
    * Step 10: Submit Dweets Through a Django Form
    * Step 11: Prevent Double Submissions and Handle Errors
    * Step 12: Improve the Front-End User Experience