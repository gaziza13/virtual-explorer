# Virtual Explorer

## Project Overview
Virtual Explorer is a platform designed to provide users with a virtual tour experience of various locations worldwide. It allows users to explore landmarks, read detailed descriptions, view captivating photos, and engage in virtual tours using cutting-edge virtual reality (VR) technologies.

## Features

### Frontend
- **Interactive World Map:** Explore different locations worldwide on an interactive map interface.
- **Landmark Pages:** Dive into detailed descriptions of landmarks, including photos, historical insights, and interesting facts.
- **Virtual Tours:** Immerse yourself in virtual tours using VR technologies for a lifelike experience.
- **Reviews and Ratings:** Rate and leave reviews about the places you've visited.
- **Enhanced User Experience:** Utilize animations and interactive elements to enhance user engagement.

### Backend
- **Data Management:** Store information about places, descriptions, photos, and user reviews efficiently.
- **API Endpoints:** Access data about places and manage virtual tours through well-defined API endpoints.
- **User Authentication:** Secure user authentication system with profile management functionalities.
- **Data Security:** Ensure the security and privacy of user data.
- **Virtual Tour Management:** Manage and conduct virtual tours seamlessly.

## Additional Functionality
- **User Contributions:** Allow users and organizations to add their own locations to enrich the platform's content.
- **Integration with VR Services:** Seamlessly integrate with VR services to enhance the virtual experience.

## API Endpoints
- `GET /places/`: Retrieve a list of all available places.
- `GET /places/{place_id}/`: Get detailed information about a specific place.
- `POST /places/`: Create a new place (restricted to administrators).
- `PUT /places/{place_id}/`: Update information about a place (restricted to administrators).
- `DELETE /places/{place_id}/`: Delete a place (restricted to administrators).
- `POST /places/{place_id}/reviews/`: Add a review for a place.
- `GET /places/{place_id}/reviews/`: Fetch reviews for a place.
- `POST /places/{place_id}/virtual_tours/`: Create a virtual tour for a place.
- `GET /places/{place_id}/virtual_tours/{tour_id}/`: Retrieve information about a specific virtual tour.
- `POST /places/{place_id}/virtual_tours/{tour_id}/start/`: Start a virtual tour.
- `POST /places/{place_id}/virtual_tours/{tour_id}/stop/`: End a virtual tour.

## Contributors
- [Gaziza Akhmetzhan](https://github.com/gaziza13)
- [Dauren Zhumabay](https://github.com/skapar)
