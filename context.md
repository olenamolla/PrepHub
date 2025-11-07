# PrepHub - Technical Interview Preparation Tracker

## Project Overview
PrepHub is a web application designed to help developers systematically prepare for technical interviews by tracking their problem-solving progress and implementing spaced repetition learning techniques.

## Technology Stack

### Frontend
- **Framework:** React
- **Language:** JavaScript
- **State Management:** React Context (initial phase)
  - Will migrate to Redux when adding features like:
    - Offline support
    - Complex filtering/sorting
    - Real-time updates
    - Multiple data source management
- **UI Library:** Material-UI/Chakra UI
- **API Communication:** Axios

### Backend
- **Framework:** Django
- **Language:** Python
- **API:** Django REST Framework
- **Authentication:** JWT (JSON Web Tokens)

### Database
- **System:** PostgreSQL
- **ORM:** Django ORM

### Deployment
- **Platform:** Railway.app (Initial deployment)
  - More cost-effective than AWS for MVP
  - Simpler deployment process
  - Built-in PostgreSQL support
  - Free tier available for development
- **Future Migration:** AWS
  - Services planned:
    - EC2 or ECS for application hosting
    - RDS for PostgreSQL
    - S3 for static files
    - Route 53 for DNS management

## Core Features (MVP)
1. User Authentication System
2. Problem Tracking
   - Date/Time of solving
   - Data Structure/Algorithm topic
   - Difficulty level
   - Pattern recognition
   - Notes and reflections
3. Problem Categorization
4. Spaced Repetition System
5. Progress Analytics
6. Problem Priority Management

## Future Iterations
- Performance analytics
- Social features
- Problem recommendations
- Integration with coding platforms
- Mobile responsive design
- Offline support
