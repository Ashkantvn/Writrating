# Writrating 
**Writrating** is a comprehensive, open-source platform for tech enthusiasts to review, compare, and stay informed about the latest digital devices.

![Device discovery](/docs/img/logo/logo.png)

## Project Goals
- **Create Reliable Data**: Ensure the accuracy and reliability of all data presented on the platform.
- **Website Security**: Implement robust security measures to protect user data and the website itself.
- **Data Privacy**: Do not save any critical or specific data from users to maintain their privacy.
- **Optimized Performance**: Ensure the platform is optimized for performance to provide a seamless user experience.

## Main Features
- **Device Listings**: Browse through a comprehensive list of digital devices with detailed specifications.
- **Blogs**:View, and manage content about digital devices.
- **Device Reviews**: Read and write reviews for various digital devices to share and gain insights.
- **Device Comparisons**: Compare multiple devices side by side to help users make informed decisions.
- **User Authentication**:login and registration system for managing user accounts.
- **User Roles and Permissions**: Different levels of access and control based on user roles (Guest, Normal User, Admin, Superuser, Validator).
- **Responsive Design**: Fully responsive design to ensure optimal viewing experience on various devices.
- **Commenting System**: Engage with the community through comments on reviews and blog posts.
- **Content Management**: Admins can create, edit, and manage their own blogs and reviews.

## User Roles and Permissions
### Guests
- **Permissions**:
  - View detailed information about devices.
  - Access list of devices, reviews, and blogs.

### Normal Users
- **Permissions**:
  - View information about digital devices.
  - Send comments, and reports.
  - Compare devices.

### Admins
- **Permissions**:
  - Have all the permissions of normal users.
  - Create, edit, and manage their own blogs, reviews, and device data on the website.

### Superusers
- **Permissions**:
  - Full control over all aspects of the platform.

### Validators
- **Permissions**:
  - Have all the permissions of normal users.
  - Review and validate data to ensure it meets publication standards.

## Technologies Used
- **Backend**: Django, Django REST Framework
- **Frontend**: React, Next
